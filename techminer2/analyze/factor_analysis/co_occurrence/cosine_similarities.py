# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Cosine Similarities
===============================================================================

>>> from sklearn.decomposition import PCA
>>> from techminer2.factor_analysis.co_occurrence import cosine_similarities
>>> cosine_similarities(
...     #
...     # PARAMS:
...     field="author_keywords",
...     association_index=None,
...     #
...     # ITEM PARAMS:
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
                                                            cosine_similariries
rows                                                                           
FINTECH 31:5168                                      INNOVATION 07:0911 (0.322)
INNOVATION 07:0911            FINANCIAL_SERVICES 04:0667 (0.521); TECHNOLOGY...
FINANCIAL_SERVICES 04:0667    FINANCIAL_TECHNOLOGY 03:0461 (0.645); INNOVATI...
FINANCIAL_INCLUSION 03:0590   CASE_STUDY 02:0340 (0.923); BLOCKCHAIN 02:0305...
FINANCIAL_TECHNOLOGY 03:0461  BANKING 02:0291 (0.814); BUSINESS_MODELS 02:07...

    
"""
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import (
    cosine_similarity as sklearn_cosine_similarity,
)  # type: ignore

from .terms_by_dimension_frame import terms_by_dimension_frame


def cosine_similarities(
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

    embedding = terms_by_dimension_frame(
        #
        # FUNCTION PARAMS:
        field=field,
        association_index=association_index,
        #
        # TERM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # DECOMPOSITION:
        decomposition_estimator=decomposition_estimator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    similarity = sklearn_cosine_similarity(embedding)

    term_similarities = []
    for i in range(similarity.shape[0]):
        values_to_sort = []
        for j in range(similarity.shape[1]):
            if i != j and similarity[i, j] > 0:
                values_to_sort.append(
                    (
                        embedding.index[j],
                        similarity[i, j],
                    )
                )
        sorted_values = sorted(values_to_sort, key=lambda x: x[1], reverse=True)
        sorted_values = [f"{x[0]} ({x[1]:>0.3f})" for x in sorted_values]
        sorted_values = "; ".join(sorted_values)
        term_similarities.append(sorted_values)

    term_similarities = pd.DataFrame(
        {"cosine_similariries": term_similarities},
        index=embedding.index,
    )

    return term_similarities
