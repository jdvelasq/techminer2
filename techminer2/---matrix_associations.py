"""
Matrix / Associations
===============================================================================


"""
import pandas as pd


def matrix_associations(matrix):

    names_cols = matrix.columns.get_level_values(0)
    names_rows = matrix.index.get_level_values(0)
    n_rows = matrix.shape[0]
    n_cols = matrix.shape[1]
    edges = []
    for i_row in range(0, n_rows):
        for i_col in range(0, n_cols):
            if matrix.iloc[i_row, i_col] > 0:
                edges.append(
                    {
                        "word_A": names_rows[i_row],
                        "word_B": names_cols[i_col],
                        "co_occ": matrix.iloc[i_row, i_col],
                    }
                )

    co_occ = pd.DataFrame(edges)
    co_occ = co_occ.sort_values(by="co_occ", ascending=False)
    co_occ = co_occ.reset_index(drop=True)

    return co_occ
