import argparse
import json
from apfs_scan.apfs_api.utils import DATA_DICT_COLUMNS, exception_log_and_exit
from apfs_scan.apfs_api.apfs_cloud_api_hooks import ApfsSession
from apfs_scan.apfs_api.forecast_parser import filter_on_field, load_apfs_data
from pandas import DataFrame
from os import getcwd
from os.path import abspath, exists, join, basename
import logging


class ApfsArgParser():
    parser: argparse.ArgumentParser

    def __init__(self):
        self.init_logging()
        self.init_parser()
        self.add_filter_args()

    def init_logging(self) -> None:
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

        #self.parser.add_argument(
            #"--forcast_records", "--out", "-o",
            #action="store",
            #nargs=1,
            #type=argparse.FileType('rw', encoding='utf-8'),
            #default=abspath(join(getcwd(), "/apf-data/apfs-forecast-data.json")),
        #)

    def add_filter_args(self) -> None:
        # Generate the filter arguments dynamically from the DATA_DICT_COLUMNS pulled from the API
        for flag in DATA_DICT_COLUMNS:
            self.parser.add_argument(
                f"--{flag}",
                action="store",
                help=f"Filter the results by {flag} specified",
                nargs='?',
            )


def apfs_cli_wrapper():
    #apfs_api = ApfsSession()

    apfs_cli = ApfsArgParser()
    logging.debug('Created cli parser')

    args = vars(apfs_cli.parser.parse_args())

    for flag in DATA_DICT_COLUMNS:
        if args[flag] is not None:
            print(filter_on_field(load_apfs_data(
                json.load(open(".\\request-response-examples\\apfs-cloud.dhs.gov.json", encoding='utf-8'))),
                                  field=flag, value=args[flag]))

    logging.debug('apfs_cli args: ' + str(args))

def validate_output_file(file_path):
    try:
        if not exists(file_path):
            logging.error("File path does not exist")
            raise FileNotFoundError
    except FileNotFoundError as e:
        create_outfile(file_path)
    except Exception as e:
        exception_log_and_exit(e)

def create_outfile(file_path):
    return True


if __name__ == '__main__':
    apfs_cli_wrapper()
