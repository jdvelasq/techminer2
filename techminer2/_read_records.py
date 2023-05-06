"""Functions for reads (full/filtered) records of the documents.csv file."""

import os

import pandas as pd


def read_records(
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """load filter records"""
    records = _get_records_from_file(directory, database)
    records = _filter_records_by_year(records, start_year, end_year)
    records = _apply_filters_to_records(records, **filters)
    return records


def _apply_filters_to_records(records, **filters):
    # Apply filters in order
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


def _filter_records_by_year(records, start_year, end_year):
    if start_year is not None:
        records = records[records.year >= start_year]
    if end_year is not None:
        records = records[records.year <= end_year]
    return records


def _get_records_from_file(directory, database):
    file_name = {
        "documents": "_documents.csv",
        "references": "_references.csv",
        "cited_by": "_cited_by.csv",
    }[database]
    file_path = os.path.join(directory, "processed", file_name)
    records = pd.read_csv(file_path, sep=",", encoding="utf-8")
    records = records.drop_duplicates()
    return records
