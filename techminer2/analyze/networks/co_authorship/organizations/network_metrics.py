"""
Metrics
===============================================================================


Smoke tests:
    >>> from techminer2.packages.networks.co_authorship.organizations import NetworkMetrics
    >>> (
    ...     NetworkMetrics()
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
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                                                        Degree  ...  PageRank
    Goethe Univ Frankfurt (DEU) 2:1065                       3  ...  0.063492
    Pennsylvania State Univ (USA) 1:0576                     3  ...  0.063492
    Singapore Manag Univ (SMU) (SGP) 1:0576                  3  ...  0.063492
    Univ of Delaware (USA) 1:0576                            3  ...  0.063492
    Columbia Grad Sch of Bus (USA) 1:0390                    3  ...  0.063492
    Univ of Chicago (USA) 1:0390                             3  ...  0.063492
    Univ of Texas at Austin (USA) 1:0390                     3  ...  0.063492
    [UKN] Stanford GSB and the Hoover Inst, United ...       3  ...  0.063492
    Univ of New South Wales (AUS) 2:0340                     2  ...  0.092660
    Fed Reserv Bank of Philadelphia (USA) 3:0317             1  ...  0.063492
    Baylor Univ (USA) 2:0395                                 1  ...  0.048908
    Univ of Sydney (AUS) 2:0300                              1  ...  0.048908
    Fed Reserv Bank of Chicago (USA) 2:0253                  1  ...  0.063492
    Hankyong Nac Univ (KOR) 1:0557                           1  ...  0.063492
    Western Illinois Univ (USA) 1:0557                       1  ...  0.063492
    <BLANKLINE>
    [15 rows x 4 columns]



    >>> (
    ...     NetworkMetrics()
    ...     #
    ...     # FIELD:
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
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/tests/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                                                        Degree  ...  PageRank
    Goethe Univ Frankfurt (DEU)                              3  ...  0.063492
    Pennsylvania State Univ (USA)                            3  ...  0.063492
    Singapore Manag Univ (SMU) (SGP)                         3  ...  0.063492
    Univ of Delaware (USA)                                   3  ...  0.063492
    Columbia Grad Sch of Bus (USA)                           3  ...  0.063492
    Univ of Chicago (USA)                                    3  ...  0.063492
    Univ of Texas at Austin (USA)                            3  ...  0.063492
    [UKN] Stanford GSB and the Hoover Inst, United ...       3  ...  0.063492
    Univ of New South Wales (AUS)                            2  ...  0.092660
    Fed Reserv Bank of Philadelphia (USA)                    1  ...  0.063492
    Baylor Univ (USA)                                        1  ...  0.048908
    Univ of Sydney (AUS)                                     1  ...  0.048908
    Fed Reserv Bank of Chicago (USA)                         1  ...  0.063492
    Hankyong Nac Univ (KOR)                                  1  ...  0.063492
    Western Illinois Univ (USA)                              1  ...  0.063492
    <BLANKLINE>
    [15 rows x 4 columns]


"""

from techminer2._internals import ParamsMixin
from techminer2.analyze.networks.co_occurrence.usr.network_metrics import (
    NetworkMetrics as UserNetworkMetrics,
)


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNetworkMetrics()
            .update(**self.params.__dict__)
            .with_field("organizations")
            .run()
        )
