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


>>> from techminer2.tech_mining.svd.cooc_matrix.brute_force import cluster_centers
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
...     # SVD PARAMS:
...     n_components=5,
...     algorithm_svd="randomized",
...     n_iter=5,
...     n_oversamples=10,
...     power_iteration_normalizer="auto",
...     random_state=0,
...     tol=0.0, 
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
CL_0     2.589022 -0.284559 -0.696730 -0.128216 -0.114045
CL_1     2.191300  2.743745  0.587870 -0.255850 -0.246496
CL_2     3.077928 -1.582192  3.288760  0.538517 -0.444533
CL_3     3.508127  1.302022 -0.478506  2.851510  0.595582
CL_4    32.944613 -2.098291 -0.628479 -0.556423 -0.056630
CL_5     7.107926  7.057955  1.108932 -1.186841  0.652848


"""
from typing import Literal

from .....core.factor_analysis import FactorAnalyzer


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

    analyzer.run_clustering(brute_force_labels=brute_force_labels)

    return analyzer.cluster_centers()
