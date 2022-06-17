import os

from . import logging


def save_documents(documents, directory="./"):

    filename = os.path.join(directory, "processed", "documents.csv")
    documents.to_csv(
        filename,
        sep=",",
        encoding="utf-8",
        index=False,
    )

    logging.info(f"Documents saved/merged to '{filename}'")
