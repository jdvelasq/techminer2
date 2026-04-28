"""
DocumentsByTheme
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
    >>> from tm2p.portfolio.thematic_struct.topic_modeling import DocumentsByTheme
    >>> df =(
    ...     DocumentsByTheme()
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
    >>> df.head()
    THEME                                                      0  ...         9
    DOCUMENT                                                      ...
    Agarwal S, 2020, ASIA-PAC J FINANC STUD, V49, P...  0.020002  ...  0.020001
    Ajouz M, 2023, CUAD ECON, V46, P189, DOI 10.328...  0.323943  ...  0.020005
    Al-Sartawi A, 2024, J FINANC REP ACC, DOI 10.11...  0.011115  ...  0.011113
    Alam N, 2019, FINTECH ISLAM FINANC DIGIT DEV DI...  0.819971  ...  0.020002
    Aldboush HHH, 2023, INTERN J FINANC STUD, V11, ...  0.819963  ...  0.020006
    <BLANKLINE>
    [5 rows x 10 columns]




"""

from tm2p._intern import ParamsMixin

from ._intern.compute_tables import compute_tables


class DocumentsByTheme(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        _, documents_by_theme = compute_tables(self.params)

        return documents_by_theme
