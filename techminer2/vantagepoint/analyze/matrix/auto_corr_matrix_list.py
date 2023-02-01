"""
Auto-correlation Matrix List
===============================================================================

Returns an auto-correlation matrix.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.auto_corr_matrix_list(
...     criterion='authors',
...     topics_length=10,
...     directory=directory,
... )
                 row            column      CORR
0     Arner DW 3:185    Arner DW 3:185  1.000000
1     Arner DW 3:185  Buckley RP 3:185  1.000000
2    Brennan R 2:014   Brennan R 2:014  1.000000
3   Buckley RP 3:185    Arner DW 3:185  1.000000
4   Buckley RP 3:185  Buckley RP 3:185  1.000000
5   Butler T/1 2:041  Butler T/1 2:041  1.000000
6      Crane M 2:014     Crane M 2:014  1.000000
7     Grassi L 2:002    Grassi L 2:002  1.000000
8     Hamdan A 2:018    Hamdan A 2:018  1.000000
9        Lin W 2:017       Lin W 2:017  1.000000
10       Lin W 2:017     Singh C 2:017  1.000000
11     Sarea A 2:012     Sarea A 2:012  1.000000
12     Singh C 2:017       Lin W 2:017  1.000000
13     Singh C 2:017     Singh C 2:017  1.000000
14   Brennan R 2:014     Crane M 2:014  1.000000
15     Crane M 2:014   Brennan R 2:014  1.000000
16    Hamdan A 2:018     Sarea A 2:012  0.416667
17     Sarea A 2:012    Hamdan A 2:018  0.416667


"""
from .auto_corr_matrix import auto_corr_matrix


def auto_corr_matrix_list(
    criterion,
    method="pearson",
    topics_length=50,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Returns an auto-correlation matrix list."""

    matrix = auto_corr_matrix(
        criterion=criterion,
        method=method,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=custom_topics,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix = _transform_to_matrix_list(criterion, matrix)

    return matrix


def _transform_to_matrix_list(criterion, matrix):
    matrix = matrix.melt(value_name="CORR", var_name="column", ignore_index=False)
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={"index": "row"})
    matrix = matrix.sort_values(
        by=["CORR", "row", "column"], ascending=[False, True, True]
    )
    matrix = matrix[matrix.CORR != 0.0]
    matrix = matrix.reset_index(drop=True)
    return matrix
