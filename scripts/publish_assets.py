"""Publish prebuilt, checksummed assets. No private signing key or app execution.

Git blobs are temporary transfer objects; app binaries do not enter the public
repository's source tree. Published GitHub Release assets are durable downloads.
"""
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request

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

def main():
    plan=json.loads((ROOT/'publish-plan.json').read_text())
    tag=plan['tag']
    if plan['schema']!=1 or not re.fullmatch(r'beta-2\.0\.[0-9]+\.[0-9]+\.[0-9]+',tag):raise ValueError('Invalid release plan')
    notes=(ROOT/'release-notes.md').read_text();staging=ROOT/'dist';staging.mkdir(exist_ok=True);files=[]
    for entry in plan['assets']:
        name=entry['name']
        if not re.fullmatch(r'[A-Za-z0-9_.-]+',name) or not 0<entry['bytes']<40_000_000:raise ValueError('Invalid release asset')
        output=bytearray()
        for chunk in entry['chunks']:
            if not re.fullmatch('[0-9a-f]{40}',chunk['git_blob']):raise ValueError('Invalid transfer blob')
            blob=api(API+'/git/blobs/'+chunk['git_blob'])
            if blob.get('encoding')!='base64':raise ValueError('Invalid blob encoding')
            body=base64.b64decode(blob['content'])
            if len(body)!=chunk['bytes'] or checksum(body)!=chunk['sha256']:raise ValueError('Transfer checksum failed')
            output.extend(body)
            if len(output)>entry['bytes']:raise ValueError('Transfer exceeds declared size')
        if len(output)!=entry['bytes'] or checksum(output)!=entry['sha256']:raise ValueError('Release checksum failed')
        file=staging/name;file.write_bytes(output);files.append((entry,file))
    try:release=api(API+'/releases/tags/'+urllib.parse.quote(tag,safe=''))
    except urllib.error.HTTPError as error:
        if error.code!=404:raise
        release=api(API+'/releases','POST',dict(tag_name=tag,target_commitish=os.environ['GITHUB_SHA'],name=plan['title'],body=notes,draft=True,prerelease=True))
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
    if release['draft']:release=api(API+'/releases/'+str(release['id']),'PATCH',dict(draft=False,prerelease=True))
    print(json.dumps(dict(release=release['html_url'],assets=[e['name'] for e,_ in files],signing_key_used=False)))

if __name__=='__main__':main()
