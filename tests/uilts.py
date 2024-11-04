from pandas import read_json, DataFrame


def load_test_json_into_dataframe() -> DataFrame:
    return read_json(path_or_buf='request-response-examples\\apfs-cloud.dhs.gov.json')

