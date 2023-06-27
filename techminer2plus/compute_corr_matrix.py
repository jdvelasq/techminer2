"""Computes the correlation matrix for a given data matrix."""

import pandas as pd

from .co_occurrence_matrix import CoocMatrix
from .tf_matrix import TFMatrix


def compute_corr_matrix(
    method,
    data_matrix,
):
    """Computes the correlation matrix for a given data matrix.

    INPUTS:
      method: str
        The correlation method. See pandas.DataFrame.corr for more information.
      data_matrix: pandas.DataFrame
        The data matrix. It is a TF matrix.
    OUTPUTS:
        corr_matrix: pandas.DataFrame
            The correlation matrix.
    """

    if isinstance(data_matrix, TFMatrix):
        table = data_matrix.table_.copy()
    elif isinstance(data_matrix, CoocMatrix):
        table = data_matrix.matrix_.copy()
    else:
        raise TypeError("data_matrix must be a TFMatrix or a CorrMatrix.")

    corr_matrix = pd.DataFrame(
        0.0,
        columns=table.columns.to_list(),
        index=table.columns.to_list(),
    )

    for col in table.columns:
        for row in table.columns:
            if col == row:
                corr_matrix.loc[row, col] = 1.0
            else:
                matrix = table[[col, row]].copy()
                matrix = matrix.loc[(matrix != 0).any(axis=1)]
                matrix = matrix.astype(float)
                sumproduct = matrix[row].mul(matrix[col], axis=0).sum()
                if matrix.shape[0] == 0:
                    corr = 0.0
                elif sumproduct == 0.0:
                    corr = 0.0
                elif matrix.shape[0] == 1:
                    corr = 1.0
                elif matrix.shape[0] > 1:
                    corr = table[col].corr(other=table[row], method=method)
                else:
                    corr = 0.0
                corr_matrix.loc[row, col] = corr
                corr_matrix.loc[col, row] = corr

    return corr_matrix
