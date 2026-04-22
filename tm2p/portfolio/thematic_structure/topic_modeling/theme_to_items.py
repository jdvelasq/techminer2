"""
ThemeToItems
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
    >>> from tm2p.portfolio.thematic_stucture.topic_modeling import ThemeToItems
    >>> mapping = (
    ...     ThemeToItems()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_top_n_units(20)
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
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> import pprint
    >>> pprint.pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['fintech 157:34856',
         'financial services 031:07105',
         'the impact 021:04968',
         'banks 031:06740',
         'fintech development 015:03625',
         'banking 025:04625',
         'innovation 033:07734',
         'data 026:05921',
    ...


    >>> mapping = (
    ...     ThemeToItems()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_top_n_units(20)
    ...     .having_units_ordered_by(UnitOrderBy.OCC)
    ...     .having_unit_occurrence_between(None, None)
    ...     .having_unit_global_citation_between(None, None)
    ...     .having_units_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
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
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> import pprint
    >>> pprint.pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['fintech',
         'financial services',
         'the impact',
         'banks',
         'fintech development',
         'banking',
         'innovation',
         'data',
    ...

"""

from tm2p._intern import ParamsMixin
from tm2p.portfolio.thematic_structure.topic_modeling.components_by_item import (
    ComponentsByItem,
)


class ThemeToItems(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        components_by_item = ComponentsByItem().update(**self.params.__dict__).run()

        mapping = {}
        for i_row in range(components_by_item.shape[0]):
            sorting_indices = components_by_item.iloc[i_row, :].sort_values(
                ascending=False
            )
            components_by_item = components_by_item[sorting_indices.index]
            mapping[i_row] = list(components_by_item.columns)

        return mapping
