import unittest
from os.path import abspath
from typing import Any

import requests

from apfs_scan.apfs_api.apfs_wayback_api_hooks import WayBackApfsSession


class ApfsParserTesting(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ApfsParserTesting, self).__init__(*args, **kwargs)

    @unittest.skip('Work in progress')
    def test_init_wayback_apfs_session(self):
        self.assertIsInstance(WayBackApfsSession(),
                              WayBackApfsSession)

    @unittest.skip('Work in progress')
    def test_api_apfs_call(self):
        wb_api: WayBackApfsSession = WayBackApfsSession()
        wb_api.api_apfs_call()
        self.assertIsInstance(wb_api.forcast_history_json, dict[str, Any])


if __name__ == '__main__':
    pass
    #unittest.main()
