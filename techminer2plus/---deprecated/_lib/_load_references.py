import os

import pandas as pd


def load_references(directory):
    "Load references from the project directory."

    filename = os.path.join(directory, "processed", "references.csv")
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    references = pd.read_csv(filename, sep=",", encoding="utf-8")

    return references
