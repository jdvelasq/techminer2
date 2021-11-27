"""
Co-occurrence matrix
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> co_occurrence_matrix(column='authors', min_occ=6,directory=directory)
authors                Rabbani MR Reyes-Mercado P Khan S Arner DW
#d                              8               7      6        6
#c                            65              0      52       125
authors         #d #c                                            
Rabbani MR      8  65           8               0      6        0
Reyes-Mercado P 7  0            0               7      0        0
Khan S          6  52           6               0      6        0
Arner DW        6  125          0               0      0        6



"""
import numpy as np
import pandas as pd

from .tf_matrix import tf_matrix
from .utils import *
from .utils import index_terms2counters

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def co_occurrence_matrix(
    column,
    by=None,
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    association=None,
    scheme=None,
    sep="; ",
    directory="./",
):

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

        matrix_in_rows = tf_matrix(
            directory=directory,
            column=by,
            min_occ=min_occ_by,
            max_occ=max_occ_by,
            scheme=scheme,
            sep=sep,
        )

        matrix_in_rows = matrix_in_rows.dropna()

        common_documents = matrix_in_columns.index.intersection(matrix_in_rows.index)
        matrix_in_columns = matrix_in_columns.loc[common_documents, :]
        matrix_in_rows = matrix_in_rows.loc[common_documents, :]

    matrix_values = np.matmul(
        matrix_in_rows.transpose().values, matrix_in_columns.values
    )

    co_occ_matrix = pd.DataFrame(
        matrix_values,
        columns=matrix_in_columns.columns,
        index=matrix_in_rows.columns,
    )

    co_occ_matrix = association_index(
        matrix=co_occ_matrix,
        association=association,
    )

    # ---< remove rows and columns with no associations >---------------------------------
    co_occ_matrix = co_occ_matrix.loc[:, (co_occ_matrix != 0).any(axis=0)]
    co_occ_matrix = co_occ_matrix.loc[(co_occ_matrix != 0).any(axis=1), :]

    return co_occ_matrix
