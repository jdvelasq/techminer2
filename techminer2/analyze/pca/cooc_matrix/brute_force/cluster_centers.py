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


>>> from techminer2.analyze.pca.cooc_matrix.brute_force import cluster_centers
>>> cluster_centers(
...     #
...     # PARAMS:
...     field="author_keywords",
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
...     pca_tol=0.0,
...     iterated_power="auto",
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0, 
...     #
...     # BRUTE FORCE PARAMS:
...     brute_force_labels={
...         'MOBILE_FINTECH_PAYMENT_SERVICES 04:0485': 0, 
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
CL_0    -1.762480 -0.921386 -1.001378 -0.837152  0.120628
CL_1    -2.400146  1.967561  0.552642 -0.326373 -0.097746
CL_2    -1.325489 -2.589322  2.659909  0.423820 -0.599179
CL_3    -1.057332  0.457949 -1.239698  2.403005  0.228861
CL_4    28.639787 -0.692394 -0.115513 -0.022970 -0.078264
CL_5     2.209097  6.587357  1.655333 -0.454795  0.615174


"""
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
