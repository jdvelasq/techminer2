"""
Co-occurrence Matrix
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=4,
...    directory=directory,
... )
column                          regtech 28:329  ...  financial services 04:168
row                                             ...                           
regtech 28:329                              28  ...                          3
fintech 12:249                              12  ...                          2
compliance 07:030                            7  ...                          0
regulatory technology 07:037                 2  ...                          0
regulation 05:164                            4  ...                          1
artificial intelligence 04:023               2  ...                          0
financial regulation 04:035                  2  ...                          2
financial services 04:168                    3  ...                          4
<BLANKLINE>
[8 rows x 8 columns]


"""
from ....vantagepoint__co_occ_matrix_list import vantagepoint__co_occ_matrix_list


def co_occ_matrix(
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
