"""
NodeMetrics
===============================================================================

Smoke tests:
    >>> from tm2p.enum import Field, AssociationIndex, ItemOrderBy
    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import NodeMetrics
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(CoOccurrenceUnit.KW)
    ...     #
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by(ItemOrderBy.OCC)
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     .using_minimum_item_co_occurrence(1)
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


    >>> from tm2p.portfolio.thematic_stucture.co_occurrence.first_order_network import NodeMetrics
    >>> df = (
    ...     NodeMetrics()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .with_co_occurrence_unit(CoOccurrenceUnit.KW)
    ...     #
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

"""

from tm2p._intern.networks import BaseNodeMetrics

from ._intern.create_nx_graph import create_nx_graph


class NodeMetrics(
    BaseNodeMetrics,
):
    """:meta private:"""

    def create_nx_graph(self, params):
        return create_nx_graph(params)


# from tm2p._intern import ParamsMixin, remove_counters
# from tm2p._intern.plots.nx import compute_node_metrics

# from ._intern.create_nx_graph import create_nx_graph


# class NodeMetrics(
#     ParamsMixin,
# ):
#     """:meta private:"""

#     def run(self):
#         """:meta private:"""

#         use_counters = self.params.counters
#         self.params.counters = True
#         nx_graph = create_nx_graph(self.params)
#         df = compute_node_metrics(nx_graph=nx_graph)

#         if use_counters is False:
#             self.params.counters = False
#             names = df.index.tolist()
#             names = [remove_counters(name) for name in names]
#             df.index = names

#         return df
