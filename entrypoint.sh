#!/bin/sh

python3 -m apfs_scan.apfs_cli.apfs_cli_parser -s last_updated_date -o ./www/api/scan_results
python3 -m http.server --directory ./www/ 8080