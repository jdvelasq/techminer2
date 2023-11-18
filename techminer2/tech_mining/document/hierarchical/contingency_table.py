# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Contingency Table
===============================================================================

>>> from techminer2.analyze.document.hierarchical import contingency_table
>>> contingency_table(
...     field='words',
...     #
...     # ITEM FILTERS:
...     top_n=50,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # HIERARCHICAL PARAMS:
...     n_themes=6,
...     metric=None,
...     memory=None,
...     connectivity=None,
...     compute_full_tree="auto",
...     linkage="ward",
...     distance_threshold=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head(20)
theme                TH_0  TH_1  TH_2  TH_3  TH_4  TH_5
words                                                  
fintech 50:8135         7     6     4     8     8    17
financial 44:7123       7     6     2     8     8    13
© 42:6879               6     5     4     8     7    12
technology 39:6527      6     5     4     5     7    12
new 26:4793             2     4     1     0     8    11
service 26:4327         7     5     4     2     5     3
industry 23:4517        4     4     0     2     8     5
study 23:3158           4     3     4     4     6     2
model 19:3820           2     2     4     2     5     4
innovation 19:3070      1     6     1     0     6     5
development 19:2499     4     5     1     1     3     5
author 18:2443          4     4     2     2     2     4
market 17:3446          3     5     1     1     3     4
data 17:2392            3     0     2     8     0     4
research 17:2383        2     2     2     4     4     3
paper 14:2240           1     3     3     3     2     2
finance 14:2199         2     2     0     1     3     6
result 14:2183          0     4     3     4     3     0
sector 13:2748          4     2     1     1     3     2
institution 13:2648     4     4     0     0     1     4


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
    # HIERARCHICAL PARAMS:
    n_themes=8,
    metric=None,
    memory=None,
    connectivity=None,
    compute_full_tree="auto",
    linkage="ward",
    distance_threshold=None,
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
    classifier.hierarchical(
        #
        # HIERARCHICAL PARAMS:
        n_themes=n_themes,
        metric=metric,
        memory=memory,
        connectivity=connectivity,
        compute_full_tree=compute_full_tree,
        linkage=linkage,
        distance_threshold=distance_threshold,
    )
    classifier.fit()
    return classifier.contingecy_table()
