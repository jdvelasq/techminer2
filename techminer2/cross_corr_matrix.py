"""
Cross-correlation Matrix
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"

>>> cross_corr_matrix(
...     'authors', 
...     by='countries',
...     top_n=10,
...     directory=directory,
... )
                   Arner DW 7:220  ...  Zetzsche DA 4:092
Arner DW 7:220           1.000000  ...           0.905757
Barberis JN 4:146        0.946946  ...           0.723015
Brennan R 3:008         -0.242974  ...          -0.278930
Buckley RP 6:217         0.992973  ...           0.939966
Hamdan A 2:011          -0.362204  ...          -0.415804
Lin W 2:007             -0.183258  ...          -0.186017
Ryan P 3:008            -0.242974  ...          -0.278930
Sarea A 2:006           -0.362204  ...          -0.415804
Turki M 2:011           -0.362204  ...          -0.415804
Zetzsche DA 4:092        0.905757  ...           1.000000
<BLANKLINE>
[10 rows x 10 columns]

"""
from .co_occ_matrix_list import (
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
    matrix_list = _add_counters_to_items(column, by, directory, database, matrix_list)
    matrix_list = _select_top_n_items(top_n, matrix_list, "column")

    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
    matrix = matrix.fillna(0)
    matrix = matrix.corr(method=method)
    matrix.columns = matrix.columns.to_list()
    matrix.index = matrix.index.to_list()

    return matrix


from .occurrence_matrix import occurrence_matrix

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def cross_corr_matrix_xx(
    column,
    by=None,
    method="pearson",
    min_occ=1,
    max_occ=None,
    min_occ_by=1,
    max_occ_by=None,
    scheme=None,
    sep="; ",
    directory="./",
):

    co_occ_matrix = occurrence_matrix(
        directory=directory,
        column=column,
        by=by,
        min_occ=min_occ,
        max_occ=max_occ,
        min_occ_by=min_occ_by,
        max_occ_by=max_occ_by,
        scheme=scheme,
        sep=sep,
    )

    matrix = co_occ_matrix.corr(method=method)

    return matrix
