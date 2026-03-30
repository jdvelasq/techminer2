"""
Theme to Documents Mapping
===============================================================================


Smoke tests:
    >>> from sklearn.decomposition import LatentDirichletAllocation
    >>> lda = LatentDirichletAllocation(
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
    ... )
    >>> from tm2p import ItemOrderBy, Field
    >>> from tm2p.synthes.topic_model import ThemeToDocumentsMapping
    >>> mapping = (
    ...     ThemeToDocumentsMapping()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_items_in_top(50)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(lda)
    ...     .using_top_items_by_theme(5)
    ...     #
    ...     # TFIDF:
    ...     .using_binary_item_frequencies(False)
    ...     .using_tfidf_norm(None)
    ...     .using_tfidf_smooth_idf(False)
    ...     .using_tfidf_sublinear_tf(False)
    ...     .using_tfidf_use_idf(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> import pprint
    >>> pprint.pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['Al-Sartawi A, 2024, J FINANC REP ACC, DOI 10.1108/JFRA-01-2024-0010',
         'Anagnostopoulos I, 2018, J ECON BUS, V100, P7, DOI '
         '10.1016/j.jeconbus.2018.07.003',
         'Arner DW, 2020, EUR BUS ORG LAW REV, V21, P7, DOI '
         '10.1007/s40804-020-00183-y',
         'Awais M, 2023, RESOUR POLIC, V81, DOI 10.1016/j.resourpol.2023.103309',
         'Barberis J, 2016, ECON WIND, P69, DOI 10.1007/978-3-319-42448-4_5',
         'Barbu CM, 2021, J THEOR APPL ELECTRON COMMER RES, V16, P1415, DOI '
         '10.3390/jtaer16050080',
    ...
"""

from tm2p._intern import ParamsMixin
from tm2p.synthes.topic.documents_by_theme_dataframe import DocumentsByThemeDataFrame


class ThemeToDocumentsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        frame = DocumentsByThemeDataFrame().update(**self.params.__dict__).run()

        assigned_topics_to_documents = frame.idxmax(axis=1)

        mapping = {}
        for article, theme in zip(
            assigned_topics_to_documents.index, assigned_topics_to_documents
        ):
            if theme not in mapping:
                mapping[theme] = []
            mapping[theme].append(article)

        return mapping
