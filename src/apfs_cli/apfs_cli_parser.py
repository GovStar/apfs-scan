import argparse


class apfs_argparser():
    parser: argparse.ArgumentParser

    def __init__(self):
        self.parser = self.init_parser()

    def init_parser(self) -> argparse.ArgumentParser:
        return argparse.ArgumentParser(
            prog='apfs_cli',
            description='A cli to search, agate, and export acquisition forecasts',
        )

    def parse_args(self):
        self.parser.add_argument(
            "--color",
            action=ChoicesAction,
            nargs="+",
            action_values=["red", "blue", "green"],
        )
