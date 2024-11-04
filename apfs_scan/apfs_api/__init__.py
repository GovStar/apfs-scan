from apfs_scan.apfs_api.apfs_cloud_api_hooks import (
    ApfsSession,
)

from apfs_scan.apfs_api.apfs_wayback_api_hooks import (
    WayBackApfsSession,
)

from apfs_scan.apfs_api.forecast_parser import (
    load_apfs_data,
    filter_on_field,
)

from apfs_scan.apfs_api.utils import (
    DATA_DICT_COLUMNS,
    exception_log_and_exit,
)


def init_apfs_api_logger():
    import logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S', level=logging.DEBUG, handlers=[
                            logging.FileHandler('apfs_api.log'),
                            # logging.StreamHandler()
                        ])
    logging.debug('Started apfs_api')


init_apfs_api_logger()
