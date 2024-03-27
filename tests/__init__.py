import os
import unittest
import sys


def init_apfs_cli_logger():
    import logging
    loggers = logging.getLogger(__name__)
    logging.basicConfig(filename='apfs_testing.log', level=logging.DEBUG)
    logging.debug('Starting unit tests')


init_apfs_cli_logger()
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "apfs_scan"
)
sys.path.append(SOURCE_PATH)

loader = unittest.TestLoader()
testSuite = loader.discover('tests')
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)
