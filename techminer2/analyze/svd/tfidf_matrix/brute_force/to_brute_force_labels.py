# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
To Brute Force Labels
===============================================================================


>>> from techminer2.analyze.svd.tfidf_matrix.brute_force import to_brute_force_labels
>>> to_brute_force_labels(
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
...        'FINTECH 31:5168': 0, 'FINANCIAL_INCLUSION 03:0590': 0, 'CASE_STUDIES 03:0442': 0, 
...        'BLOCKCHAIN 03:0369': 0, 'CROWDFUNDING 03:0335': 0, 'MOBILE_PAYMENT 03:0309': 0, 
...        'CYBER_SECURITY 02:0342': 0, 'ARTIFICIAL_INTELLIGENCE 02:0327': 0, 
...        'INNOVATION 07:0911': 1, 'DIGITAL 03:0434': 1, 'BANKING 03:0375': 1, 
...        'FINANCIAL_INSTITUTION 02:0484': 1, 'TECHNOLOGIES 02:0310': 1, 
...        'FINANCIAL_SERVICES 04:0667': 2, 'FINANCIAL_TECHNOLOGY 04:0551': 2, 
...        'BUSINESS 03:0896': 2, 'FUTURE_RESEARCH 02:0691': 2, 'SHADOW_BANKING 03:0643': 3, 
...        'PEER_TO_PEER_LENDING 03:0324': 3, 'MARKETPLACE_LENDING 03:0317': 3
...     },
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )  # doctest: +ELLIPSIS
{'FINTECH 31:5168': 0, 'FINANCIAL_INCLUSION 03:0590': 0, 'CASE_STUDIES 03:0442': 0, ...



"""
from typing import Literal

from ....._common.factor_analysis import FactorAnalyzer


def to_brute_force_labels(
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

    data_frame = analyzer.communities()

    member2group = {}
    for i_col, col in enumerate(data_frame.columns):
        terms = data_frame[col].to_list()
        terms = [term for term in terms if term != ""]
        # terms = [" ".join(term.split(" ")[:-1]) for term in terms]
        for term in terms:
            member2group[term] = i_col

    return member2group
