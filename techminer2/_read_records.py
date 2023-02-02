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
    if filters is None:
        return records
    for filter_name, filter_value in filters.items():
        database = records[["article", filter_name]]
        database[filter_name] = database[filter_name].str.split(";")
        database = database.explode(filter_name)
        database[filter_name] = database[filter_name].str.strip()
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
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"file '{file_path}' not found")
    records = pd.read_csv(file_path, sep=",", encoding="utf-8")
    return records
