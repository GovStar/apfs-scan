import unittest

from pandas import DataFrame

from src.apfs_api.forecast_parser import load_APFS_data
from src.apfs_api.apfs_cloud_api_hooks import ApfsSession
from src.apfs_api.utils import DATA_DICT_COLUMNS


class ApfsParserTesting(unittest.TestCase):

    apfs_api: ApfsSession

    def __init__(self, *args, **kwargs):
        super(ApfsParserTesting, self).__init__(*args, **kwargs)
        self.apfs_api = ApfsSession()

    def test_load_json_into_dataframe(self):
        self.assertIsInstance(load_APFS_data(self.apfs_api.forcast_records_json), DataFrame)
        self.assertGreaterEqual((load_APFS_data(self.apfs_api.forcast_records_json)).size, 1)
        # Checks current data against last know data columns
        self.assertListEqual(list(load_APFS_data(self.apfs_api.forcast_records_json)), DATA_DICT_COLUMNS)


if __name__ == '__main__':
    unittest.main()
