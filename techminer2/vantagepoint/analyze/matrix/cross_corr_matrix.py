"""
Cross-correlation Matrix
===============================================================================



>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> vantagepoint.analyze.matrix.cross_corr_matrix(
...     criterion_for_columns = 'authors', 
...     criterion_for_rows='countries',
...     topics_length=10,
...     directory=directory,
... )
                   Arner DW 3:185  ...  Turki M 2:018
Arner DW 3:185           1.000000  ...            0.0
Buckley RP 3:185         1.000000  ...            0.0
Barberis JN 2:161        0.922664  ...            0.0
Brennan R 2:014          0.000000  ...            0.0
Butler T/1 2:041         0.000000  ...            0.0
Crane M 2:014            0.000000  ...            0.0
Hamdan A 2:018           0.000000  ...            1.0
Lin W 2:017             -0.365858  ...            0.0
Singh C 2:017           -0.365858  ...            0.0
Turki M 2:018            0.000000  ...            1.0
<BLANKLINE>
[10 rows x 10 columns]


"""
from .auto_corr_matrix import _compute_corr_matrix
from .occ_matrix import occ_matrix


def cross_corr_matrix(
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
    """Compute the cross-correlation matrix."""

    data_matrix = occ_matrix(
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

    corr_matrix = _compute_corr_matrix(method, data_matrix)

    return corr_matrix
