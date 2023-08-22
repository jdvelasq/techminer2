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


>>> from techminer2.co_occurrence.factor.pca.co_occurrence_matrix.abstract_nlp_phrases.hierarchical import cluster_centers
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
...     n_components=5,
...     whiten=False,
...     svd_solver="auto",
...     tol=0.0,
...     iterated_power="auto",
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0, 
...     #
...     # AGLOMERATIVE_CLUSTERING PARAMS:
...     n_clusters=6,
...     metric=None,
...     memory=None,
...     connectivity=None,
...     compute_full_tree="auto",
...     linkage="ward",
...     distance_threshold=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
            DIM_0     DIM_1     DIM_2     DIM_3     DIM_4
LABELS                                                   
CL_0     0.558948 -1.765481  2.380435 -0.285201 -1.117479
CL_1    -3.233806  0.841224  0.262736 -1.563526  1.555041
CL_2    -1.111548  2.449297 -2.730278 -1.069162 -1.204536
CL_3    -2.329782 -1.540305 -0.921917  2.716063  1.157734
CL_4     9.061725  8.966662  2.968123  1.973129  1.080564
CL_5    14.285131 -5.374639 -3.692899 -0.595423 -0.408645

"""
from .......factor_analysis import FactorAnalyzer

UNIT_OF_ANALYSIS = "abstract_nlp_phrases"


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
    # HIERARCHICAL PARAMS:
    n_clusters=None,
    metric=None,
    memory=None,
    connectivity=None,
    compute_full_tree="auto",
    linkage="ward",
    distance_threshold=None,
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

    analyzer = FactorAnalyzer(field=UNIT_OF_ANALYSIS)

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

    analyzer.pca(
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
    )

    analyzer.compute_embedding()

    analyzer.hierarchical(
        #
        # HIERARCHICAL PARAMS:
        n_clusters=n_clusters,
        metric=metric,
        memory=memory,
        connectivity=connectivity,
        compute_full_tree=compute_full_tree,
        linkage=linkage,
        distance_threshold=distance_threshold,
    )

    analyzer.run_clustering()

    return analyzer.cluster_centers()
