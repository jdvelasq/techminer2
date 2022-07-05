"""
Auto-correlation Matrix List
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2 import *
>>> directory = "data/"

>>> auto_corr_matrix_list(
...     column='authors',
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
95     Hamdan A 2:011     Arner DW 7:220 -0.030101
96   Buckley RP 6:217     Hamdan A 2:011 -0.030133
97     Hamdan A 2:011   Buckley RP 6:217 -0.030133
98     Butler T 2:005     Hamdan A 2:011 -0.033401
99     Hamdan A 2:011     Butler T 2:005 -0.033401
<BLANKLINE>
[100 rows x 3 columns]


"""
from .auto_corr_matrix import auto_corr_matrix


def auto_corr_matrix_list(
    column,
    method="pearson",
    top_n=50,
    directory="./",
    database="documents",
):
    """Returns an auto-correlation matrix list."""

    matrix = auto_corr_matrix(
        column=column,
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
