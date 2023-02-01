"""
Cross-correlation Matrix List
===============================================================================

Returns an auto-correlation matrix.

>>> from techminer2 import vantagepoint__cross_corr_matrix_list
>>> directory = "data/regtech/"

>>> vantagepoint__cross_corr_matrix_list(
...     criterion_for_columns='authors',
...     criterion_for_rows="author_keywords",
...     topics_length=10,
...     directory=directory,
... )
                  row             column      CORR
0      Arner DW 7:220     Arner DW 7:220  1.000000
1   Barberis JN 4:146  Barberis JN 4:146  1.000000
2     Brennan R 3:008    Brennan R 3:008  1.000000
3     Brennan R 3:008       Ryan P 3:008  1.000000
4    Buckley RP 6:217   Buckley RP 6:217  1.000000
..                ...                ...       ...
71      Turki M 2:011  Barberis JN 4:146 -0.113228
72     Arner DW 7:220     Hamdan A 2:011 -0.292322
73     Arner DW 7:220      Turki M 2:011 -0.292322
74     Hamdan A 2:011     Arner DW 7:220 -0.292322
75      Turki M 2:011     Arner DW 7:220 -0.292322
<BLANKLINE>
[76 rows x 3 columns]

"""
from .vantagepoint.analyze.matrix.auto_corr_matrix_list import _transform_to_matrix_list
from .vantagepoint__cross_corr_matrix import vantagepoint__cross_corr_matrix


def vantagepoint__cross_corr_matrix_list(
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

    matrix = vantagepoint__cross_corr_matrix(
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
