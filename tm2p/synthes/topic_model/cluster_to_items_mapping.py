"""
Cluster to Terms Mapping
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
    >>> from tm2p.synthes.topic_model import ClusterToItemsMapping
    >>> mapping = (
    ...     ClusterToItemsMapping()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.CONCEPT_NORM)
    ...     .having_items_in_top(20)
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
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> import pprint
    >>> pprint.pprint(mapping)  # doctest: +NORMALIZE_WHITESPACE +ELLIPSIS
    {0: ['fintech 156:33429',
         'consumers 017:03475',
         'the development 026:05689',
         'banks 031:06740',
         'financial technology 047:08455',
         'financial services 031:07105',
         'data 026:05921',
         'technology 026:04985',
         'fintech development 015:03625',
         'banking 026:04784',
         'financial-technology 016:02809',
         'finance 050:10972',
         'innovation 033:07734',
         'china 033:06419',
         'the impact 021:04968',
         'sustainable development 018:02898',
         'financial inclusion 022:04623',
         'blockchain 017:04405',
         'the role 015:02528',
         'evidence 018:03900'],
     1: ['financial inclusion 022:04623',
         'finance 050:10972',
         'fintech 156:33429',
         'the development 026:05689',
         'technology 026:04985',
         'fintech development 015:03625',
         'china 033:06419',
         'data 026:05921',
         'financial technology 047:08455',
         'the role 015:02528',
         'consumers 017:03475',
         'sustainable development 018:02898',
         'financial services 031:07105',
         'evidence 018:03900',
         'banking 026:04784',
         'the impact 021:04968',
         'banks 031:06740',
         'blockchain 017:04405',
         'innovation 033:07734',
         'financial-technology 016:02809'],
     2: ['fintech 156:33429',
         'financial technology 047:08455',
         'financial services 031:07105',
         'financial inclusion 022:04623',
         'innovation 033:07734',
         'finance 050:10972',
         'data 026:05921',
         'blockchain 017:04405',
         'the development 026:05689',
         'financial-technology 016:02809',
         'the impact 021:04968',
         'banking 026:04784',
         'china 033:06419',
         'the role 015:02528',
         'technology 026:04985',
         'sustainable development 018:02898',
         'banks 031:06740',
         'evidence 018:03900',
         'consumers 017:03475',
         'fintech development 015:03625'],
     3: ['innovation 033:07734',
         'fintech 156:33429',
         'finance 050:10972',
         'financial technology 047:08455',
         'financial services 031:07105',
         'blockchain 017:04405',
         'technology 026:04985',
         'the development 026:05689',
         'banks 031:06740',
         'fintech development 015:03625',
         'financial-technology 016:02809',
         'banking 026:04784',
         'financial inclusion 022:04623',
         'the impact 021:04968',
         'china 033:06419',
         'data 026:05921',
         'evidence 018:03900',
         'consumers 017:03475',
         'sustainable development 018:02898',
         'the role 015:02528'],
     4: ['finance 050:10972',
         'fintech 156:33429',
         'technology 026:04985',
         'blockchain 017:04405',
         'innovation 033:07734',
         'financial technology 047:08455',
         'consumers 017:03475',
         'data 026:05921',
         'financial services 031:07105',
         'sustainable development 018:02898',
         'banks 031:06740',
         'banking 026:04784',
         'china 033:06419',
         'the role 015:02528',
         'financial inclusion 022:04623',
         'financial-technology 016:02809',
         'the impact 021:04968',
         'the development 026:05689',
         'fintech development 015:03625',
         'evidence 018:03900'],
     5: ['banking 026:04784',
         'fintech 156:33429',
         'data 026:05921',
         'the impact 021:04968',
         'financial inclusion 022:04623',
         'financial technology 047:08455',
         'blockchain 017:04405',
         'technology 026:04985',
         'financial services 031:07105',
         'the development 026:05689',
         'banks 031:06740',
         'the role 015:02528',
         'fintech development 015:03625',
         'innovation 033:07734',
         'china 033:06419',
         'consumers 017:03475',
         'finance 050:10972',
         'financial-technology 016:02809',
         'sustainable development 018:02898',
         'evidence 018:03900'],
     6: ['china 033:06419',
         'fintech 156:33429',
         'evidence 018:03900',
         'fintech development 015:03625',
         'banks 031:06740',
         'the impact 021:04968',
         'data 026:05921',
         'the development 026:05689',
         'financial-technology 016:02809',
         'financial technology 047:08455',
         'finance 050:10972',
         'sustainable development 018:02898',
         'innovation 033:07734',
         'financial inclusion 022:04623',
         'financial services 031:07105',
         'consumers 017:03475',
         'the role 015:02528',
         'banking 026:04784',
         'technology 026:04985',
         'blockchain 017:04405'],
     7: ['financial-technology 016:02809',
         'the role 015:02528',
         'fintech 156:33429',
         'financial technology 047:08455',
         'sustainable development 018:02898',
         'financial services 031:07105',
         'data 026:05921',
         'consumers 017:03475',
         'finance 050:10972',
         'evidence 018:03900',
         'financial inclusion 022:04623',
         'the impact 021:04968',
         'blockchain 017:04405',
         'banks 031:06740',
         'china 033:06419',
         'innovation 033:07734',
         'the development 026:05689',
         'fintech development 015:03625',
         'technology 026:04985',
         'banking 026:04784'],
     8: ['banks 031:06740',
         'banking 026:04784',
         'fintech 156:33429',
         'china 033:06419',
         'the role 015:02528',
         'fintech development 015:03625',
         'innovation 033:07734',
         'finance 050:10972',
         'sustainable development 018:02898',
         'financial technology 047:08455',
         'financial services 031:07105',
         'data 026:05921',
         'the impact 021:04968',
         'blockchain 017:04405',
         'technology 026:04985',
         'financial-technology 016:02809',
         'consumers 017:03475',
         'the development 026:05689',
         'financial inclusion 022:04623',
         'evidence 018:03900'],
     9: ['fintech 156:33429',
         'sustainable development 018:02898',
         'the impact 021:04968',
         'finance 050:10972',
         'innovation 033:07734',
         'fintech development 015:03625',
         'data 026:05921',
         'technology 026:04985',
         'china 033:06419',
         'the development 026:05689',
         'financial services 031:07105',
         'the role 015:02528',
         'financial inclusion 022:04623',
         'banks 031:06740',
         'consumers 017:03475',
         'financial technology 047:08455',
         'blockchain 017:04405',
         'evidence 018:03900',
         'banking 026:04784',
         'financial-technology 016:02809']}


"""

from tm2p._intern import ParamsMixin
from tm2p.synthes.topic_model.components_by_item_dataframe import (
    ComponentsByItemDataFrame,
)


class ClusterToItemsMapping(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        theme_term_matrix = (
            ComponentsByItemDataFrame().update(**self.params.__dict__).run()
        )

        mapping = {}
        for i_row in range(theme_term_matrix.shape[0]):
            sorting_indices = theme_term_matrix.iloc[i_row, :].sort_values(
                ascending=False
            )
            theme_term_matrix = theme_term_matrix[sorting_indices.index]
            if self.params.top_n is not None:
                mapping[i_row] = list(theme_term_matrix.columns[: self.params.top_n])
            else:
                mapping[i_row] = list(theme_term_matrix.columns)

        return mapping
