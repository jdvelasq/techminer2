import pandas as pd  # type: ignore


def remove_isolated_nodes_from_matrix_list(matrix_list: pd.DataFrame) -> pd.DataFrame:
    matrix_list = matrix_list.copy()
    selected = [row["rows"] != row["columns"] for _, row in matrix_list.iterrows()]
    matrix_list = matrix_list.loc[selected, :]
    return matrix_list
