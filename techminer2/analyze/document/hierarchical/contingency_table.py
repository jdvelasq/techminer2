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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head(20)
theme                          TH_0  TH_1  TH_2  TH_3  TH_4  TH_5
words                                                            
REGTECH 48:557                    5    15     8    12     5     3
REGULATORS 30:466                 5    13     3     3     5     1
NEW_TECHNOLOGIES 22:381           3    13     3     1     0     2
REGULATORY_TECHNOLOGY 20:276      3     7     5     3     2     0
COMPLIANCE 18:368                 5     7     2     1     2     1
BANK 18:305                       2     3     5     4     1     3
FINANCIAL_INSTITUTIONS 16:224     3     6     2     0     5     0
CHALLENGE 16:203                  2     9     1     1     3     0
PAPER 15:371                      4     5     0     1     1     4
APPLICATION 15:210                1     6     7     1     0     0
APPROACH 14:360                   4     2     1     2     4     1
develop 13:254                    2     1     0     6     2     2
AUTHOR 13:243                     1     0     6     1     3     2
base 13:061                       1     5     1     3     2     1
FINTECH 12:364                    3     3     3     2     1     0
FINANCIAL_CRISIS 12:235           3     4     1     3     1     0
FINDINGS 12:120                   0     2     4     0     2     4
REGULATORY_COMPLIANCE 11:360      3     4     4     0     0     0
DATA 11:221                       2     4     1     0     0     4
well 11:194                       3     3     1     2     0     2


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
