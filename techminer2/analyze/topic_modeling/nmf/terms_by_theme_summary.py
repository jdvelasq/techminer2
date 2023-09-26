# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Terms by Theme Summary
===============================================================================


>>> from techminer2.analyze.topic_modeling.nmf import terms_by_theme_summary
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
...     # NMF PARAMS:
...     n_components=10,
...     init=None,
...     solver="cd",
...     beta_loss="frobenius",
...     tol=0.0001,
...     max_iter=200,
...     alpha_W=0.0,
...     alpha_H=0.0,
...     l1_ratio=0.0,
...     shuffle=False,
...     random_state=0,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
  Theme  ...                                              Terms
0  TH_0  ...  FINTECH 12:249; REGTECH 28:329; REGULATORS 05:...
1  TH_1  ...  REGULATORS 05:164; RISK_MANAGEMENT 03:014; REG...
2  TH_2  ...  COMPLIANCE 07:030; REGTECH 28:329; DATA_PROTEC...
3  TH_3  ...  ANTI_MONEY_LAUNDERING 06:044; REGULATORY_TECHN...
4  TH_4  ...  REGTECH 28:329; MANUAL_INTERVENTION 01:000; AL...
5  TH_5  ...  FINANCIAL_REGULATION 04:035; FINANCIAL_SERVICE...
6  TH_6  ...  MILES 01:005; NEOLOGY 01:005; THEOLOGY_OF_ENLI...
7  TH_7  ...  REGTECH 28:329; CHARITYTECH 02:017; ENGLISH_LA...
8  TH_8  ...  FINANCIAL_SERVICES 04:168; REGTECH 28:329; FIN...
9  TH_9  ...  REGULATORY_TECHNOLOGY 07:037; INNOVATION 03:01...
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
    # NMF PARAMS:
    n_components=10,
    init=None,
    solver="cd",
    beta_loss="frobenius",
    tol=0.0001,
    max_iter=200,
    alpha_W=0.0,
    alpha_H=0.0,
    l1_ratio=0.0,
    shuffle=False,
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

    tm.nmf(
        n_components=n_components,
        init=init,
        solver=solver,
        beta_loss=beta_loss,
        tol=tol,
        max_iter=max_iter,
        alpha_W=alpha_W,
        alpha_H=alpha_H,
        l1_ratio=l1_ratio,
        shuffle=shuffle,
        random_state=random_state,
    )

    tm.fit()
    tm.compute_components()
    tm.compute_documents_by_theme()

    return tm.terms_by_theme_summary(n_top_terms)
