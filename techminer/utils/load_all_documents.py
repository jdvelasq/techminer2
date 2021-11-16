import os

import pandas as pd

from . import logging


def load_all_documents(directory):

    if directory is None:
        logging.info("*")
        logging.info("*  Argument `directory` is **None**. ")
        logging.info(
            "*  Loading data from DEBUG directory /workspaces/techminer-api/tests/data/"
        )
        logging.info("*")
        directory = "/workspaces/techminer-api/tests/data/"

    filename = os.path.join(directory, "documents.csv")
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    documents = pd.read_csv(filename, sep=",", encoding="utf-8")

    documents = documents.set_index("document_id")

    return documents
