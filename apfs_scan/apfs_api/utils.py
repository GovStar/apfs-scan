# Last known data columns
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


def exception_log_and_exit(exception: Exception):
    import logging
    logging.exception("unrecoverable exception: ", exception)
    logging.error("Exiting with code 1 after unrecoverable exception")
    exit(1)
