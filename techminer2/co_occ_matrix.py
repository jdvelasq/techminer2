"""
Co-occurrence Matrix
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import co_occ_matrix
>>> co_occ_matrix(
...    column='author_keywords',
...    row='authors',
...    min_occ=3,
...    directory=directory,
... )
column             regtech 70:462  ...  data protection officer 03:008
row                                ...                                
Arner DW 7:220                  6  ...                               0
Buckley RP 6:217                5  ...                               0
Barberis JN 4:146               3  ...                               0
Zetzsche DA 4:092               4  ...                               0
Brennan R 3:008                 3  ...                               3
Ryan P 3:008                    3  ...                               3
<BLANKLINE>
[6 rows x 5 columns]


>>> co_occ_matrix(
...    column='author_keywords',
...    min_occ=4,
...    directory=directory,
... )
column                                    regtech 70:462  ...  suptech 04:003
row                                                       ...                
regtech 70:462                                        70  ...               4
fintech 42:406                                        42  ...               0
blockchain 18:109                                     17  ...               0
artificial intelligence 13:065                        10  ...               0
compliance 12:020                                     12  ...               0
regulatory technologies (regtech) 12:047               4  ...               0
financial technologies 09:032                          5  ...               0
financial regulation 08:091                            8  ...               0
machine learning 06:013                                6  ...               0
regulation 06:120                                      5  ...               0
financial inclusion 05:068                             5  ...               0
financial service 05:135                               5  ...               0
accountability 04:022                                  4  ...               0
anti-money laundering 04:030                           0  ...               0
bank 04:001                                            0  ...               0
big data 04:027                                        4  ...               0
crowdfunding 04:030                                    4  ...               0
cryptocurrencies 04:029                                0  ...               0
financial innovation 04:007                            4  ...               0
innovation 04:029                                      0  ...               0
insurtech 04:005                                       4  ...               0
suptech 04:003                                         4  ...               4
<BLANKLINE>
[22 rows x 22 columns]


"""
from .vantagepoint__co_occ_matrix_list import vantagepoint__co_occ_matrix_list


def co_occ_matrix(
    column,
    row=None,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    database="documents",
):
    """Creates a co-occurrence matrix."""

    if row is None:
        row = column

    matrix_list = vantagepoint__co_occ_matrix_list(
        column=column,
        row=row,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        directory=directory,
        database=database,
    )

    matrix = matrix_list.pivot(index="row", columns="column", values="OCC")
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
