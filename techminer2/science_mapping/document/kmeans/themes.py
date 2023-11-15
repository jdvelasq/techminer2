# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Themes
===============================================================================

>>> from techminer2.analyze.document.kmeans import themes
>>> x = themes(
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
>>> print(x.to_markdown())
|    | TH_0               | TH_1                | TH_2                | TH_4                | TH_5             |
|---:|:-------------------|:--------------------|:--------------------|:--------------------|:-----------------|
|  0 | © 42:6879          | technology 39:6527  | fintech 50:8135     | innovation 19:3070  | increase 11:1716 |
|  1 | study 23:3158      | new 26:4793         | financial 44:7123   | development 19:2499 | company 09:1671  |
|  2 | model 19:3820      | service 26:4327     | research 17:2383    | paper 14:2240       |                  |
|  3 | author 18:2443     | industry 23:4517    | finance 14:2199     | well 13:1908        |                  |
|  4 | data 17:2392       | market 17:3446      | make 13:1355        | offer 13:1850       |                  |
|  5 | result 14:2183     | sector 13:2748      | consumer 12:1472    | bank 13:1843        |                  |
|  6 | impact 13:2198     | institution 13:2648 | traditional 11:2254 | apply 11:2052       |                  |
|  7 | propose 13:1711    | business 13:2615    | discuss 10:2133     | aim 10:1111         |                  |
|  8 | system 12:1826     | information 12:2653 | area 09:1646        | banking 10:1032     |                  |
|  9 | customer 11:2437   | risk 11:1636        |                     |                     |                  |
| 10 | identify 11:1435   | process 10:2113     |                     |                     |                  |
| 11 | digital 10:1855    | change 10:2050      |                     |                     |                  |
| 12 | finding 10:1362    | “ 09:1743           |                     |                     |                  |
| 13 | investment 09:2077 | ” 09:1743           |                     |                     |                  |
| 14 |                    | focus 09:1631       |                     |                     |                  |
| 15 |                    | potential 09:1570   |                     |                     |                  |



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
    return classifier.themes()
