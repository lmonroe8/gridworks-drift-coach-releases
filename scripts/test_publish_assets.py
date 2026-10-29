"""Integrity and credential isolation checks for the CI artifact transport."""
import base64
import hashlib
import io
import json
import os
import unittest
import zipfile
from unittest.mock import patch
os.environ.setdefault('GITHUB_REPOSITORY','lmonroe8/gridworks-drift-coach-releases')
os.environ.setdefault('GH_TOKEN','test-token-never-forward')
import publish_assets as p

class TransportTests(unittest.TestCase):
    def setUp(self):
        self.payload=b'checked installer fixture'
        self.entry=dict(name='Gridworks-Drift-Coach-Beta-2.0.zip',bytes=len(self.payload),
            sha256=hashlib.sha256(self.payload).hexdigest(),artifact_transport_blob='a'*40)
        stream=io.BytesIO()
        with zipfile.ZipFile(stream,'w') as z:z.writestr(self.entry['name'],self.payload)
        self.outer=stream.getvalue()
        self.ticket=dict(url='https://sdmntprcentralus.oaiusercontent.com/files/test/raw?se=fixture',
            bytes=len(self.outer),sha256=hashlib.sha256(self.outer).hexdigest(),member=self.entry['name'])
    def execute(self,ticket=None,outer=None,entry=None):
        descriptor=json.dumps(ticket or self.ticket).encode()
        class Opener:
            def open(inner,request,timeout):
                self.assertIsNone(request.get_header('Authorization'))
                self.assertNotIn('GH_TOKEN',dict(request.header_items()))
                return io.BytesIO(self.outer if outer is None else outer)
        with patch.object(p,'transfer_blob',return_value=descriptor),patch.object(p.urllib.request,'build_opener',return_value=Opener()):
            return p.asset_bytes(entry or self.entry)
    def test_valid_nested_asset_and_no_auth(self):self.assertEqual(self.execute(),self.payload)
    def test_outer_tamper_rejected(self):
        with self.assertRaisesRegex(ValueError,'transport checksum'):self.execute(outer=self.outer[:-1]+b'x')
    def test_inner_tamper_rejected(self):
        with self.assertRaisesRegex(ValueError,'Release checksum'):self.execute(entry={**self.entry,'sha256':'0'*64})
    def test_untrusted_url_rejected(self):
        for url in ['http://sdmntprcentralus.oaiusercontent.com/x','https://example.com/x',
                    'https://sdmntprcentralus.oaiusercontent.com.evil.test/x',
                    'https://user:pass@sdmntprcentralus.oaiusercontent.com/x']:
            with self.subTest(url=url),self.assertRaisesRegex(ValueError,'endpoint'):
                self.execute(ticket={**self.ticket,'url':url})
    def test_redirect_rejected(self):
        with self.assertRaisesRegex(ValueError,'redirects'):
            p.NoTransportRedirect().redirect_request(None,None,302,'',{},'https://example.com')
    def test_expansion_rejected_before_read(self):
        with self.assertRaisesRegex(ValueError,'size differs'):self.execute(entry={**self.entry,'bytes':len(self.payload)+1})
    def test_extra_archive_member_rejected(self):
        stream=io.BytesIO()
        with zipfile.ZipFile(stream,'w') as z:
            z.writestr(self.entry['name'],self.payload);z.writestr('unexpected',b'x')
        raw=stream.getvalue()
        with self.assertRaisesRegex(ValueError,'contents'):
            self.execute(ticket={**self.ticket,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()},outer=raw)
    def test_legacy_chunks_supported(self):
        entry={k:v for k,v in self.entry.items() if k!='artifact_transport_blob'}
        entry['chunks']=[dict(git_blob='a'*40,bytes=len(self.payload),sha256=entry['sha256'])]
        with patch.object(p,'transfer_blob',return_value=self.payload):self.assertEqual(p.asset_bytes(entry),self.payload)
class AssetLimitsTests(unittest.TestCase):
    def test_current_installer_size_is_supported(self):
        p.validate_asset(dict(name='Gridworks-Drift-Coach-Setup.zip',bytes=47_604_649))
    def test_invalid_or_unbounded_assets_are_rejected(self):
        for size in (0,-1,64_000_000,True,'47604649'):
            with self.subTest(size=size),self.assertRaises(ValueError):
                p.validate_asset(dict(name='Gridworks-Drift-Coach-Setup.zip',bytes=size))
        with self.assertRaises(ValueError):p.validate_asset(dict(name='../private.pem',bytes=100))

class ProductionReleaseTests(unittest.TestCase):
    def test_production_is_stable_and_latest(self):
        self.assertEqual(p.release_options(dict(schema=1,tag='v7.12.0',prerelease=False)),dict(prerelease=False,make_latest='true'))
    def test_legacy_beta_stays_prerelease(self):
        self.assertEqual(p.release_options(dict(schema=1,tag='beta-2.0.7.11.0')),dict(prerelease=True,make_latest='false'))
    def test_beta_tag_cannot_be_relabelled_as_production(self):
        with self.assertRaises(ValueError):p.release_options(dict(schema=1,tag='beta-2.0.7.11.0',prerelease=False))
if __name__=='__main__':unittest.main()


