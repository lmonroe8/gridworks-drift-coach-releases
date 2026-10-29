import copy
import hashlib
import json
import unittest
from unittest.mock import patch

import publish_manual as p


class ManualPublicationTests(unittest.TestCase):
    def setUp(self):
        self.plan = json.loads((p.ROOT / 'manual-publish-plan.json').read_text())
        self.release = {
            'id': p.RELEASE_ID, 'tag_name': p.TAG, 'draft': False, 'prerelease': False,
            'body': 'Existing release notes', 'html_url': 'https://github.com/example/release',
            'assets': [{'id': e['id'], 'name': e['name'], 'size': e['bytes'],
                        'digest': e['digest']} for e in self.plan['original_assets']],
        }
        self.calls = []

    def api(self, url, method='GET', body=None, kind='application/json'):
        self.calls.append((url, method, body, kind))
        if method == 'POST':
            name = p.urllib.parse.parse_qs(p.urllib.parse.urlsplit(url).query)['name'][0]
            e = next(e for e in self.plan['assets'] if e['name'] == name)
            uploaded = {'name': name, 'size': e['bytes'], 'digest': 'sha256:' + e['sha256'],
                        'browser_download_url': p.BASE + name}
            self.release['assets'].append(uploaded)
            return copy.deepcopy(uploaded)
        if method == 'PATCH':
            self.assertEqual(set(body), {'body'})
            self.release.update(body)
        return copy.deepcopy(self.release)

    def publish(self):
        with patch.object(p, 'api', self.api), patch.object(p, 'asset_bytes', return_value=b'document'):
            return p.publish(self.plan)

    def test_adds_only_documents_and_preserves_notes(self):
        original = copy.deepcopy(self.release['assets'])
        self.publish()
        self.assertEqual(self.release['assets'][:4], original)
        self.assertEqual(len(self.release['assets']), 6)
        self.assertTrue(self.release['body'].startswith('Existing release notes\n\n'))
        self.assertIn(p.DOCS, self.release['body'])

    def test_retry_does_not_upload_or_edit_again(self):
        self.publish()
        self.calls.clear()
        self.publish()
        self.assertTrue(all(c[1] == 'GET' for c in self.calls))

    def test_changed_application_asset_stops_before_write(self):
        self.release['assets'][0]['digest'] = 'sha256:changed'
        with self.assertRaises(ValueError):
            self.publish()
        self.assertTrue(all(c[1] == 'GET' for c in self.calls))

    def test_conflicting_document_is_never_replaced(self):
        self.release['assets'].append({'name': next(iter(p.NAMES)), 'size': 1, 'digest': 'sha256:changed'})
        with self.assertRaises(ValueError):
            self.publish()
        self.assertTrue(all(c[1] == 'GET' for c in self.calls))

    def test_both_transfers_verify_before_publication(self):
        with patch.object(p, 'api', self.api), patch.object(p, 'asset_bytes', side_effect=[b'document', ValueError('checksum')]):
            with self.assertRaises(ValueError):
                p.publish(self.plan)
        self.assertTrue(all(c[1] == 'GET' for c in self.calls))

    def test_other_release_rejected(self):
        self.plan['release_id'] += 1
        with self.assertRaises(ValueError):
            self.publish()
        self.assertEqual(self.calls, [])


if __name__ == '__main__':
    unittest.main()
