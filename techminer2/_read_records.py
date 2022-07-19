"""Functions for reads (full/filtered) records of the documents.csv file."""

import os

import pandas as pd
import yaml

# read the records of the documents.csv file and apply an optional filter
# to the records.
#
# Parameters:
# - directory: the directory of the project
# - database: the database to read (either "documents" or "references")
# - use_filter: if True, apply the filter to the records
#
# Returns:
# - a pandas DataFrame with the records of the database
#
# Raises:
# - FileNotFoundError: if the file does not exist


def read_records(directory="./", database="documents", use_filter=True):
    """load filter records"""

    file_name = {
        "documents": "_documents.csv",
        "references": "_references.csv",
        "cited_by": "_cited_by.csv",
    }[database]

    file_path = os.path.join(directory, "processed", file_name)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"file '{file_path}' not found")

    records = pd.read_csv(file_path, sep=",", encoding="utf-8")
    if use_filter:
        if database != "documents":
            raise (
                NotImplementedError(
                    "filter not implemented for references and cited_by"
                )
            )
        records = _filter_records(directory, records)
    return records


# Filter the records of the database.
#
# Parameters:
# - records: the records of the database
#
# Returns:
# - a pandas DataFrame with the filtered records of the database
def _filter_records(directory, records):
    """docs"""

    filter_ = _load_filter(directory)
    year_min, year_max = filter_["first_year"], filter_["last_year"]
    records = records.query(f"year >= {year_min}")
    records = records.query(f"year <= {year_max}")

    min_citations, max_citations = filter_["min_citations"], filter_["max_citations"]
    records = records.query(f"global_citations >= {min_citations}")
    records = records.query(f"global_citations <= {max_citations}")

    bradford = filter_["bradford"]
    records = records.query(f"bradford <= {bradford}")

    for key, value in filter_.items():
        if key in [
            "first_year",
            "last_year",
            "min_citations",
            "max_citations",
            "bradford",
        ]:
            continue

        if value is False:
            records = records.query(f"document_type != '{key}'")

    return records


def _load_filter(directory):
    yaml_filename = os.path.join(directory, "processed", "filter.yaml")
    with open(yaml_filename, "r", encoding="utf-8") as yaml_file:
        filter_ = yaml.load(yaml_file, Loader=yaml.FullLoader)
    return filter_


def read_filtered_records(**kwars):
    print("deprecated")


def read_all_records(**kwars):
    print("deprecated")
