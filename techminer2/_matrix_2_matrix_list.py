"""Matrix -> Matrix List transformation"""


def matrix_2_matrix_list(matrix):
    """
    Convert a matrix to a matrix list.

    Args:
        matrix (pd.DataFrame): The matrix to convert.

    Returns:
        pd.DataFrame: The matrix list.
    """

    # Melt the matrix to a long format
    matrix_list = matrix.melt(value_name="OCC", var_name="column", ignore_index=False)

    # Reset the index and rename the index column to "row"
    matrix_list = matrix_list.reset_index().rename(columns={"index": "row"})

    # Sort the matrix list by "OCC", "row", and "column" columns
    matrix_list = matrix_list.sort_values(
        by=["OCC", "row", "column"], ascending=[False, True, True]
    )

    # Remove rows with OCC value of 0
    matrix_list = matrix_list[matrix_list.OCC.astype(float) != 0.0].reset_index(
        drop=True
    )

    return matrix_list
