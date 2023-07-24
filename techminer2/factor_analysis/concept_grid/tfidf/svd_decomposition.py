# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
SVD Factor Decomposition
===============================================================================



>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"
>>> factors = vantagepoint.explore.concept_grid.tfidf.svd_decomposition(
...     root_dir="data/regtech/",
...     field='author_keywords',
...     top_n=20,
...     n_components=5,
... )
>>> factors.centers_.round(3)
      DIM_0  DIM_1  DIM_2  DIM_3  DIM_4
CL_0  0.672 -0.296  0.420 -0.298 -0.335
CL_1  0.935  0.720  0.333  0.439 -0.242
CL_2  0.596  0.369 -0.218 -0.495  0.927
CL_3  0.804 -1.333 -0.021  0.984  0.473
CL_4  1.000 -1.313  0.692 -2.625 -1.653


>>> print(factors.communities_.to_markdown())
|    | CL_0                           | CL_1                         | CL_2                        | CL_3                           | CL_4               |
|---:|:-------------------------------|:-----------------------------|:----------------------------|:-------------------------------|:-------------------|
|  0 | REGTECH 28:329                 | FINTECH 12:249               | FINANCIAL_SERVICES 04:168   | COMPLIANCE 07:030              | CHARITYTECH 02:017 |
|  1 | REGULATORY_TECHNOLOGY 07:037   | REGULATION 05:164            | FINANCIAL_REGULATION 04:035 | ACCOUNTABILITY 02:014          | ENGLISH_LAW 02:017 |
|  2 | ANTI_MONEY_LAUNDERING 05:034   | RISK_MANAGEMENT 03:014       | INNOVATION 03:012           | DATA_PROTECTION_OFFICER 02:014 |                    |
|  3 | ARTIFICIAL_INTELLIGENCE 04:023 | SUPTECH 03:004               | DATA_PROTECTION 02:027      |                                |                    |
|  4 | BLOCKCHAIN 03:005              | SEMANTIC_TECHNOLOGIES 02:041 |                             |                                |                    |
|  5 | SMART_CONTRACTS 02:022         |                              |                             |                                |                    |


"""
from typing import Literal

from ...factor_clustering import factor_clustering
from ...factors.tfidf.svd_decomposition import svd_decomposition as factor_svd_decomposition


def svd_decomposition(
    #
    # TF PARAMS:
    field: str,
    is_binary: bool = False,
    cooc_within: int = 1,
    #
    # TF-IDF parameters:
    norm: Literal["l1", "l2", None] = None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # SVD PARAMS:
    n_components=None,
    algorithm="randomized",
    n_iter=5,
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
    tol=0.0,
    #
    # KMEANS PARAMS:
    kmeans_init="k-means++",
    kmeans_n_init=10,
    kmeans_max_iter=300,
    kmeans_tol=0.0001,
    kmeans_random_state=0,
    kmeans_algorithm: Literal["lloyd", "elkan", "auto", "full"] = "auto",
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    factor_matrix = factor_svd_decomposition(
        #
        # TF PARAMS:
        field=field,
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # TF-IDF parameters:
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # SVD PARAMS:
        n_components=n_components,
        algorithm=algorithm,
        n_iter=n_iter,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        tol=tol,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return factor_clustering(
        factor_matrix=factor_matrix,
        #
        # KMEANS PARAMS:
        n_clusters=n_components,
        init=kmeans_init,
        n_init=kmeans_n_init,
        max_iter=kmeans_max_iter,
        tol=kmeans_tol,
        random_state=kmeans_random_state,
        algorithm=kmeans_algorithm,
    )
