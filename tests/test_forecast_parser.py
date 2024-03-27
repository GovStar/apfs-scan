import unittest
from os.path import abspath

from pandas import DataFrame

from apfs_scan.apfs_api.forecast_parser import load_apfs_data, filter_on_field, ApfsForecastParser
from apfs_scan.apfs_api.apfs_cloud_api_hooks import ApfsSession
from apfs_scan.apfs_api.utils import DATA_DICT_COLUMNS


class ApfsParserTesting(unittest.TestCase):
    apfs_api: ApfsSession

    def __init__(self, *args, **kwargs):
        super(ApfsParserTesting, self).__init__(*args, **kwargs)
        self.apfs_api = ApfsSession()

    def test_load_json_into_dataframe(self):
        self.assertIsInstance(load_apfs_data(self.apfs_api.forcast_records_json), DataFrame)
        self.assertGreaterEqual((load_apfs_data(self.apfs_api.forcast_records_json)).size, 1)
        # Checks current data against last know data columns
        self.assertListEqual(list(load_apfs_data(self.apfs_api.forcast_records_json)), DATA_DICT_COLUMNS)

    def test_filter_data_on_field(self):
        self.assertEqual(self.apfs_api.DATA_DICT_COLUMNS[2], 'organization')
        self.assertEqual((filter_on_field(load_apfs_data(apfs_json=self.apfs_api.forcast_records_json),
                                          field=DATA_DICT_COLUMNS[2], value='DHS HQ')).shape[0], 3)

    def test_Apfs_Forecast_Parser(self):
        self.assertIsInstance(ApfsForecastParser(apfs_file_path=abspath("./request-response-examples/apfs-cloud.dhs.gov.json")), ApfsForecastParser)
        self.assertGreaterEqual(ApfsForecastParser(apfs_file_path=abspath("./request-response-examples/apfs-cloud.dhs.gov.json")).apfs_data.size, 1)


if __name__ == '__main__':
    unittest.main()
