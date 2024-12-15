"""Create local citations column in documents database."""

import os

import pandas as pd  # type: ignore

from ._message import message


def create_local_citations_column_in_documents_database(root_dir):
    """Create `local_citations` column in documents database

    :meta private:
    """

    message("Creating `local_citations` column in documents database")

    # counts the number of citations for each local reference
    documents_path = os.path.join(root_dir, "databases", "_main.csv.zip")
    documents = pd.read_csv(documents_path, compression="zip")
    local_references = documents.local_references.copy()
    local_references = local_references.dropna()
    local_references = local_references.str.split(";")
    local_references = local_references.explode()
    local_references = local_references.str.strip()
    local_references = local_references.value_counts()
    values_dict = local_references.to_dict()

    # assigns the number of citations to each document in documents database
    documents["local_citations"] = documents.article
    documents["local_citations"] = documents["local_citations"].map(values_dict)
    documents["local_citations"] = documents["local_citations"].fillna(0)

    # saves the new column in the references database
    documents.to_csv(documents_path, index=False, compression="zip")
