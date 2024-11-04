from pandas import DataFrame as df


def pretty_print_forecast_data(data: df, display_fields: list) -> str:
    import logging
    from tabulate import tabulate

    logger = logging.getLogger(__name__)
    output: str = tabulate(tabular_data=data, headers=display_fields, tablefmt="outline")
    logger.debug("pretty_print_forecast_data: "+output[:1000])

    return output
