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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head(20)
theme                          TH_0  TH_1  TH_2  TH_3  TH_4  TH_5
words                                                            
REGTECH 48:557                    7    10     3     9    17     2
REGULATORS 30:466                 3    10     2     3    11     1
NEW_TECHNOLOGIES 22:381           3     8     0     1     8     2
REGULATORY_TECHNOLOGY 20:276      6     7     0     2     5     0
COMPLIANCE 18:368                 1    10     1     2     3     1
BANK 18:305                       3     4     1     3     4     3
FINANCIAL_INSTITUTIONS 16:224     2     6     2     2     4     0
CHALLENGE 16:203                  1     5     2     1     7     0
PAPER 15:371                      0     6     1     3     2     3
APPLICATION 15:210                5     3     0     4     3     0
APPROACH 14:360                   2     4     2     3     3     0
develop 13:254                    0     2     2     3     4     2
AUTHOR 13:243                     6     2     0     2     2     1
base 13:061                       1     2     2     6     2     0
FINTECH 12:364                    3     3     0     3     3     0
FINANCIAL_CRISIS 12:235           0     5     1     1     5     0
FINDINGS 12:120                   5     0     0     2     2     3
REGULATORY_COMPLIANCE 11:360      3     7     0     1     0     0
DATA 11:221                       1     3     0     2     2     3
well 11:194                       0     4     0     1     5     1


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
