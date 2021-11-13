"""
Import records

"""

import os

import pandas as pd
import yaml

from . import logging
from .thesaurus import read_textfile


def load_filtered_documents(directory):
    """
    Loads documents from project directory.

    """

    if directory is None:
        # debug data
        directory = "/workspaces/techminer-api/tests/data/"

    if directory[-1] != "/":
        directory += "/"

    # Load documents
    filename = directory + "documents.csv"
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    documents = pd.read_csv(filename, sep=",", encoding="utf-8")

    # Filter documents
    yaml_filename = directory + "filter.yaml"
    with open(yaml_filename, "r", encoding="utf-8") as yaml_file:
        filter_ = yaml.load(yaml_file, Loader=yaml.FullLoader)

    year_min, year_max = filter_["first_year"], filter_["last_year"]
    documents = documents.query(f"pub_year >= {year_min}")
    documents = documents.query(f"pub_year <= {year_max}")

    citations_min, citations_max = filter_["citations_min"], filter_["citations_max"]
    documents = documents.query(f"global_citations >= {citations_min}")
    documents = documents.query(f"global_citations <= {citations_max}")

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

    return documents


# def save_documents(records, directory):
#     """
#     Saves records to project directory.

#     """
#     if directory[-1] != "/":
#         directory += "/"

#     filename = directory + "documents.csv"
#     if os.path.isfile(filename):
#         logging.info(f"The file '{filename}' was rewrited.")

#     records.to_csv(filename, sep=",", encoding="utf-8", index=False)


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


# def load_thesaurus_from_textfile(project_directory, textfile):
#     """
#     Loads thesaurus from textfile.

#     """
#     if project_directory[-1] != "/":
#         project_directory += "/"

#     filename = project_directory + textfile
#     return read_textfile(filename)
