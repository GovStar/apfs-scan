import argparse
from apfs_api.utils import DATA_DICT_COLUMNS


class ApfsArgParser():
    parser: argparse.ArgumentParser

    def __init__(self):
        self.parser = self.init_parser()
        self.parse_args()
        self.add_filter_args()

    def init_parser(self) -> argparse.ArgumentParser:
        return argparse.ArgumentParser(
            prog='apfs_cli',
            description='A cli to search, agate, and export acquisition forecasts',
        )

    def parse_args(self):
        self.parser.add_argument(
            "--field", "-c",
            action="extend",
            nargs="*",
            choices=DATA_DICT_COLUMNS,
        )

        self.parser.add_argument(
            "--sort", "-s",
            action="store",
            nargs=1,
            choices=DATA_DICT_COLUMNS,
        )

    def add_filter_args(self):
        # Here be dragons
        for flag in DATA_DICT_COLUMNS:
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
