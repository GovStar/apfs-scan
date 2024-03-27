import json
import logging
from os import access, W_OK
from typing import List, Dict, Optional, Any
import requests
from pandas import DataFrame, read_json
from os.path import exists
from gzip import GzipFile, decompress
from requests import Session
from io import BytesIO
from apfs_scan.apfs_api.utils import exception_log_and_exit


class WayBackApfsSession:
    APFS_URL: str = 'apfs-cloud.dhs.gov/api/forecast/*'
    WAYBACK_API_ENDPOINT: str = 'https://archive.org/wayback/available'

    session: requests.Session
    wayback_response: requests.Response
    payload: Dict[str, str] = {"url": APFS_URL,
                               "output": "json",
                               }
    header: Dict[str, str] = {
        "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'}
    forcast_history_json: dict[str, Any]
    apfs_file_path: str
    apfs_gzip_response: bytes
    max_tries: int = 3
    # 5 second cooldown between api calls, to prevent getting blocked
    api_call_cooldown: int = 5
    forcast_records_df: DataFrame
    apfs_file_exist: bool
    response: Optional[requests.Response] = None
    DATA_DICT_COLUMNS: List[str]
    data_time_stamp: float
    logger: logging.Logger
    no_connect: bool = False

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.api_apfs_call()
        self.populate_data_history()
        self.update_data_dict_columns()

    def api_apfs_call(self) -> None:
        try:
            self.session = Session()
            self.session.headers.update(self.header)
            self.session.params = self.payload
            self.session.adapters.DEFAULT_RETRIES = self.max_tries
            self.wayback_response = self.session.get(url=self.WAYBACK_API_ENDPOINT, params=self.payload)
            self.forcast_history_json = self.wayback_response.json()
            if self.wayback_response.status_code != 200:
                self.logger.error("WayBack connection returned a bad status code")
                raise requests.HTTPError("WayBack connection returned a bad status code")
            else:
                self.logger.debug("APFS connection good status code: " + str(self.wayback_response.status_code))
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
            self.forcast_records_df = DataFrame.from_dict(self.forcast_history_json['archived_snapshots']['closest']['url'])
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
            json.loads(json.dumps(self.forcast_history_json))
            if len(self.forcast_history_json) < 1:
                self.logger.error("APFS returned no data")
            else:
                self.logger.debug("APFS returned data")
        except ValueError as e:
            self.logger.error("APFS returned a bad or no JSON data")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS validate_apfs_data unhandled error: " + str(e))
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

    def decompress_apfs_response(self) -> None:
        try:
            self.forcast_history_json = decompress(self.apfs_gzip_response)
        except ValueError as e:
            self.logger.error("APFS returned a bad type when decompressing")
            exception_log_and_exit(e)
        except Exception as e:
            self.logger.error("APFS decompress_apfs_response unhandled error: " + str(e))
            exception_log_and_exit(e)