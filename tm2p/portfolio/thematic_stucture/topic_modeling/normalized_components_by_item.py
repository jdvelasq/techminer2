"""
NormalizedComponentsByItem
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
    >>> from tm2p.enum import ItemOrderBy, Field
    >>> from tm2p.portfolio.thematic_stucture.topic_modeling import NormalizedComponentsByItem
    >>> df = (
    ...     NormalizedComponentsByItem()
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
    >>> df.round(3).head()
    ITEM       fintech 157:34856  ...  the emergence 010:01933
    COMPONENT                     ...
    0                      0.201  ...                    0.016
    1                      0.165  ...                    0.037
    2                      0.156  ...                    0.001
    3                      0.176  ...                    0.018
    4                      0.142  ...                    0.001
    <BLANKLINE>
    [5 rows x 50 columns]


    >>> df = (
    ...     NormalizedComponentsByItem()
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
    ...     .using_counters(False)
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
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.round(3).head()
               fintech  financial technology  ...  the potential  the emergence
    COMPONENT                                 ...
    0            0.201                 0.091  ...          0.007          0.016
    1            0.165                 0.089  ...          0.001          0.037
    2            0.156                 0.001  ...          0.001          0.001
    3            0.176                 0.002  ...          0.002          0.018
    4            0.142                 0.105  ...          0.001          0.001
    <BLANKLINE>
    [5 rows x 50 columns]

"""

from tm2p._intern import ParamsMixin

from .components_by_item import ComponentsByItem


class NormalizedComponentsByItem(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        df = ComponentsByItem().update(**self.params.__dict__).run()
        df = df.div(df.sum(axis=1), axis=0)

        return df
