"""Verify published Gridworks downloads over unauthenticated public HTTPS.

This program never reads credentials, mutates a release, advances an update
feed, or executes downloaded content. Every byte is checked against the plan.
"""
from __future__ import annotations

import argparse
import ast
import base64
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import socket
import stat
import struct
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile

REPOSITORY = "lmonroe8/gridworks-drift-coach-releases"
API = "https://api.github.com/repos/" + REPOSITORY
MAX_ASSET = 138_000_000
MAX_JSON = 2_000_000
MAX_UNPACKED = 800_000_000
PUBLIC_ASSET_HOSTS = {"github.com", "release-assets.githubusercontent.com", "objects.githubusercontent.com"}
RETRY_CODES = {404, 408, 429, 500, 502, 503, 504}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(body):
    return hashlib.sha256(body).hexdigest()


def safe_https(url, hosts):
    require(isinstance(url, str) and len(url) <= 12_000 and not any(ord(c) < 33 for c in url), "Invalid public URL")
    parsed = urllib.parse.urlsplit(url)
    require(parsed.scheme == "https" and parsed.hostname in hosts and not parsed.username and not parsed.password
            and parsed.port in (None, 443) and not parsed.fragment, "Unexpected public download endpoint")
    return parsed


class PublicRedirect(urllib.request.HTTPRedirectHandler):
    max_redirections = 5

    def redirect_request(self, request, fp, code, message, headers, newurl):
        safe_https(newurl, PUBLIC_ASSET_HOSTS)
        require(not any(name.lower() in ("authorization", "cookie") for name, _ in request.header_items()),
                "Authenticated request is not allowed for public downloads")
        redirected = super().redirect_request(request, fp, code, message, headers, newurl)
        if redirected:
            require(not any(name.lower() in ("authorization", "cookie") for name, _ in redirected.header_items()),
                    "Authenticated redirect is not allowed")
        return redirected


class NoAPIRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        raise ValueError("Public release API must not redirect")


def network_label(error):
    # Exception strings may include a temporary signed redirect URL; omit them.
    if isinstance(error, urllib.error.HTTPError):
        return "HTTP " + str(error.code)
    return type(error).__name__


def api_json(url, attempts=4):
    parsed = safe_https(url, {"api.github.com"})
    require(parsed.path.startswith("/repos/" + REPOSITORY + "/releases/"), "Unexpected public API path")
    opener = urllib.request.build_opener(NoAPIRedirect())
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "Gridworks-Public-Download-Verification"})
            with opener.open(request, timeout=90) as response:
                require(response.status == 200, "Public release API did not return 200")
                body = response.read(MAX_JSON + 1)
                require(len(body) <= MAX_JSON, "Public release metadata exceeds limit")
            return json.loads(body)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, socket.timeout) as error:
            retryable = not isinstance(error, urllib.error.HTTPError) or error.code in RETRY_CODES
            if not retryable or attempt + 1 == attempts:
                raise ValueError("Unauthenticated release lookup failed (" + network_label(error) + ")") from None
            time.sleep(min(2 ** (attempt + 1), 8))
    raise ValueError("Public release lookup did not complete")


def public_download(entry, asset, destination, attempts=4):
    url = asset["browser_download_url"]
    safe_https(url, {"github.com"})
    opener = urllib.request.build_opener(PublicRedirect())
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"Accept": "application/octet-stream",
                "User-Agent": "Gridworks-Public-Download-Verification"})
            total, hasher = 0, hashlib.sha256()
            with opener.open(request, timeout=90) as response, destination.open("wb") as output:
                require(response.status == 200, "Public asset did not return 200")
                safe_https(response.geturl(), PUBLIC_ASSET_HOSTS)
                declared = response.headers.get("Content-Length")
                require(declared is None or int(declared) == entry["bytes"], "Public asset Content-Length differs")
                while True:
                    data = response.read(min(1_048_576, entry["bytes"] - total + 1))
                    if not data:
                        break
                    total += len(data)
                    require(total <= entry["bytes"], "Public asset exceeds planned length")
                    hasher.update(data)
                    output.write(data)
            require(total == entry["bytes"] and hasher.hexdigest() == entry["sha256"], "Public asset checksum differs")
            return dict(name=entry["name"], bytes=total, sha256=hasher.hexdigest(), public_url=url, verified=True)
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, socket.timeout) as error:
            retryable = not isinstance(error, urllib.error.HTTPError) or error.code in RETRY_CODES
            if not retryable or attempt + 1 == attempts:
                raise ValueError("Public download failed for " + entry["name"] + " (" + network_label(error) + ")") from None
            time.sleep(min(2 ** (attempt + 1), 8))
    raise ValueError("Public download did not complete")


