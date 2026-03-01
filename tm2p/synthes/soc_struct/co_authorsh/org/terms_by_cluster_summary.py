"""
Terms by Cluster Summary
===============================================================================


Smoke tests:
    >>> from tm2p.packages.networks.co_authorship.organizations import TermsByClusterSummary
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
       Cluster  ...                                              Terms
    0        0  ...  Goethe Univ Frankfurt (DEU) 2:1065; Pennsylvan...
    1        1  ...  Columbia Grad Sch of Bus (USA) 1:0390; Univ of...
    2        2  ...  Baylor Univ (USA) 2:0395; Univ of New South Wa...
    3        3  ...  Fed Reserv Bank of Philadelphia (USA) 3:0317; ...
    4        4  ...  Hankyong Nac Univ (KOR) 1:0557; Western Illino...
    5        5  ...                        Univ of Zurich (CHE) 3:0434
    6        6  ...  Max Planck Inst for Innovation and Competition...
    7        7  ...                             Pace Univ (USA) 2:0323
    8        8  ...                     Sungkyunkwan Univ (KOR) 2:0307
    9        9  ...                        Univ of Latvia (LVA) 2:0163
    <BLANKLINE>
    [10 rows x 4 columns]




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
            .with_source_field("organizations")
            .run()
        )
