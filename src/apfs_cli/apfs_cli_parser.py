import argparse
from apfs_api.utils import DATA_DICT_COLUMNS
from apfs_api.apfs_cloud_api_hooks import ApfsSession
from pandas import DataFrame
import logging

class ApfsArgParser():
    parser: argparse.ArgumentParser
    apfs_api: ApfsSession
    def __init__(self):
        self.init_logging()
        self.init_apfs_api()
        self.init_parser()
        self.parse_args()
        self.add_filter_args()

    def init_apfs_api(self) -> None:
        self.apfs_api = ApfsSession()

    def init_logging(self) -> None:
        logging.basicConfig(filename='myapp.log', level=logging.INFO)
        logging.debug('Started CLI')

    def init_parser(self) -> None:
        self.parser = argparse.ArgumentParser(
            prog='apfs_cli',
            description='A cli to search, agate, and export acquisition forecasts',
        )

        self.parser.add_argument(
            "--sort", "-s",
            action="store",
            nargs=1,
            default="id",
            choices=DATA_DICT_COLUMNS,
        )

    def add_filter_args(self) -> None:
        # Generate the filter arguments dynamically from the DATA_DICT_COLUMNS pulled from the API
        for flag in self.apfs_api.DATA_DICT_COLUMNS:
            self.parser.add_argument(
                f"--{flag}",
                action="store",
                help=f"Filter the results by {flag} specified",
                nargs='?',
            )


def apfs_cli_wrapper():
    parser = ApfsArgParser().parser
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    apfs_cli_wrapper()
