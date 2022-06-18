"""
Co-occurrence Matrix / Associations
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> co_occurrence_matrix_associations(
...     column='author_keywords', 
...     min_occ=3, 
...     directory=directory,
... ).head()
                   word_A   word_B  co_occ
0     financial inclusion  fintech      15
1  financial technologies  fintech      14
2              blockchain  fintech      13
3              innovation  fintech      10
4              regulation  fintech      10


"""
import pandas as pd

from .co_occurrence_matrix import co_occurrence_matrix


def co_occurrence_matrix_associations(
    column,
    min_occ=1,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column,
        min_occ=min_occ,
        directory=directory,
    )

    # -------------------------------------------------------------------------
    names = coc_matrix.columns.get_level_values(0)
    n_cols = coc_matrix.shape[1]
    edges = []
    for i_row in range(1, n_cols):
        for i_col in range(0, i_row):
            if coc_matrix.iloc[i_row, i_col] > 0:
                edges.append(
                    {
                        "word_A": names[i_row],
                        "word_B": names[i_col],
                        "co_occ": coc_matrix.iloc[i_row, i_col],
                    }
                )

    # -------------------------------------------------------------------------
    co_occ = pd.DataFrame(edges)
    co_occ = co_occ.sort_values(
        by=["co_occ", "word_A", "word_B"], ascending=[False, True, True]
    )
    co_occ = co_occ.reset_index(drop=True)
    return co_occ
