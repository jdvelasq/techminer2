"""
Terms by Cluster Summary
===============================================================================


Smoke tests:
    >>> from tm2p.co_occurrence_network.user import TermsByClusterSummary
    >>> (
    ...     TermsByClusterSummary()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
       Cluster  ...                                              Terms
    0        0  ...  FINTECH; INNOVATION; FINANCIAL_SERVICES; FINAN...
    1        1  ...  FINANCE; FINANCIAL_SERVICE; BUSINESS_MODELS; B...
    2        2  ...  FINANCIAL_TECHNOLOGY; CROWDFUNDING; SUSTAINABI...
    <BLANKLINE>
    [3 rows x 4 columns]

    >>> from tm2p.co_occurrence_network.user import TermsByClusterSummary
    >>> (
    ...     TermsByClusterSummary()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
    ...     .having_items_in_top(20)
    ...     .having_items_ordered_by("OCC")
    ...     .having_item_occurrences_between(None, None)
    ...     .having_item_citations_between(None, None)
    ...     .having_items_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_clustering_algorithm_or_dict("louvain")
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("tests/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
       Cluster  ...                                              Terms
    0        0  ...  FINTECH 32:5393; INNOVATION 08:0990; FINANCIAL...
    1        1  ...  FINANCE 11:1950; FINANCIAL_SERVICE 04:1036; BU...
    2        2  ...  FINANCIAL_TECHNOLOGY 03:0461; CROWDFUNDING 03:...
    <BLANKLINE>
    [3 rows x 4 columns]



"""

from tm2p._internals import ParamsMixin
from tm2p._internals.nx import (
    internal__cluster_nx_graph,
    internal__summarize_communities,
)
from tm2p.synthes.concept_struct.co_occur._internals.create_nx_graph import (
    internal__create_nx_graph,
)


class TermsByClusterSummary(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__summarize_communities(self.params, nx_graph)

        nx_graph = internal__create_nx_graph(self.params)
        nx_graph = internal__cluster_nx_graph(self.params, nx_graph)
        return internal__summarize_communities(self.params, nx_graph)
