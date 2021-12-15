"""
Occurrence Matrix
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> occurrence_matrix(column='authors', min_occ=3,directory=directory)
authors           Wojcik D Rabbani MR Hornuf L
#d                       5          3        3
#c                     19         39       110
authors    #d #c                              
Wojcik D   5  19         5          0        0
Rabbani MR 3  39         0          3        0
Hornuf L   3  110        0          0        3



"""
import numpy as np
import pandas as pd

from .tf_matrix import tf_matrix
from .utils import *
from .utils import index_terms2counters

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def occurrence_matrix(
    column,
    by=None,
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    normalization=None,
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
        association=normalization,
    )

    # ---< remove rows and columns with no associations >---------------------------------
    co_occ_matrix = co_occ_matrix.loc[:, (co_occ_matrix != 0).any(axis=0)]
    co_occ_matrix = co_occ_matrix.loc[(co_occ_matrix != 0).any(axis=1), :]

    return co_occ_matrix
