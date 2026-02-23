"""
Terms by Cluster Summary
===============================================================================


Smoke tests:
    >>> from techminer2.co_occurrence_network.keywords import TermsByClusterSummary
    >>> df = (
    ...     TermsByClusterSummary()
    ...     #
    ...     # FIELD:
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
    >>> df   # doctest: +SKIP
       Cluster  ...                                              Terms
    0        0  ...  FINTECH 32:5393; FINANCE 11:1950; FINANCIAL_SE...
    1        1  ...  FINANCIAL_TECHNOLOGIES 03:0461; CROWDFUNDING 0...
    2        2  ...  FINANCIAL_INSTITUTION 04:0746; COMMERCE 03:084...
    <BLANKLINE>
    [3 rows x 4 columns]


"""

from techminer2._internals import ParamsMixin
from techminer2.analyze._networks.co_occurrence.usr.terms_by_cluster_summary import (
    TermsByClusterSummary as UserTermsByClusterSummary,
)


class TermsByClusterSummary(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserTermsByClusterSummary()
            .update(**self.params.__dict__)
            .with_field("keywords")
            .run()
        )
