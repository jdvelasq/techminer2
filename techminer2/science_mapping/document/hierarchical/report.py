# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Report
===============================================================================

>>> from techminer2.analyze.document.hierarchical import report
>>> report(
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
--INFO-- The file 'example/reports/document_clustering/hierarchical/theme_000_abstracts_report.txt' was created.
--INFO-- The file 'example/reports/document_clustering/hierarchical/theme_001_abstracts_report.txt' was created.
--INFO-- The file 'example/reports/document_clustering/hierarchical/theme_002_abstracts_report.txt' was created.
--INFO-- The file 'example/reports/document_clustering/hierarchical/theme_003_abstracts_report.txt' was created.
--INFO-- The file 'example/reports/document_clustering/hierarchical/theme_004_abstracts_report.txt' was created.
--INFO-- The file 'example/reports/document_clustering/hierarchical/theme_005_abstracts_report.txt' was created.


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
    classifier.report()
