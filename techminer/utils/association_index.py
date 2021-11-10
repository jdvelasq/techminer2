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
        for col in normalized_matrix.columns:
            for row in normalized_matrix.index:
                matrix.at[row, col] = normalized_matrix.at[row, col] / (
                    normalized_matrix.loc[row, row]
                    + normalized_matrix.at[col, col]
                    - normalized_matrix.at[row, col]
                )
    elif association == "dice":
        for col in normalized_matrix.columns:
            for row in normalized_matrix.index:
                matrix.at[row, col] = normalized_matrix.at[row, col] / (
                    normalized_matrix.loc[row, row]
                    + normalized_matrix.at[col, col]
                    + 2 * normalized_matrix.at[row, col]
                )
    elif association == "salton":  # cosine
        for col in normalized_matrix.columns:
            for row in normalized_matrix.index:
                matrix.at[row, col] = normalized_matrix.at[row, col] / np.sqrt(
                    (normalized_matrix.loc[row, row] * normalized_matrix.at[col, col])
                )

    elif association == "equivalence":
        for col in normalized_matrix.columns:
            for row in normalized_matrix.index:
                matrix.at[row, col] = normalized_matrix.at[row, col] ** 2 / (
                    normalized_matrix.loc[row, row] * normalized_matrix.at[col, col]
                )
    elif association == "inclusion":
        for col in normalized_matrix.columns:
            for row in normalized_matrix.index:
                matrix.at[row, col] = normalized_matrix.at[row, col] / min(
                    normalized_matrix.loc[row, row], normalized_matrix.at[col, col]
                )

    elif association == "mutualinfo":
        n_columns = len(normalized_matrix.columns)
        for col in normalized_matrix.columns:
            for row in normalized_matrix.index:
                matrix.at[row, col] = np.log(
                    normalized_matrix.at[row, col]
                    / (
                        n_columns
                        * normalized_matrix.loc[row, row]
                        * normalized_matrix.at[col, col]
                    )
                )
    elif association == "association":
        for col in normalized_matrix.columns:
            for row in normalized_matrix.index:
                matrix.at[row, col] = normalized_matrix.at[row, col] / (
                    normalized_matrix.loc[row, row] * normalized_matrix.at[col, col]
                )
    else:
        raise ValueError("Unknown normalization method.")

    return normalized_matrix
