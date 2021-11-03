"""
Time Report
===============================================================================
"""

import pandas as pd

from .plots import *
from .utils import load_records_from_directory


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
    return _count_documents_by_year_from_records(load_records_from_directory(directory))


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
    return _count_local_citations_by_year_from_records(
        load_records_from_directory(directory)
    )


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
    return _count_global_citations_by_year_from_records(
        load_records_from_directory(directory)
    )


# ---< PUBLIC FUNCTIONS >---------------------------------------------------#


def count_documents_by_year(dirpath_or_records):
    """
    Counts the number of documents by year.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.Series with the number of documents by year.
    """
    if isinstance(dirpath_or_records, str):
        return _count_documents_by_year_from_directory(dirpath_or_records)
    elif isinstance(dirpath_or_records, pd.DataFrame):
        return _count_documents_by_year_from_records(dirpath_or_records)
    else:
        raise TypeError("dirpath_or_records must be a string or a pandas.DataFrame")


def count_global_citations_by_year(dirpath_or_records):
    """
    Counts the number of global citations by year.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.Series with the number of global citations by year.
    """
    if isinstance(dirpath_or_records, str):
        return _count_global_citations_by_year_from_directory(dirpath_or_records)
    elif isinstance(dirpath_or_records, pd.DataFrame):
        return _count_global_citations_by_year_from_records(dirpath_or_records)
    else:
        raise TypeError("dirpath_or_records must be a string or a pandas.DataFrame")


def count_local_citations_by_year(dirpath_or_records):
    """
    Counts the number of local citations by year.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.Series with the number of local citations by year.
    """
    if isinstance(dirpath_or_records, str):
        return _count_local_citations_by_year_from_directory(
            directory=dirpath_or_records
        )
    elif isinstance(dirpath_or_records, pd.DataFrame):
        return _count_local_citations_by_year_from_records(records=dirpath_or_records)
    else:
        raise TypeError("dirpath_or_records must be a string or a pandas.DataFrame")


def mean_global_citations_by_year(dirpath_or_records):
    """
    Counts the mean number of global citations by year.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.Series with the mean number of global citations by year.
    """
    mgcy = count_global_citations_by_year(dirpath_or_records).sort_index(
        ascending=True
    ) / count_documents_by_year(dirpath_or_records).sort_index(ascending=True)
    mgcy = mgcy.rename("mean_global_citations")
    mgcy = mgcy.round(2)
    return mgcy


def mean_local_citations_by_year(dirpath_or_records):
    """
    Counts the mean number of local citations by year.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.Series with the mean number of local citations by year.
    """
    mlcy = count_local_citations_by_year(dirpath_or_records).sort_index(
        ascending=True
    ) / count_documents_by_year(dirpath_or_records).sort_index(ascending=True)
    mlcy = mlcy.rename("mean_local_citations")
    mlcy = mlcy.round(2)
    return mlcy


def time_report(dirpath_or_records):
    """
    Counts the number of terms by record.

    :param dirpath_or_records: path to the directory or the records object
    :return: a pandas.DataFrame with the analysis.
    """

    num_documents = count_documents_by_year(dirpath_or_records).to_frame()
    global_citations = count_global_citations_by_year(dirpath_or_records).to_frame()
    local_citations = count_local_citations_by_year(dirpath_or_records).to_frame()
    mean_global_citations = mean_global_citations_by_year(dirpath_or_records)
    mean_local_citations = mean_local_citations_by_year(dirpath_or_records)

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
    analysis = analysis.sort_index(ascending=True, axis="index")
    analysis = analysis.assign(
        cum_num_documents=num_documents.sort_index(ascending=True).cumsum()
    )
    analysis = analysis.assign(
        cum_global_citations=global_citations.sort_index(ascending=True).cumsum()
    )
    analysis = analysis.assign(
        cum_local_citations=local_citations.sort_index(ascending=True).cumsum()
    )

    return analysis


# class TimeAnalyzer:
#     def __init__(
#         self,
#         dirpath_or_records,
#     ):
#         _table = time_analysis(
#             dirpath_or_records=dirpath_or_records,
#         )

#         self._table = _table

