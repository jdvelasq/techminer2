"""
Co-word analyzer
===============================================================================

"""
import numpy as np
from sklearn.cluster import KMeans

from .association_index import association_index
from .co_occurrence_matrix import co_occurrence_matrix
from .plots.heatmap import heatmap
from .utils import adds_counters_to_axis

# pylint: disable=too-many-arguments


class CoWordAnalyzer:
    def __init__(
        self,
        directory_or_records,
        column,
        min_occurrence_column=1,
        max_occurrence_column=99999,
        max_terms=20,
        stopwords=None,
        association_metric="jaccard",
        clustering_algorithm=KMeans(),
        sep="; ",
    ):

        _table = co_occurrence_matrix(
            directory_or_records=directory_or_records,
            column=column,
            by=None,
            min_occurrence_column=min_occurrence_column,
            max_occurrence_column=max_occurrence_column,
            min_occurrence_by=min_occurrence_column,
            max_occurrence_by=max_occurrence_column,
            stopwords=stopwords,
            scheme=None,
            sep=sep,
        )

        normalized = association_index(_table, association_metric)
        dissimilarity_matrix = 1 - normalized
        dissimilarity_matrix = np.fill_diagonal(dissimilarity_matrix, 0)
        clustering_algorithm.fit(dissimilarity_matrix)

        _table = adds_counters_to_axis(
            directory_or_records=directory_or_records,
            table=_table,
            column=column,
            axis="columns",
            sep=sep,
        )
        _table = adds_counters_to_axis(
            directory_or_records=directory_or_records,
            table=_table,
            column=column,
            axis="index",
            sep=sep,
        )

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
