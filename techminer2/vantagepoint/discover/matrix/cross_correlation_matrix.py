# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _cross_correlation_matrix:

Cross-correlation Matrix
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> tm2.cross_correlation_matrix(
...     rows_and_columns='authors', 
...     cross_with='countries',
...     top_n=10,
...     root_dir=root_dir,
... ).round(3)
                   Arner DW 3:185  ...  Crane M 2:014
Arner DW 3:185              1.000  ...          0.000
Buckley RP 3:185            1.000  ...          0.000
Barberis JN 2:161           0.907  ...          0.000
Butler T 2:041              0.000  ...          0.886
Hamdan A 2:018              0.000  ...          0.000
Turki M 2:018               0.000  ...          0.000
Lin W 2:017                -0.235  ...          0.000
Singh C 2:017              -0.235  ...          0.000
Brennan R 2:014             0.000  ...          1.000
Crane M 2:014               0.000  ...          1.000
<BLANKLINE>
[10 rows x 10 columns]

"""
from .co_occurrence_matrix import co_occurrence_matrix
from .compute_corr_matrix import compute_corr_matrix


def cross_correlation_matrix(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
    cross_with,
    method="pearson",
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Compute the cross-correlation matrix."""
    #
    # Main:
    #
    data_matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=rows_and_columns,
        rows=cross_with,
        #
        # COLUMN PARAMS:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    corr_matrix = compute_corr_matrix(method, data_matrix)

    return corr_matrix
