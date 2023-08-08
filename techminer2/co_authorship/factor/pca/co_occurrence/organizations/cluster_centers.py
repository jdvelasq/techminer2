# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Cluster Centers
===============================================================================


>>> from techminer2.co_authorship.factor.pca.co_occurrence.organizations import cluster_centers
>>> cluster_centers(
...     #
...     # PARAMS:
...     association_index=None,
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # PCA PARAMS:
...     n_components=6,
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
             DIM_0         DIM_1  ...         DIM_4         DIM_5
CL_0  2.500000e-01  5.000000e-01  ... -1.796875e-01  1.250000e-01
CL_1 -8.957663e+15 -6.376544e+15  ... -2.434575e+14 -8.651303e+14
CL_2 -2.500000e-01  5.000000e-01  ... -2.656250e-01 -5.625000e-01
CL_3  0.000000e+00  0.000000e+00  ...  5.937500e-01  4.375000e-01
CL_4  1.000000e+00 -2.500000e-01  ...  3.046875e-01 -2.500000e-01
CL_5  1.000000e+00 -2.500000e-01  ... -5.000000e-01  1.250000e-01
<BLANKLINE>
[6 rows x 6 columns]

"""
from typing import Literal

from ......factor_analysis.co_occurrence.pca.factor_clusters import factor_clusters

UNIT_OF_ANALYSIS = "organizations"


def cluster_centers(
    #
    # PARAMS:
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
    """
    :meta private:
    """

    return factor_clusters(
        #
        # COOC PARAMS:
        rows_and_columns=UNIT_OF_ANALYSIS,
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
        # KMEANS PARAMS:
        kmeans_init=kmeans_init,
        kmeans_n_init=kmeans_n_init,
        kmeans_max_iter=kmeans_max_iter,
        kmeans_tol=kmeans_tol,
        kmeans_random_state=kmeans_random_state,
        kmeans_algorithm=kmeans_algorithm,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).centers_
