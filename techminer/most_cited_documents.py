"""
Most cited documents
===============================================================================
"""

import pandas as pd

from .utils import *


def most_cited_documents(
    directory,
    global_citations=True,
    normalized_citations=False,
    n_top=50,
):
    """
    Returns the most cited documents of the given directory or records.

    Parameters
    ----------
    dirpath_or_records: str
        path to the directory or the records object.
    global_citations: bool
        Whether to use global citations or not.
    normalized_citations: bool
        Whether to use normalized citations or not.

    Returns
    -------
    most_cited_documents: pandas.DataFrame
        Most cited documents.
    """

    documents = load_filtered_documents(directory)

    max_pub_year = documents.pub_year.dropna().max()

    documents["global_normalized_citations"] = documents.global_citations.map(
        lambda w: round(w / max_pub_year, 3), na_action="ignore"
    )

    documents["local_normalized_citations"] = documents.local_citations.map(
        lambda w: round(w / max_pub_year, 3), na_action="ignore"
    )

    documents["global_citations"] = documents.global_citations.map(
        int, na_action="ignore"
    )

    citations_column = {
        (True, True): "global_normalized_citations",
        (True, False): "global_citations",
        (False, True): "local_normalized_citations",
        (False, False): "local_citations",
    }[(global_citations, normalized_citations)]

    documents = documents.sort_values(citations_column, ascending=False)
    documents = documents.reset_index(drop=True)

    documents = documents[
        [
            "authors",
            "pub_year",
            "document_title",
            "source_name",
            "document_id",
            citations_column,
        ]
    ]

    if n_top is not None:
        documents = documents.head(n_top)

    documents = documents.sort_values(by=citations_column, ascending=False)

    return documents
