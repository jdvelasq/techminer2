"""
Cross-correlation Matrix List
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2 import vantagepoint__cross_corr_matrix_list
>>> directory = "data/regtech/"

>>> vantagepoint__cross_corr_matrix_list(
...     column='authors',
...     by="author_keywords",
...     top_n=10,
...     directory=directory,
... )
                  row             column      CORR
0      Arner DW 7:220     Arner DW 7:220  1.000000
1   Barberis JN 4:146  Barberis JN 4:146  1.000000
2     Brennan R 3:008    Brennan R 3:008  1.000000
3     Brennan R 3:008       Ryan P 3:008  1.000000
4    Buckley RP 6:217   Buckley RP 6:217  1.000000
..                ...                ...       ...
95      Turki M 2:011   Buckley RP 6:217 -0.249260
96       Das SR 2:028     Hamdan A 2:011 -0.258227
97       Das SR 2:028      Turki M 2:011 -0.258227
98     Hamdan A 2:011       Das SR 2:028 -0.258227
99      Turki M 2:011       Das SR 2:028 -0.258227
<BLANKLINE>
[100 rows x 3 columns]

"""
from .vantagepoint__cross_corr_matrix import vantagepoint__cross_corr_matrix


def vantagepoint__cross_corr_matrix_list(
    column,
    by,
    method="pearson",
    top_n=50,
    directory="./",
    database="documents",
):
    """Returns an auto-correlation matrix list."""

    matrix = vantagepoint__cross_corr_matrix(
        column=column,
        by=by,
        method=method,
        top_n=top_n,
        directory=directory,
        database=database,
    )

    matrix = matrix.melt(value_name="CORR", var_name="column", ignore_index=False)
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={"index": "row"})
    matrix = matrix.sort_values(
        by=["CORR", "row", "column"], ascending=[False, True, True]
    )
    matrix = matrix.reset_index(drop=True)

    return matrix