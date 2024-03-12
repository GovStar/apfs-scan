import unittest
import requests

from apfs_api.apfs_cloud_api_hooks import ApfsSession


class ApfsHookTesting(unittest.TestCase):
    apfs_api: ApfsSession

    def __init__(self, *args, **kwargs):
        super(ApfsHookTesting, self).__init__(*args, **kwargs)
        self.apfs_api = ApfsSession()

    def test_apfs_session(self):
        self.assertIsInstance(self.apfs_api.home_page, requests.Response)

    def test_apfs_json(self):
        self.assertIsNotNone(self.apfs_api.forcast_records_json)
        self.assertGreaterEqual(len(self.apfs_api.forcast_records_json), 1)

    def test_apfs_session_cookie(self):
        # Python can convert str of hex to int, so this is a
        # good way to check if it is a valid cookie since it should be a long hex string.
        self.assertIsInstance(int(self.apfs_api.apfs_cookie, 16), int)


if __name__ == '__main__':
    unittest.main()
