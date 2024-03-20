import unittest
from os.path import abspath

import requests

from apfs_scan.apfs_api.apfs_wayback_api_hooks import WayBackApfsSession


class ApfsParserTesting(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ApfsParserTesting, self).__init__(*args, **kwargs)

    def test_init_waybackapfsession(self):
        self.assertIsInstance(WayBackApfsSession(apfs_file_path=abspath(".\\testfiles\\waybacktest.json")),
                              WayBackApfsSession)

    def test


if __name__ == '__main__':
    unittest.main()
