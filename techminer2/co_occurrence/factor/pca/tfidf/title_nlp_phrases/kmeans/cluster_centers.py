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


>>> from techminer2.co_occurrence.factor.pca.tfidf.title_nlp_phrases.kmeans import cluster_centers
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
...     pca_tol=0.0,
...     iterated_power="auto",
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0, 
...     #
...     # KMEANS PARAMS:
...     n_clusters=6,
...     init="k-means++",
...     n_init=10,
...     max_iter=300,
...     kmeans_tol=0.0001,
...     algorithm="auto",
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
           DIM_0     DIM_1     DIM_2     DIM_3         DIM_4
LABELS                                                      
CL_0   -0.036030 -0.006999 -0.318621 -0.067038 -2.020305e-01
CL_1    0.815436  0.055350  0.312766  0.015109  1.414278e-15
CL_2   -0.502705  0.767727  0.335516  0.013205  2.393561e-16
CL_3   -0.423170 -0.756891  0.466034 -0.521179 -1.847326e-15
CL_4   -0.281075 -0.471698  0.033264  0.871695  3.411520e-15
CL_5   -0.046465 -0.009206 -0.512931 -0.165907  7.071068e-01




"""
from typing import Literal

from .......factor_analysis import FactorAnalyzer

UNIT_OF_ANALYSIS = "title_nlp_phrases"


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
    pca_tol=0.0,
    iterated_power="auto",
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
    #
    # KMEANS PARAMS:
    n_clusters=8,
    init="k-means++",
    n_init=10,
    max_iter=300,
    kmeans_tol=0.0001,
    algorithm="auto",
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
        tol=pca_tol,
        iterated_power=iterated_power,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        random_state=random_state,
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
        algorithm=algorithm,
    )

    analyzer.run_clustering()

    return analyzer.cluster_centers()
