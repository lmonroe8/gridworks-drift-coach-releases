"""Add the reviewed 7.14 manual to its existing release; never replace assets."""
import json
from pathlib import Path
import urllib.parse

from publish_assets import API, ROOT, api, asset_bytes, validate_asset

TAG = 'v7.14.0'
RELEASE_ID = 428384798
NAMES = {
    'Gridworks_Drift_Coach_7.14_Visual_Instruction_Manual.pdf': 'application/pdf',
    'Gridworks_Drift_Coach_7.14_Screenshot_Pack.zip': 'application/zip',
}
BASE = 'https://github.com/lmonroe8/gridworks-drift-coach-releases/releases/download/' + TAG + '/'
MARKER = '## Visual instruction manual'
DOCS = '\n'.join([
    MARKER, '',
    '- [Download the 49-page PDF instruction manual](' + BASE + 'Gridworks_Drift_Coach_7.14_Visual_Instruction_Manual.pdf)',
    '- [Download the full-size screenshot pack](' + BASE + 'Gridworks_Drift_Coach_7.14_Screenshot_Pack.zip)', '',
    'Covers all 16 app sections, with 39 app views and seven dashboard/overlay examples. '
    'The PDF includes clickable contents and step-by-step instructions. '
    'The screenshot ZIP includes an HTML gallery and CSV index. '
    'Screenshots use demonstration data; SimHub images are native-template previews.',
])


def verify_release(release, plan):
    if (release['id'] != RELEASE_ID or release['tag_name'] != TAG
            or release['draft'] or release['prerelease'] or release.get('immutable')):
        raise ValueError('Expected the existing public stable 7.14 release')
    existing = {a['name']: a for a in release['assets']}
    for original in plan['original_assets']:
        current = existing.get(original['name'], {})
        if any(current.get(k) != v for k, v in {
                'id': original['id'], 'size': original['bytes'], 'digest': original['digest']}.items()):
            raise ValueError('An existing application asset changed')
    for entry in plan['assets']:
        previous = existing.get(entry['name'])
        if previous and (previous['size'] != entry['bytes']
                         or previous.get('digest') != 'sha256:' + entry['sha256']):
            raise ValueError('Existing manual asset differs; never overwrite it')
    return existing


def publish(plan):
    if (plan.get('schema') != 1 or plan.get('tag') != TAG
            or plan.get('release_id') != RELEASE_ID or len(plan['assets']) != 2
            or {e['name'] for e in plan['assets']} != set(NAMES)
            or len(plan['original_assets']) != 4):
        raise ValueError('Unexpected manual publication plan')
    release_url = API + '/releases/' + str(RELEASE_ID)
    release = api(release_url)
    existing = verify_release(release, plan)
    # Reconstruct and verify both documents before publishing either one.
    prepared = []
    for entry in plan['assets']:
        validate_asset(entry)
        if entry.get('content_type') != NAMES[entry['name']]:
            raise ValueError('Unexpected document content type')
        prepared.append((entry, asset_bytes(entry)))
    for entry, body in prepared:
        if entry['name'] in existing:
            continue
        upload = API.replace('api.github.com', 'uploads.github.com')
        upload += '/releases/' + str(RELEASE_ID) + '/assets?'
        upload += urllib.parse.urlencode({'name': entry['name']})
        uploaded = api(upload, 'POST', body, NAMES[entry['name']])
        if (uploaded['size'] != entry['bytes']
                or uploaded.get('digest') != 'sha256:' + entry['sha256']):
            raise ValueError('Published document checksum did not verify')
    current = api(release_url)
    verified = verify_release(current, plan)
    if not set(NAMES).issubset(verified):
        raise ValueError('Missing published document')
    body = current.get('body') or ''
    if MARKER in body and DOCS not in body:
        raise ValueError('Review the existing manual section before editing it')
    if DOCS not in body:
        updated = api(release_url, 'PATCH', {'body': body.rstrip() + '\n\n' + DOCS + '\n'})
        verify_release(updated, plan)
        if DOCS not in updated['body']:
            raise ValueError('Manual links were not saved')
    receipt = {'release': current['html_url'], 'assets': [
        {'name': e['name'], 'sha256': e['sha256'], 'bytes': e['bytes'],
         'url': verified[e['name']]['browser_download_url']} for e in plan['assets']]}
    print(json.dumps(receipt))
    return receipt


if __name__ == '__main__':
    publish(json.loads((ROOT / 'manual-publish-plan.json').read_text()))
