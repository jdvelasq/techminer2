"""
Occurrence Matrix / Associations
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> occurrence_associations(
...     column='authors', 
...     min_occ=2, 
...     by="author_keywords",
...     min_occ_by=6,
...     directory=directory,
... ).head()
                   word_A        word_B  co_occ
0                 fintech      Wojcik D       5
1                 fintech      Hornuf L       3
2              innovation        Iman N       2
3                 fintech  Zavolokina L       2
4  financial technologies      Wojcik D       2


"""
import pandas as pd

from .occurrence_matrix import occurrence_matrix


def occurrence_associations(
    column,
    by=None,
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    normalization=None,
    directory="./",
):

    matrix = occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        by=by,
        min_occ_by=min_occ_by,
        max_occ_by=max_occ_by,
        normalization=normalization,
        directory=directory,
    )

    # -------------------------------------------------------------------------
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

    # -------------------------------------------------------------------------
    co_occ = pd.DataFrame(edges)
    co_occ = co_occ.sort_values(by="co_occ", ascending=False)
    co_occ = co_occ.reset_index(drop=True)
    return co_occ
