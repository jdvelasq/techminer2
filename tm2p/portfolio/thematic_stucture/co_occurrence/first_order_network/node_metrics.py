"""
NodeMetrics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, AssociationIndex, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import NodeMetrics
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_co_occurrence_threshold(1)
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
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
                                       DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    sustainable development 005:00604           0.368421                0.015984              0.612903  0.072935                0.188111    0.571429            5  0.219061
    economic growth 005:00660                   0.315789                0.005750              0.593750  0.067878                0.169307    0.733333            5  0.201535
    innovation 009:01703                        0.368421                0.018519              0.612903  0.062300                0.177346    0.523810            5  0.176421
    technology 007:01409                        0.421053                0.019688              0.633333  0.058452                0.220966    0.571429            5  0.165730
    banking 010:02599                           0.526316                0.043275              0.678571  0.056300                0.259523    0.466667            5  0.155370


    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import NodeMetrics
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # FIELD:
    ...     .with_source_field(Field.AUTHKW_NORM)
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index(AssociationIndex.ASSOCIATION_STRENGTH)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/scopus/")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> print(df.head().to_string())  # doctest: +NORMALIZE_WHITESPACE
                             DEGREE_CENTRALITY  BETWEENNESS_CENTRALITY  CLOSENESS_CENTRALITY  PAGERANK  EIGENVECTOR_CENTRALITY  CLUSTERING  CORE_NUMBER  STRENGTH
    sustainable development           0.368421                0.015984              0.612903  0.072935                0.188111    0.571429            5  0.219061
    economic growth                   0.315789                0.005750              0.593750  0.067878                0.169307    0.733333            5  0.201535
    innovation                        0.368421                0.018519              0.612903  0.062300                0.177346    0.523810            5  0.176421
    technology                        0.421053                0.019688              0.633333  0.058452                0.220966    0.571429            5  0.165730
    banking                           0.526316                0.043275              0.678571  0.056300                0.259523    0.466667            5  0.155370

"""

from tm2p._intern import ParamsMixin, remove_counters
from tm2p._intern.nx import compute_node_metrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        use_counters = self.params.counters
        self.params.counters = True
        nx_graph = create_nx_graph(self.params)
        df = compute_node_metrics(nx_graph=nx_graph)

        if use_counters is False:
            self.params.counters = False
            names = df.index.tolist()
            names = [remove_counters(name) for name in names]
            df.index = names

        return df
