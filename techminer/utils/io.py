"""
Import records

"""

import os

import pandas as pd
import yaml


def save_documents(documents, directory):

    if directory is None:
        directory = "/workspaces/techminer-api/tests/data/"

    filename = os.path.join(directory, "documents.csv")
    documents.to_csv(
        filename,
        sep=",",
        encoding="utf-8",
        index=False,
    )


def load_all_documents(directory):

    if directory is None:
        directory = "/workspaces/techminer-api/tests/data/"

    if directory[-1] != "/":
        directory += "/"

    filename = directory + "documents.csv"
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    documents = pd.read_csv(filename, sep=",", encoding="utf-8")

    documents.index = documents.document_id

    return documents


def load_filtered_documents(directory):
    """
    Loads documents from project directory.

    """
    documents = load_all_documents(directory)

    # Filter documents
    yaml_filename = directory + "filter.yaml"
    with open(yaml_filename, "r", encoding="utf-8") as yaml_file:
        filter_ = yaml.load(yaml_file, Loader=yaml.FullLoader)

    year_min, year_max = filter_["first_year"], filter_["last_year"]
    documents = documents.query(f"pub_year >= {year_min}")
    documents = documents.query(f"pub_year <= {year_max}")

    min_citations, max_citations = filter_["min_citations"], filter_["max_citations"]
    documents = documents.query(f"global_citations >= {min_citations}")
    documents = documents.query(f"global_citations <= {max_citations}")

    bradford = filter_["bradford"]
    documents = documents.query(f"bradford_law_zone <= {bradford}")

    for key, value in filter_.items():
        if key in [
            "first_year",
            "last_year",
            "citations_min",
            "citations_max",
            "bradford",
        ]:
            continue

        if value is False:
            documents = documents.query(f"document_type != '{key}'")

    documents.index = documents.document_id

    return documents


def load_stopwords(directory):
    """
    Loads stopwords from the project directory.

    """
    if directory[-1] != "/":
        directory += "/"
    filename = directory + "stopwords.txt"
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    return [
        line.strip()
        for line in open(
            filename,
            "r",
            encoding="utf-8",
        ).readlines()
    ]
