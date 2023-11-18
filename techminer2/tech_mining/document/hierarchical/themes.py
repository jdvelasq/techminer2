# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Themes
===============================================================================

>>> from techminer2.analyze.document.hierarchical import themes
>>> x = themes(
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
... )
>>> print(x.to_markdown())
|    | TH_0                | TH_1                | TH_2                | TH_3             | TH_4             | TH_5               |
|---:|:--------------------|:--------------------|:--------------------|:-----------------|:-----------------|:-------------------|
|  0 | service 26:4327     | innovation 19:3070  | information 12:2653 | data 17:2392     | industry 23:4517 | fintech 50:8135    |
|  1 | author 18:2443      | development 19:2499 | “ 09:1743           | research 17:2383 | study 23:3158    | financial 44:7123  |
|  2 | sector 13:2748      | market 17:3446      | ” 09:1743           | impact 13:2198   | model 19:3820    | © 42:6879          |
|  3 | institution 13:2648 | paper 14:2240       |                     | propose 13:1711  | business 13:2615 | technology 39:6527 |
|  4 | offer 13:1850       | result 14:2183      |                     | consumer 12:1472 | discuss 10:2133  | new 26:4793        |
|  5 | system 12:1826      | well 13:1908        |                     | finding 10:1362  | process 10:2113  | finance 14:2199    |
|  6 | customer 11:2437    | bank 13:1843        |                     |                  | area 09:1646     | identify 11:1435   |
|  7 | increase 11:1716    | make 13:1355        |                     |                  |                  | investment 09:2077 |
|  8 | digital 10:1855     | traditional 11:2254 |                     |                  |                  | potential 09:1570  |
|  9 | company 09:1671     | apply 11:2052       |                     |                  |                  |                    |
| 10 | focus 09:1631       | risk 11:1636        |                     |                  |                  |                    |
| 11 |                     | change 10:2050      |                     |                  |                  |                    |
| 12 |                     | aim 10:1111         |                     |                  |                  |                    |
| 13 |                     | banking 10:1032     |                     |                  |                  |                    |



"""
from ..document_classifier import DocumentClassifier


def themes(
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
    return classifier.themes()
