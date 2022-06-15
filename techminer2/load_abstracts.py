"""
Load abstracs file.
=========================================================================================

Load abstracts from main documents collection.

"""
import os

import pandas as pd


def load_abstracts(directory):
    """Load abstracts.csv file."""

    filename = os.path.join(directory, "processed", "abstracts.csv")
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    documents = pd.read_csv(filename, sep=",", encoding="utf-8")

    return documents
