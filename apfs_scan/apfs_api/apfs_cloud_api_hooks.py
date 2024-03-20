import json
import logging
from os import access, W_OK
from typing import List
from time import time
import requests
from pandas import DataFrame, read_json
from os.path import getmtime, exists
from requests import Session
from apfs_scan.apfs_api.utils import exception_log_and_exit


# TODO: update class to not touch files
class ApfsSession:
    session: requests.Session
    home_page: requests.Response
    forcast_records_json: dict
    apfs_cookie: str
    forcast_records_df: DataFrame
    apfs_file_exist: bool
    data_ofd: bool = False
    DATA_DICT_COLUMNS: List[str]
    data_time_stamp: float
    logger: logging.Logger

    def __init__(self, data_ofd: bool):
        self.data_ofd = data_ofd
        self.logger = logging.getLogger(__name__)
        self.check_data_refresh()
        if self.data_ofd:
            self.setup_apfs_connection()
        self.update_data_dict_columns()

    def setup_apfs_connection(self) -> None:
        try:
            user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            self.session = Session()
            self.session.headers.update({'User-Agent': user_agent})
            self.home_page = self.session.get(url='https://apfs-cloud.dhs.gov')
            self.forcast_records_json = self.session.get(url='https://apfs-cloud.dhs.gov/api/forecast/').json()
            self.forcast_records_df = DataFrame.from_dict(self.forcast_records_json)

            if self.home_page.status_code != 200:
                self.logger.error("APFS connection returned a bad status code")
                raise requests.HTTPError("APFS connection returned a bad status code")
            else:
                self.logger.debug("APFS connection good status code: " + str(self.home_page.status_code))

        except requests.HTTPError as e:
            self.logger.error("APFS connection returned a bad status code")
            exception_log_and_exit(e)
        except requests.RequestException as e:
            self.logger.error("APFS request connection error")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS unhandled error: "+str(e))
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

        if time_diff > 7200:
            self.data_ofd = True
        else:
            self.logger.debug("APFS local new enough not pulling more data: " + str(time_diff))

    def update_data_dict_columns(self) -> None:
        try:
            self.DATA_DICT_COLUMNS = self.forcast_records_df.columns.to_list()
        except ValueError as e:
            self.logger.error("APFS json data is bad")
            exception_log_and_exit(e)
        except TypeError as e:
            self.logger.error("APFS json return type is unexpected")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS update_data_dict_columns unhandled error: "+str(e))
            exception_log_and_exit(e)

    def validate_apfs_data(self) -> None:
        try:
            # Will throw an error if not a valid type this works as type validating
            json.loads(json.dumps(self.forcast_records_json))
            if len(self.forcast_records_json) < 1:
                self.logger.error("APFS returned no data")
            else:
                self.logger.debug("APFS returned data")
        except ValueError as e:
            self.logger.error("APFS returned a bad or no JSON data")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS validate_apfs_data unhandled error: "+str(e))
            exception_log_and_exit(e)

    def update_ofd_data(self) -> None:
        if self.data_ofd:
            self.logger.debug("APFS data is of date")
            self.forcast_records_json = self.get_apfs_data()
            self.update_data_dict_columns()
            self.data_ofd = False
            self.logger.info("APFS data updated")
        else:
            self.logger.debug("APFS data is not of date")
