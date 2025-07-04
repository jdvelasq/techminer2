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
    >>> from techminer2.packages.networks.co_occurrence.user import NetworkMetrics
    >>> (
    ...     NetworkMetrics()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
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
    FINTECH 32:5393                            16     0.305878   0.863636  0.172069
    FINANCE 11:1950                            15     0.168525   0.826087  0.115158
    COMMERCE 03:0846                           11     0.071313   0.703704  0.057044
    FINANCIAL_SERVICE 04:1036                  10     0.040499   0.678571  0.062022
    FINANCIAL_SERVICES 05:0746                  9     0.029890   0.655172  0.061755
    INNOVATION 08:0990                          8     0.018751   0.633333  0.072217
    FINANCIAL_INSTITUTION 03:0488               8     0.021815   0.633333  0.040117
    BUSINESS_MODELS 03:1335                     7     0.009380   0.612903  0.036324
    BLOCKCHAIN 03:0881                          7     0.008767   0.612903  0.036903
    FINANCIAL_TECHNOLOGY 03:0461                6     0.025412   0.575758  0.035056
    CROWDFUNDING 03:0335                        6     0.009640   0.593750  0.034090
    ELECTRONIC_MONEY 03:0305                    6     0.000975   0.593750  0.031891
    SUSTAINABILITY 03:0227                      6     0.013051   0.558824  0.041226
    SUSTAINABLE_DEVELOPMENT 03:0227             6     0.013051   0.558824  0.041226
    FINANCIAL_SERVICES_INDUSTRIES 02:0696       5     0.000000   0.513514  0.032790




    >>> from techminer2.packages.networks.co_occurrence.user import NetworkMetrics
    >>> (
    ...     NetworkMetrics()
    ...     #
    ...     # FIELD:
    ...     .with_field("raw_keywords")
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
    FINTECH                            16     0.305878   0.863636  0.172069
    FINANCE                            15     0.168525   0.826087  0.115158
    COMMERCE                           11     0.071313   0.703704  0.057044
    FINANCIAL_SERVICE                  10     0.040499   0.678571  0.062022
    FINANCIAL_SERVICES                  9     0.029890   0.655172  0.061755
    INNOVATION                          8     0.018751   0.633333  0.072217
    FINANCIAL_INSTITUTION               8     0.021815   0.633333  0.040117
    BUSINESS_MODELS                     7     0.009380   0.612903  0.036324
    BLOCKCHAIN                          7     0.008767   0.612903  0.036903
    FINANCIAL_TECHNOLOGY                6     0.025412   0.575758  0.035056
    CROWDFUNDING                        6     0.009640   0.593750  0.034090
    ELECTRONIC_MONEY                    6     0.000975   0.593750  0.031891
    SUSTAINABILITY                      6     0.013051   0.558824  0.041226
    SUSTAINABLE_DEVELOPMENT             6     0.013051   0.558824  0.041226
    FINANCIAL_SERVICES_INDUSTRIES       5     0.000000   0.513514  0.032790



"""
from ....._internals.mixins import ParamsMixin
from ....._internals.nx import internal__compute_network_metrics
from .._internals.create_nx_graph import internal__create_nx_graph


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        nx_graph = internal__create_nx_graph(self.params)
        return internal__compute_network_metrics(params=self.params, nx_graph=nx_graph)
