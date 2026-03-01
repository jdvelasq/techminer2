"""
Terms by Cluster Summary
===============================================================================


Smoke tests:
    >>> from tm2p.co_occurrence_network.index_keywords import TermsByClusterSummary
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
    ...     .using_item_counters(True)
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
    0        0  ...  FINANCE 10:1866; FINANCIAL_SERVICE 05:1115; CO...
    1        1  ...  INVESTMENT 02:0418; FINANCIAL_SYSTEM 02:0385; ...
    2        2  ...  FINTECH 10:1412; ELECTRONIC_MONEY 03:0305; FIN...
    3        3  ...  SURVEYS 03:0484; FINANCIAL_INDUSTRIES 02:0323;...
    <BLANKLINE>
    [4 rows x 4 columns]



"""

from tm2p._intern import ParamsMixin
from tm2p.synthes.concept_struct.co_occur.usr.terms_by_cluster_summary import (
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
            .with_source_field("index_keywords")
            .run()
        )
