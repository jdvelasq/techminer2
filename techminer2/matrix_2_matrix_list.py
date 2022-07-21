"""Matrix -> Matrix List transformation"""


def matrix_2_matrix_list(matrix):
    """
    Transform a matrix into a matrix list.
    """

    matrix_list = matrix.melt(value_name="OCC", var_name="column", ignore_index=False)
    matrix_list = matrix_list.reset_index()
    matrix_list = matrix_list.rename(columns={"index": "row"})
    matrix_list = matrix_list.sort_values(
        by=["OCC", "row", "column"], ascending=[False, True, True]
    )
    matrix_list = matrix_list[matrix_list.OCC.astype(float) != 0.0]
    matrix_list = matrix_list.reset_index(drop=True)

    return matrix_list
