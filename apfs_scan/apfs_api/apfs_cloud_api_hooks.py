import json
import logging
from os import access, W_OK
from typing import List, Dict, Any, Optional
from time import time
import requests
from pandas import DataFrame, read_json
from requests import Session
from apfs_scan.apfs_api.utils import exception_log_and_exit


class ApfsSession:
    session: requests.Session
    home_page: requests.Response
    forcast_records_json: Optional[Dict[str, Any]]
    forcast_records_df: DataFrame
    DATA_DICT_COLUMNS: List[str]
    data_time_stamp: float
    logger: logging.Logger

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.setup_apfs_connection()
        self.update_data_dict_columns()

    def setup_apfs_connection(self) -> None:
        try:
            user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            self.session = Session()
            self.session.headers.update({'User-Agent': user_agent})
            self.home_page = self.session.get(url='https://apfs-cloud.dhs.gov')
            self.forcast_records_json = self.session.get(url='https://apfs-cloud.dhs.gov/api/forecast/').json()
            self.logger.debug('forcast_records_json: '+str(self.forcast_records_json[1:10]))
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

