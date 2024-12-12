# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Cross-correlation Matrix
===============================================================================

>>> from techminer2.correlation_matrix import cross_correlation_matrix
>>> cross_correlation_matrix(
...     #
...     # FUNCTION PARAMS:
...     rows_and_columns='authors', 
...     cross_with='countries',
...     method="pearson",
...     #
...     # ITEM PARAMS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).round(3)
                      Jagtiani J. 3:0317  ...  Zavolokina L. 2:0181
Jagtiani J. 3:0317                 1.000  ...                   0.0
Gomber P. 2:1065                   0.200  ...                   0.0
Hornuf L. 2:0358                   0.000  ...                   0.0
Gai K. 2:0323                      0.632  ...                   0.0
Qiu M. 2:0323                      0.632  ...                   0.0
Sun X./3 2:0323                    0.632  ...                   0.0
Lemieux C. 2:0253                  1.000  ...                   0.0
Dolata M. 2:0181                   0.000  ...                   1.0
Schwabe G. 2:0181                  0.000  ...                   1.0
Zavolokina L. 2:0181               0.000  ...                   1.0
<BLANKLINE>
[10 rows x 10 columns]

    

"""
from ..analyze.co_occurrence_matrix.co_occurrence_matrix import co_occurrence_matrix
from ._compute_corr_matrix import compute_corr_matrix


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
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""
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
        col_custom_terms=custom_terms,
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
