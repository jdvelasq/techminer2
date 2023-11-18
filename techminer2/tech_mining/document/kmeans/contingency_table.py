# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Contingency Table
===============================================================================

>>> from techminer2.analyze.document.kmeans import contingency_table
>>> contingency_table(
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
... ).head(20)
theme                TH_0  TH_1  TH_2  TH_3  TH_4  TH_5
words                                                  
fintech 50:8135        10    10    15     1     7     7
financial 44:7123       9     9    13     1     7     5
© 42:6879              10     9     9     1     6     7
technology 39:6527      9    10     7     1     7     5
new 26:4793             1    10     6     1     6     2
service 26:4327         6     8     1     1     6     4
industry 23:4517        2     8     4     0     6     3
study 23:3158           8     1     3     1     6     4
model 19:3820           6     4     2     1     4     2
innovation 19:3070      1     3     6     1     7     1
development 19:2499     2     2     3     0     6     6
author 18:2443          5     0     5     1     3     4
market 17:3446          0     5     3     0     4     5
data 17:2392            7     2     6     1     0     1
research 17:2383        4     2     5     1     2     3
paper 14:2240           4     1     3     1     5     0
finance 14:2199         1     4     7     0     0     2
result 14:2183          6     1     1     1     4     1
sector 13:2748          2     4     2     1     2     2
institution 13:2648     0     6     1     0     4     2


"""

from ..document_classifier import DocumentClassifier


def contingency_table(
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
    return classifier.contingecy_table()
