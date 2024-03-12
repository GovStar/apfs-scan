import pandas as pd
from apfs_api.apfs_cloud_api_hooks import ApfsSession
import json


def load_APFS_data(apfsJson: json) -> pd.DataFrame:
    return pd.DataFrame(apfsJson)