def validate_plan(plan):
    require(plan.get("schema") == 1 and re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", plan.get("tag", "")), "Invalid stable release plan")
    require(plan.get("prerelease") is False, "Expected a production release")
    assets = plan.get("assets")
    require(isinstance(assets, list) and 1 <= len(assets) <= 20, "Unexpected release asset count")
    require(len({entry["name"] for entry in assets}) == len(assets), "Duplicate planned asset names")
    for entry in assets:
        require(re.fullmatch(r"[A-Za-z0-9_.-]+", entry["name"]), "Unsafe planned asset name")
        require(entry["name"] not in (".", ".."), "Unsafe planned asset name")
        require(type(entry["bytes"]) is int and 0 < entry["bytes"] < MAX_ASSET, "Invalid planned asset size")
        require(re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]), "Invalid planned asset checksum")
    require("Gridworks-Drift-Coach-Setup.zip" in {entry["name"] for entry in assets}, "Missing installer asset")
    return plan["tag"][1:]


def validate_release(plan, release):
    require(release.get("tag_name") == plan["tag"] and release.get("draft") is False
            and release.get("prerelease") is False and release.get("published_at"), "Release is not publicly published as planned")
    expected_url = "https://github.com/" + REPOSITORY + "/releases/tag/" + plan["tag"]
    require(release.get("html_url") == expected_url, "Public release URL differs")
    assets = release.get("assets", [])
    names = [asset.get("name") for asset in assets]
    require(len(names) == len(set(names)), "Duplicate remote asset names")
    mapping = {asset["name"]: asset for asset in assets}
    for entry in plan["assets"]:
        require(entry["name"] in mapping, "Planned public asset is missing")
        asset = mapping[entry["name"]]
        require(asset.get("state") == "uploaded" and asset.get("size") == entry["bytes"], "Public asset metadata differs")
        require(asset.get("digest") in (None, "sha256:" + entry["sha256"]), "GitHub asset digest differs")
        expected_download = "https://github.com/" + REPOSITORY + "/releases/download/" + plan["tag"] + "/" + entry["name"]
        require(asset.get("browser_download_url") == expected_download, "Public asset URL differs")
    return mapping


def inspect_zip(archive, total_limit=MAX_UNPACKED, members_limit=3000):
    infos = archive.infolist()
    names = [item.filename for item in infos]
    require(len(infos) <= members_limit and len(names) == len(set(name.casefold() for name in names)), "Unsafe ZIP member count or duplicates")
    require(sum(item.file_size for item in infos) <= total_limit, "ZIP exceeds unpacked size limit")
    for item in infos:
        name = item.filename
        path = PurePosixPath(name)
        require(name and not path.is_absolute() and ".." not in path.parts and "\\" not in name
                and path.as_posix() == name.rstrip("/") and not any(":" in part for part in path.parts), "Unsafe ZIP path")
        require(not stat.S_ISLNK(item.external_attr >> 16) and not item.flag_bits & 1, "Unsafe ZIP member type")
    require(archive.testzip() is None, "ZIP CRC validation failed")


def installer_version(path, version):
    with zipfile.ZipFile(path) as archive:
        inspect_zip(archive, MAX_ASSET, 2)
        require(archive.namelist() == ["Gridworks-Drift-Coach/Gridworks-Setup.exe", "Gridworks-Drift-Coach/START-HERE.html"],
                "Public installer ZIP members differ")
        exe = archive.read("Gridworks-Drift-Coach/Gridworks-Setup.exe")
    require(len(exe) > 256 and exe[:2] == b"MZ" and exe[-56:-40] == b"GRIDWORKSSETUP1\0", "Invalid public Windows installer")
    pe = struct.unpack_from("<I", exe, 0x3C)[0]
    require(pe + 6 < len(exe) and exe[pe:pe + 4] == b"PE\0\0" and struct.unpack_from("<H", exe, pe + 4)[0] == 0x8664,
            "Public installer is not x64")
    length = struct.unpack_from("<Q", exe, len(exe) - 40)[0]
    require(0 < length < len(exe) - 56, "Public installer payload length differs")
    payload = exe[-56 - length:-56]
    require(hashlib.sha256(payload).digest() == exe[-32:], "Public installer payload checksum differs")
    with zipfile.ZipFile(io.BytesIO(payload)) as archive:
        inspect_zip(archive)
        bundle = json.loads(archive.read("Bundle.json"))
        require(bundle.get("version") == version, "Public installer Bundle version differs")
        tree = ast.parse(archive.read("Sim-Center/release_info.py").decode("utf-8"))
        versions = [ast.literal_eval(node.value) for node in tree.body if isinstance(node, ast.Assign)
                    and any(isinstance(target, ast.Name) and target.id == "BUILD_VERSION" for target in node.targets)]
        require(versions == [version], "Public installer application version differs")
    return dict(version=version, x64=True, two_member_zip=True, payload_bytes=len(payload), payload_sha256=digest(payload),
                bundle_and_app_versions_match=True, executed=False)


