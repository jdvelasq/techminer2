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
    >>> from techminer2.packages.networks.co_occurrence.index_keywords import NetworkMetrics
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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(15)  # doctest: +SKIP
                                           Degree  Betweenness  Closeness  PageRank
    FINANCE 10:1866                            17     0.293665   0.904762  0.158323
    FINTECH 10:1412                            16     0.239669   0.863636  0.145196
    FINANCIAL_SERVICE 05:1115                  11     0.057505   0.678571  0.074187
    CYBER_SECURITY 02:0342                      9     0.028947   0.655172  0.052388
    COMMERCE 03:0846                            7     0.031384   0.612903  0.047843
    SURVEYS 03:0484                             6     0.000000   0.575758  0.050608
    ELECTRONIC_MONEY 03:0305                    6     0.009259   0.575758  0.037268
    BLOCKCHAIN 02:0736                          6     0.019006   0.575758  0.033923
    INVESTMENT 02:0418                          6     0.069103   0.593750  0.036107
    DESIGN_METHODOLOGY_APPROACH 02:0329         6     0.004094   0.593750  0.045469
    SALES 02:0329                               6     0.004094   0.593750  0.045469
    FINANCIAL_INDUSTRIES 02:0323                6     0.000000   0.575758  0.046643
    SECURITY_AND_PRIVACY 02:0323                6     0.000000   0.575758  0.046643
    PERCEIVED_USEFULNESS 02:0346                5     0.003899   0.558824  0.028316
    FINANCIAL_SERVICES_INDUSTRIES 02:0696       4     0.000000   0.542857  0.032397



    >>> from techminer2.packages.networks.co_occurrence.index_keywords import NetworkMetrics
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
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... )
    >>> df.head(15)  # doctest: +SKIP
                                   Degree  Betweenness  Closeness  PageRank
    FINANCE                            17     0.293665   0.904762  0.158323
    FINTECH                            16     0.239669   0.863636  0.145196
    FINANCIAL_SERVICE                  11     0.057505   0.678571  0.074187
    CYBER_SECURITY                      9     0.028947   0.655172  0.052388
    COMMERCE                            7     0.031384   0.612903  0.047843
    SURVEYS                             6     0.000000   0.575758  0.050608
    ELECTRONIC_MONEY                    6     0.009259   0.575758  0.037268
    BLOCKCHAIN                          6     0.019006   0.575758  0.033923
    INVESTMENT                          6     0.069103   0.593750  0.036107
    DESIGN_METHODOLOGY_APPROACH         6     0.004094   0.593750  0.045469
    SALES                               6     0.004094   0.593750  0.045469
    FINANCIAL_INDUSTRIES                6     0.000000   0.575758  0.046643
    SECURITY_AND_PRIVACY                6     0.000000   0.575758  0.046643
    PERCEIVED_USEFULNESS                5     0.003899   0.558824  0.028316
    FINANCIAL_SERVICES_INDUSTRIES       4     0.000000   0.542857  0.032397



"""
from techminer2._internals.mixins import ParamsMixin
from techminer2.packages.networks.co_occurrence.user.network_metrics import (
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
            .with_field("index_keywords")
            .run()
        )
