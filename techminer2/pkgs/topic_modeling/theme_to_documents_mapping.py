# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Theme to Documents Mapping
===============================================================================

## >>> from sklearn.decomposition import LatentDirichletAllocation
## >>> lda = LatentDirichletAllocation(
## ...     n_components=10,
## ...     learning_decay=0.7,
## ...     learning_offset=50.0,
## ...     max_iter=10,
## ...     batch_size=128,
## ...     evaluate_every=-1,
## ...     perp_tol=0.1,
## ...     mean_change_tol=0.001,
## ...     max_doc_update_iter=100,
## ...     random_state=0,
## ... )
## >>> from techminer2.pkgs.topic_modeling import theme_to_documents_mapping
## >>> mapping = (
## ...     ThemeToDocumentsMapping()
## ...     #
## ...     # FIELD:
## ...     .with_field("descriptors")
## ...     .having_terms_in_top(50)
## ...     .having_terms_ordered_by("OCC")
## ...     .having_term_occurrences_between(None, None)
## ...     .having_term_citations_between(None, None)
## ...     .having_terms_in(None)
## ...     #
## ...     # DECOMPOSITION:
## ...     .using_decomposition_estimator(lda)
## ...     .using_top_terms_by_theme(5)
## ...     #
## ...     # TFIDF:
## ...     .using_binary_term_frequencies(False)
## ...     .using_row_normalization(None)
## ...     .using_idf_reweighting(False)
## ...     .using_idf_weights_smoothing(False)
## ...     .using_sublinear_tf_scaling(False)
## ...     #
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
## >>> import pprint
## >>> pprint.pprint(mapping)



"""
from .documents_by_theme_dataframe import documents_by_theme_frame


def theme_to_documents_mapping(
    field,
    #
    # TF PARAMS:
    is_binary: bool = True,
    cooc_within: int = 1,
    #
    # TF-IDF parameters:
    norm=None,
    use_idf=False,
    smooth_idf=False,
    sublinear_tf=False,
    #
    # TOP TERMS:
    n_top_terms=5,
    #
    # TERM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # ESTIMATOR:
    sklearn_estimator=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    frame = documents_by_theme_frame(
        field=field,
        #
        # TF PARAMS:
        is_binary=is_binary,
        cooc_within=cooc_within,
        #
        # TF-IDF parameters:
        norm=norm,
        use_idf=use_idf,
        smooth_idf=smooth_idf,
        sublinear_tf=sublinear_tf,
        #
        # TOP TERMS:
        n_top_terms=n_top_terms,
        #
        # TERM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_terms=custom_terms,
        #
        # ESTIMATOR:
        sklearn_estimator=sklearn_estimator,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    assigned_topics_to_documents = frame.idxmax(axis=1)

    mapping = {}
    for article, theme in zip(
        assigned_topics_to_documents.index, assigned_topics_to_documents
    ):
        if theme not in mapping:
            mapping[theme] = []
        mapping[theme].append(article)

    return mapping
