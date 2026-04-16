"""
NodeMetrics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import AssociationIndex, CollaborationUnit, Field, ItemOrderBy
    >>> from tm2p.portfolio.social_structure.collaboration_network import NodeMetrics
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # ANALYSIS UNIT:
    ...     .with_collaboration_unit(CollaborationUnit.AUTH)
    ...     #
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_minimum_pair_co_occurrence(1)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_global_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().round(3).to_string())  # doctest: +NORMALIZE_WHITESPACE
    METRIC                  DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    NODE
    Chichuan Lee 002:00717              0.105                     0.0                 0.105     0.055                   0.289         1.0            2       1.0
    Chinhsien Yu 002:00717              0.105                     0.0                 0.105     0.055                   0.289         1.0            2       1.0
    Jinsong Zhao 002:00717              0.105                     0.0                 0.105     0.055                   0.289         1.0            2       1.0
    Huaping Sun 002:00656               0.105                     0.0                 0.105     0.055                   0.289         1.0            2       1.0
    Linnan Yan 002:00656                0.105                     0.0                 0.105     0.055                   0.289         1.0            2       1.0


"""

from tm2p._intern.networks import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self):
        return create_nx_graph(self.params)
