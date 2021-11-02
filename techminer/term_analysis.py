"""
Term Analysis
===============================================================================




"""

import pandas as pd

from .plots import *
from .utils import load_records_from_directory


def _count_records_by_term_from_records(records, column, sep):
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
        .rename("num_records")
    )


def _count_records_by_term_from_directory(directory, column, sep):
    """
    Counts the number of documents containing a given term.

    :param directory: path to the directory
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of documents containing a given term.
    """
    return _count_records_by_term_from_records(
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


def count_records_by_term(directory_or_records, column, sep="; "):
    """
    Counts the number of documents containing a given term.

    :param directory_or_records: path to the directory or the records object
    :param column: column to be used to count the documents
    :param sep: separator to be used to split the column
    :return: a pandas.Series with the number of documents containing a given term.
    """
    if isinstance(directory_or_records, str):
        return _count_records_by_term_from_directory(directory_or_records, column, sep)
    elif isinstance(directory_or_records, pd.DataFrame):
        return _count_records_by_term_from_records(directory_or_records, column, sep)
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

    num_records = count_records_by_term(directory_or_records, column, sep).to_frame()
    global_citations = count_global_citations_by_term(
        directory_or_records, column, sep
    ).to_frame()
    local_citations = count_local_citations_by_term(
        directory_or_records, column, sep
    ).to_frame()

    analysis = pd.concat([num_records, global_citations, local_citations], axis=1)

    return analysis


class TermAnalyzer:
    def __init__(
        self,
        directory_or_records,
        column,
        top_by="num_records",
        min_occ=1,
        max_terms=20,
        sep="; ",
    ) -> None:
        _table = term_analysis(
            directory_or_records=directory_or_records,
            column=column,
            sep=sep,
        )
        _table.sort_values(by=top_by, ascending=False, inplace=True)
        _table.query(f"num_records >= {min_occ}", inplace=True)
        _table = _table.head(max_terms)
        self._table = _table

    def sort_values(
        self,
        by,
        ascending=True,
        key=None,
    ):
        return self._table.sort_values(
            by=by,
            ascending=ascending,
            key=key,
            inplace=True,
        )

    def sort_index(
        self,
        ascending=True,
        axis="columns",
        key=None,
    ):
        return self._table.sort_index(
            ascending=ascending,
            key=key,
            inplace=True,
        )

    @property
    def table_(self):
        return self._table

    def bar(
        self,
        column,
        cmap="Greys",
        figsize=(6, 5),
        darkness=None,
        fontsize=9,
        edgecolor="k",
        linewidth=0.5,
        zorder=10,
        ylabel=None,
        xlabel=None,
    ):
        if ylabel is None:
            ylabel = column

        return bar_plot(
            height=self._table[column],
            cmap=cmap,
            figsize=figsize,
            darkness=darkness,
            fontsize=fontsize,
            edgecolor=edgecolor,
            linewidth=linewidth,
            zorder=zorder,
            ylabel=ylabel,
            xlabel=xlabel,
        )

    def barh(
        self,
        column,
        cmap="Greys",
        figsize=(6, 5),
        darkness=None,
        fontsize=9,
        edgecolor="k",
        linewidth=0.5,
        zorder=10,
        ylabel=None,
        xlabel=None,
    ):

        if ylabel is None:
            ylabel = column

        return barh_plot(
            width=self._table[column],
            cmap=cmap,
            figsize=figsize,
            darkness=darkness,
            fontsize=fontsize,
            edgecolor=edgecolor,
            linewidth=linewidth,
            zorder=zorder,
            ylabel=ylabel,
            xlabel=xlabel,
        )

    def pie(
        self,
        column,
        darkness=None,
        cmap="Greys",
        figsize=(6, 6),
        fontsize=9,
        wedgeprops={
            "width": 0.6,
            "edgecolor": "k",
            "linewidth": 0.5,
            "linestyle": "-",
            "antialiased": True,
        },
    ):
        return pie_plot(
            x=self._table[column],
            darkness=darkness,
            cmap=cmap,
            figsize=figsize,
            fontsize=fontsize,
            wedgeprops=wedgeprops,
        )

    def wordcloud(
        self,
        column,
        darkness=None,
        figsize=(6, 6),
        font_path=None,
        width=400,
        height=200,
        margin=2,
        ranks_only=None,
        prefer_horizontal=0.9,
        mask=None,
        scale=1,
        max_words=200,
        min_font_size=4,
        stopwords=None,
        random_state=None,
        background_color="white",
        max_font_size=None,
        font_step=1,
        mode="RGB",
        relative_scaling="auto",
        regexp=None,
        collocations=True,
        cmap="Blues",
        normalize_plurals=True,
        contour_width=0,
        contour_color="black",
        repeat=False,
    ):
        return wordcloud_(
            x=self._table[column],
            darkness=darkness,
            figsize=figsize,
            font_path=font_path,
            width=width,
            height=height,
            margin=margin,
            ranks_only=ranks_only,
            prefer_horizontal=prefer_horizontal,
            mask=mask,
            scale=scale,
            max_words=max_words,
            min_font_size=min_font_size,
            stopwords=stopwords,
            random_state=random_state,
            background_color=background_color,
            max_font_size=max_font_size,
            font_step=font_step,
            mode=mode,
            relative_scaling=relative_scaling,
            regexp=regexp,
            collocations=collocations,
            cmap=cmap,
            normalize_plurals=normalize_plurals,
            contour_width=contour_width,
            contour_color=contour_color,
            repeat=repeat,
        )

    def treemap(
        self,
        column,
        darkness=None,
        cmap="Greys",
        fontsize=9,
        alpha=0.8,
        figsize=(6, 5),
    ):
        return treemap(
            x=self.table_[column],
            darkness=darkness,
            cmap=cmap,
            figsize=figsize,
            fontsize=fontsize,
            alpha=alpha,
        )
