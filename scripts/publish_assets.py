"""Publish prebuilt, checksummed assets. No private signing key or app execution.

Git blobs are temporary transfer objects; app binaries do not enter the public
repository's source tree. Published GitHub Release assets are durable downloads.
"""
import base64
import hashlib
import io
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request
import zipfile

ROOT=Path(__file__).resolve().parents[1]
REPO=os.environ['GITHUB_REPOSITORY']
if REPO!='lmonroe8/gridworks-drift-coach-releases':raise SystemExit('Unexpected release repository')
API='https://api.github.com/repos/'+REPO
TOKEN=os.environ['GH_TOKEN']

def api(url,method='GET',body=None,kind='application/json'):
    parsed=urllib.parse.urlsplit(url)
    if parsed.scheme!='https' or parsed.hostname not in ('api.github.com','uploads.github.com'):raise ValueError('Unexpected GitHub endpoint')
    if isinstance(body,dict):body=json.dumps(body).encode()
    headers={'Authorization':'Bearer '+TOKEN,'Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'Gridworks-Release-Publisher','Content-Type':kind}
    request=urllib.request.Request(url,data=body,method=method,headers=headers)
    with urllib.request.urlopen(request,timeout=90) as response:return json.load(response)

def checksum(body):return hashlib.sha256(body).hexdigest()


class NoTransportRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        raise ValueError('Build transport redirects are not allowed')

_BLOBS={}

def transfer_blob(sha,limit):
    if not re.fullmatch('[0-9a-f]{40}',sha):raise ValueError('Invalid transfer blob')
    if sha in _BLOBS:
        if len(_BLOBS[sha])>limit:raise ValueError('Transfer blob exceeds limit')
        return _BLOBS[sha]
    blob=api(API+'/git/blobs/'+sha)
    if blob.get('encoding')!='base64':raise ValueError('Invalid blob encoding')
    body=base64.b64decode(blob['content'])
    if len(body)>limit:raise ValueError('Transfer blob exceeds limit')
    _BLOBS[sha]=body
    return body

def transport_asset(entry):
    ticket=json.loads(transfer_blob(entry['artifact_transport_blob'],10_000))
    url=ticket['url'];parsed=urllib.parse.urlsplit(url)
    if (len(url)>6000 or parsed.scheme!='https' or parsed.username or parsed.password
        or parsed.port not in (None,443) or parsed.fragment
        or not re.fullmatch(r'sdmntpr[a-z0-9-]*\.oaiusercontent\.com',parsed.hostname or '')):
        raise ValueError('Unexpected build transport endpoint')
    if not 0<ticket['bytes']<42_000_000 or not re.fullmatch('[0-9a-f]{64}',ticket['sha256']):
        raise ValueError('Invalid build transport limits')
    if ticket['member']!=entry['name']:raise ValueError('Unexpected build archive member')
    # This request deliberately has no GitHub token or repository headers.
    request=urllib.request.Request(url,headers={'User-Agent':'Gridworks-Release-Transfer'})
    try:
        with urllib.request.build_opener(NoTransportRedirect()).open(request,timeout=90) as response:
            body=response.read(ticket['bytes']+1)
    except Exception:
        raise ValueError('Build transport download failed; refresh transfer ticket') from None
    if len(body)!=ticket['bytes'] or checksum(body)!=ticket['sha256']:
        raise ValueError('Build transport checksum failed')
    with zipfile.ZipFile(io.BytesIO(body)) as archive:
        if archive.namelist()!=[ticket['member']]:raise ValueError('Unexpected build archive contents')
        info=archive.getinfo(ticket['member'])
        if info.file_size!=entry['bytes']:raise ValueError('Build archive size differs')
        output=archive.read(info)
    return output

def asset_bytes(entry):
    if 'artifact_transport_blob' in entry:
        if 'chunks' in entry:raise ValueError('Ambiguous release transport')
        output=transport_asset(entry)
    else:
        output=bytearray()
        for chunk in entry['chunks']:
            body=transfer_blob(chunk['git_blob'],1_048_576)
            if len(body)!=chunk['bytes'] or checksum(body)!=chunk['sha256']:
                raise ValueError('Transfer checksum failed')
            output.extend(body)
            if len(output)>entry['bytes']:raise ValueError('Transfer exceeds declared size')
    if len(output)!=entry['bytes'] or checksum(output)!=entry['sha256']:
        raise ValueError('Release checksum failed')
    return bytes(output)


def release_options(plan):
    tag=plan.get('tag','')
    beta=bool(re.fullmatch(r'beta-2\.0\.[0-9]+\.[0-9]+\.[0-9]+',tag))
    stable=bool(re.fullmatch(r'v[0-9]+\.[0-9]+\.[0-9]+',tag))
    prerelease=plan.get('prerelease',beta)
    if plan.get('schema')!=1 or not (beta or stable) or type(prerelease) is not bool:
        raise ValueError('Invalid release plan')
    if beta and not prerelease:raise ValueError('Production releases require a v version tag')
    return dict(prerelease=prerelease,make_latest='false' if prerelease else 'true')


def main():
    plan=json.loads((ROOT/'publish-plan.json').read_text())
    tag=plan['tag']
    options=release_options(plan)
    notes=(ROOT/'release-notes.md').read_text();staging=ROOT/'dist';staging.mkdir(exist_ok=True);files=[]
    for entry in plan['assets']:
        name=entry['name']
        if not re.fullmatch(r'[A-Za-z0-9_.-]+',name) or not 0<entry['bytes']<40_000_000:raise ValueError('Invalid release asset')
        output=asset_bytes(entry)
        file=staging/name;file.write_bytes(output);files.append((entry,file))
    try:release=api(API+'/releases/tags/'+urllib.parse.quote(tag,safe=''))
    except urllib.error.HTTPError as error:
        if error.code!=404:raise
        release=api(API+'/releases','POST',dict(tag_name=tag,target_commitish=os.environ['GITHUB_SHA'],name=plan['title'],body=notes,draft=True,**options))
    existing={a['name']:a for a in release.get('assets',[])}
    for entry,file in files:
        previous=existing.get(entry['name'])
        if previous:
            if previous.get('size')!=entry['bytes'] or previous.get('digest')!='sha256:'+entry['sha256']:raise ValueError('Existing release asset differs; use a new build version')
            continue
        if not release['draft']:raise ValueError('Do not modify an already published release')
        upload=release['upload_url'].split('{',1)[0]+'?'+urllib.parse.urlencode({'name':entry['name']})
        asset=api(upload,'POST',file.read_bytes(),'application/octet-stream')
        if asset['size']!=entry['bytes'] or (asset.get('digest') and asset['digest']!='sha256:'+entry['sha256']):raise ValueError('Uploaded asset did not verify')
    if release['draft']:release=api(API+'/releases/'+str(release['id']),'PATCH',dict(draft=False,**options))
    print(json.dumps(dict(release=release['html_url'],assets=[e['name'] for e,_ in files],signing_key_used=False)))

if __name__=='__main__':main()
