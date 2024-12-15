"""Creates `local_citations` column in references database."""

import os

import pandas as pd  # type: ignore

from ._message import message


def create_local_citations_column_in_references_database(directory):
    """Create `local_citations` column in references database

    :meta private:
    """

    references_path = os.path.join(directory, "databases", "_references.csv.zip")
    if not os.path.exists(references_path):
        return

    message("Creating `local_citations` column in references database")

    # counts the number of citations for each local reference
    documents_path = os.path.join(directory, "databases", "_main.csv.zip")
    documents = pd.read_csv(documents_path, compression="zip")
    local_references = documents.local_references.copy()
    local_references = local_references.dropna()
    local_references = local_references.str.split(";")
    local_references = local_references.explode()
    local_references = local_references.str.strip()
    local_references = local_references.value_counts()
    values_dict = local_references.to_dict()

    # assigns the number of citations to each reference in references database

    references = pd.read_csv(references_path, compression="zip")
    references["local_citations"] = references.article
    references["local_citations"] = references["local_citations"].map(values_dict)
    references["local_citations"] = references["local_citations"].fillna(0)

    # saves the new column in the references database
    references.to_csv(references_path, index=False, compression="zip")
