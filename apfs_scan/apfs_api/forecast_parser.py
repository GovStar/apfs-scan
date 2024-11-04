import logging
from os import access, W_OK
from time import time
from typing import List, Any

import pandas as pd
from pandas import DataFrame, read_json, Series
from pickle import PickleError

from apfs_scan.apfs_api.utils import DATA_DICT_COLUMNS, exception_log_and_exit
from os.path import getmtime, exists
import logging


def load_apfs_data(apfs_json) -> pd.DataFrame:
    return pd.DataFrame(apfs_json)


def filter_on_field(data: pd.DataFrame, field: DATA_DICT_COLUMNS, value: str) -> pd.DataFrame:
    filtered_data = data[data[field] == value]
    if filtered_data.empty:
        logging.info(f"No data found for {field} with value {value}")
    return filtered_data


class ApfsForecastParser:
    apfs_data: pd.DataFrame
    apfs_data_view: Any
    logger: logging.Logger
    data_ofd: bool = False
    data_time_stamp: float
    apfs_file_exist: bool
    apfs_file_path: str

    def __init__(self, apfs_file_path: str):
        self.logger = logging.getLogger(__name__)
        self.apfs_file_exist = False
        self.apfs_file_path = apfs_file_path
        self.validate_output_file()
        if self.apfs_file_exist:
            self.read_apfs_data()
            self.check_data_refresh()
        else:
            self.data_ofd = True

    def filter_view_on_field(self, select_values: dict[str, Any]) -> None:
        #self.apfs_data_view = self.apfs_data.loc[(self.apfs_data[list(select_values)] == Series(select_values)).all(axis=1)]
        mask = pd.Series([True] * len(self.apfs_data))
        for column, value in select_values.items():
            if column in self.apfs_data.columns:
                mask &= (self.apfs_data[column] == value)

        self.apfs_data_view = self.apfs_data[mask]
        self.logger.debug("apfs_data_view updated: "+str(self.apfs_data_view.head()))

    def validate_output_file(self) -> None:
        self.logger.debug("validate_output_file passed path: " + str(self.apfs_file_path))
        try:
            # Checks if file exists and is writeable
            access(self.apfs_file_path, W_OK)
            does_exist: bool = exists(self.apfs_file_path)
            logging.debug("File exist status: " + str(does_exist))
            self.apfs_file_exist = exists(self.apfs_file_path)
        except FileNotFoundError as e:
            self.logger.error("APFS file path is not writeable")
            exception_log_and_exit(e)
        except PermissionError as e:
            self.logger.error("APFS file path does not have write permissions")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS validate_output_file unhandled error: " + str(e))
            exception_log_and_exit(e)

    def check_data_refresh(self) -> None:
        # time uses ms since epoc and are in UTC time
        if not self.apfs_file_exist:
            self.logger.debug("APFS local data does not exist yet setting data to out of date")
            self.data_ofd = True
            # Exit function early if file does not exist
            return None

        self.data_time_stamp = getmtime(self.apfs_file_path)
        time_diff: float = time() - self.data_time_stamp
        self.logger.debug("APFS local vs remote data time difference: " + str(time_diff))

        # Checks if older than one week in seconds
        if time_diff > 100: #604800:
            self.data_ofd = True
            self.logger.debug(
                "APFS local not new enough, setting data_ofd to true and pulling more data: " + str(time_diff))
        else:
            self.logger.debug("APFS local new enough setting data_ofd to false " + str(time_diff))

    def write_apfs_data(self) -> None:
        try:
            self.logger.debug("Writing apfs forcast data to pickle file")
            DataFrame.to_pickle(self.apfs_data, self.apfs_file_path+'.pickle')
            DataFrame.to_json(self.apfs_data,  self.apfs_file_path+'.json')
            DataFrame.to_html(self.apfs_data, self.apfs_file_path+'.html')
            # DataFrame.to_html(self.apfs_data, )
        except PickleError as e:
            self.logger.error("APFS failed pickling when writing to file")
            exception_log_and_exit(e)
        except ValueError as e:
            self.logger.error("APFS returned a bad type when writing to file")
            exception_log_and_exit(e)
        except FileNotFoundError as e:
            self.logger.error("APFS file path does not exist")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS write_apfs_data unhandled error: " + str(e))
            exception_log_and_exit(e)

    def read_apfs_data(self) -> None:
        try:
            with open(self.apfs_file_path, 'r', encoding='utf-8') as outfile:
                self.logger.debug("Reading apfs forcast from file: " + self.apfs_file_path)
                self.apfs_data = DataFrame.read_pickle(outfile, compression='zstd')
            self.logger.debug("apfs_data read: " + str(self.apfs_data.head()))
        except ValueError as e:
            self.logger.error("APFS returned a bad type when writing to file")
            exception_log_and_exit(e)
        except FileNotFoundError as e:
            self.logger.error("APFS file path does not exist")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS write_apfs_data unhandled error: " + str(e))
            exception_log_and_exit(e)
