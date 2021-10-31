"""
Term Analysis
===============================================================================




"""

import pandas as pd

from techminer.utils.io import load_records


def _count_documents_by_term_from_records(records, column, sep):
    """
    Counts the number of documents containing a given term.

    :param records: records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of documents containing a given term.
    """
    records = records[[column]].copy()
    if sep is not None:
        records[column] = records[column].str.split(sep)
        records = records.explode(column)
    return (
        records.groupby(column, as_index=True)
        .size()
        .sort_values(ascending=False)
        .rename("num_documents")
    )


def _count_documents_by_term_from_directory(directory, column, sep):
    """
    Counts the number of documents containing a given term.

    :param directory: path to the directory
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of documents containing a given term.
    """
    return _count_documents_by_term_from_records(
        load_records(directory),
        column,
        sep,
    )


def _count_citations_by_term_from_records(records, column, sep, citations_column):
    """
    Counts the number of citations of a given term.

    :param records: records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of citations of a given term.
    """
    records = records[[column, citations_column]].copy()
    if sep is not None:
        records[column] = records[column].str.split(sep)
        records = records.explode(column)
    return (
        records.groupby(column, as_index=True)
        .sum()
        .sort_values(by=citations_column, ascending=False)
    ).astype(int)[citations_column]


def _count_citations_by_term_from_directory(directory, column, sep, citations_column):
    """
    Counts the number of local citations of a given term.

    :param directory: path to the directory
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of local citations of a given term.
    """
    return _count_citations_by_term_from_records(
        load_records(directory),
        column,
        sep,
        citations_column,
    )


# ---< PUBLIC FUNCTIONS >---------------------------------------------------#


def count_documents_by_term(directory_or_records, column, sep="; "):
    """
    Counts the number of documents containing a given term.

    :param directory_or_records: path to the directory or the records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of documents containing a given term.
    """
    if isinstance(directory_or_records, str):
        return _count_documents_by_term_from_directory(
            directory_or_records, column, sep
        )
    elif isinstance(directory_or_records, pd.DataFrame):
        return _count_documents_by_term_from_records(directory_or_records, column, sep)
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")


def count_global_citations_by_term(directory_or_records, column, sep="; "):
    """
    Counts the number of global citations of a given term.

    :param directory_or_records: path to the directory or the records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of global citations of a given term.
    """
    if isinstance(directory_or_records, str):
        return _count_citations_by_term_from_directory(
            directory_or_records, column, sep, "global_citations"
        )
    elif isinstance(directory_or_records, pd.DataFrame):
        return _count_citations_by_term_from_records(
            directory_or_records, column, sep, "global_citations"
        )
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")


def count_local_citations_by_term(directory_or_records, column, sep="; "):
    """
    Counts the number of local citations of a given term.

    :param directory_or_records: path to the directory or the records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of local citations of a given term.
    """
    if isinstance(directory_or_records, str):
        return _count_citations_by_term_from_directory(
            directory_or_records, column, sep, "local_citations"
        )
    elif isinstance(directory_or_records, pd.DataFrame):
        return _count_citations_by_term_from_records(
            directory_or_records, column, sep, "local_citations"
        )
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")


def term_analysis(directory_or_records, column, sep="; "):
    """
    Counts the number of terms by record.

    :param directory_or_records: path to the directory or the records object
    :param column: column to be used to count the terms
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of terms by record.
    """

    num_documents = count_documents_by_term(
        directory_or_records, column, sep
    ).to_frame()
    global_citations = count_global_citations_by_term(
        directory_or_records, column, sep
    ).to_frame()
    local_citations = count_local_citations_by_term(
        directory_or_records, column, sep
    ).to_frame()

    analysis = pd.concat([num_documents, global_citations, local_citations], axis=1)

    return analysis
