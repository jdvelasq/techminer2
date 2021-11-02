"""
Import records

"""

import os

import pandas as pd
from techminer.utils import logging


def load_records_from_directory(directory, fileerror=True):
    """
    Loads records from project directory.

    """
    if directory[-1] != "/":
        directory += "/"

    filename = directory + "records.csv"

    if not os.path.isfile(filename):
        if fileerror:
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        return pd.DataFrame()
    return pd.read_csv(filename, sep=",", encoding="utf-8")


def save_records_to_directory(records, directory):
    """
    Saves records to project directory.

    """
    if directory[-1] != "/":
        directory += "/"

    filename = directory + "records.csv"
    if os.path.isfile(filename):
        logging.info(f"The file '{filename}' was rewrited.")

    records.to_csv(filename, sep=",", encoding="utf-8", index=False)


def load_stopwords_from_directory(directory):
    """
    Loads stopwords from project directory.

    """
    if directory is None:
        return []

    if directory[-1] != "/":
        directory += "/"

    filename = directory + "stopwords.txt"

    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")

    return [line.strip() for line in open(filename, "r", encoding="utf-8").readlines()]
