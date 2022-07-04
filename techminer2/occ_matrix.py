"""
OCC Matrix
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"

>>> occ_matrix(
...    column='author_keywords', 
...    by='authors',
...    min_occ=3,
...    directory=directory,
... )
author_keywords    regtech 70:462  ...  data protection officer 03:008
authors                            ...                                
Arner DW 7:220                  6  ...                               0
Buckley RP 6:217                5  ...                               0
Barberis JN 4:146               3  ...                               0
Zetzsche DA 4:092               4  ...                               0
Brennan R 3:008                 3  ...                               3
Ryan P 3:008                    3  ...                               3
<BLANKLINE>
[6 rows x 5 columns]

"""
from .occ_flood_matrix import occ_flood_matrix


def occ_matrix(
    column,
    by,
    min_occ=None,
    max_occ=None,
    directory="./",
):
    flood_matrix = occ_flood_matrix(
        column=column,
        by=by,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
    )

    matrix = flood_matrix.pivot(index=by, columns=column, values="OCC")
    matrix = matrix.fillna(0)
    matrix = matrix.astype(int)

    columns = sorted(
        matrix.columns.tolist(), key=lambda x: x.split()[-1].split(":")[0], reverse=True
    )
    indexes = sorted(
        matrix.index.tolist(), key=lambda x: x.split()[-1].split(":")[0], reverse=True
    )
    matrix = matrix.loc[indexes, columns]

    return matrix
