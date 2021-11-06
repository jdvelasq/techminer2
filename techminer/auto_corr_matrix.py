"""
Auto-correlation matrix
===============================================================================

"""
import numpy as np
import pandas as pd

from .tf_matrix import tf_matrix
from .utils import adds_counters_to_axis
from .utils.io import load_filtered_documents

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def auto_corr_matrix(
    directory,
    column,
    method="pearson",
    min_occ=1,
    max_occ=None,
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

    doc_term_matrix = tf_matrix(
        directory=directory,
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        scheme=scheme,
        sep=sep,
    )
    matrix = doc_term_matrix.corr(method=method)

    documents = load_filtered_documents(directory)
    matrix = adds_counters_to_axis(
        documents, matrix, axis="columns", column=column, sep=sep
    )
    matrix = adds_counters_to_axis(
        documents, matrix, axis="index", column=column, sep=sep
    )

    return matrix
