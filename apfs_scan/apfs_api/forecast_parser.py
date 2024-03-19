import logging

import pandas as pd
from apfs_scan.apfs_api.apfs_cloud_api_hooks import ApfsSession
from apfs_scan.apfs_api.utils import DATA_DICT_COLUMNS
import json
import logging


def load_apfs_data(apfs_json) -> pd.DataFrame:
    return pd.DataFrame(apfs_json)


def filter_on_field(data: pd.DataFrame, field: DATA_DICT_COLUMNS, value: str) -> pd.DataFrame:
    filtered_data = data[data[field] == value]
    if filtered_data.empty:
        logging.info(f"No data found for {field} with value {value}")
    return filtered_data
