# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Theme Summary
===============================================================================


>>> from techminer2.analyze.topic_modeling.lda import terms_by_theme_summary
>>> terms_by_theme_summary(
...     #
...     # TF PARAMS:
...     field="author_keywords",
...     is_binary=True,
...     cooc_within=1,
...     #
...     n_top_terms=5,
...     #
...     # ITEM FILTERS:
...     top_n=None,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # LDA PARAMS:
...     n_components=10,
...     learning_decay=0.7,
...     learning_offset=50.0,
...     max_iter=10,
...     batch_size=128,
...     evaluate_every=-1,
...     perp_tol=0.1,
...     mean_change_tol=0.001,
...     max_doc_update_iter=100,
...     random_state=0,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
  Theme  ...                                              Terms
0  TH_0  ...  FINTECH 31:5168; BLOCKCHAIN 03:0369; FINANCIAL...
1  TH_1  ...  FINANCIAL_TECHNOLOGY 04:0551; FINTECH 31:5168;...
2  TH_2  ...  FINTECH 31:5168; FINANCIAL_INCLUSION 03:0590; ...
3  TH_3  ...  FINTECH 31:5168; INNOVATION 07:0911; CROWDFUND...
4  TH_4  ...  FINTECH 31:5168; INNOVATION 07:0911; CROWDFUND...
5  TH_5  ...  FINTECH 31:5168; MARKETPLACE_LENDING 03:0317; ...
6  TH_6  ...  FINTECH 31:5168; FINANCE 02:0309; TECHNOLOGIES...
7  TH_7  ...  FINTECH 31:5168; BUSINESS 03:0896; FINANCIAL_I...
8  TH_8  ...  CROWDFUNDING 03:0335; PEER_TO_PEER_LENDING 03:...
9  TH_9  ...  FINTECH 31:5168; INNOVATION 07:0911; DIGITALIZ...
<BLANKLINE>
[10 rows x 4 columns]



"""

from ..topic_modeler import TopicModeler


def terms_by_theme_summary(
    #
    # TF PARAMS:
    field: str,
    is_binary: bool = False,
    cooc_within: int = 1,
    #
    n_top_terms=5,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # LDA PARAMS:
    n_components=10,
    learning_decay=0.7,
    learning_offset=50.0,
    max_iter=10,
    batch_size=128,
    evaluate_every=-1,
    perp_tol=0.1,
    mean_change_tol=0.001,
    max_doc_update_iter=100,
    random_state=0,
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

    tm = TopicModeler()
    tm.build_tf_matrix(
        #
        # TF PARAMS:
        field=field,
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # ITEM FILTERS:
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

    tm.lda(
        n_components=n_components,
        learning_decay=learning_decay,
        learning_offset=learning_offset,
        max_iter=max_iter,
        batch_size=batch_size,
        evaluate_every=evaluate_every,
        perp_tol=perp_tol,
        mean_change_tol=mean_change_tol,
        max_doc_update_iter=max_doc_update_iter,
        random_state=random_state,
    )

    tm.fit()
    tm.compute_components()
    tm.compute_documents_by_theme()

    return tm.terms_by_theme_summary(n_top_terms)
