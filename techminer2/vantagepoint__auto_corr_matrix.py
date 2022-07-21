"""
Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__auto_corr_matrix
>>> vantagepoint__auto_corr_matrix(
...     column='authors',
...     top_n=10,
...     directory=directory,
... )
                   Arner DW 7:220  ...  Hamdan A 2:011
Arner DW 7:220           1.000000  ...       -0.030101
Buckley RP 6:217         0.994905  ...       -0.030133
Barberis JN 4:146        0.932362  ...       -0.026364
Zetzsche DA 4:092        0.948713  ...       -0.029984
Brennan R 3:008         -0.018995  ...       -0.024252
Ryan P 3:008            -0.018995  ...       -0.024252
Butler T 2:005          -0.026161  ...       -0.033401
Crane M 2:008           -0.019294  ...       -0.024634
Das SR 2:028            -0.018175  ...       -0.023205
Hamdan A 2:011          -0.030101  ...        1.000000
<BLANKLINE>
[10 rows x 10 columns]


"""
from .vantagepoint__co_occ_matrix import vantagepoint__co_occ_matrix


def vantagepoint__auto_corr_matrix(
    column,
    method="pearson",
    top_n=50,
    directory="./",
    database="documents",
):
    """Returns an auto-correlation."""

    coc_matrix = vantagepoint__co_occ_matrix(
        column=column,
        row=None,
        top_n=None,
        min_occ=None,
        max_occ=None,
        directory=directory,
        database=database,
    )

    coc_matrix = _select_top_n_from_columns(matrix=coc_matrix, top_n=top_n)

    coc_matrix.columns = coc_matrix.columns.to_list()

    matrix = coc_matrix.corr(method=method)

    return matrix


def _select_top_n_from_columns(matrix, top_n):

    terms = matrix.columns.to_list()
    sorted_terms = sorted(
        terms, key=lambda x: x.split()[-1].split(":")[0], reverse=True
    )
    sorted_terms = sorted_terms[:top_n]

    matrix = matrix[sorted_terms]

    return matrix
