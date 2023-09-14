# flake8: noqa
# pylint: disable=line-too-long
"""
Topic Extraction with LDA
===============================================================================

Topic extraction using LDA.


>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"

>>> themes = tm2p.topic_extraction_with_lda(
...     field="author_keywords",
...     occ_range=(2, None),
...     n_components=10,
...     root_dir=root_dir,
...  )
>>> themes
Themes(n-themes=3)



"""
from sklearn.decomposition import LatentDirichletAllocation

from ..topic_extraction import topic_extraction


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def topic_extraction_with_lda(
    #
    # TFIDF PARAMS:
    field,
    is_binary=False,
    cooc_within=1,
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
    """Emergent themes extraction with LDA"""

    estimator_class = LatentDirichletAllocation
    estimator_params = {
        "learning_decay": learning_decay,
        "learning_offset": learning_offset,
        "max_iter": max_iter,
        "learning_method": "online",
        "batch_size": batch_size,
        "evaluate_every": evaluate_every,
        "perp_tol": perp_tol,
        "mean_change_tol": mean_change_tol,
        "max_doc_update_iter": max_doc_update_iter,
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
