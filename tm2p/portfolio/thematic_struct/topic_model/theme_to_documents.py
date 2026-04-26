"""
ThemeToDocuments
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
    >>> from tm2p.enum import UnitOrderBy, Field
    >>> from tm2p.portfolio.thematic_stucture.topic_modeling import ThemeToDocuments
    >>> mapping = (
    ...     ThemeToDocuments()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_top_n_units(50)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(lda)
    ...     #
    ...     # TFIDF:
    ...     .using_binary_item_frequencies(False)
    ...     .using_tfidf_norm(None)
    ...     .using_tfidf_smooth_idf(False)
    ...     .using_tfidf_sublinear_tf(False)
    ...     .using_tfidf_use_idf(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> import pprint
    >>> pprint.pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['Alam N, 2019, FINTECH ISLAM FINANC DIGIT DEV DISRUPT, P1, DOI '
         '10.1007/978-3-030-24666-2',
         'Aldboush HHH, 2023, INTERN J FINANC STUD, V11, DOI 10.3390/ijfs11030090',
         'Allen F, 2021, REV CORP FINANC, V1, P259, DOI 10.1561/114.00000007',
         'Ashta A, 2021, STRATEG CHANG, V30, P211, DOI 10.1002/jsc.2404',
         'Bartlett R, 2022, J FINANC ECON, V143, P30, DOI '
         '10.1016/j.jfineco.2021.05.047',
    ...

"""

from tm2p._intern import ParamsMixin
from tm2p.portfolio.thematic_struct.topic_model.documents_by_theme import (
    DocumentsByTheme,
)


class ThemeToDocuments(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        frame = DocumentsByTheme().update(**self.params.__dict__).run()

        assigned_topics_to_documents = frame.idxmax(axis=1)

        mapping = {}
        for article, theme in zip(
            assigned_topics_to_documents.index, assigned_topics_to_documents
        ):
            if theme not in mapping:
                mapping[theme] = []
            mapping[theme].append(article)

        return mapping
