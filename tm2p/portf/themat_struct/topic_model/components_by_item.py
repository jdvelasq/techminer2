"""
ComponentsByItem
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
    >>> from tm2p.portfolio.thematic_stucture.topic_modeling import ComponentsByItem
    >>> df = (
    ...     ComponentsByItem()
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
    >>> df
    ITEM       fintech 157:34856  ...  the emergence 010:01933
    COMPONENT                     ...
    0                  38.575909  ...                 3.099910
    1                  18.323350  ...                 4.100031
    2                  14.623242  ...                 0.100000
    3                  10.942926  ...                 1.099976
    4                  15.809338  ...                 0.100012
    5                  15.558222  ...                 0.100000
    6                  21.047484  ...                 0.100005
    7                   4.579642  ...                 0.100022
    8                  10.610498  ...                 0.100000
    9                   7.929388  ...                 2.100044
    <BLANKLINE>
    [10 rows x 50 columns]


    >>> df = (
    ...     ComponentsByItem()
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
    ...     .where_root_directory("tests/tinyml-scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df
                 fintech  financial technology  ...  the potential  the emergence
    COMPONENT                                   ...
    0          38.575909             17.580221  ...       1.424702       3.099910
    1          18.323350              9.852608  ...       0.100004       4.100031
    2          14.623242              0.100017  ...       0.100002       0.100000
    3          10.942926              0.100011  ...       0.100010       1.099976
    4          15.809338             11.702023  ...       0.100000       0.100012
    5          15.558222              1.441787  ...       0.100010       0.100000
    6          21.047484              5.621334  ...       4.900290       0.100005
    7           4.579642              1.174907  ...       2.974984       0.100022
    8          10.610498              3.718032  ...       1.099998       0.100000
    9           7.929388              1.709060  ...       0.100000       2.100044
    <BLANKLINE>
    [10 rows x 50 columns]


"""

from tm2p._intern import ParamsMixin

from ._intern.compute_tables import compute_tables


class ComponentsByItem(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        components_by_item, _ = compute_tables(self.params)

        return components_by_item
