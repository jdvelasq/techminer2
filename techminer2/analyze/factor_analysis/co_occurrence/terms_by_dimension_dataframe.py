# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Dimension Frame
===============================================================================

>>> from sklearn.decomposition import PCA
>>> from techminer2.analyze.factor_analysis.co_occurrence import terms_by_dimension_frame
>>> (
...     TermsByDimensionDataFrame()
...     .set_analysis_params(
...         association_index=None,
...         decomposition_estimator = PCA(
...             n_components=5,
...             whiten=False,
...             svd_solver="auto",
...             tol=0.0,
...             iterated_power="auto",
...             n_oversamples=10,
...             power_iteration_normalizer="auto",
...             random_state=0, 
...         ),
...     #
...     ).set_item_params(
...         field="author_keywords",
...         top_n=20,
...         occ_range=(None, None),
...         gc_range=(None, None),
...         custom_terms=None,
...     #
...     ).set_database_params(
...         root_dir="example/", 
...         database="main",
...         year_filter=(None, None),
...         cited_by_filter=(None, None),
...     #
...     ).build()
... ).head()
dim                                   0         1         2         3         4
rows                                                                           
FINTECH 31:5168               28.659528 -0.524730 -0.513789 -0.042977  0.238539
INNOVATION 07:0911             2.377465  5.757771  2.713115 -1.188306 -0.116040
FINANCIAL_SERVICES 04:0667    -0.090716  2.761290  0.416833  2.583089 -0.502611
FINANCIAL_INCLUSION 03:0590   -0.631683 -0.611095 -1.728676 -0.825425 -0.947171
FINANCIAL_TECHNOLOGY 03:0461  -1.487691  0.959672 -0.271058  0.837526 -0.690393

    
"""
import pandas as pd  # type: ignore

from ...co_occurrence_matrix import co_occurrence_matrix
from ...co_occurrence_matrix.internals.normalize_co_occurrence_matrix import (
    normalize_co_occurrence_matrix,
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

    matrix_values = normalize_co_occurrence_matrix(matrix_values, association_index)
    decomposition_estimator.fit(matrix_values)
    trans_matrix_values = decomposition_estimator.transform(matrix_values)

    embedding = pd.DataFrame(
        trans_matrix_values,
        index=matrix_values.index,
        columns=list(range(decomposition_estimator.n_components)),
    )
    embedding.columns.name = "dim"

    return embedding
