import argparse
import json
from typing import Any

from apfs_scan.apfs_api.utils import DATA_DICT_COLUMNS, exception_log_and_exit
from apfs_scan.apfs_api.apfs_cloud_api_hooks import ApfsSession
from apfs_scan.apfs_api.forecast_parser import ApfsForecastParser
from apfs_scan.apfs_cli.prettyprintformate import pretty_print_forecast_data
from os import getcwd
from os.path import abspath, exists, dirname
import logging


def path_vail(path: str):
    path = abspath(path)
    if exists(dirname(path)):
        return path
    else:
        raise NotADirectoryError(path)


class TestingFileAction(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        setattr(namespace, self.dest, values)

        self.validate_output_file()

    def validate_output_file(file_path):
        try:
            if not exists(file_path):
                logging.error("File path does not exist")
                raise FileNotFoundError
        except FileNotFoundError as e:
            exception_log_and_exit(e)
        except Exception as e:
            exception_log_and_exit(e)

    def create_outfile(file_path):
        return True


class ApfsArgParser:
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

        self.parser.add_argument(
            "--forcast-records", "--out", "-o",
            action="store",
            nargs=1,
            type=path_vail,
        )

    def add_filter_args(self) -> None:
        # Generate the filter arguments dynamically from the DATA_DICT_COLUMNS pulled from the API
        try:
            for flag in DATA_DICT_COLUMNS:
                self.parser.add_argument(
                    f"--{flag}",
                    action="store",
                    help=f"Filter the results by {flag} specified",
                    nargs='?',
                )
        except NameError as e:
            pass
        except Exception as e:
            exception_log_and_exit(e)


def apfs_cli_wrapper():
    logger = logging.getLogger(__name__)

    apfs_cli: ApfsArgParser = ApfsArgParser()
    logger.debug('Created cli parser')
    logger.debug("CWD: " + str(getcwd()))
    args: dict[str, Any] = vars(apfs_cli.parser.parse_args())
    logger.debug('apfs_cli args: ' + str(args))
    logger.debug('Input path: ' + str(args['forcast_records']))

    apfs_handler = ApfsForecastParser(apfs_file_path=args['forcast_records'][0])

    if apfs_handler.data_ofd:
        logger.debug('Pulling new data from API')
        apfs_api = ApfsSession()
        apfs_handler.apfs_data = apfs_api.forcast_records_df.copy()
        apfs_handler.write_apfs_data()

    filter_fields: dict = {k: v for k, v in args.items() if v is not None and k in apfs_handler.apfs_data.columns.values}
    display_fields: list = list(set(DATA_DICT_COLUMNS) & set(args.keys()))

    logger.debug('filter_fields: ' + str(filter_fields))
    logger.debug('display_fields: ' + str(display_fields[0:10]))

    apfs_handler.filter_view_on_field(select_values=filter_fields)
    # apfs_handler.filter_view_on_field(field=display_fields, select_values=filter_fields)
    # print(pretty_print_forecast_data(apfs_handler.apfs_data_view, display_fields=display_fields))
    print(str(apfs_handler.apfs_data_view))


if __name__ == '__main__':
    apfs_cli_wrapper()
