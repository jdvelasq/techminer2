def matrix_to_matrix_list(matrix, value_name):
    matrix = matrix.melt(value_name=value_name, var_name="column", ignore_index=False)
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={"index": "row"})
    matrix = matrix.sort_values(
        by=[value_name, "row", "column"], ascending=[False, True, True]
    )
    matrix = matrix[matrix[value_name] != 0.0]
    matrix = matrix.reset_index(drop=True)

    return matrix
