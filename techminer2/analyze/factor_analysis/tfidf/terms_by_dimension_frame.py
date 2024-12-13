# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Dimension Frane
===============================================================================

>>> from sklearn.decomposition import PCA
>>> from techminer2.factor_analysis.tfidf import terms_by_dimension_frame
>>> terms_by_dimension_frame(
...     #
...     # PARAMS:
...     field="author_keywords",
...     #
...     # TF PARAMS:
...     is_binary=True,
...     cooc_within=1,
...     #
...     # TF-IDF PARAMS:
...     norm=None,
...     use_idf=False,
...     smooth_idf=False,
...     sublinear_tf=False,
...     #
...     # TERM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DESOMPOSITION PARAMS:
...     decomposition_estimator = PCA(
...         n_components=5,
...         whiten=False,
...         svd_solver="auto",
...         tol=0.0,
...         iterated_power="auto",
...         n_oversamples=10,
...         power_iteration_normalizer="auto",
...         random_state=0, 
...     ),
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
dim                                  0         1         2         3         4
author_keywords                                                               
FINTECH 31:5168               4.959197 -0.131331 -0.127054 -0.021353  0.127476
INNOVATION 07:0911            0.316050  1.870215  1.111843 -0.552452 -0.021560
FINANCIAL_SERVICES 04:0667   -0.082353  0.895051  0.128205  1.239682 -0.242869
FINANCIAL_INCLUSION 03:0590  -0.039071 -0.170843 -0.618483 -0.383141 -0.474122
FINANCIAL_TECHNOLOGY 03:0461 -0.228786  0.327462 -0.051164  0.419388 -0.291788

    
"""
import pandas as pd  # type: ignore

from ....metrics.tfidf_frame import tfidf_frame


def terms_by_dimension_frame(
    #
    # PARAMS:
    field,
    #
    # TF PARAMS:
    is_binary: bool = True,
    cooc_within: int = 1,
    #
    # TERM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # TF-IDF parameters:
    norm=None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
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

    matrix_values = tfidf_frame(
        #
        # TF PARAMS:
        field=field,
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # TF-IDF parameters:
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).T

    decomposition_estimator.fit(matrix_values)
    trans_matrix_values = decomposition_estimator.transform(matrix_values)

    embedding = pd.DataFrame(
        trans_matrix_values,
        index=matrix_values.index,
        columns=list(range(decomposition_estimator.n_components)),
    )
    embedding.columns.name = "dim"

    return embedding
