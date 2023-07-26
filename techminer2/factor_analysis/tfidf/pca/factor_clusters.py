# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Factor Clusters
===============================================================================


>>> from techminer2.factor_analysis.tfidf.pca import factor_clusters
>>> clusters = factor_clusters(
...     #
...     # TF PARAMS:
...     field='author_keywords',
...     is_binary=False,
...     cooc_within=1,
...     #
...     # TF-IDF parameters:
...     norm=None,
...     use_idf=False,
...     smooth_idf=False,
...     sublinear_tf=False,
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
CL_0 -0.181  0.056  0.143  0.584 -0.261
CL_1 -0.986  0.496 -1.330 -0.246  1.000
CL_2  2.190  1.605  1.000  2.970  2.335
CL_3 -1.614 -0.802  1.000 -1.861 -1.535
CL_4  7.818  3.838  6.033  1.000  3.224


>>> print(clusters.communities_.to_markdown())
|    | CL_0                           | CL_1                        | CL_2               | CL_3                           | CL_4                   |
|---:|:-------------------------------|:----------------------------|:-------------------|:-------------------------------|:-----------------------|
|  0 | REGTECH 28:329                 | FINANCIAL_SERVICES 04:168   | CHARITYTECH 02:017 | ANTI_MONEY_LAUNDERING 05:034   | SMART_CONTRACTS 02:022 |
|  1 | FINTECH 12:249                 | FINANCIAL_REGULATION 04:035 | ENGLISH_LAW 02:017 | ARTIFICIAL_INTELLIGENCE 04:023 |                        |
|  2 | REGULATORY_TECHNOLOGY 07:037   | INNOVATION 03:012           |                    |                                |                        |
|  3 | COMPLIANCE 07:030              | DATA_PROTECTION 02:027      |                    |                                |                        |
|  4 | REGULATION 05:164              |                             |                    |                                |                        |
|  5 | RISK_MANAGEMENT 03:014         |                             |                    |                                |                        |
|  6 | BLOCKCHAIN 03:005              |                             |                    |                                |                        |
|  7 | SUPTECH 03:004                 |                             |                    |                                |                        |
|  8 | SEMANTIC_TECHNOLOGIES 02:041   |                             |                    |                                |                        |
|  9 | ACCOUNTABILITY 02:014          |                             |                    |                                |                        |
| 10 | DATA_PROTECTION_OFFICER 02:014 |                             |                    |                                |                        |

    

"""
from typing import Literal

from ...factor_clustering import factor_clustering
from .factor_matrix import factor_matrix


def factor_clusters(
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
    """Creates a factor matrix from the co-occurrence matrix."""

    matrix = factor_matrix(
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
