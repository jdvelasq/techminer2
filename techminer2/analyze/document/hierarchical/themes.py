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
|    | TH_0                        | TH_1                          | TH_2                    | TH_3            | TH_4            | TH_5           |
|---:|:----------------------------|:------------------------------|:------------------------|:----------------|:----------------|:---------------|
|  0 | APPROACH 14:360             | REGTECH 48:557                | BANK 18:305             | develop 13:254  | CHANGING 07:183 | PURPOSE 10:212 |
|  1 | FINTECH 12:364              | REGULATORS 30:466             | APPLICATION 15:210      | suggest 08:238  |                 | limit 10:087   |
|  2 | well 11:194                 | NEW_TECHNOLOGIES 22:381       | AUTHOR 13:243           | increase 08:171 |                 |                |
|  3 | RIGHTS 11:186               | REGULATORY_TECHNOLOGY 20:276  | FINDINGS 12:120         | CHANGE 07:331   |                 |                |
|  4 | reserve 11:184              | COMPLIANCE 18:368             | RESEARCH 10:212         |                 |                 |                |
|  5 | DEVELOPMENT 10:385          | FINANCIAL_INSTITUTIONS 16:224 | apply 10:169            |                 |                 |                |
|  6 | POTENTIAL 09:387            | CHALLENGE 16:203              | FINANCIAL_SECTOR 09:196 |                 |                 |                |
|  7 | REPORTING 09:255            | PAPER 15:371                  |                         |                 |                 |                |
|  8 | SOLUTION 09:060             | base 13:061                   |                         |                 |                 |                |
|  9 | FINANCIAL_REGULATION 08:361 | FINANCIAL_CRISIS 12:235       |                         |                 |                 |                |
| 10 | FINANCIAL_SYSTEM 07:363     | REGULATORY_COMPLIANCE 11:360  |                         |                 |                 |                |
| 11 |                             | DATA 11:221                   |                         |                 |                 |                |
| 12 |                             | propose 11:188                |                         |                 |                 |                |
| 13 |                             | STUDY 10:068                  |                         |                 |                 |                |
| 14 |                             | improve 09:183                |                         |                 |                 |                |
| 15 |                             | reduce 09:054                 |                         |                 |                 |                |
| 16 |                             | FINANCE 09:030                |                         |                 |                 |                |
| 17 |                             | address 08:167                |                         |                 |                 |                |
| 18 |                             | enhance 08:049                |                         |                 |                 |                |
| 19 |                             | RISKS 08:043                  |                         |                 |                 |                |
| 20 |                             | explore 08:037                |                         |                 |                 |                |
| 21 |                             | BUSINESS 08:027               |                         |                 |                 |                |
| 22 |                             | IMPACT 07:203                 |                         |                 |                 |                |
| 23 |                             | make 07:190                   |                         |                 |                 |                |
| 24 |                             | PRACTICE 07:187               |                         |                 |                 |                |



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
