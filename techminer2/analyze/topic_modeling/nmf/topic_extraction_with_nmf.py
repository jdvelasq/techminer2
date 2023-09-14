# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Topic Extraction with NMF
===============================================================================

Topic extraction using non-negative matrix factorization.


>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"

>>> n_components, terms_by_theme, documents_by_theme = tm2p.topic_extraction_with_nmf(
...     field="author_keywords",
...     top_n=50,
...     n_components=10,
...     root_dir=root_dir,
... )

>>> n_components


"""
from sklearn.decomposition import NMF

from ..topic_extraction import topic_extraction


def topic_extraction_with_nmf(
    #
    # TFIDF PARAMS:
    field: str,
    is_binary: bool = False,
    cooc_within: int = 1,
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
    """Emergent themes extraction with LDA"""

    estimator_class = NMF
    estimator_params = {
        "init": init,
        "solver": solver,
        "beta_loss": beta_loss,
        "tol": tol,
        "max_iter": max_iter,
        "alpha_W": alpha_W,
        "alpha_H": alpha_H,
        "l1_ratio": l1_ratio,
        "shuffle": shuffle,
        "random_state": random_state,
    }

    return topic_extraction(
        #
        # TFIDF PARAMS:
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
        # ESTIMATOR PARAMS:
        n_components=n_components,
        estimator_class=estimator_class,
        estimator_params=estimator_params,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
