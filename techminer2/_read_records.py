"""Functions for reads (full/filtered) records of the documents.csv file."""

import os

import pandas as pd
import yaml


def read_all_records(directory, database="documents"):
    "Reads all records of the specified file."

    file_name = {
        "documents": "_documents.csv",
        "references": "_references.csv",
        "cited_by": "_cited_by.csv",
    }[database]

    file_path = os.path.join(directory, "processed", file_name)
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    records = pd.read_csv(file_path, sep=",", encoding="utf-8")
    return records


def read_filtered_records(directory):
    """Loads documents from project directory."""
    documents = read_all_records(directory)

    # Filter documents
    yaml_filename = os.path.join(directory, "processed", "filter.yaml")
    with open(yaml_filename, "r", encoding="utf-8") as yaml_file:
        filter_ = yaml.load(yaml_file, Loader=yaml.FullLoader)

    year_min, year_max = filter_["first_year"], filter_["last_year"]
    documents = documents.query(f"year >= {year_min}")
    documents = documents.query(f"year <= {year_max}")

    min_citations, max_citations = filter_["min_citations"], filter_["max_citations"]
    documents = documents.query(f"global_citations >= {min_citations}")
    documents = documents.query(f"global_citations <= {max_citations}")

    bradford = filter_["bradford"]
    documents = documents.query(f"bradford <= {bradford}")

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
            documents = documents.query(f"document_type != '{key}'")

    return documents
