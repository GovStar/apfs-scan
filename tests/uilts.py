from pandas import read_json


def load_test_json_into_dataframe():
    return read_json(path_or_buf='request-response-examples\\apfs-cloud.dhs.gov.json')

