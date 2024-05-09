from apfs_scan.apfs_cli.apfs_cli_parser import (
    ApfsArgParser,
)


def init_apfs_cli_logger():
    import logging
    loggers = logging.getLogger(__name__)
    logging.basicConfig(filename='/app/apfs_cli.log', level=logging.DEBUG)
    logging.debug('Starting apfs_cli')


init_apfs_cli_logger()
