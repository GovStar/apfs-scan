


## Key Functionality
- capture changes day-to-day to APFS records
    - Hash previous day records and compare to current day records
- Notify if key-words are found
- filter and display data for internal research purposes 
- Use pytest for testing 

## Example

Command `python3 -m apfs_scan.apfs_cli.apfs_cli_parser -o APFS_DATA/scan_resutls --sort last_updated_date`

Oputput: 
```console
<frozen runpy>:128: RuntimeWarning: 'apfs_scan.apfs_cli.apfs_cli_parser' found in sys.modules after import of package 'apfs_scan.apfs_cli', but prior to execution of 'apfs_scan.apfs_cli.apfs_cli_parser'; this may result in unpredictable behaviour
        id mission  ... published_date previous_published_date
0    67080    None  ...     10/03/2024                    None
1    67082    None  ...     10/07/2024                    None
2    68483    None  ...     10/29/2024                    None
3    52728    None  ...     07/01/2021              10/26/2020
4    64441    None  ...     02/22/2024              11/02/2023
..     ...     ...  ...            ...                     ...
838  66540    None  ...     06/10/2024                    None
839  68503    None  ...     10/11/2024                    None
840  68502    None  ...     10/16/2024                    None
841  68518    None  ...     10/16/2024                    None
842  68519    None  ...     10/16/2024                    None

[843 rows x 43 columns]
```


## HELP

Output of `python3 -m apfs_scan.apfs_cli.apfs_cli_parser -o APFS_DATA/scan_resutls --sort last_updated_date --help`

