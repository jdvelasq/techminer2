"""
Association Index (*) --- ChatGPT
===============================================================================

Association index is used to measure the similarity between two terms in a
co-occurrence matrix. The association index is a normalized version of the
co-occurrence matrix.



"""
import numpy as np

from ...classes import CocMatrix, NormCocMatrix


def association_index(obj, index_name):
    """
    Calculate the association index for a co-occurrence matrix.

    Args:
        obj: A :class:`CocMatrix` instance.
        index_name (str): The association index to be used. Available options
            are:
            - ``"jaccard"``: Jaccard index.
            - ``"dice"``: Dice index.
            - ``"salton"``: Salton index.
            - ``"equivalence"``: Equivalente index.
            - ``"inclusion"``: Inclusion index.
            - ``"mutualinfo"``: Mutual information index.
            - ``"association"``: Association index.

    """

    def jaccard(matrix, normalized_matrix):
        """Jaccard index."""

        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / (
                    matrix.loc[row, row]
                    + matrix.at[col, col]
                    - matrix.at[row, col]
                )

        return matrix

    def dice(matrix, normalized_matrix):
        """Dice index."""

        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / (
                    matrix.loc[row, row] + matrix.at[col, col]
                )

        return matrix

    def salton(matrix, normalized_matrix):
        """Salton index."""

        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / np.sqrt(
                    matrix.loc[row, row] * matrix.at[col, col]
                )

        return matrix

    def equivalence(matrix, normalized_matrix):
        """Equivalence index."""

        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] ** 2 / (
                    matrix.loc[row, row] * matrix.at[col, col]
                )

        return matrix

    def inclusion(matrix, normalized_matrix):
        """Inclusion index."""

        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / min(
                    matrix.loc[row, row], matrix.at[col, col]
                )

        return matrix

    def mutualinfo(matrix, normalized_matrix):
        """Mutual information index."""

        n_columns = len(matrix.columns)
        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = np.log(
                    matrix.at[row, col]
                    / (n_columns * matrix.loc[row, row] * matrix.at[col, col])
                )

        return matrix

    def association(matrix, normalized_matrix):
        """Association index."""

        for col in matrix.columns:
            for row in matrix.index:
                normalized_matrix.at[row, col] = matrix.at[row, col] / (
                    matrix.loc[row, row] * matrix.at[col, col]
                )

        return matrix

    #
    # Main:
    #

    if not isinstance(obj, CocMatrix):
        raise TypeError("obj must be a CocMatrix instance")

    if isinstance(index_name, str) and index_name == "None":
        index_name = None

    if index_name is None:
        return obj

    fnc = {
        "jaccard": jaccard,
        "dice": dice,
        "salton": salton,
        "equivalence": equivalence,
        "inclusion": inclusion,
        "mutualinfo": mutualinfo,
        "association": association,
    }[index_name]

    matrix = obj.matrix_.copy()
    matrix = matrix.applymap(float)
    normalized_matrix = matrix.copy()
    normalized_matrix = fnc(matrix, normalized_matrix)

    for index in range(len(normalized_matrix)):
        normalized_matrix.iloc[index, index] = 0.0

    normcocmatrix = NormCocMatrix()
    normcocmatrix.matrix_ = normalized_matrix
    normcocmatrix.prompt_ = obj.prompt_
    normcocmatrix.metric_ = obj.metric_
    normcocmatrix.columns_ = obj.columns_
    normcocmatrix.rows_ = obj.rows_
    normcocmatrix.association_index_ = index_name

    return normcocmatrix
