import os

import pandas as pd


def load_all_documents(directory):
    "Load all current documents from the project directory."

    filename = os.path.join(directory, "processed", "documents.csv")
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    documents = pd.read_csv(filename, sep=",", encoding="utf-8")

    return documents
