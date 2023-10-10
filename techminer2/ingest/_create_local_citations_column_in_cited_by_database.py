"""Create local citations column in cited-by database."""

import os

import pandas as pd


def create_local_citations_column_in_cited_by_database(root_dir):
    """Create local citations column in cited-by database."""

    # message("Creating `local_citations` column in documents database")

    # counts the number of citations for each local reference
    documents_path = os.path.join(root_dir, "databases", "_cited_by.csv.zip")
    documents = pd.read_csv(documents_path, compression="zip")
    documents["local_citations"] = 0

    # saves the new column in the references database
    documents.to_csv(documents_path, index=False, compression="zip")
