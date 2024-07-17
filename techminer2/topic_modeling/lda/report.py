# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Report
===============================================================================


>>> from techminer2.science_mapping.topic_modeling.lda import report
>>> report(
...     #
...     # TF PARAMS:
...     field="author_keywords",
...     is_binary=True,
...     cooc_within=1,
...     #
...     # ITEM FILTERS:
...     top_n=None,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # LDA PARAMS:
...     n_components=10,
...     learning_decay=0.7,
...     learning_offset=50.0,
...     max_iter=10,
...     batch_size=128,
...     evaluate_every=-1,
...     perp_tol=0.1,
...     mean_change_tol=0.001,
...     max_doc_update_iter=100,
...     random_state=0,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_000_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_001_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_002_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_003_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_004_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_005_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_006_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_007_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_008_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/topic_modeling/lda/theme_009_abstracts_report.txt' was created.




"""

from .._core.topic_modeler import TopicModeler


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
    # LDA PARAMS:
    n_components=10,
    learning_decay=0.7,
    learning_offset=50.0,
    max_iter=10,
    batch_size=128,
    evaluate_every=-1,
    perp_tol=0.1,
    mean_change_tol=0.001,
    max_doc_update_iter=100,
    random_state=0,
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

    tm = TopicModeler()
    tm.build_tf_matrix(
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

    tm.lda(
        n_components=n_components,
        learning_decay=learning_decay,
        learning_offset=learning_offset,
        max_iter=max_iter,
        batch_size=batch_size,
        evaluate_every=evaluate_every,
        perp_tol=perp_tol,
        mean_change_tol=mean_change_tol,
        max_doc_update_iter=max_doc_update_iter,
        random_state=random_state,
    )

    tm.fit()
    tm.compute_components()
    tm.compute_documents_by_theme()

    tm.report()
