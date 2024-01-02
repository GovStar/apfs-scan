import requests, toml, boto3, ssl, urllib3, json, pprint
from datetime import datetime

##Global Variables
APFS_URL = 'https://apfs-cloud.dhs.gov/api/forecast/'
APFS_DATA = []

##Functions

# Enables custom HTTP adapater using the custom SSL options
class CustomHttpAdapter (requests.adapters.HTTPAdapter):
    '''Transport adapter" that allows us to use custom ssl_context.'''

    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = urllib3.poolmanager.PoolManager(
            num_pools=connections, maxsize=maxsize,
            block=block, ssl_context=self.ssl_context)

# Enables legacy SSL settings due to government websites not being fully supported with SSL 3.0
def get_legacy_session():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    ctx.options |= 0x4  # OP_LEGACY_SERVER_CONNECT
    session = requests.session()
    session.mount('https://', CustomHttpAdapter(ctx))
    return session

# Request the data from the API
def get_apfs_data():
    apfs = get_legacy_session().get(APFS_URL)
    apfs.data = json.loads(apfs.text)
    print("Queriried the data from the APFS API")
    return apfs.data[0]

def apfs_data(force_refresh=False):
    global APFS_DATA
    if len(APFS_DATA) == 0 or force_refresh:
        APFS_DATA = get_apfs_data()
    return APFS_DATA

##MAIN LOGIC
r = apfs_data()
print(r.keys())

# print(get_apfs_data())