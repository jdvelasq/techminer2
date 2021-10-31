"""
Documents and citations by term
================

"""

import pandas as pd
from techminer.utils.io import load_records

# ---< count_documents_by_term >-----------------------------------------------


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


# ---< count_global_citations_by_term, count_local_citations_by_term >----------------------------


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


# ---< count_documents_by_year >-----------------------------------------------


def _count_documents_by_year_from_records(records):
    """
    Counts the number of documents by year.

    :param records: records object
    :return: a pandas.Series with the number of documents by year.
    """
    return (
        records.groupby("pub_year", as_index=True)
        .size()
        .sort_values(ascending=False)
        .rename("num_documents")
    )


def _count_documents_by_year_from_directory(directory):
    """
    Counts the number of documents by year.

    :param directory: path to the directory
    :return: a pandas.Series with the number of documents by year.
    """
    return _count_documents_by_year_from_records(load_records(directory))


def count_documents_by_year(directory_or_records):
    """
    Counts the number of documents by year.

    :param directory_or_records: path to the directory or the records object
    :return: a pandas.Series with the number of documents by year.
    """
    if isinstance(directory_or_records, str):
        return _count_documents_by_year_from_directory(directory_or_records)
    elif isinstance(directory_or_records, pd.DataFrame):
        return _count_documents_by_year_from_records(directory_or_records)
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")


# ---< count_local_citations_by_year >-----------------------------------------------


def _count_local_citations_by_year_from_records(records):
    """
    Counts the number of local citations by year.

    :param records: records object
    :return: a pandas.Series with the number of local citations by year.
    """
    records = records[["pub_year", "local_citations"]].copy()
    return (
        records.groupby("pub_year", as_index=True)
        .sum()
        .sort_values(by="local_citations", ascending=False)
    )["local_citations"]


def _count_local_citations_by_year_from_directory(directory):
    """
    Counts the number of local citations by year.

    :param directory: path to the directory
    :return: a pandas.Series with the number of local citations by year.
    """
    return _count_local_citations_by_year_from_records(load_records(directory))


def count_local_citations_by_year(directory_or_records):
    """
    Counts the number of local citations by year.

    :param directory_or_records: path to the directory or the records object
    :return: a pandas.Series with the number of local citations by year.
    """
    if isinstance(directory_or_records, str):
        return _count_local_citations_by_year_from_directory(directory_or_records)
    elif isinstance(directory_or_records, pd.DataFrame):
        return _count_local_citations_by_year_from_records(directory_or_records)
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")


# ----< count_global_citations_by_year >-----------------------------------------------


def _count_global_citations_by_year_from_records(records):
    """
    Counts the number of global citations by year.

    :param records: records object
    :return: a pandas.Series with the number of global citations by year.
    """
    records = records[["pub_year", "global_citations"]].copy()
    return (
        records.groupby("pub_year", as_index=True)
        .sum()
        .sort_values(by="global_citations", ascending=False)
    )["global_citations"]


def _count_global_citations_by_year_from_directory(directory):
    """
    Counts the number of global citations by year.

    :param directory: path to the directory
    :return: a pandas.Series with the number of global citations by year.
    """
    return _count_global_citations_by_year_from_records(load_records(directory))


def count_global_citations_by_year(directory_or_records):
    """
    Counts the number of global citations by year.

    :param directory_or_records: path to the directory or the records object
    :return: a pandas.Series with the number of global citations by year.
    """
    if isinstance(directory_or_records, str):
        return _count_global_citations_by_year_from_directory(directory_or_records)
    elif isinstance(directory_or_records, pd.DataFrame):
        return _count_global_citations_by_year_from_records(directory_or_records)
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")


# ----< mean citations by year >------------------------------------------------------


def mean_global_citations_by_year(directory_or_records):
    """
    Counts the mean number of global citations by year.

    :param directory_or_records: path to the directory or the records object
    :return: a pandas.Series with the mean number of global citations by year.
    """
    mgcy = count_global_citations_by_year(directory_or_records).sort_index(
        ascending=True
    ) / count_documents_by_year(directory_or_records).sort_index(ascending=True)
    mgcy = mgcy.rename("mean_global_citations")
    mgcy = mgcy.round(2)
    return mgcy


def mean_local_citations_by_year(directory_or_records):
    """
    Counts the mean number of local citations by year.

    :param directory_or_records: path to the directory or the records object
    :return: a pandas.Series with the mean number of local citations by year.
    """
    mlcy = count_local_citations_by_year(directory_or_records).sort_index(
        ascending=True
    ) / count_documents_by_year(directory_or_records).sort_index(ascending=True)
    mlcy = mlcy.rename("mean_local_citations")
    mlcy = mlcy.round(2)
    return mlcy


# ----< count terms by column >-------------------------------------------------------


def count_terms_by_column(directory_or_records, column, sep="; "):
    """
    Counts the number of terms by record.

    :param directory_or_records: path to the directory or the records object
    :param column: column to be used to count the terms
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of terms by record.
    """
    if isinstance(directory_or_records, str):
        records = load_records(directory_or_records)
    else:
        records = directory_or_records

    if sep is not None:
        records[column] = records[column].str.split(sep)
        records[column] = records[column].map(len)
    else:
        records[column] = records[column].map(len)

    return records[column]


# ----< term analysis >---------------------------------------------------------------


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


def time_analysis(directory_or_records):
    """
    Counts the number of terms by record.

    :param directory_or_records: path to the directory or the records object
    :return: a pandas.DataFrame with the analysis.
    """

    num_documents = count_documents_by_year(directory_or_records).to_frame()
    global_citations = count_global_citations_by_year(directory_or_records).to_frame()
    local_citations = count_local_citations_by_year(directory_or_records).to_frame()
    mean_global_citations = mean_global_citations_by_year(directory_or_records)
    mean_local_citations = mean_local_citations_by_year(directory_or_records)

    analysis = pd.concat(
        [
            num_documents,
            global_citations,
            local_citations,
            mean_global_citations,
            mean_local_citations,
        ],
        axis=1,
    )

    return analysis
