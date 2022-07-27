"""
Co-occurrence Matrix
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__co_occ_matrix
>>> vantagepoint__co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=4,
...    directory=directory,
... )
column                          regtech 69:461  ...  suptech 04:003
row                                             ...                
regtech 69:461                              69  ...               4
fintech 42:406                              42  ...               3
blockchain 18:109                           17  ...               1
artificial intelligence 13:065              10  ...               0
compliance 12:020                           12  ...               0
regulatory technology 12:047                 4  ...               0
financial technology 09:032                  5  ...               0
financial regulation 08:091                  8  ...               0
machine learning 06:013                      6  ...               1
regulation 06:120                            5  ...               0
financial inclusion 05:068                   5  ...               0
financial services 05:135                    5  ...               0
accountability 04:022                        4  ...               0
anti-money laundering 04:030                 2  ...               0
banking 04:001                               3  ...               0
big data 04:027                              4  ...               0
crowdfunding 04:030                          4  ...               0
cryptocurrency 04:029                        3  ...               0
financial innovation 04:007                  4  ...               0
innovation 04:029                            3  ...               0
insurtech 04:005                             4  ...               0
suptech 04:003                               4  ...               4
<BLANKLINE>
[22 rows x 22 columns]



"""
from .vantagepoint__co_occ_matrix_list import vantagepoint__co_occ_matrix_list


def vantagepoint__co_occ_matrix(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Creates a co-occurrence matrix."""

    matrix_list = vantagepoint__co_occ_matrix_list(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
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
