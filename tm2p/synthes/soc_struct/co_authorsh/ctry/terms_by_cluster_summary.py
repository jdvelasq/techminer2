"""
Terms by Cluster Summary
===============================================================================


Smoke tests:
    >>> from tm2p.packages.networks.co_authorship.countries import TermsByClusterSummary
    >>> (
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
       Cluster  ...                                              Terms
    0        0  ...  United States 16:3189; China 08:1085; South Ko...
    1        1  ...  Germany 07:1814; Netherlands 03:0300; Denmark ...
    2        2  ...  Australia 05:0783; United Kingdom 03:0636; Hon...
    3        3  ...                                Switzerland 04:0660
    4        4  ...                                     Latvia 02:0163
    5        5  ...                                      Spain 01:0225
    6        6  ...                                  Indonesia 01:0102
    7        7  ...                                   Slovenia 01:0102
    8        8  ...                          Brunei Darussalam 01:0090
    <BLANKLINE>
    [9 rows x 4 columns]




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
            .with_source_field("countries")
            .run()
        )
