import unittest
from os import system


from apfs_scan.apfs_cli import apfs_cli_parser

class ApfsParserTesting(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(ApfsParserTesting, self).__init__(*args, **kwargs)

    def test_cli_filering(self):
        system('python -m apfs_scan.apfs_cli.python apfs_cli --organization "DHS HQ" --sort "organization"')

if __name__ == '__main__':
    unittest.main()