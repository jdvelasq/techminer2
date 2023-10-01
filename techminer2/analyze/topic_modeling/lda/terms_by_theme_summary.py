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
0  TH_0  ...  REGTECH 28:329; FINANCIAL_SERVICES 04:168; REG...
1  TH_1  ...  FINTECH 12:249; REGTECH 28:329; ARTIFICIAL_INT...
2  TH_2  ...  REGTECH 28:329; FINTECH 12:249; REGULATORS 05:...
3  TH_3  ...  REGTECH 28:329; COMPLIANCE 07:030; DATA_PROTEC...
4  TH_4  ...  FINANCIAL_REGULATION 04:035; SMART_CONTRACT 02...
5  TH_5  ...  REGTECH 28:329; FINTECH 12:249; SUPTECH 03:004...
6  TH_6  ...  REGULATORY_TECHNOLOGY 07:037; ELECTRONIC_TRANS...
7  TH_7  ...  FINTECH 12:249; REGTECH 28:329; REGULATORS 05:...
8  TH_8  ...  FIRM_ACQUISITIVENESS 01:000; MERGERS_AND_ACQUI...
9  TH_9  ...  ANTI_MONEY_LAUNDERING 06:044; INNOVATION 03:01...
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
