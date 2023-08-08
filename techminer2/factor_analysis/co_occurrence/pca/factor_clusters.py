# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _factor_analysis.co_occurrences.pca.factor_clusters:

Factor Clusters
===============================================================================

>>> from techminer2.factor_analysis.co_occurrences.pca import factor_clusters
>>> clusters = factor_clusters(
...     #
...     # COOC PARAMS:
...     rows_and_columns='author_keywords',
...     association_index=None,
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # PCA PARAMS:
...     n_components=5,
...     whiten=False,
...     svd_solver="auto",
...     tol=0.0,
...     iterated_power="auto",
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0,
...     #
...     # KMEANS PARAMS:
...     kmeans_init="k-means++",
...     kmeans_n_init=10,
...     kmeans_max_iter=300,
...     kmeans_tol=0.0001,
...     kmeans_random_state=0,
...     kmeans_algorithm="auto",
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> clusters.centers_.round(3)
       DIM_0  DIM_1  DIM_2  DIM_3  DIM_4
CL_0  -0.076  0.330  0.060  0.251  0.206
CL_1  -2.312 -0.364 -0.182  0.172 -0.456
CL_2   7.233  2.579  1.000  4.195  2.943
CL_3  16.498  3.313  5.874  1.000  2.437
CL_4  -7.692  0.422 -4.046 -1.167  1.000


>>> print(clusters.communities_.to_markdown())
|    | CL_0                         | CL_1                           | CL_2               | CL_3                   | CL_4                   |
|---:|:-----------------------------|:-------------------------------|:-------------------|:-----------------------|:-----------------------|
|  0 | REGTECH 28:329               | ANTI_MONEY_LAUNDERING 05:034   | CHARITYTECH 02:017 | SMART_CONTRACTS 02:022 | DATA_PROTECTION 02:027 |
|  1 | FINTECH 12:249               | ARTIFICIAL_INTELLIGENCE 04:023 | ENGLISH_LAW 02:017 |                        |                        |
|  2 | REGULATORY_TECHNOLOGY 07:037 | INNOVATION 03:012              |                    |                        |                        |
|  3 | COMPLIANCE 07:030            | BLOCKCHAIN 03:005              |                    |                        |                        |
|  4 | REGULATION 05:164            | SEMANTIC_TECHNOLOGIES 02:041   |                    |                        |                        |
|  5 | FINANCIAL_SERVICES 04:168    | ACCOUNTABILITY 02:014          |                    |                        |                        |
|  6 | FINANCIAL_REGULATION 04:035  | DATA_PROTECTION_OFFICER 02:014 |                    |                        |                        |
|  7 | RISK_MANAGEMENT 03:014       |                                |                    |                        |                        |
|  8 | SUPTECH 03:004               |                                |                    |                        |                        |



"""
from typing import Literal

from ...factor_clustering import factor_clustering
from .factor_matrix import factor_matrix


def factor_clusters(
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
    # PCA PARAMS:
    n_components=None,
    whiten=False,
    svd_solver="auto",
    tol=0.0,
    iterated_power="auto",
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
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
    """Creates a factor matrix from the co-occurrence matrix.

    :meta private:
    """

    matrix = factor_matrix(
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
        # PCA PARAMS:
        n_components=n_components,
        whiten=whiten,
        svd_solver=svd_solver,
        tol=tol,
        iterated_power=iterated_power,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return factor_clustering(
        factor_matrix=matrix,
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
