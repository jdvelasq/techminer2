"""
Occurrence Matrix
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint__occ_matrix
>>> vantagepoint__occ_matrix(
...    criterion_for_columns='author_keywords',
...    criterion_for_rows='authors',
...    min_occ_per_topic=3,
...    directory=directory,
... )
column             regtech 69:461  ...  semantic web 03:002
row                                ...                     
Arner DW 7:220                  6  ...                    0
Buckley RP 6:217                5  ...                    0
Barberis JN 4:146               3  ...                    0
Zetzsche DA 4:092               4  ...                    0
Brennan R 3:008                 3  ...                    1
Ryan P 3:008                    3  ...                    1
<BLANKLINE>
[6 rows x 16 columns]




"""
from .vantagepoint__occ_matrix_list import vantagepoint__occ_matrix_list


def vantagepoint__occ_matrix(
    criterion_for_columns,
    criterion_for_rows=None,
    topics_length=None,
    min_occ_per_topic=None,
    min_citations_per_topic=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Creates a co-occurrence matrix."""

    if criterion_for_rows is None:
        criterion_for_rows = criterion_for_columns

    matrix_list = vantagepoint__occ_matrix_list(
        criterion_for_columns=criterion_for_columns,
        criterion_for_rows=criterion_for_rows,
        topics_length=topics_length,
        min_occ_per_topic=min_occ_per_topic,
        min_citations_per_topic=min_citations_per_topic,
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
