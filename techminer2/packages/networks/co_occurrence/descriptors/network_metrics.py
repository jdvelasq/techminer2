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
    >>> from techminer2.packages.networks.co_occurrence.descriptors import NetworkMetrics
    >>> (
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
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                                    Degree  Betweenness  Closeness  PageRank
    FINTECH 44:6942                     19     0.011241   1.000000  0.133687
    FINANCE 21:3481                     19     0.011241   1.000000  0.075377
    TECHNOLOGIES 17:1943                19     0.011241   1.000000  0.073365
    FINANCIAL_SERVICE 12:2100           19     0.011241   1.000000  0.063524
    REGULATORS 08:0974                  19     0.011241   1.000000  0.050305
    INNOVATION 15:2741                  18     0.009759   0.950000  0.063445
    FINANCIAL_TECHNOLOGIES 14:2005      18     0.007445   0.950000  0.065707
    BANKS 09:1133                       18     0.006604   0.950000  0.047331
    PRACTITIONER 06:1194                18     0.006604   0.950000  0.034435
    THE_DEVELOPMENT 09:1293             17     0.008148   0.904762  0.046894
    DATA 07:1086                        17     0.009528   0.904762  0.033658
    BANKING 07:0851                     17     0.006714   0.904762  0.041254
    BUSINESS_MODEL 05:1578              17     0.004242   0.904762  0.034400
    SERVICES 07:1226                    16     0.001096   0.863636  0.040660
    CONSUMERS 07:0925                   16     0.003093   0.863636  0.033560



Example:
    >>> from techminer2.packages.networks.co_occurrence.descriptors import NetworkMetrics
    >>> (
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
    ...     .where_root_directory_is("example/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                            Degree  Betweenness  Closeness  PageRank
    FINTECH                     19     0.011241   1.000000  0.133687
    FINANCE                     19     0.011241   1.000000  0.075377
    TECHNOLOGIES                19     0.011241   1.000000  0.073365
    FINANCIAL_SERVICE           19     0.011241   1.000000  0.063524
    REGULATORS                  19     0.011241   1.000000  0.050305
    INNOVATION                  18     0.009759   0.950000  0.063445
    FINANCIAL_TECHNOLOGIES      18     0.007445   0.950000  0.065707
    BANKS                       18     0.006604   0.950000  0.047331
    PRACTITIONER                18     0.006604   0.950000  0.034435
    THE_DEVELOPMENT             17     0.008148   0.904762  0.046894
    DATA                        17     0.009528   0.904762  0.033658
    BANKING                     17     0.006714   0.904762  0.041254
    BUSINESS_MODEL              17     0.004242   0.904762  0.034400
    SERVICES                    16     0.001096   0.863636  0.040660
    CONSUMERS                   16     0.003093   0.863636  0.033560





"""
from ....._internals.mixins import ParamsMixin
from ..user.network_metrics import NetworkMetrics as UserNetworkMetrics


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
