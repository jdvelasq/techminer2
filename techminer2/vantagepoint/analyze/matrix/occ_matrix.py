"""
Occurrence Matrix
===============================================================================


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.occ_matrix(
...    criterion_for_columns='author_keywords',
...    criterion_for_rows='authors',
...    topic_min_occ=3,
...    directory=directory,
... )
column            regtech 28:329  ...  financial services 04:168
row                               ...                           
Arner DW 3:185                 2  ...                          1
Buckley RP 3:185               2  ...                          1
<BLANKLINE>
[2 rows x 4 columns]



"""
from .occ_matrix_list import occ_matrix_list


def occ_matrix(
    criterion_for_columns,
    criterion_for_rows=None,
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

    if criterion_for_rows is None:
        criterion_for_rows = criterion_for_columns

    matrix_list = occ_matrix_list(
        criterion_for_columns=criterion_for_columns,
        criterion_for_rows=criterion_for_rows,
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
