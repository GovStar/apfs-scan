ARG PYTHON_VERSION=3.13
ARG OUTPUT_PATH=./APFS_DATA/
ARG OUTPUT_FILE=${OUTPUT_PATH}scan_results.json
FROM python:${PYTHON_VERSION}-slim as base

EXPOSE 8080

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY www ./www

COPY apfs_scan ./apfs_scan

COPY config.toml .

COPY entrypoint.sh .

# Run the application.
ENTRYPOINT ["/entrypoint.sh"]