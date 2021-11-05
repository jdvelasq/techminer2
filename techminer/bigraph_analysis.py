"""
Bigraph analyzer
===============================================================================

"""

from .co_occurrence_matrix import co_occurrence_matrix
from .heat_map import heat_map
from .utils import adds_counters_to_axis

# pylint: disable=too-many-arguments


class BigraphAnalyzer:
    def __init__(
        self,
        directory_or_records,
        column,
        by=None,
        top_by="num_docs",
        min_occurrence_column=1,
        max_occurrence_column=99999,
        max_terms_column=20,
        min_occurrence_by=1,
        max_occurrence_by=99999,
        max_terms_by=20,
        stopwords=None,
        sep_column="; ",
        sep_by="; ",
    ):
        _table = co_occurrence_matrix(
            directory_or_records=directory_or_records,
            column=column,
            by=by,
            min_occurrence_column=min_occurrence_column,
            max_occurrence_column=max_occurrence_column,
            min_occurrence_by=min_occurrence_by,
            max_occurrence_by=max_occurrence_by,
            stopwords=stopwords,
            scheme=None,
            sep=sep_column,
        )

        _table = adds_counters_to_axis(
            directory_or_records=directory_or_records,
            table=_table,
            column=column,
            axis="columns",
            sep=sep_column,
        )
        _table = adds_counters_to_axis(
            directory_or_records=directory_or_records,
            table=_table,
            column=by,
            axis="index",
            sep=sep_by,
        )

        if top_by == "num_docs":
            _table = _table.sort_index(axis="columns", level=[1, 2, 0], ascending=False)
            _table = _table.sort_index(axis="index", level=[1, 2, 0], ascending=False)
            _table = _table.iloc[:max_terms_by, :max_terms_column]
        elif top_by == "cited_by":
            _table = _table.sort_index(axis="columns", level=[2, 1, 0], ascending=False)
            _table = _table.sort_index(axis="index", level=[2, 1, 0], ascending=False)
            _table = _table.iloc[:max_terms_by, :max_terms_column]
        else:
            raise ValueError(f"top_by={top_by} not supported")

        #
        self._table = _table

    @property
    def table_(self):
        return self._table

    def sort_index(
        self,
        axis=0,
        level=None,
        ascending=True,
        kind="quicksort",
        na_position="last",
        sort_remaining=True,
        key=None,
    ):
        self._table.sort_index(
            axis=axis,
            level=level,
            ascending=ascending,
            kind=kind,
            na_position=na_position,
            sort_remaining=sort_remaining,
            key=key,
            inplace=True,
        )

    def sort_values(
        self,
        by,
        axis=0,
        ascending=True,
        kind="quicksort",
        na_position="last",
        key=None,
    ):
        self._table.sort_values(
            by=by,
            axis=axis,
            ascending=ascending,
            kind=kind,
            na_position=na_position,
            key=key,
        )

    def heatmap(
        self,
        cmap="Greys",
        figsize=(6, 6),
        fontsize=9,
    ):
        return heatmap(
            self.table_,
            cmap=cmap,
            figsize=figsize,
            fontsize=fontsize,
        )
