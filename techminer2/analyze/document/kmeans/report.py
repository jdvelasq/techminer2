# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Themes
===============================================================================

>>> from techminer2.analyze.document.kmeans import report
>>> report(
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
--INFO-- The file 'data/regtech/reports/document_clustering/kmeans/theme_000_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/document_clustering/kmeans/theme_001_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/document_clustering/kmeans/theme_002_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/document_clustering/kmeans/theme_003_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/document_clustering/kmeans/theme_004_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/document_clustering/kmeans/theme_005_abstracts_report.txt' was created.

"""

from ..document_classifier import DocumentClassifier


def report(
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
    classifier.report()
