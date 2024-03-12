import json
import logging
from typing import List, Any

import requests
from dataclasses import dataclass,field
from collections import defaultdict
from requests import request, Session, cookies
from apfs_api.utils import exception_log_and_exit,DATA_DICT_COLUMNS


@dataclass(init=True, repr=True, eq=True)
class ApfsSession:
    session: requests.Session = Session()
    home_page: requests.Response = session.get(url='https://apfs-cloud.dhs.gov')
    forcast_records_json = session.get(url='https://apfs-cloud.dhs.gov/api/forecast/').json()
    apfs_cookie: str = home_page.cookies.items()[0][1]
    DATA_DICT_COLUMNS: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.test_apfs_connection()
        self.validate_apfs_data()
        self.update_DATA_DICT_COLUMNS()

    def test_apfs_connection(self) -> bool:
        if self.home_page.status_code != 200:
            logging.error("APFS connection returned a bad status code")
            exception_log_and_exit(self.home_page.raise_for_status())
            return False
        else:
            logging.debug("APFS connection good status code: " + str(self.home_page.status_code))
        return True

    def validate_apfs_data(self) -> bool:
        try:
            # Will throw an error if not a valid type this works as type validating
            json.load(self.forcast_records_json)
            if len(self.forcast_records_json) < 1:
                logging.error("APFS returned no data")
                return False
            else:
                logging.debug("APFS returned data")
        except ValueError as e:
            logging.error("APFS returned a bad or no JSON data")
            exception_log_and_exit(e)
            return False
        except Exception as e:
            logging.error("APFS unknown error")
            exception_log_and_exit(e)
            return False
        return True

    def update_DATA_DICT_COLUMNS(self) -> None:
        try:
            self.DATA_DICT_COLUMNS = list(self.forcast_records_json[0].keys())
        except ValueError as e:
            logging.error("APFS dataframe data is bad")
            exception_log_and_exit(e)
            return False
        except Exception as e:
            logging.error("APFS unknown error")
            exception_log_and_exit(e)
            return False
        return True


if __name__ == '__main__':
    ApfsSession()
