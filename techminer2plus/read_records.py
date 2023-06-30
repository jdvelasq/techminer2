"""Read records"""

import os.path

import pandas as pd


def read_records(
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """loads and filter records of main database text files."""

    def _get_records_from_file(directory, database):
        """Read raw records from a file."""

        file_name = None

        if database.startswith("_CLUSTER_"):
            file_name = database + ".csv"
        if database.startswith("_CLUSTERS_"):
            file_name = database + ".csv"

        if file_name is None:
            file_name = {
                "main": "_main.csv",
                "references": "_references.csv",
                "cited_by": "_cited_by.csv",
            }[database]

        file_path = os.path.join(directory, "databases", file_name)
        records = pd.read_csv(file_path, sep=",", encoding="utf-8")
        records = records.drop_duplicates()

        return records

    def _filter_records_by_year(records, year_filter):
        """Filter records by year."""

        if year_filter is None:
            return records

        if not isinstance(year_filter, tuple):
            raise TypeError(
                "The year_filter parameter must be a tuple of two values."
            )

        if len(year_filter) != 2:
            raise ValueError(
                "The year_filter parameter must be a tuple of two values."
            )

        start_year, end_year = year_filter

        if start_year is not None:
            records = records[records.year >= start_year]

        if end_year is not None:
            records = records[records.year <= end_year]

        return records

    def _filter_records_by_citations(records, cited_by_filter):
        """Filter records by year."""

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

    def _apply_filters_to_records(records, **filters):
        """Apply user filters in order."""

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

    records = _get_records_from_file(root_dir, database)
    records = _filter_records_by_year(records, year_filter)
    records = _filter_records_by_citations(records, cited_by_filter)
    records = _apply_filters_to_records(records, **filters)

    return records
