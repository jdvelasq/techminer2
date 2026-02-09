# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Metrics
===============================================================================


Example:
    >>> from techminer2.co_occurrence_network.descriptors import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(15) # doctest: +SKIP
                                             Degree  ...  PageRank
    FINTECH 38:6131                              19  ...  0.149865
    REGULATORS 08:0974                           18  ...  0.062888
    THE_DEVELOPMENT 09:1293                      16  ...  0.059116
    PRACTITIONER 06:1194                         16  ...  0.041293
    TECHNOLOGIES 15:1633                         15  ...  0.080583
    FINANCIAL_TECHNOLOGIES 12:1615               15  ...  0.070783
    INNOVATION 08:1816                           15  ...  0.047284
    FINANCE 10:1188                              14  ...  0.043346
    BANKS 08:1049                                14  ...  0.048601
    DATA 07:1086                                 14  ...  0.035925
    SERVICES 06:1089                             14  ...  0.041161
    CONSUMERS 07:0925                            13  ...  0.040264
    THE_FINANCIAL_SERVICES_INDUSTRY 06:1237      13  ...  0.046934
    FINANCIAL_SERVICES 06:1116                   13  ...  0.043357
    FINTECH_COMPANIES 05:1072                    13  ...  0.031250
    <BLANKLINE>
    [15 rows x 4 columns]



Example:
    >>> from techminer2.co_occurrence_network.descriptors import NetworkMetrics
    >>> df = (
    ...     NetworkMetrics()
    ...     #
    ...     # FIELD:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_term_occurrences_between(None, None)
    ...     .having_term_citations_between(None, None)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
    ...     #
    ...     # NETWORK:
    ...     .using_association_index("association")
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory("examples/small/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(15) # doctest: +SKIP
                                     Degree  Betweenness  Closeness  PageRank
    FINTECH                              19     0.040223   1.000000  0.149865
    REGULATORS                           18     0.036134   0.950000  0.062888
    THE_DEVELOPMENT                      16     0.024057   0.863636  0.059116
    PRACTITIONER                         16     0.024195   0.863636  0.041293
    TECHNOLOGIES                         15     0.014720   0.826087  0.080583
    FINANCIAL_TECHNOLOGIES               15     0.017453   0.826087  0.070783
    INNOVATION                           15     0.015292   0.826087  0.047284
    FINANCE                              14     0.018000   0.791667  0.043346
    BANKS                                14     0.010319   0.791667  0.048601
    DATA                                 14     0.017852   0.791667  0.035925
    SERVICES                             14     0.010865   0.791667  0.041161
    CONSUMERS                            13     0.010131   0.760000  0.040264
    THE_FINANCIAL_SERVICES_INDUSTRY      13     0.006532   0.760000  0.046934
    FINANCIAL_SERVICES                   13     0.008387   0.760000  0.043357
    FINTECH_COMPANIES                    13     0.017973   0.760000  0.031250




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
            .with_field("descriptors")
            .run()
        )
