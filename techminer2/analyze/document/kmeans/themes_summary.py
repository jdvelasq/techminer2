# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Themes Summary
===============================================================================

>>> from techminer2.analyze.document.kmeans import themes_summary
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
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
  Theme  ...                                              Terms
0  TH_0  ...  APPLICATION 15:210; AUTHOR 13:243; FINTECH 12:...
1  TH_1  ...  NEW_TECHNOLOGIES 22:381; REGULATORY_TECHNOLOGY...
2  TH_2  ...                                    CHANGING 07:183
3  TH_3  ...  base 13:061; propose 11:188; reserve 11:184; R...
4  TH_4  ...  REGTECH 48:557; REGULATORS 30:466; CHALLENGE 1...
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
