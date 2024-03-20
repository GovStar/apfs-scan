import json
import logging
from os import access, W_OK
from typing import List, Dict, Optional, Any
import requests
from pandas import DataFrame, read_json
from os.path import exists
from requests import Session
from apfs_scan.apfs_api.utils import exception_log_and_exit


class WayBackApfsSession:
    APFS_URL: str = 'apfs-cloud.dhs.gov/api/forecast/*'
    WAYBACK_API_ENDPOINT: str = 'https://archive.org/wayback/available'

    session: requests.Session
    home_page: requests.Response
    payload: Dict[str, str] = {"url": APFS_URL}
    header: Dict[str, str] = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'}
    forcast_records_json: dict[str, Any]
    forcast_history_json: dict[str, Any]
    apfs_file_path: str
    forcast_records_df: DataFrame
    apfs_file_exist: bool
    response: Optional[requests.Response] = None
    DATA_DICT_COLUMNS: List[str]
    data_time_stamp: float
    logger: logging.Logger
    no_connect: bool = False

    def __init__(self, apfs_file_path: str):
        self.logger = logging.getLogger(__name__)
        self.apfs_file_path = apfs_file_path
        self.validate_output_file()
        if not self.no_connect:
            self.setup_apfs_connection()
        self.write_apfs_data()
        self.update_data_dict_columns()

    def setup_apfs_connection(self) -> None:
        try:
            user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            self.session = Session()
            self.session.headers.update(self.header)
            self.forcast_history_json = self.session.get(url=self.WAYBACK_API_ENDPOINT, params=self.payload).json()
            if self.home_page.status_code != 200:
                self.logger.error("WayBack connection returned a bad status code")
                raise requests.HTTPError("WayBack connection returned a bad status code")
            else:
                self.logger.debug("APFS connection good status code: " + str(self.home_page.status_code))
        except requests.HTTPError as e:
            self.logger.error("WayBack connection returned a bad status code")
            exception_log_and_exit(e)
        except requests.RequestException as e:
            self.logger.error("WayBack request connection error")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("WayBack unhandled error: " + str(e))
            exception_log_and_exit(e)

    def populate_data_history(self) -> None:
        try:
            self.forcast_records_json = self.session.get(
                url=self.forcast_history_json['archived_snapshots']['closest']['url']).json()
            self.forcast_records_df = DataFrame.from_dict(self.forcast_records_json)
        except requests.HTTPError as e:
            self.logger.error("WayBack connection returned a bad status code")
            exception_log_and_exit(e)
        except requests.RequestException as e:
            self.logger.error("WayBack request connection error")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("WayBack unhandled error: " + str(e))
            exception_log_and_exit(e)

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
            self.logger.error("APFS update_data_dict_columns unhandled error: " + str(e))
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
            self.logger.error("APFS validate_apfs_data unhandled error: " + str(e))
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

    def validate_output_file(self) -> None:
        self.logger.debug(self.apfs_file_path)
        try:
            # Checks if file exists and is writeable
            access(self.apfs_file_path, W_OK)
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

    def write_apfs_data(self) -> None:
        try:
            with open(self.apfs_file_path, 'w', encoding='utf-8') as outfile:
                self.logger.debug("Writing apfs forcast data to file")
                DataFrame.to_json(self.forcast_records_df, outfile)
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
                self.forcast_records_df = read_json(outfile)
        except ValueError as e:
            self.logger.error("APFS returned a bad type when writing to file")
            exception_log_and_exit(e)
        except FileNotFoundError as e:
            self.logger.error("APFS file path does not exist")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS write_apfs_data unhandled error: " + str(e))
            exception_log_and_exit(e)

    def pull_historic_data(self) -> None:
        try:
            self.forcast_records_df = DataFrame.from_json(self.apfs_file_path)
        except ValueError as e:
            self.logger.error("APFS returned a bad type when reading from file")
            exception_log_and_exit(e)
        except FileNotFoundError as e:
            self.logger.error("APFS file path does not exist")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS pull_historic_data unhandled error: " + str(e))
            exception_log_and_exit(e)
