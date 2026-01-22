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
    >>> from techminer2.co_occurrence_network.keywords import NetworkMetrics
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
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(15)  # doctest: +SKIP
                                           Degree  Betweenness  Closeness  PageRank
    FINTECH 32:5393                            17     0.297229   0.904762  0.176778
    FINANCE 11:1950                            15     0.146589   0.826087  0.106299
    FINANCIAL_SERVICE 08:1680                  12     0.058925   0.730769  0.090850
    COMMERCE 03:0846                           12     0.069688   0.730769  0.056386
    FINANCIAL_INSTITUTION 04:0746               9     0.026023   0.655172  0.044484
    INNOVATION 08:0990                          8     0.016138   0.633333  0.067003
    FINANCIAL_SERVICES_INDUSTRIES 03:0949       8     0.007073   0.633333  0.040259
    FINANCIAL_TECHNOLOGIES 03:0461              8     0.038012   0.633333  0.039879
    BUSINESS_MODEL 04:1472                      7     0.003272   0.612903  0.043398
    BLOCKCHAIN 04:0945                          7     0.004386   0.612903  0.037191
    CROWDFUNDING 03:0335                        6     0.009552   0.593750  0.032085
    SUSTAINABILITY 03:0227                      6     0.009607   0.558824  0.038928
    SUSTAINABLE_DEVELOPMENT 03:0227             6     0.009607   0.558824  0.038928
    FINANCIAL_INCLUSION 03:0590                 5     0.000000   0.575758  0.034408
    ELECTRONIC_MONEY 03:0305                    5     0.000000   0.575758  0.026567


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
    ...     .where_root_directory("examples/fintech/")
    ...     .where_database("main")
    ...     .where_record_years_range(None, None)
    ...     .where_record_citations_range(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(15)  # doctest: +SKIP
                                   Degree  Betweenness  Closeness  PageRank
    FINTECH                            17     0.297229   0.904762  0.176778
    FINANCE                            15     0.146589   0.826087  0.106299
    FINANCIAL_SERVICE                  12     0.058925   0.730769  0.090850
    COMMERCE                           12     0.069688   0.730769  0.056386
    FINANCIAL_INSTITUTION               9     0.026023   0.655172  0.044484
    INNOVATION                          8     0.016138   0.633333  0.067003
    FINANCIAL_SERVICES_INDUSTRIES       8     0.007073   0.633333  0.040259
    FINANCIAL_TECHNOLOGIES              8     0.038012   0.633333  0.039879
    BUSINESS_MODEL                      7     0.003272   0.612903  0.043398
    BLOCKCHAIN                          7     0.004386   0.612903  0.037191
    CROWDFUNDING                        6     0.009552   0.593750  0.032085
    SUSTAINABILITY                      6     0.009607   0.558824  0.038928
    SUSTAINABLE_DEVELOPMENT             6     0.009607   0.558824  0.038928
    FINANCIAL_INCLUSION                 5     0.000000   0.575758  0.034408
    ELECTRONIC_MONEY                    5     0.000000   0.575758  0.026567




"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.networks.co_occurrence.usr.network_metrics import (
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
            .with_field("keywords")
            .run()
        )
