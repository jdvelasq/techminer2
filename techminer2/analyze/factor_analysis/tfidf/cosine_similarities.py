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

## >>> from sklearn.decomposition import PCA
## >>> from techminer2.analyze.factor_analysis.tfidf import cosine_similarities
## >>> (
## ...     CosineSimilarities()
## ...     .set_analysis_params(
## ...         decomposition_estimator = PCA(
## ...             n_components=5,
## ...             whiten=False,
## ...             svd_solver="auto",
## ...             tol=0.0,
## ...             iterated_power="auto",
## ...             n_oversamples=10,
## ...             power_iteration_normalizer="auto",
## ...             random_state=0, 
## ...         ),
## ...     #
## ...     ).set_tf_params(
## ...         is_binary=True,
## ...         cooc_within=1,
## ...     #
## ...     ).set_tfidf_params(
## ...         norm=None,
## ...         use_idf=False,
## ...         smooth_idf=False,
## ...         sublinear_tf=False,
## ...     #
## ...     ).set_item_params(
## ...         field="author_keywords",
## ...         top_n=20,
## ...         occ_range=(None, None),
## ...         gc_range=(None, None),
## ...         custom_terms=None,
## ...     #
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... ).head()
                                                            cosine_similariries
author_keywords                                                                
FINTECH 31:5168                                      INNOVATION 07:0911 (0.106)
INNOVATION 07:0911            TECHNOLOGY 02:0310 (0.771); BANKING 02:0291 (0...
FINANCIAL_SERVICES 04:0667    FINANCIAL_TECHNOLOGY 03:0461 (0.885); BUSINESS...
FINANCIAL_INCLUSION 03:0590   CASE_STUDY 02:0340 (0.971); BLOCKCHAIN 02:0305...
FINANCIAL_TECHNOLOGY 03:0461  FINANCIAL_SERVICES 04:0667 (0.885); BUSINESS_M...
    
"""
import pandas as pd  # type: ignore
from sklearn.metrics.pairwise import (
    cosine_similarity as sklearn_cosine_similarity,
)  # type: ignore

from .terms_by_dimension_dataframe import terms_by_dimension_frame


def cosine_similarities(
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

    embedding = terms_by_dimension_frame(
        #
        # FUNCTION PARAMS:
        field=field,
        #
        # TF PARAMS:
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # TERM PARAMS:
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
