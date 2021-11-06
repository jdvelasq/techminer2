"""
Co-occurrence matrix
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


def co_occurrence_matrix(
    directory,
    column,
    by=None,
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

    if by is None or column == by:
        by = column
        matrix_in_columns = tf_matrix(
            directory=directory,
            column=column,
            min_occ=min_occ,
            max_occ=max_occ,
            scheme=scheme,
            sep=sep,
        )
        matrix_in_columns = matrix_in_columns.dropna()
        matrix_in_rows = matrix_in_columns.copy()
    else:

        matrix_in_columns = tf_matrix(
            directory=directory,
            column=column,
            min_occ=min_occ,
            max_occ=max_occ,
            scheme=scheme,
            sep=sep,
        )

        matrix_in_columns = matrix_in_columns.dropna()

        matrix_in_rows = tf_matrix(
            directory_or_records=directory,
            column=by,
            min_occ=min_occ_by,
            max_occ=max_occ_by,
            scheme=scheme,
            sep=sep,
        )

        matrix_in_rows = matrix_in_rows.loc[matrix_in_columns.index, :]
        matrix_in_rows = matrix_in_rows.dropna()
        matrix_in_columns = matrix_in_columns.loc[matrix_in_rows.index, :]

    matrix = np.matmul(matrix_in_rows.transpose().values, matrix_in_columns.values)

    pdf = pd.DataFrame(
        matrix,
        columns=matrix_in_columns.columns,
        index=matrix_in_rows.columns,
    )

    documents = load_filtered_documents(directory)
    pdf = adds_counters_to_axis(documents, pdf, axis="columns", column=column, sep=sep)
    pdf = adds_counters_to_axis(documents, pdf, axis="index", column=by, sep=sep)

    return pdf
