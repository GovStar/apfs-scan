import requests
from dataclasses import dataclass
from requests import request, Session, cookies


@dataclass
class ApfsSession:
    session: requests.Session = Session()
    home_page: requests.Response = session.get(url='https://apfs-cloud.dhs.gov')
    forcast_records_json = session.get(url='https://apfs-cloud.dhs.gov/api/forecast/').json()
    apfs_cookie: str = home_page.cookies.items()[0][1]


if __name__ == '__main__':
    ApfsSession()
