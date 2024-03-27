from tabulate import tabulate
from pandas import DataFrame as df


def pretty_print_forecast_data(data: df):
    print_columns = ["apfs_number", "mission", "requirements_title", "contract_status"]

    return tabulate(tabular_data=data, headers=print_columns, tablefmt="double_grid")
