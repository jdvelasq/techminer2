# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Theme to Documents Mapping
===============================================================================


Example:
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
    >>> from techminer2.packages.topic_modeling.user import ThemeToDocumentsMapping
    >>> mapping = (
    ...     ThemeToDocumentsMapping()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_descriptors")
    ...     .having_terms_in_top(50)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # DECOMPOSITION:
    ...     .using_decomposition_algorithm(lda)
    ...     .using_top_terms_by_theme(5)
    ...     #
    ...     # TFIDF:
    ...     .using_binary_term_frequencies(False)
    ...     .using_row_normalization(None)
    ...     .using_idf_reweighting(False)
    ...     .using_idf_weights_smoothing(False)
    ...     .using_sublinear_tf_scaling(False)
    ...     #
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> import pprint
    >>> pprint.pprint(mapping)  # doctest: +ELLIPSIS
    {0: ['Anshari M., 2019, ENERGY PROCEDIA, V156, P234',
         'Arner D.W., 2017, NORTHWEST J INTL LAW BUS, V37, P373',
         'Deng X., 2019, SUSTAINABILITY, V11',
         'Dorfleitner G., 2017, FINTECH IN GER, P1',
         'Du W.D., 2019, J STRATEGIC INFORM SYST, V28, P50',
         'Gimpel H., 2018, ELECTRON MARK, V28, P245',
         'Goldstein I., 2019, REV FINANC STUD, V32, P1647',
         'Gomber P., 2017, J BUS ECON, V87, P537',
    ...

"""
from ...._internals.mixins import ParamsMixin
from .documents_by_theme_data_frame import DocumentsByThemeDataFrame


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