#     @property
#     def table_(self):
#         return self._table

#     def bar(
#         self,
#         column,
#         cmap="Greys",
#         figsize=(6, 5),
#         darkness=None,
#         fontsize=9,
#         edgecolor="k",
#         linewidth=0.5,
#         zorder=10,
#         ylabel=None,
#         xlabel=None,
#     ):

#         if column == "num_documents":
#             darkness = self._table["global_citations"]
#             if ylabel is None:
#                 ylabel = "Num Documents by Year"
#         elif column == "global_citations":
#             darkness = self._table["num_docum]ents"]
#             if ylabel is None:
#                 ylabel = "Global Citations by Year"
#         elif column == "local_citations":
#             darkness = self._table["num_documents"]
#             if ylabel is None:
#                 ylabel = "Local Citations by Year"
#         elif column == "cum_num_documents":
#             darkness = self._table["cum_global_citations"]
#             if ylabel is None:
#                 ylabel = "Cumulative Num Documents by Year"
#         elif column == "cum_global_citations":
#             darkness = self._table["cum_num_documents"]
#             if ylabel is None:
#                 ylabel = "Cumulative Global Citations by Year"
#         elif column == "cum_local_citations":
#             darkness = self._table["cum_num_documents"]
#             if ylabel is None:
#                 ylabel = "Cumulative Local Citations by Year"
#         else:
#             darkness = None
#             if ylabel is None:
#                 ylabel = column.replace("_", " ").title()

#         return bar_plot(
#             height=self._table[column],
#             cmap=cmap,
#             figsize=figsize,
#             darkness=darkness,
#             fontsize=fontsize,
#             edgecolor=edgecolor,
#             linewidth=linewidth,
#             zorder=zorder,
#             ylabel=ylabel,
#             xlabel=xlabel,
#         )

#     def barh(
#         self,
#         column,
#         cmap="Greys",
#         figsize=(6, 5),
#         darkness=None,
#         fontsize=9,
#         edgecolor="k",
#         linewidth=0.5,
#         zorder=10,
#         ylabel=None,
#         xlabel=None,
#     ):

#         if column == "num_documents":
#             darkness = self._table["global_citations"]
#             if xlabel is None:
#                 xlabel = "Num Documents by Year"
#         elif column == "global_citations":
#             darkness = self._table["num_documents"]
#             if xlabel is None:
#                 xlabel = "G]lobal Citations by Year"
#         elif column == "local_citations":
#             darkness = self._table["num_documents"]
#             if xlabel is None:
#                 xlabel = "Local Citations by Year"
#         elif column == "cum_num_documents":
#             darkness = self._table["cum_global_citations"]
#             if xlabel is None:
#                 xlabel = "Cumulative Num Documents by Year"
#         elif column == "cum_global_citations":
#             darkness = self._table["cum_num_documents"]
#             if xlabel is None:
#                 xlabel = "Cumulative Global Citations by Year"
#         elif column == "cum_local_citations":
#             darkness = self._table["cum_num_documents"]
#             if xlabel is None:
#                 xlabel = "Cumulative Local Citations by Year"
#         else:
#             darkness = None
#             if xlabel is None:
#                 xlabel = column.replace("_", " ").title()

#         return barh_plot(
#             width=self._table[column],
#             cmap=cmap,
#             figsize=figsize,
#             darkness=darkness,
#             fontsize=fontsize,
#             edgecolor=edgecolor,
#             linewidth=linewidth,
#             zorder=zorder,
#             ylabel=ylabel,
#             xlabel=xlabel,
#         )

#     def pie(
#         self,
#         column,
#         darkness=None,
#         cmap="Greys",
#         figsize=(6, 6),
#         fontsize=9,
#         wedgeprops={
#             "width": 0.6,
#             "edgecolor": "k",
#             "linewidth": 0.5,
#             "linestyle": "-",
#             "antialiased": True,
#         },
#     ):
#         return pie_plot(
#             x=self._table[column],
#             darkness=darkness,
#             cmap=cmap,
#             figsize=figsize,
#             fontsize=fontsize,
#             wedgeprops=wedgeprops,
#         )
