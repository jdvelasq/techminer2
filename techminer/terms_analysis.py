"""
Terms analysis
===============================================================================




"""

import pandas as pd

from .plots import *
from .utils import *


def _count_citations_by_term(directory, column, sep, citations_column, min_occ=1):
    """
    Counts the number of citations of a given term.

    :param records: records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of citations of a given term.
    """

    documents = load_filtered_documents(directory)
    documents = documents[[column, citations_column]].copy()

    if sep is not None:
        documents[column] = documents[column].str.split(sep)
        documents = documents.explode(column)

    citations_by_term = (
        documents.groupby(column, as_index=True)
        .sum()
        .sort_values(by=citations_column, ascending=False)
    ).astype(int)[citations_column]

    if min_occ is not None:
        documents_by_term = count_documents_by_term(directory, column, sep, min_occ)
        citations_by_term = citations_by_term[documents_by_term.index]

    return citations_by_term


# ---< PUBLIC FUNCTIONS >---------------------------------------------------#


def count_documents_by_term(directory, column, sep="; ", min_occ=1):
    """
    Counts the number of documents containing a given term.

    :param records: records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of documents containing a given term.
    """
    documents = load_filtered_documents(directory)
    documents = documents[[column]].copy()

    if sep is not None:
        documents[column] = documents[column].str.split(sep)
        documents = documents.explode(column)

    documents_by_term = (
        documents.groupby(column, as_index=True)
        .size()
        .sort_values(ascending=False)
        .rename("num_documents")
    )

    if min_occ is not None:
        documents_by_term = documents_by_term[documents_by_term >= min_occ]

    return documents_by_term


def count_global_citations_by_term(directory, column, sep="; ", min_occ=None):
    """
    Counts the number of global citations of a given term.

    :param dirpath_or_records: path to the directory or the records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of global citations of a given term.
    """

    return _count_citations_by_term(directory, column, sep, "global_citations", min_occ)


def count_local_citations_by_term(directory, column, sep="; ", min_occ=None):
    """
    Counts the number of local citations of a given term.

    :param dirpath_or_records: path to the directory or the records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of local citations of a given term.
    """
    return _count_citations_by_term(directory, column, sep, "local_citations", min_occ)


def terms_analysis(directory, column, sep="; ", min_occ=1):
    """
    Counts the number of terms by record.

    :param dirpath_or_records: path to the directory or the records object
    :param column: column to be used to count the terms
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of terms by record.
    """

    num_documents = count_documents_by_term(directory, column, sep, min_occ)
    global_citations = count_global_citations_by_term(directory, column, sep, min_occ)
    local_citations = count_local_citations_by_term(directory, column, sep, min_occ)

    report = pd.concat(
        [
            num_documents,
            global_citations,
            local_citations,
        ],
        axis=1,
    )

    report.sort_values(by="num_documents", ascending=False, inplace=True)

    return report
