"""
Functions for handling the records.


"""
from os.path import isfile

import pandas as pd


def load_records(directory="./", fileerror=True):
    """
    Loads records from project directory.

    """
    if directory[-1] != "/":
        directory += "/"
    filename = directory + "records.csv"
    if not isfile(filename):
        if fileerror:
            raise FileNotFoundError(f"The file '{filename}' does not exist.")
        return pd.DataFrame()

    return pd.read_csv(filename, sep=",", encoding="utf-8")


def save_records(records, directory="./"):
    """
    Saves records to project directory.

    """
    if directory[-1] != "/":
        directory += "/"
    filename = directory + "records.csv"
    records.to_csv(filename, sep=",", encoding="utf-8")
