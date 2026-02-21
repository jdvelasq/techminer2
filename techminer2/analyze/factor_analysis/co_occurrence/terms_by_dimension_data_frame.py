"""
Terms by Dimension Frame
===============================================================================

## >>> from sklearn.decomposition import PCA
## >>> pca = PCA(
## ...     n_components=5,
## ...     whiten=False,
## ...     svd_solver="auto",
## ...     tol=0.0,
## ...     iterated_power="auto",
## ...     n_oversamples=10,
## ...     power_iteration_normalizer="auto",
## ...     random_state=0,
## ... )
## >>> from techminer2.packages.factor_analysis.co_occurrence import terms_by_dimension_frame
## >>> (
## ...     TermsByDimensionDataFrame()
## ...     #
## ...     # FIELD:
## ...     .with_field("descriptors")
## ...     .having_terms_in_top(50)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(None, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # DECOMPOSITION:
## ...     .using_decomposition_estimator(pca)
## ...     #
## ...     # ASSOCIATION INDEX:
## ...     .using_association_index(None)
## ...     #
## ...     # DATABASE:
## ...     .where_root_directory("examples/tests/")
## ...     .where_database("main")
## ...     .where_record_years_range(None, None)
## ...     .where_record_citations_range(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .run()
## ... ).head()



"""

import pandas as pd  # type: ignore

from techminer2.analyze.metrics.co_occurrence_matrix._internals.normalize_matrix import (
    internal__normalize_matrix,
)


def terms_by_dimension_frame(
    #
    # PARAMS:
    field,
    association_index=None,
    #
    # TERM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DECOMPOSITION:
    decomposition_estimator=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    matrix_values = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=field,
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

    matrix_values = internal__normalize_matrix(matrix_values, association_index)
    decomposition_estimator.fit(matrix_values)
    trans_matrix_values = decomposition_estimator.transform(matrix_values)

    embedding = pd.DataFrame(
        trans_matrix_values,
        index=matrix_values.index,
        columns=list(range(decomposition_estimator.n_components)),
    )
    embedding.columns.name = "dim"

    return embedding
