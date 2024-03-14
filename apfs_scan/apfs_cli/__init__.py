from apfs_scan.apfs_cli.apfs_cli_parser import (
    ApfsArgParser,
)

#from ..apfs_api import *

def init_apfs_cli_logger():
    import logging
    logging.basicConfig(filename='apfs_cli.log', level=logging.INFO)
    logging.debug('Starting apfs_cli')
