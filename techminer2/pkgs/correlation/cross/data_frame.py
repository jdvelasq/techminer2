# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Cross-correlation Matrix
===============================================================================

>>> from techminer2.analyze.correlation_matrix import cross_correlation_matrix
>>> (
...     DataFrame()
...     #
...     .with_field("authors")
...     .with_cross_field('countries'),
...     .with_top_n_terms(10)
...     #
...     .having_term_occurrences_between(None, None)
...     .having_term_citations_between(None, None)
...     .having_terms_in(None)
...     #
...     .with_correlation_method("pearson")
...     #
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     #
...     .build()
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
# from ...cross_co_occurrence.matrix import co_occurrence_matrix
from ..internals.internal__compute_corr_matrix import internal__compute_corr_matrix


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

    corr_matrix = internal__compute_corr_matrix(method, data_matrix)

    return corr_matrix
