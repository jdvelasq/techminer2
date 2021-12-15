"""
Association index or similarity coefficient
===============================================================================

"""

import numpy as np


def association_index(matrix, association):
    """
    Calculate the association index for a given association.

    Parameters
    ----------
    matrix : pandas.DataFrame
        The matrix to calculate the association index for.
    association : str
        The association to calculate the association index for.

    Returns
    -------
    float
        The association index.

    """
    matrix = matrix.copy()

    if isinstance(association, str) and association == "None":
        association = None

    if association is None:
        matrix = matrix.applymap(int)
        return matrix

    matrix = matrix.applymap(float)
    normalized_matrix = matrix.copy()

    if association == "jaccard":
        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / (
                    matrix.loc[row, row] + matrix.at[col, col] - matrix.at[row, col]
                )
    elif association == "dice":
        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / (
                    matrix.loc[row, row] + matrix.at[col, col] + 2 * matrix.at[row, col]
                )
    elif association == "salton":  # cosine
        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / np.sqrt(
                    (matrix.loc[row, row] * matrix.at[col, col])
                )

    elif association == "equivalence":
        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] ** 2 / (
                    matrix.loc[row, row] * matrix.at[col, col]
                )
    elif association == "inclusion":
        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / min(
                    matrix.loc[row, row], matrix.at[col, col]
                )

    elif association == "mutualinfo":
        n_columns = len(matrix.columns)
        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = np.log(
                    matrix.at[row, col]
                    / (n_columns * matrix.loc[row, row] * matrix.at[col, col])
                )
    elif association == "association":
        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / (
                    matrix.loc[row, row] * matrix.at[col, col]
                )
    else:
        raise ValueError("Unknown normalization method.")

    return normalized_matrix
