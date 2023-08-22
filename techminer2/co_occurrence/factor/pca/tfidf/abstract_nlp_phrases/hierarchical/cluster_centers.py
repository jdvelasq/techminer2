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


>>> from techminer2.co_occurrence.factor.pca.tfidf.abstract_nlp_phrases.hierarchical import cluster_centers
>>> cluster_centers(
...     #
...     # TF PARAMS:
...     is_binary=True,
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
CL_0   -0.568603  0.392286 -0.410744 -0.329262 -0.141727
CL_1   -0.337626 -0.593202 -0.029877  0.846846  0.298212
CL_2    0.154067 -0.271112  0.711023 -0.202996 -0.720538
CL_3    0.384490 -0.107354  0.392966 -0.963503  1.220978
CL_4    1.513684  2.646565  0.760537  0.762787  0.233871
CL_5    2.769419 -1.127397 -1.365969  0.046809 -0.292650




"""
from typing import Literal

from .......factor_analysis import FactorAnalyzer

UNIT_OF_ANALYSIS = "abstract_nlp_phrases"


def cluster_centers(
    #
    # TF PARAMS:
    is_binary: bool = True,
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

    analyzer.tfidf(
        #
        # TF PARAMS:
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
