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
                                             Degree  ...  PageRank
    FINTECH 44:6942                              19  ...  0.137168
    FINANCE 21:3481                              19  ...  0.078102
    TECHNOLOGIES 15:1810                         19  ...  0.071642
    FINANCIAL_SERVICE 12:2100                    19  ...  0.065198
    INNOVATION 15:2741                           18  ...  0.065477
    FINANCIAL_TECHNOLOGIES 14:2005               18  ...  0.066703
    REGULATORS 08:0974                           18  ...  0.050151
    BANKS 09:1133                                17  ...  0.048698
    DATA 07:1086                                 17  ...  0.035346
    BUSINESS_MODEL 05:1578                       17  ...  0.034291
    THE_DEVELOPMENT 08:1173                      16  ...  0.042315
    SERVICES 07:1226                             16  ...  0.042786
    BANKING 07:0851                              16  ...  0.042321
    INVESTMENT 06:1294                           16  ...  0.037517
    THE_FINANCIAL_SERVICES_INDUSTRY 06:1237      16  ...  0.042754
    <BLANKLINE>
    [15 rows x 4 columns]


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
    FINTECH                              19     0.016624   1.000000  0.137168
    FINANCE                              19     0.016624   1.000000  0.078102
    TECHNOLOGIES                         19     0.016624   1.000000  0.071642
    FINANCIAL_SERVICE                    19     0.016624   1.000000  0.065198
    INNOVATION                           18     0.014480   0.950000  0.065477
    FINANCIAL_TECHNOLOGIES               18     0.011683   0.950000  0.066703
    REGULATORS                           18     0.011300   0.950000  0.050151
    BANKS                                17     0.007195   0.904762  0.048698
    DATA                                 17     0.013603   0.904762  0.035346
    BUSINESS_MODEL                       17     0.008278   0.904762  0.034291
    THE_DEVELOPMENT                      16     0.007951   0.863636  0.042315
    SERVICES                             16     0.003987   0.863636  0.042786
    BANKING                              16     0.006415   0.863636  0.042321
    INVESTMENT                           16     0.003987   0.863636  0.037517
    THE_FINANCIAL_SERVICES_INDUSTRY      16     0.003987   0.863636  0.042754




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
