import unittest
import requests

from apfs_scan.apfs_api.apfs_cloud_api_hooks import ApfsSession


class ApfsHookTesting(unittest.TestCase):
    apfs_api: ApfsSession

    def __init__(self, *args, **kwargs):
        super(ApfsHookTesting, self).__init__(*args, **kwargs)
        self.apfs_api = ApfsSession()

    def test_apfs_json(self):
        self.assertIsNotNone(self.apfs_api.forcast_records_json)
        self.assertGreaterEqual(len(self.apfs_api.forcast_records_json), 1)


if __name__ == '__main__':
    unittest.main()
