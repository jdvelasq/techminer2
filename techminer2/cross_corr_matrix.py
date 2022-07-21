"""
Cross-correlation Matrix
===============================================================================


>>> from techminer2 import *
>>> directory = "data/regtech/"

>>> cross_corr_matrix(
...     'authors', 
...     by='countries',
...     top_n=10,
...     directory=directory,
... )
                   Arner DW 7:220  ...  Zetzsche DA 4:092
Arner DW 7:220           1.000000  ...           0.943564
Barberis JN 4:146        0.930115  ...           0.758266
Brennan R 3:008         -0.246183  ...          -0.250873
Buckley RP 6:217         0.995464  ...           0.958911
Crane M 2:008           -0.246183  ...          -0.250873
Das SR 2:028            -0.246183  ...          -0.250873
Hamdan A 2:011          -0.436436  ...          -0.444750
Ryan P 3:008            -0.246183  ...          -0.250873
Turki M 2:011           -0.436436  ...          -0.444750
Zetzsche DA 4:092        0.943564  ...           1.000000
<BLANKLINE>
[10 rows x 10 columns]

"""
from .vantagepoint__co_occ_matrix_list import (
    _add_counters_to_items,
    _create_matrix_list,
    _remove_stopwords,
    _select_top_n_items,
)


def cross_corr_matrix(
    column,
    by,
    method="pearson",
    top_n=50,
    directory="./",
    database="documents",
):

    matrix_list = _create_matrix_list(
        column=column,
        row=by,
        directory=directory,
        database=database,
    )

    matrix_list = _remove_stopwords(directory, matrix_list)
    matrix_list = _add_counters_to_items(
        column, "column", directory, database, matrix_list
    )
    matrix_list = _add_counters_to_items(by, "row", directory, database, matrix_list)
    matrix_list = _select_top_n_items(top_n, matrix_list, "column")

    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    matrix = matrix.fillna(0)
    matrix = matrix.corr(method=method)
    matrix.columns = matrix.columns.to_list()
    matrix.index = matrix.index.to_list()

    return matrix
