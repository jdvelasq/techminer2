"""
Co-occurrence Matrix
===============================================================================

"""
import numpy as np
import pandas as pd

from techminer.utils.io import load_records_from_directory

from .tf_matrix import tf_matrix


# pyltin: disable=c0103
# pylint: disable=too-many-arguments
def _co_occurrence_matrix_from_records(
    records,
    column,
    by,
    min_occurrence_column,
    max_occurrence_column,
    min_occurrence_by,
    max_occurrence_by,
    stopwords,
    scheme,
    sep,
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
        records = records[[column, "record_id"]].dropna()
        matrix_in_columns = tf_matrix(
            directory_or_records=records,
            column=column,
            min_occurrence=min_occurrence_column,
            max_occurrence=max_occurrence_column,
            stopwords=stopwords,
            scheme=scheme,
            sep=sep,
        )
        matrix_in_rows = matrix_in_columns.copy()
    else:
        records = records[[column, by, "record_id"]].dropna()

        matrix_in_columns = tf_matrix(
            directory_or_records=records,
            column=column,
            min_occurrence=min_occurrence_column,
            max_occurrence=max_occurrence_column,
            stopwords=stopwords,
            scheme=scheme,
            sep=sep,
        )

        matrix_in_rows = tf_matrix(
            directory_or_records=records,
            column=by,
            min_occurrence=min_occurrence_by,
            max_occurrence=max_occurrence_by,
            stopwords=stopwords,
            scheme=scheme,
            sep=sep,
        )

    matrix = np.matmul(matrix_in_rows.transpose().values, matrix_in_columns.values)

    pdf = pd.DataFrame(
        matrix,
        columns=matrix_in_columns.columns,
        index=matrix_in_rows.columns,
    )

    return pdf


def _co_occurrence_matrix_from_directory(
    directory,
    column,
    by,
    min_occurrence_column,
    max_occurrence_column,
    min_occurrence_by,
    max_occurrence_by,
    stopwords,
    scheme,
    sep,
):

    return _co_occurrence_matrix_from_records(
        records=load_records_from_directory(directory),
        column=column,
        by=by,
        min_occurrence_column=min_occurrence_column,
        max_occurrence_column=max_occurrence_column,
        min_occurrence_by=min_occurrence_by,
        max_occurrence_by=max_occurrence_by,
        stopwords=stopwords,
        scheme=scheme,
        sep=sep,
    )


def co_occurrence_matrix(
    directory_or_records,
    column,
    by=None,
    min_occurrence_column=1,
    max_occurrence_column=99999,
    min_occurrence_by=1,
    max_occurrence_by=99999,
    stopwords=None,
    scheme=None,
    sep="; ",
):
    if isinstance(directory_or_records, str):
        return _co_occurrence_matrix_from_directory(
            directory=directory_or_records,
            column=column,
            by=by,
            min_occurrence_column=min_occurrence_column,
            max_occurrence_column=max_occurrence_column,
            min_occurrence_by=min_occurrence_by,
            max_occurrence_by=max_occurrence_by,
            stopwords=stopwords,
            scheme=scheme,
            sep=sep,
        )
    elif isinstance(directory_or_records, pd.DataFrame):
        return _co_occurrence_matrix_from_records(
            records=directory_or_records,
            column=column,
            by=by,
            min_occurrence_column=min_occurrence_column,
            max_occurrence_column=max_occurrence_column,
            min_occurrence_by=min_occurrence_by,
            max_occurrence_by=max_occurrence_by,
            stopwords=stopwords,
            scheme=scheme,
            sep=sep,
        )
    else:
        raise TypeError("directory_or_records must be a string or a pandas.DataFrame")
