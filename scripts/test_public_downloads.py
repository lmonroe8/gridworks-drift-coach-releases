"""Offline fixtures for the CI-only public download verifier."""
import base64
import hashlib
import io
import json
from pathlib import Path
import struct
import tempfile
import unittest
import urllib.request
import zipfile

from verify_public_downloads import PublicRedirect, digest, inspect_zip, installer_version, offline_zip, validate_release


class PublicDownloadValidation(unittest.TestCase):
    def test_public_release_must_be_nondraft_with_exact_download_urls(self):
        name = "Gridworks-Drift-Coach-Setup.zip"
        tag = "v7.19.5"
        base = "https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/"
        plan = {"tag": tag, "assets": [{"name": name, "bytes": 3, "sha256": digest(b"abc")} ]}
        release = {"tag_name": tag, "draft": False, "prerelease": False, "published_at": "fixture",
                   "html_url": base + "tag/" + tag, "assets": [{"name": name, "state": "uploaded", "size": 3,
                   "digest": "sha256:" + digest(b"abc"), "browser_download_url": base + "download/" + tag + "/" + name}]}
        self.assertIn(name, validate_release(plan, release))
        release["draft"] = True
        with self.assertRaises(ValueError):
            validate_release(plan, release)
        release["draft"] = False
        release["assets"][0]["browser_download_url"] = "https://example.com/asset"
        with self.assertRaises(ValueError):
            validate_release(plan, release)

    def installer(self, root, version="7.19.5", corrupt=False):
        payload = io.BytesIO()
        with zipfile.ZipFile(payload, "w", zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("Bundle.json", json.dumps({"version": version}))
            archive.writestr("Sim-Center/release_info.py", "BUILD_VERSION=" + repr(version))
        data = payload.getvalue()
        stub = bytearray(256)
        stub[:2] = b"MZ"
        struct.pack_into("<I", stub, 0x3C, 0x80)
        stub[0x80:0x84] = b"PE\0\0"
        struct.pack_into("<H", stub, 0x84, 0x8664)
        checksum = hashlib.sha256(data).digest() if not corrupt else bytes(32)
        exe = stub + data + b"GRIDWORKSSETUP1\0" + struct.pack("<Q", len(data)) + checksum
        path = root / "installer.zip"
        with zipfile.ZipFile(path, "w") as archive:
            archive.writestr("Gridworks-Drift-Coach/Gridworks-Setup.exe", exe)
            archive.writestr("Gridworks-Drift-Coach/START-HERE.html", "Fixture")
        return path

    def test_public_installer_checks_embedded_payload_and_both_versions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.installer(root)
            report = installer_version(path, "7.19.5")
            self.assertTrue(report["bundle_and_app_versions_match"])
            self.assertFalse(report["executed"])
            with self.assertRaisesRegex(ValueError, "version differs"):
                installer_version(path, "7.19.6")
            self.installer(root, corrupt=True)
            with self.assertRaisesRegex(ValueError, "payload checksum"):
                installer_version(path, "7.19.5")

    def test_offline_zip_requires_planned_patch_bytes_and_no_extra_members(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            name = "Gridworks-7.19.2-to-7.19.5.gwupdate"
            body = b"fixture patch bytes"
            entry = {"name": name, "bytes": len(body), "sha256": digest(body)}
            path = root / "offline.zip"
            manifest = {"version": "7.19.5", "channel": "stable"}
            envelope = {"schema": 1, "algorithm": "rsa-sha256", "payload": base64.b64encode(json.dumps(manifest).encode()).decode()}
            with zipfile.ZipFile(path, "w") as archive:
                for item in ("updater.py", "update_common.py", "update_trust.json", "Update-Gridworks.cmd", "Update-Gridworks.ps1", "UPDATE-README.txt"):
                    archive.writestr(item, "fixture")
                archive.writestr("latest.json", json.dumps(envelope))
                archive.writestr(name, body)
            self.assertEqual(offline_zip(path, "7.19.5", {name: entry})["embedded_patches_verified"], [name])
            changed = dict(entry, sha256="0" * 64)
            with self.assertRaisesRegex(ValueError, "checksum differs"):
                offline_zip(path, "7.19.5", {name: changed})
            with zipfile.ZipFile(path, "a") as archive:
                archive.writestr("unexpected.key", "fixture")
            with self.assertRaisesRegex(ValueError, "Unexpected offline ZIP"):
                offline_zip(path, "7.19.5", {name: entry})

    def test_download_redirects_cannot_forward_credentials_or_leave_allowlist(self):
        handler = PublicRedirect()
        url = "https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/v7.19.5/file.zip"
        request = urllib.request.Request(url, headers={"Authorization": "Bearer fixture-only"})
        with self.assertRaisesRegex(ValueError, "Authenticated"):
            handler.redirect_request(request, None, 302, "Found", {}, "https://release-assets.githubusercontent.com/file")
        clean = urllib.request.Request(url, headers={"User-Agent": "Fixture"})
        redirected = handler.redirect_request(clean, None, 302, "Found", {}, "https://release-assets.githubusercontent.com/file")
        self.assertNotIn("Authorization", dict(redirected.header_items()))
        with self.assertRaisesRegex(ValueError, "endpoint"):
            handler.redirect_request(clean, None, 302, "Found", {}, "https://example.com/file")

    def test_public_zip_path_traversal_is_rejected(self):
        data = io.BytesIO()
        with zipfile.ZipFile(data, "w") as archive:
            archive.writestr("../outside", "fixture")
        with zipfile.ZipFile(io.BytesIO(data.getvalue())) as archive:
            with self.assertRaisesRegex(ValueError, "Unsafe ZIP path"):
                inspect_zip(archive)


if __name__ == "__main__":
    unittest.main()
