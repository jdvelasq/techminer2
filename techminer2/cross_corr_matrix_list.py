"""
Cross-correlation Matrix List
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2 import *
>>> directory = "data/"

>>> cross_corr_matrix_list(
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
95      Sarea A 2:006     Arner DW 7:220 -0.283651
96   Buckley RP 6:217      Sarea A 2:006 -0.310634
97      Sarea A 2:006   Buckley RP 6:217 -0.310634
98      Sarea A 2:006  Zetzsche DA 4:092 -0.311531
99  Zetzsche DA 4:092      Sarea A 2:006 -0.311531
<BLANKLINE>
[100 rows x 3 columns]

"""
from .cross_corr_matrix import cross_corr_matrix


def cross_corr_matrix_list(
    column,
    by,
    method="pearson",
    top_n=50,
    directory="./",
    database="documents",
):
    """Returns an auto-correlation matrix list."""

    matrix = cross_corr_matrix(
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
