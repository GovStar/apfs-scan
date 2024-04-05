# Last known data columns
from typing import Dict, Any

DATA_DICT_COLUMNS: list = ['id', 'mission', 'organization', 'small_business_program',
                           'dollar_range', 'contract_vehicle', 'competitive', 'award_quarter',
                           'estimated_release_date', 'publish_date', 'previous_publish_date',
                           'requirements_contact_phone', 'naics', 'apfs_number',
                           'requirements_title', 'requirement', 'contract_status', 'contractor',
                           'contract_number', 'estimated_period_of_performance_start',
                           'estimated_period_of_performance_end', 'anticipated_award_date',
                           'estimated_solicitation_release_date', 'place_of_performance_city',
                           'place_of_performance_state', 'requirements_contact_first_name',
                           'requirements_contact_last_name', 'requirements_contact_email',
                           'alternate_contact_first_name', 'alternate_contact_last_name',
                           'alternate_contact_phone', 'alternate_contact_email', 'fiscal_year',
                           'created_on', 'requirements_office', 'contracting_office',
                           'apfs_coordinator_office', 'current_state', 'last_updated_date',
                           'published_date', 'previous_published_date']

SAME_opportunity_pointOfContact_json: Dict[str, Any] = {'Fax': '', 'Type': '', 'Email': '', 'Phone': '', 'Title': '',
                                                        'Full name': '', 'additionalInfo': Dict[str, Any]}
SAM_opportunity_country_json: Dict[str, Any] = {'code': '', 'name': ''}
SAM_opportunity_state_json: Dict[str, Any] = {'code': '', 'name': ''}
SAM_opportunity_city_json: Dict[str, Any] = {'code': '', 'name': '', 'state': '', 'stateCode': ''}
SAM_opportunity_location_json: Dict[str, Any] = {'streetAddress': '', 'streetAddress2': '',
                                                 'city': SAM_opportunity_city_json,
                                                 'country': SAM_opportunity_country_json, 'zip': ''}
SAM_opportunity_awardee_json: Dict[str, Any] = {'name': '', 'ueiSAM': '', 'location': SAM_opportunity_location_json}
SAM_opportunity_award_json: Dict[str, Any] = {'number': 'str', 'amount': int, 'date': '',
                                              'awardee': SAM_opportunity_awardee_json}
SAM_opportunity_officeAddress_json: Dict[str, Any] = {'city': '', 'state': '', 'zip': ''}
SAM_opportunity_placeOfPerformance_json: Dict[str, Any] = {'streetAddress': '', 'streetAddress2': '',
                                                           'city': SAM_opportunity_city_json,
                                                           'state': SAM_opportunity_state_json,
                                                           'country': SAM_opportunity_country_json, 'zip': ''}

SAM_opportunity_request_params: Dict[str, Any] = {'ptype': '', 'solnum': '', 'noticeid': '', 'title': '',
                                                  'postedFrom': '', 'postedTo': '', 'deptname': '', 'subtier': '',
                                                  'state': '', 'status (Coming Soon)': '', 'zip': '',
                                                  'organizationCode': '', 'organizationName': '', 'typeOfSetAside': '',
                                                  'typeOfSetAsideDescription': '', 'ncode': '', 'ccode': '',
                                                  'rdlfrom': '',
                                                  'rdlto': '', 'limit': int, 'offset': int}
SAM_opportunity_response_params: Dict[str, Any] = {'totalRecords': int, 'limit': int, 'offset': int, 'title': '',
                                                   'solicitationNumber': '', 'fullParentPathName': '',
                                                   'fullParentPathCode': '',
                                                   'department': '', 'subtier': '', 'office': '', 'postedDate': '',
                                                   'type': '', 'baseType': '', 'archiveType': '', 'archiveDate': '',
                                                   'setAside': '', 'setAsideCode': '',
                                                   'responseDeadLine': '', 'naics': '', 'classificationCode': '',
                                                   'active': '', 'data.award': SAM_opportunity_award_json,
                                                   'pointofContact': SAME_opportunity_pointOfContact_json,
                                                   'description': '',
                                                   'organizationType': '',
                                                   'officeAddress': SAM_opportunity_officeAddress_json,
                                                   'placeOfPerformance': SAM_opportunity_placeOfPerformance_json,
                                                   'additionalInfoLink': ' ', 'uiLink': '', 'links': [str],
                                                   'resourceLinks': [str]
                                                   }

SAM_cityLookUp_county_json: Dict[str, Any] = {'country': '', 'code2': '', 'code': ''}
SAM_cityLookUp_state_json: Dict[str, Any] = {'statecode': '', 'state': ''}
SAM_cityLookUp_request_json: Dict[str, Any] = {'api_key': '', 'cc': '', 'searchby': '', 'searchvalue' : '', 'q': '', 'active': '', 'citycode': ''}
SAM_cityLookUp_response_json: Dict[str, Any] = {'cityCode': '', 'city': '', 'state': '', 'searchvalue' : '', 'q': '', 'active': '', 'citycode': ''}

SAM_countyLookUp_request_json: Dict[str, Any] = {'api_key': '', 'searchby': '', 'searchvalue': '', 'q': '', 'active': ''}
SAM_countyLookUp_response_json: Dict[str, Any] = {'country': '', 'countryFullName': '', 'countryCode2': '', 'countrycode': '', 'href': ''}

SAM_stateLookUp_county_json: Dict[str, Any] = {'country': '', 'countryFullName': '', 'countryCode2': '', 'countrycode': ''}
SAM_stateLookUp_request_json: Dict[str, Any] = {'api_key': '', 'cc': '', 'searchby': '', 'q': '', 'active': ''}
SAM_stateLookUp_response_json: Dict[str, Any] = {'statecode': '', 'state': '', 'stateType': '', 'country': SAM_stateLookUp_county_json, 'href': ''}

SAM_zipLookUp_request_json: Dict[str, Any] = {'api_key': '', 'zip': '', 'citycode': '', 'countycode': '', 'statecode': ''}
SAM_zipLookUp_response_json: Dict[str, Any] = {'zipCode': '', 'description': ''}

def exception_log_and_exit(exception: Exception):
    import logging
    logger = logging.getLogger(__name__)
    logger.exception("unrecoverable exception: ", exception)
    logger.error("Exiting with code 1 after unrecoverable exception")
    exit(1)
