"""
Time analysis
===============================================================================
"""

import pandas as pd

from .plots import *
from .utils import load_filtered_documents


def count_documents_by_year(directory):
    """
    Counts the number of documents by year.

    :param directory: path to the directory or the records object
    :return: a pandas.Series with the number of documents by year.
    """
    documents = load_filtered_documents(directory)
    return (
        documents.groupby("pub_year", as_index=True)
        .size()
        .sort_values(ascending=False)
        .rename("num_documents")
    )


def count_global_citations_by_year(directory):
    """
    Counts the number of global citations by year.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.Series with the number of global citations by year.
    """
    documents = load_filtered_documents(directory)
    documents = documents[["pub_year", "global_citations"]].copy()
    return (
        documents.groupby("pub_year", as_index=True)
        .sum()
        .sort_values(by="global_citations", ascending=False)
    )["global_citations"]


def count_local_citations_by_year(directory):
    """
    Counts the number of local citations by year.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.Series with the number of local citations by year.
    """
    documents = load_filtered_documents(directory)
    documents = documents[["pub_year", "local_citations"]].copy()
    return (
        documents.groupby("pub_year", as_index=True)
        .sum()
        .sort_values(by="local_citations", ascending=False)
    )["local_citations"]


def mean_global_citations_by_year(directory):
    """
    Counts the mean number of global citations by year.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.Series with the mean number of global citations by year.
    """
    mgcy = count_global_citations_by_year(directory).sort_index(
        ascending=True
    ) / count_documents_by_year(directory).sort_index(ascending=True)
    mgcy = mgcy.rename("mean_global_citations")
    mgcy = mgcy.round(2)
    return mgcy


def mean_local_citations_by_year(directory):
    """
    Counts the mean number of local citations by year.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.Series with the mean number of local citations by year.
    """
    mlcy = count_local_citations_by_year(directory).sort_index(
        ascending=True
    ) / count_documents_by_year(directory).sort_index(ascending=True)
    mlcy = mlcy.rename("mean_local_citations")
    mlcy = mlcy.round(2)
    return mlcy


def time_analysis(directory):
    """
    Counts the number of terms by record.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.DataFrame with the analysis.
    """

    num_documents = count_documents_by_year(directory).to_frame()
    global_citations = count_global_citations_by_year(directory).to_frame()
    local_citations = count_local_citations_by_year(directory).to_frame()
    mean_global_citations = mean_global_citations_by_year(directory)
    mean_local_citations = mean_local_citations_by_year(directory)

    report = pd.concat(
        [
            num_documents,
            global_citations,
            local_citations,
            mean_global_citations,
            mean_local_citations,
        ],
        axis=1,
    )
    report = report.sort_index(ascending=True, axis="index")
    report = report.assign(
        cum_num_documents=num_documents.sort_index(ascending=True).cumsum()
    )
    report = report.assign(
        cum_global_citations=global_citations.sort_index(ascending=True).cumsum()
    )
    report = report.assign(
        cum_local_citations=local_citations.sort_index(ascending=True).cumsum()
    )

    return report
