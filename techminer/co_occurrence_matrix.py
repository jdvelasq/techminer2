"""
Co-occurrence matrix
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> co_occurrence_matrix(directory, column='authors', min_occ=6)
authors                 Rabbani MR Arner DW  ... Surjandy Schwienbacher A
#d                              10       9   ...       6               6 
#c                             72       154  ...      19              56 
authors          #d #c                       ...                         
Rabbani MR       10 72          10        0  ...        0               0
Arner DW         9  154          0        9  ...        0               0
Buckley RP       7  151          0        7  ...        0               0
Tan B            7  113          0        0  ...        0               0
Reyes-Mercado P  7  0            0        0  ...        0               0
Gozman DP        7  91           0        0  ...        0               0
Wojcik D         7  51           0        0  ...        0               0
Khan S           6  50           6        0  ...        0               0
Serrano W        6  15           0        0  ...        0               0
Fernando E       6  19           0        0  ...        6               0
Wonglimpiyarat J 6  55           0        0  ...        0               0
Ashta A          6  41           0        0  ...        0               0
Ozili PK         6  143          0        0  ...        0               0
Giudici P        6  35           0        0  ...        0               0
Zetzsche D       6  67           0        5  ...        0               0
Surjandy         6  19           0        0  ...        6               0
Schwienbacher A  6  56           0        0  ...        0               6
<BLANKLINE>
[17 rows x 17 columns]

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
    directory,
    column,
    by=None,
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    association=None,
    scheme=None,
    sep="; ",
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
