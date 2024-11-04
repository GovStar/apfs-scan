ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY APFS_DATA ./APFS_DATA

COPY apfs_scan ./apfs_scan

COPY config.toml .

# Run the application.
CMD python3 -m apfs_scan.apfs_cli.apfs_cli_parser -o APFS_DATA/scan_resutls --sort last_updated_date