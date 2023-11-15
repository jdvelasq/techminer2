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


>>> from techminer2.analyze.pca.tfidf_matrix.brute_force import cluster_centers
>>> cluster_centers(
...     #
...     # PARAMS:
...     field="author_keywords",
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
...     # BRUTE FORCE PARAMS:
...     brute_force_labels={
...         'MOBILE_PAYMENT 03:0309': 0, 
...         'FINANCIAL_INCLUSION 03:0590': 0, 'CASE_STUDIES 03:0442': 0, 
...         'BLOCKCHAIN 03:0369': 0, 'CROWDFUNDING 03:0335': 0, 
...         'FUTURE_RESEARCH 02:0691': 0, 'CYBER_SECURITY 02:0342': 0, 
...         'ARTIFICIAL_INTELLIGENCE 02:0327': 0, 'DIGITALIZATION 03:0434': 1, 
...         'BANKING 03:0375': 1, 'FINANCIAL_INSTITUTION 02:0484': 1, 
...         'TECHNOLOGIES 02:0310': 1, 'SHADOW_BANKING 03:0643': 2, 
...         'PEER_TO_PEER_LENDING 03:0324': 2, 'MARKETPLACE_LENDING 03:0317': 2, 
...         'FINANCIAL_SERVICES 04:0667': 3, 'FINANCIAL_TECHNOLOGY 04:0551': 3, 
...         'BUSINESS 03:0896': 3, 'FINTECH 31:5168': 4, 'INNOVATION 07:0911': 5
...     },
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
           DIM_0     DIM_1     DIM_2     DIM_3     DIM_4
LABELS                                                  
CL_0   -0.234234 -0.247057 -0.348292 -0.377025  0.133596
CL_1   -0.450885  0.616156  0.248541 -0.102167 -0.076328
CL_2   -0.209104 -0.907656  0.978047  0.191922 -0.270391
CL_3   -0.244325  0.079554 -0.621776  0.938110 -0.049120
CL_4    4.887806 -0.043138 -0.014483  0.018812 -0.074537
CL_5    0.149896  2.039274  0.737841  0.015960  0.269611


"""
from typing import Literal

from ....._common.factor_analysis import FactorAnalyzer


def cluster_centers(
    #
    # PARAMS:
    field,
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
    # BRUTE FORCE PARAMS:
    brute_force_labels=None,
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

    # analyzer.pcd(
    #     #
    #     # FACTOR MAP PARAMS:
    #     threshold=threshold,
    # )

    analyzer.run_clustering(brute_force_labels=brute_force_labels)

    return analyzer.cluster_centers()
