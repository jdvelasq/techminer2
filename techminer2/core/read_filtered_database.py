# pylint: disable=too-few-public-methods
"""
Read bibliometric records from a database.

"""

import os.path

import pandas as pd


def read_filtered_database(
    #
    # DATABASE PARAMS
    root_dir: str,
    database: str,
    year_filter: tuple,
    cited_by_filter: tuple,
    **filters,
):
    """loads and filter records of main database text files."""

    def get_records_from_file(directory, database):

        file_name = {
            "main": "_main.csv.zip",
            "references": "_references.csv.zip",
            "cited_by": "_cited_by.csv.zip",
        }[database]

        file_path = os.path.join(directory, "databases", file_name)
        records = pd.read_csv(file_path, sep=",", encoding="utf-8", compression="zip")
        records = records.drop_duplicates()

        return records

    def filter_records_by_year(records, year_filter):

        if year_filter is None:
            return records

        if not isinstance(year_filter, tuple):
            raise TypeError("The year_filter parameter must be a tuple of two values.")

        if len(year_filter) != 2:
            raise ValueError("The year_filter parameter must be a tuple of two values.")

        start_year, end_year = year_filter

        if start_year is not None:
            records = records[records.year >= start_year]

        if end_year is not None:
            records = records[records.year <= end_year]

        return records

    def filter_records_by_citations(records, cited_by_filter):

        if cited_by_filter is None:
            return records

        if not isinstance(cited_by_filter, tuple):
            raise TypeError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        if len(cited_by_filter) != 2:
            raise ValueError(
                "The cited_by_range parameter must be a tuple of two values."
            )

        cited_by_min, cited_by_max = cited_by_filter

        if cited_by_min is not None:
            records = records[records.global_citations >= cited_by_min]

        if cited_by_max is not None:
            records = records[records.global_citations <= cited_by_max]

        return records

    def apply_filters_to_records(records, **filters):

        for filter_name, filter_value in filters.items():
            # Split the filter value into a list of strings
            database = records[["article", filter_name]]
            database[filter_name] = database[filter_name].str.split(";")

            # Explode the list of strings into multiple rows
            database = database.explode(filter_name)

            # Remove leading and trailing whitespace from the strings
            database[filter_name] = database[filter_name].str.strip()

            # Keep only records that match the filter value
            database = database[database[filter_name].isin(filter_value)]
            records = records[records["article"].isin(database["article"])]

        return records

    records = get_records_from_file(root_dir, database)
    records = filter_records_by_year(records, year_filter)
    records = filter_records_by_citations(records, cited_by_filter)
    records = apply_filters_to_records(records, **filters)

    return records
