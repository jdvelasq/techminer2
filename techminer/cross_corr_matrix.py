"""
Cross-correlation matrix
===============================================================================

"""
import numpy as np
import pandas as pd

from .co_occurrence_matrix import co_occurrence_matrix
from .tf_matrix import tf_matrix
from .utils import adds_counters_to_axis
from .utils.io import load_filtered_documents

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def cross_corr_matrix(
    directory,
    column,
    by=None,
    method="pearson",
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    scheme=None,
    sep="; ",
):
    """
    Returns a co-occurrence matrix.

    :param directory_or_records:
        A directory or a list of records.
    :param column:
        The column to be used.
    :param by:
        The column to be used to group the records.
    :param min_occurrence:
        The minimum occurrence of a word.
    :param max_occurrence:
        The maximum occurrence of a word.
    :param stopwords:
        A list of stopwords.
    :param scheme:
        The scheme to be used.
    :param sep:
        The separator to be used.
    :return:
        A co-occurrence matrix.
    """

    co_occ_matrix = co_occurrence_matrix(
        directory=directory,
        column=column,
        by=by,
        min_occ=min_occ,
        max_occ=max_occ,
        min_occ_by=min_occ_by,
        max_occ_by=max_occ_by,
        scheme=scheme,
        sep=sep,
    )

    matrix = co_occ_matrix.corr(method=method)
    matrix = matrix.fillna(0)

    # repair NaN values in cross-correlation matrix
    np.fill_diagonal(matrix.values, 1.0)

    return matrix
