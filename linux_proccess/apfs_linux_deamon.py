import os
import grp
import signal
import daemon
import lockfile

from apfs_api.forecast_parser import ApfsForecastParser
from apfs_scan.apfs_api.apfs_cloud_api_hooks import ApfsSession

context = daemon.DaemonContext(
    working_directory='/opt/apfs_scanner/',
    umask=0o002,
    pidfile=lockfile.FileLock('/var/run/spam.pid'),
    logfile = open('/var/log/apfsScanner/apfs-scanner.log', 'w+'),
    )

context.signal_map = {
    signal.SIGTERM: program_cleanup,
    signal.SIGHUP: 'terminate',
    signal.SIGUSR1: reload_program_config,
    }

mail_gid = grp.getgrnam('mail').gr_gid
context.gid = mail_gid

important_file = open('spam.data', 'w')
interesting_file = open('eggs.data', 'w')
context.files_preserve = [important_file, interesting_file]

LINUX_DAEMON_FILE_PATH: str = '/opt/apfs_scanner/workingdatabase.json'
main_data_file = open(LINUX_DAEMON_FILE_PATH)
context.files_preserve = [main_data_file]

entry_point()

def entry_point():
    # This is where the program starts
    apfs_handler: ApfsForecastParser = ApfsForecastParser(LINUX_DAEMON_FILE_PATH)
    ApfsSession()