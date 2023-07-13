# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _auto_correlation_matrix:

Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.


>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> tm2.auto_correlation_matrix(
...     rows_and_columns='authors',
...     occ_range=(2, None),
...     root_dir=root_dir,
... ).round(3)
                    Arner DW 3:185  ...  Arman AA 2:000
Arner DW 3:185               1.000  ...             0.0
Buckley RP 3:185             1.000  ...             0.0
Barberis JN 2:161            0.787  ...             0.0
Butler T 2:041               0.000  ...             0.0
Hamdan A 2:018               0.000  ...             0.0
Turki M 2:018                0.000  ...             0.0
Lin W 2:017                  0.000  ...             0.0
Singh C 2:017                0.000  ...             0.0
Brennan R 2:014              0.000  ...             0.0
Crane M 2:014                0.000  ...             0.0
Ryan P 2:014                 0.000  ...             0.0
Sarea A 2:012                0.000  ...             0.0
Grassi L 2:002               0.000  ...             0.0
Lanfranchi D 2:002           0.000  ...             0.0
Arman AA 2:000               0.000  ...             1.0
<BLANKLINE>
[15 rows x 15 columns]


    

"""
from ..tfidf import tfidf
from .compute_corr_matrix import compute_corr_matrix

# from .list_cells_in_matrix import list_cells_in_matrix


def auto_correlation_matrix(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
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
    """Returns an auto-correlation."""

    data_matrix = tfidf(
        #
        # TF PARAMS:
        field=rows_and_columns,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    custom_items = [
        " ".join(col.split(" ")[:-1]) for col in data_matrix.columns.tolist()
    ]

    corr_matrix = compute_corr_matrix(method=method, data_matrix=data_matrix)

    return corr_matrix
