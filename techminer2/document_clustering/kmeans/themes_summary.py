# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Themes Summary
===============================================================================

>>> from techminer2.tech_mining.document.kmeans import themes_summary
>>> themes_summary(
...     field='words',
...     #
...     # ITEM FILTERS:
...     top_n=50,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # KMEANS PARAMS:
...     n_themes=6,
...     init="k-means++",
...     n_init=10,
...     max_iter=300,
...     kmeans_tol=0.0001,
...     algorithm="auto",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
  Theme  ...                                              Terms
0  TH_0  ...  © 42:6879; study 23:3158; model 19:3820; autho...
1  TH_1  ...  technology 39:6527; new 26:4793; service 26:43...
2  TH_2  ...  fintech 50:8135; financial 44:7123; research 1...
3  TH_4  ...  innovation 19:3070; development 19:2499; paper...
4  TH_5  ...                  increase 11:1716; company 09:1671
<BLANKLINE>
[5 rows x 4 columns]



"""

from ..document_classifier import DocumentClassifier


def themes_summary(
    #
    # TF PARAMS:
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
    # KMEANS PARAMS:
    n_themes=8,
    init="k-means++",
    n_init=10,
    max_iter=300,
    kmeans_tol=0.0001,
    algorithm="auto",
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

    classifier = DocumentClassifier()
    classifier.build_tf_matrix(
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
    classifier.kmeans(
        #
        # KMEANS PARAMS:
        n_themes=n_themes,
        init=init,
        n_init=n_init,
        max_iter=max_iter,
        tol=kmeans_tol,
        algorithm=algorithm,
    )
    classifier.fit()
    return classifier.themes_summary()
