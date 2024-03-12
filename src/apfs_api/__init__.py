from apfs_api.apfs_cloud_api_hooks import (
    ApfsSession,
)

from apfs_api.forecast_parser import (
    load_APFS_data,
)

from apfs_api.utils import (
    DATA_DICT_COLUMNS,
    exception_log_and_exit
)


def init_apfs_api_logger():
    import logging
    logging.basicConfig(filename='apfs_api.log', level=logging.INFO)
    logging.debug('Started apfs_api')