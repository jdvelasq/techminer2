"""
Associations for All Items
===============================================================================



>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> associations_for_all_items(
...     column='author_keywords',
...     directory=directory,
... ).head(10)
                              row                          column  OCC
0                  regtech 70:462                  regtech 70:462   70
1                  fintech 42:406                  fintech 42:406   42
2                  fintech 42:406                  regtech 70:462   42
3                  regtech 70:462                  fintech 42:406   42
4               blockchain 18:109               blockchain 18:109   18
5               blockchain 18:109                  regtech 70:462   17
6                  regtech 70:462               blockchain 18:109   17
7               blockchain 18:109                  fintech 42:406   14
8                  fintech 42:406               blockchain 18:109   14
9  artificial intelligence 13:065  artificial intelligence 13:065   13


"""
from .co_occ_matrix_list import co_occ_matrix_list


def associations_for_all_items(
    column,
    directory="./",
    database="documents",
):
    """Computes the co-occurrence matrix for a given column."""

    return co_occ_matrix_list(
        column=column,
        row=None,
        top_n=None,
        min_occ=None,
        max_occ=None,
        directory=directory,
        database=database,
    )
