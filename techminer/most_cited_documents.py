"""
Most Cited Documents
===============================================================================
"""

import pandas as pd

from techminer.utils import load_records


def _most_cited_documents_from_records(
    records,
    global_citations,
    normalized_citations,
    n_top,
):

    records = records.copy()

    max_pub_year = records.pub_year.dropna().max()

    records["global_normalized_citations"] = records.global_citations.map(
        lambda w: round(w / max_pub_year, 3), na_action="ignore"
    )

    records["local_normalized_citations"] = records.local_citations.map(
        lambda w: round(w / max_pub_year, 3), na_action="ignore"
    )

    records["global_citations"] = records.global_citations.map(int, na_action="ignore")

    citations_column = {
        (True, True): "global_normalized_citations",
        (True, False): "global_citations",
        (False, True): "local_normalized_citations",
        (False, False): "local_citations",
    }[(global_citations, normalized_citations)]

    records = records.sort_values(citations_column, ascending=False)
    records = records.reset_index(drop=True)

    records = records[
        [
            "authors",
            "pub_year",
            "document_title",
            "publication_name",
            "record_id",
            citations_column,
        ]
    ]

    if n_top is not None:
        records = records.head(n_top)

    records = records.sort_values(by=citations_column, ascending=False)

    return records


def _most_cited_documents_from_directory(
    directory,
    global_citations,
    normalized_citations,
    n_top,
):
    return _most_cited_documents_from_records(
        records=load_records(directory),
        global_citations=global_citations,
        normalized_citations=normalized_citations,
        n_top=n_top,
    )


def most_cited_documents(
    directory_or_records,
    global_citations=True,
    normalized_citations=False,
    n_top=50,
):
    """
    Returns the most cited documents of the given directory or records.

    Parameters
    ----------
    directory_or_records: str
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
    if isinstance(directory_or_records, str):
        return _most_cited_documents_from_directory(
            directory=directory_or_records,
            global_citations=global_citations,
            normalized_citations=normalized_citations,
            n_top=n_top,
        )
    elif isinstance(directory_or_records, pd.DataFrame):
        return _most_cited_documents_from_records(
            records=directory_or_records,
            global_citations=global_citations,
            normalized_citations=normalized_citations,
            n_top=n_top,
        )
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")