def offline_zip(path, version, plan_entries):
    with zipfile.ZipFile(path) as archive:
        inspect_zip(archive, MAX_ASSET, 64)
        names = archive.namelist()
        require(all("/" not in name and "\\" not in name for name in names), "Offline ZIP must contain flat files")
        expected_files = {"updater.py", "update_common.py", "update_trust.json", "latest.json", "Update-Gridworks.cmd",
                          "Update-Gridworks.ps1", "UPDATE-README.txt"}
        patches = [name for name in names if name.endswith(".gwupdate")]
        require(patches and set(names) == expected_files | set(patches), "Unexpected offline ZIP contents")
        for name in patches:
            require(name in plan_entries, "Offline ZIP contains an unplanned patch")
            entry = plan_entries[name]
            require(archive.getinfo(name).file_size == entry["bytes"], "Offline patch length differs")
            hasher, count = hashlib.sha256(), 0
            with archive.open(name) as stream:
                while True:
                    block = stream.read(1_048_576)
                    if not block:
                        break
                    count += len(block)
                    require(count <= entry["bytes"], "Offline patch exceeds plan")
                    hasher.update(block)
            require(count == entry["bytes"] and hasher.hexdigest() == entry["sha256"], "Offline patch checksum differs")
        envelope = json.loads(archive.read("latest.json"))
        require(envelope.get("schema") == 1 and envelope.get("algorithm") == "rsa-sha256", "Offline manifest envelope differs")
        manifest = json.loads(base64.b64decode(envelope["payload"], validate=True))
        require(manifest.get("version") == version and manifest.get("channel") == "stable", "Offline manifest version differs")
    return dict(safe_members=True, embedded_patches_verified=patches, manifest_version=version, executed=False)


def verify(plan):
    version = validate_plan(plan)
    release = api_json(API + "/releases/tags/" + urllib.parse.quote(plan["tag"], safe=""))
    mapping = validate_release(plan, release)
    results, details = [], {}
    entries = {entry["name"]: entry for entry in plan["assets"]}
    with tempfile.TemporaryDirectory(prefix="gridworks-public-downloads-") as temporary:
        root = Path(temporary)
        for entry in plan["assets"]:
            path = root / entry["name"]
            results.append(public_download(entry, mapping[entry["name"]], path))
            if entry["name"] == "Gridworks-Drift-Coach-Setup.zip":
                details["installer"] = installer_version(path, version)
            elif entry["name"] == "Gridworks-Small-Update-" + version + ".zip":
                details["offline_update"] = offline_zip(path, version, entries)
            path.unlink()
    return dict(passed=True, verified_at=datetime.now(timezone.utc).isoformat(), repository=REPOSITORY, version=version,
                tag=plan["tag"], release_url=release["html_url"], public_non_draft=True, unauthenticated_requests=True,
                credential_headers_used=False, assets=results, total_bytes=sum(row["bytes"] for row in results),
                details=details, downloaded_code_executed=False, release_modified=False, feed_advanced=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=Path("publish-plan.json"))
    parser.add_argument("--report", type=Path, default=Path("public-download-verification.json"))
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
        report = verify(plan)
    except Exception as error:
        # All deliberate validation errors are safe generic text; unexpected
        # exceptions expose only their type, never response bodies/redirect URLs.
        reason = str(error) if isinstance(error, ValueError) and type(error) is ValueError else type(error).__name__
        report = dict(passed=False, verified_at=datetime.now(timezone.utc).isoformat(), reason=reason,
                      unauthenticated_requests=True, release_modified=False, feed_advanced=False)
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print("GRIDWORKS_PUBLIC_DOWNLOAD_VERIFICATION " + json.dumps(report), flush=True)
        raise SystemExit(1) from None
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("GRIDWORKS_PUBLIC_DOWNLOAD_VERIFICATION " + json.dumps(report), flush=True)


if __name__ == "__main__":
    main()
