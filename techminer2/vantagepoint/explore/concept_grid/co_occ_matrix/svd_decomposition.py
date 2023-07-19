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
>>> factors = vantagepoint.explore.concept_grid.co_occ_matrix.svd_decomposition(
...     root_dir="data/regtech/",
...     rows_and_columns='author_keywords',
...     top_n=20,
...     n_components=5,
... )
>>> factors.centers_.round(3)
      DIM_0  DIM_1  DIM_2  DIM_3  DIM_4
CL_0  1.000  0.166  0.097  0.112 -0.126
CL_1  0.946  0.350 -0.128 -0.347  0.673
CL_2  1.000 -0.860 -0.027  0.536  0.242
CL_3  0.620 -0.169  0.926 -0.380 -0.115
CL_4  1.000 -0.644  0.332 -1.116 -0.625


>>> print(factors.communities_.to_markdown())
|    | CL_0                         | CL_1                        | CL_2                           | CL_3                           | CL_4               |
|---:|:-----------------------------|:----------------------------|:-------------------------------|:-------------------------------|:-------------------|
|  0 | REGTECH 28:329               | FINANCIAL_SERVICES 04:168   | COMPLIANCE 07:030              | REGULATORY_TECHNOLOGY 07:037   | CHARITYTECH 02:017 |
|  1 | FINTECH 12:249               | FINANCIAL_REGULATION 04:035 | ACCOUNTABILITY 02:014          | ANTI_MONEY_LAUNDERING 05:034   | ENGLISH_LAW 02:017 |
|  2 | REGULATION 05:164            | INNOVATION 03:012           | DATA_PROTECTION_OFFICER 02:014 | ARTIFICIAL_INTELLIGENCE 04:023 |                    |
|  3 | RISK_MANAGEMENT 03:014       | DATA_PROTECTION 02:027      |                                |                                |                    |
|  4 | BLOCKCHAIN 03:005            |                             |                                |                                |                    |
|  5 | SUPTECH 03:004               |                             |                                |                                |                    |
|  6 | SEMANTIC_TECHNOLOGIES 02:041 |                             |                                |                                |                    |
|  7 | SMART_CONTRACTS 02:022       |                             |                                |                                |                    |
    

"""
from typing import Literal

from ....discover.factor_matrix.co_occ_matrix.svd_decomposition import (
    svd_decomposition as factor_svd_decomposition,
)
from ..factor_clustering import factor_clustering


def svd_decomposition(
    #
    # COOC PARAMS:
    rows_and_columns,
    association_index=None,
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
    """Creates a factor matrix from the co-occurrence matrix."""

    factor_matrix = factor_svd_decomposition(
        #
        # COOC PARAMS:
        rows_and_columns=rows_and_columns,
        association_index=association_index,
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
