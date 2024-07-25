"""Create local citations column in cited-by database."""

import os

import pandas as pd  #  type: ignore


def create_local_citations_column_in_cited_by_database(root_dir):
    """Create local citations column in cited-by database."""

    documents_path = os.path.join(root_dir, "databases", "_cited_by.csv.zip")
    #
    if not os.path.exists(documents_path):
        return
    #
    documents = pd.read_csv(documents_path, compression="zip")
    documents["local_citations"] = 0

    # saves the new column in the references database
    documents.to_csv(documents_path, index=False, compression="zip")
