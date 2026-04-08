import pandas as pd  # type: ignore


def matrix_to_matrix_list(matrix: pd.DataFrame, value_name: str) -> pd.DataFrame:

    # matrix = matrix.reset_index(drop=False)

    matrix_list = matrix.melt(
        ignore_index=False, var_name="col", value_name=value_name
    ).reset_index()

    matrix_list = matrix_list.rename({"index": "rows", "col": "columns"}, axis=1)
    matrix_list["row_OCC"] = matrix_list["rows"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[0])
    )
    matrix_list["row_GCS"] = matrix_list["rows"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[1])
    )
    matrix_list["col_OCC"] = matrix_list["columns"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[0])
    )
    matrix_list["col_GCS"] = matrix_list["columns"].apply(
        lambda x: int(x.split(" ")[-1].split(":")[1])
    )

    matrix_list = matrix_list.sort_values(
        by=[value_name, "row_OCC", "col_OCC", "row_GCS", "col_GCS", "rows", "columns"],
        ascending=[False, False, False, False, False, True, True],
    ).reset_index(drop=True)

    matrix_list = matrix_list[["rows", "columns", value_name]]

    return matrix_list
