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


>>> from techminer2.analyze.svd.cooc_matrix.kmeans import cluster_centers
>>> cluster_centers(
...     #
...     # PARAMS:
...     field="nlp_phrases",
...     association_index=None,
...     #
...     # ITEM PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # SVD PARAMS:
...     n_components=5,
...     algorithm_svd="randomized",
...     n_iter=5,
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0,
...     tol=0.0, 
...     #
...     # KMEANS PARAMS:
...     n_clusters=6,
...     init="k-means++",
...     n_init=10,
...     max_iter=300,
...     kmeans_tol=0.0001,
...     algorithm_kmeans="auto",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
            DIM_0      DIM_1     DIM_2     DIM_3     DIM_4
LABELS                                                    
CL_0     6.577742  -1.200491  1.702951 -2.841551  1.647412
CL_1     5.392503   1.230559 -2.105539 -1.283297 -1.395292
CL_2     6.641901  -1.074545  2.497601  2.062847 -1.206214
CL_3     6.916350   1.456761 -2.298786  2.723546  3.998867
CL_4    24.062092  -5.351854 -3.714930  1.635141 -1.135873
CL_5    14.735496  10.551467  1.711705  0.094923  0.197063



"""
from typing import Literal

from ....._common.factor_analysis import FactorAnalyzer


def cluster_centers(
    #
    # PARAMS:
    field,
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
    algorithm_svd="randomized",
    n_iter=5,
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
    tol=0.0,
    #
    # KMEANS PARAMS:
    n_clusters=8,
    init="k-means++",
    n_init=10,
    max_iter=300,
    kmeans_tol=0.0001,
    algorithm_kmeans="auto",
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

    analyzer = FactorAnalyzer(field=field)

    analyzer.cooc_matrix(
        #
        # COOC PARAMS:
        association_index=association_index,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    analyzer.svd(
        #
        # SVD PARAMS:
        n_components=n_components,
        algorithm=algorithm_svd,
        n_iter=n_iter,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
        tol=tol,
    )

    analyzer.compute_embedding()

    analyzer.kmeans(
        #
        # KMEANS PARAMS:
        n_clusters=n_clusters,
        init=init,
        n_init=n_init,
        max_iter=max_iter,
        tol=kmeans_tol,
        random_state=random_state,
        algorithm=algorithm_kmeans,
    )

    analyzer.run_clustering()

    return analyzer.cluster_centers()
