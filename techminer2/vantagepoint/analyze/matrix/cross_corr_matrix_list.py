"""
Cross-correlation Matrix List
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2 import vantagepoint
>>> directory = "data/regtech/"

>>> vantagepoint.analyze.matrix.cross_corr_matrix_list(
...     criterion_for_columns='authors',
...     criterion_for_rows="author_keywords",
...     topics_length=10,
...     directory=directory,
... )
                  row             column      CORR
0      Arner DW 3:185     Arner DW 3:185  1.000000
1   Barberis JN 2:161  Barberis JN 2:161  1.000000
2     Brennan R 2:014    Brennan R 2:014  1.000000
3     Brennan R 2:014      Crane M 2:014  1.000000
4    Buckley RP 3:185   Buckley RP 3:185  1.000000
..                ...                ...       ...
71        Lin W 2:017      Turki M 2:018 -0.047088
72      Singh C 2:017     Hamdan A 2:018 -0.047088
73      Singh C 2:017      Turki M 2:018 -0.047088
74      Turki M 2:018        Lin W 2:017 -0.047088
75      Turki M 2:018      Singh C 2:017 -0.047088
<BLANKLINE>
[76 rows x 3 columns]


"""
from .auto_corr_matrix_list import _transform_to_matrix_list
from .cross_corr_matrix import cross_corr_matrix


def cross_corr_matrix_list(
    criterion_for_columns=None,
    criterion_for_rows=None,
    method="pearson",
    topics_length=None,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Returns an auto-correlation matrix list."""

    matrix = cross_corr_matrix(
        criterion_for_columns=criterion_for_columns,
        criterion_for_rows=criterion_for_rows,
        method=method,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    matrix = _transform_to_matrix_list(criterion_for_columns, matrix)

    return matrix
