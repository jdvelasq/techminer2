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
|    | TH_0                    | TH_1                          | TH_2            | TH_3            | TH_4              |
|---:|:------------------------|:------------------------------|:----------------|:----------------|:------------------|
|  0 | APPLICATION 15:210      | NEW_TECHNOLOGIES 22:381       | CHANGING 07:183 | base 13:061     | REGTECH 48:557    |
|  1 | AUTHOR 13:243           | REGULATORY_TECHNOLOGY 20:276  |                 | propose 11:188  | REGULATORS 30:466 |
|  2 | FINTECH 12:364          | COMPLIANCE 18:368             |                 | reserve 11:184  | CHALLENGE 16:203  |
|  3 | FINDINGS 12:120         | BANK 18:305                   |                 | RESEARCH 10:212 | develop 13:254    |
|  4 | FINANCIAL_SECTOR 09:196 | FINANCIAL_INSTITUTIONS 16:224 |                 | explore 08:037  | well 11:194       |
|  5 | FINANCE 09:030          | PAPER 15:371                  |                 |                 | limit 10:087      |
|  6 | suggest 08:238          | APPROACH 14:360               |                 |                 | STUDY 10:068      |
|  7 | BUSINESS 08:027         | FINANCIAL_CRISIS 12:235       |                 |                 | increase 08:171   |
|  8 | PRACTICE 07:187         | REGULATORY_COMPLIANCE 11:360  |                 |                 | enhance 08:049    |
|  9 |                         | DATA 11:221                   |                 |                 | CHANGE 07:331     |
| 10 |                         | RIGHTS 11:186                 |                 |                 |                   |
| 11 |                         | DEVELOPMENT 10:385            |                 |                 |                   |
| 12 |                         | PURPOSE 10:212                |                 |                 |                   |
| 13 |                         | apply 10:169                  |                 |                 |                   |
| 14 |                         | POTENTIAL 09:387              |                 |                 |                   |
| 15 |                         | REPORTING 09:255              |                 |                 |                   |
| 16 |                         | improve 09:183                |                 |                 |                   |
| 17 |                         | SOLUTION 09:060               |                 |                 |                   |
| 18 |                         | reduce 09:054                 |                 |                 |                   |
| 19 |                         | FINANCIAL_REGULATION 08:361   |                 |                 |                   |
| 20 |                         | address 08:167                |                 |                 |                   |
| 21 |                         | RISKS 08:043                  |                 |                 |                   |
| 22 |                         | FINANCIAL_SYSTEM 07:363       |                 |                 |                   |
| 23 |                         | IMPACT 07:203                 |                 |                 |                   |
| 24 |                         | make 07:190                   |                 |                 |                   |



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
