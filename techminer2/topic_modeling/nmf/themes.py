# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Themes
===============================================================================


>>> from techminer2.science_mapping.topic_modeling.nmf import themes
>>> themes(
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
                       TH_0  ...                               TH_9
0           FINTECH 31:5168  ...        FINANCIAL_INCLUSION 03:0590
1    DIGITALIZATION 03:0434  ...                    FINTECH 31:5168
2    CYBER_SECURITY 02:0342  ...  INTERNATIONAL_DEVELOPMENT 01:0314
3     POPULAR_PRESS 02:0181  ...            GOVERNMENTALITY 01:0314
4  CONTENT_ANALYSIS 02:0181  ...           FINANCIALISATION 01:0314
<BLANKLINE>
[5 rows x 10 columns]



"""

from .._core.topic_modeler import TopicModeler


def themes(
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

    return tm.themes(n_top_terms)