```console
usage: apfs_cli [-h]
                [--sort {id,mission,organization,small_business_program,dollar_range,contract_vehicle,competitive,award_quarter,estimated_release_date,publish_date,previous_publish_date,requirements_contact_phone,naics,apfs_number,requirements_title,requirement,contract_status,contractor,contract_number,estimated_period_of_performance_start,estimated_period_of_performance_end,anticipated_award_date,estimated_solicitation_release_date,place_of_performance_city,place_of_performance_state,requirements_contact_first_name,requirements_contact_last_name,requirements_contact_email,alternate_contact_first_name,alternate_contact_last_name,alternate_contact_phone,alternate_contact_email,fiscal_year,created_on,requirements_office,contracting_office,apfs_coordinator_office,current_state,last_updated_date,published_date,previous_published_date}]
                [--forcast-records FORCAST_RECORDS] [--id [ID]]
                [--mission [MISSION]] [--organization [ORGANIZATION]]
                [--small_business_program [SMALL_BUSINESS_PROGRAM]]
                [--dollar_range [DOLLAR_RANGE]]
                [--contract_vehicle [CONTRACT_VEHICLE]]
                [--competitive [COMPETITIVE]]
                [--award_quarter [AWARD_QUARTER]]
                [--estimated_release_date [ESTIMATED_RELEASE_DATE]]
                [--publish_date [PUBLISH_DATE]]
                [--previous_publish_date [PREVIOUS_PUBLISH_DATE]]
                [--requirements_contact_phone [REQUIREMENTS_CONTACT_PHONE]]
                [--naics [NAICS]] [--apfs_number [APFS_NUMBER]]
                [--requirements_title [REQUIREMENTS_TITLE]]
                [--requirement [REQUIREMENT]]
                [--contract_status [CONTRACT_STATUS]]
                [--contractor [CONTRACTOR]]
                [--contract_number [CONTRACT_NUMBER]]
                [--estimated_period_of_performance_start [ESTIMATED_PERIOD_OF_PERFORMANCE_START]]
                [--estimated_period_of_performance_end [ESTIMATED_PERIOD_OF_PERFORMANCE_END]]
                [--anticipated_award_date [ANTICIPATED_AWARD_DATE]]
                [--estimated_solicitation_release_date [ESTIMATED_SOLICITATION_RELEASE_DATE]]
                [--place_of_performance_city [PLACE_OF_PERFORMANCE_CITY]]
                [--place_of_performance_state [PLACE_OF_PERFORMANCE_STATE]]
                [--requirements_contact_first_name [REQUIREMENTS_CONTACT_FIRST_NAME]]
                [--requirements_contact_last_name [REQUIREMENTS_CONTACT_LAST_NAME]]
                [--requirements_contact_email [REQUIREMENTS_CONTACT_EMAIL]]
                [--alternate_contact_first_name [ALTERNATE_CONTACT_FIRST_NAME]]
                [--alternate_contact_last_name [ALTERNATE_CONTACT_LAST_NAME]]
                [--alternate_contact_phone [ALTERNATE_CONTACT_PHONE]]
                [--alternate_contact_email [ALTERNATE_CONTACT_EMAIL]]
                [--fiscal_year [FISCAL_YEAR]] [--created_on [CREATED_ON]]
                [--requirements_office [REQUIREMENTS_OFFICE]]
                [--contracting_office [CONTRACTING_OFFICE]]
                [--apfs_coordinator_office [APFS_COORDINATOR_OFFICE]]
                [--current_state [CURRENT_STATE]]
                [--last_updated_date [LAST_UPDATED_DATE]]
                [--published_date [PUBLISHED_DATE]]
                [--previous_published_date [PREVIOUS_PUBLISHED_DATE]]

A cli to search, agate, and export acquisition forecasts

options:
  -h, --help            show this help message and exit
  --sort, -s {id,mission,organization,small_business_program,dollar_range,contract_vehicle,competitive,award_quarter,estimated_release_date,publish_date,previous_publish_date,requirements_contact_phone,naics,apfs_number,requirements_title,requirement,contract_status,contractor,contract_number,estimated_period_of_performance_start,estimated_period_of_performance_end,anticipated_award_date,estimated_solicitation_release_date,place_of_performance_city,place_of_performance_state,requirements_contact_first_name,requirements_contact_last_name,requirements_contact_email,alternate_contact_first_name,alternate_contact_last_name,alternate_contact_phone,alternate_contact_email,fiscal_year,created_on,requirements_office,contracting_office,apfs_coordinator_office,current_state,last_updated_date,published_date,previous_published_date}
  --forcast-records, --out, -o FORCAST_RECORDS
  --id [ID]             Filter the results by id specified
  --mission [MISSION]   Filter the results by mission specified
  --organization [ORGANIZATION]
                        Filter the results by organization specified
  --small_business_program [SMALL_BUSINESS_PROGRAM]
                        Filter the results by small_business_program specified
  --dollar_range [DOLLAR_RANGE]
                        Filter the results by dollar_range specified
  --contract_vehicle [CONTRACT_VEHICLE]
                        Filter the results by contract_vehicle specified
  --competitive [COMPETITIVE]
                        Filter the results by competitive specified
  --award_quarter [AWARD_QUARTER]
                        Filter the results by award_quarter specified
  --estimated_release_date [ESTIMATED_RELEASE_DATE]
                        Filter the results by estimated_release_date specified
  --publish_date [PUBLISH_DATE]
                        Filter the results by publish_date specified
  --previous_publish_date [PREVIOUS_PUBLISH_DATE]
                        Filter the results by previous_publish_date specified
  --requirements_contact_phone [REQUIREMENTS_CONTACT_PHONE]
                        Filter the results by requirements_contact_phone
                        specified
  --naics [NAICS]       Filter the results by naics specified
  --apfs_number [APFS_NUMBER]
                        Filter the results by apfs_number specified
  --requirements_title [REQUIREMENTS_TITLE]
                        Filter the results by requirements_title specified
  --requirement [REQUIREMENT]
                        Filter the results by requirement specified
  --contract_status [CONTRACT_STATUS]
                        Filter the results by contract_status specified
  --contractor [CONTRACTOR]
                        Filter the results by contractor specified
  --contract_number [CONTRACT_NUMBER]
                        Filter the results by contract_number specified
  --estimated_period_of_performance_start [ESTIMATED_PERIOD_OF_PERFORMANCE_START]
                        Filter the results by
                        estimated_period_of_performance_start specified
  --estimated_period_of_performance_end [ESTIMATED_PERIOD_OF_PERFORMANCE_END]
                        Filter the results by
                        estimated_period_of_performance_end specified
  --anticipated_award_date [ANTICIPATED_AWARD_DATE]
                        Filter the results by anticipated_award_date specified
  --estimated_solicitation_release_date [ESTIMATED_SOLICITATION_RELEASE_DATE]
                        Filter the results by
                        estimated_solicitation_release_date specified
  --place_of_performance_city [PLACE_OF_PERFORMANCE_CITY]
                        Filter the results by place_of_performance_city
                        specified
  --place_of_performance_state [PLACE_OF_PERFORMANCE_STATE]
                        Filter the results by place_of_performance_state
                        specified
  --requirements_contact_first_name [REQUIREMENTS_CONTACT_FIRST_NAME]
                        Filter the results by requirements_contact_first_name
                        specified
  --requirements_contact_last_name [REQUIREMENTS_CONTACT_LAST_NAME]
                        Filter the results by requirements_contact_last_name
                        specified
  --requirements_contact_email [REQUIREMENTS_CONTACT_EMAIL]
                        Filter the results by requirements_contact_email
                        specified
  --alternate_contact_first_name [ALTERNATE_CONTACT_FIRST_NAME]
                        Filter the results by alternate_contact_first_name
                        specified
  --alternate_contact_last_name [ALTERNATE_CONTACT_LAST_NAME]
                        Filter the results by alternate_contact_last_name
                        specified
  --alternate_contact_phone [ALTERNATE_CONTACT_PHONE]
                        Filter the results by alternate_contact_phone
                        specified
  --alternate_contact_email [ALTERNATE_CONTACT_EMAIL]
                        Filter the results by alternate_contact_email
                        specified
  --fiscal_year [FISCAL_YEAR]
                        Filter the results by fiscal_year specified
  --created_on [CREATED_ON]
                        Filter the results by created_on specified
  --requirements_office [REQUIREMENTS_OFFICE]
                        Filter the results by requirements_office specified
  --contracting_office [CONTRACTING_OFFICE]
                        Filter the results by contracting_office specified
  --apfs_coordinator_office [APFS_COORDINATOR_OFFICE]
                        Filter the results by apfs_coordinator_office
                        specified
  --current_state [CURRENT_STATE]
                        Filter the results by current_state specified
  --last_updated_date [LAST_UPDATED_DATE]
                        Filter the results by last_updated_date specified
  --published_date [PUBLISHED_DATE]
                        Filter the results by published_date specified
  --previous_published_date [PREVIOUS_PUBLISHED_DATE]
                        Filter the results by previous_published_date
                        specified

```