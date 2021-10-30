import pandas as pd
from techminer.data import load_records
from techminer.utils import extract_country_name
from techminer.utils.map import map_


def extract_coutries(directory_or_records, column):
    """
    Extracts countries from a given column.
    :param directory_or_records:
    :param column:

    :return:
    """
    if isinstance(directory_or_records, str):
        records = load_records(directory_or_records)
    else:
        records = directory_or_records.copy()

    countries = map_(records, column, extract_country_name)
    countries = countries.str.split("; ")
    countries = countries.map(lambda x: list(set(x)) if isinstance(x, list) else x)
    countries = countries.map(lambda x: "; ".join(x) if isinstance(x, list) else x)

    return countries


def extract_institutions(directory_or_records, column):
    """
    Extracts institutions from a given column.
    :param directory_or_records:
    :param column:

    :return:
    """
    if isinstance(directory_or_records, str):
        records = load_records(directory_or_records)
    else:
        records = directory_or_records.copy()

    countries = map_(records, column, extract_institution_name)
    countries = countries.str.split("; ")
    countries = countries.map(lambda x: list(set(x)) if isinstance(x, list) else x)
    countries = countries.map(lambda x: "; ".join(x) if isinstance(x, list) else x)

    return countries
