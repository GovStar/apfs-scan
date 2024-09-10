## Why am I here?
The APFS Scanner is a way to quickly sort through the many contracts DHS posts on their [Aquisition Planning Forcast System](https://apfs-cloud.dhs.gov/). Their UI is quite clunky, and does not make it easy to sort through and view valuable information. This scanner is a way to pull out all relevant information from their API Endpoint, and save it in a JSON object for GovStar's planning purposes. 

## How do I run this thing locally?
1. Install the [Docker Desktop App](https://www.docker.com/products/docker-desktop/)
2. Open the Docker Desktop App, and ensure the Docker Engine is running. The bottom left corner should be green and sa "Engine running".
3. Run `docker compose up`. 
4. Click the Volume tab in the Docker Desktop App, and select the `apfs-scan_apfs_data` Volume. This is where we hold the data pulled from APFS.
5. Within the Volume, you will see a file named 'data_XX-XX-XXXX'. Select the file you want, and there will be a JSON object of all contracts pulled from the [APFS](https://apfs-cloud.dhs.gov/) API that day.

## What are the product implications? 
After running the scanner, you will get a file with a JSON object of all the contracts pulled from the APFS API.

## Key Functionality of the APFS Scanner
- Capture changes day-to-day to APFS records
    - Hash previous day records and compare to current day records
- Notify if key-words are found
- Filter and display data for internal research purposes
- Use pytest for testing 