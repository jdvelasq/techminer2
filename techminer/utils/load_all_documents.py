import os

import pandas as pd


def load_all_documents(directory):

    filename = os.path.join(directory, "documents.csv")
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    documents = pd.read_csv(filename, sep=",", encoding="utf-8")

    return documents
