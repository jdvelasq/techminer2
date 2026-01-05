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
    >>> #
    >>> # TEST PREPARATION
    >>> #
    >>> from techminer2.thesaurus.descriptors import ApplyThesaurus, InitializeThesaurus
    >>> InitializeThesaurus(root_directory="examples/fintech/", quiet=True).run()
    >>> ApplyThesaurus(root_directory="examples/fintech/", quiet=True).run()


    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2.packages.networks.co_occurrence.author_keywords import NetworkMetrics
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
    >>> .head(15)  # doctest: +SKIP
                                     Degree  Betweenness  Closeness  PageRank
    FINTECH 31:5168                      18     0.701977   0.950000  0.235612
    FINANCIAL_SERVICE 04:0667             8     0.053718   0.633333  0.072599
    INNOVATION 07:0911                    7     0.033055   0.612903  0.084031
    TECHNOLOGIES 02:0310                  6     0.023308   0.593750  0.045900
    BLOCKCHAIN 03:0369                    5     0.014620   0.558824  0.048082
    FINANCIAL_INSTITUTION 02:0484         5     0.014676   0.575758  0.034275
    FINANCE 02:0309                       5     0.015316   0.575758  0.036884
    ROBOTS 02:0289                        5     0.011696   0.558824  0.037662
    REGTECH 02:0266                       5     0.013701   0.575758  0.040572
    BUSINESS_MODEL 03:0896                4     0.001949   0.558824  0.044621
    FINANCIAL_TECHNOLOGIES 03:0461        4     0.001949   0.558824  0.033433
    BANKING 02:0291                       4     0.000000   0.431818  0.034247
    MARKETPLACE_LENDING 03:0317           3     0.000000   0.527778  0.045739
    CASE_STUDIES 02:0340                  3     0.002924   0.527778  0.029823
    ARTIFICIAL_INTELLIGENCE 02:0327       3     0.000000   0.527778  0.025308




    >>> #
    >>> # CODE TESTED
    >>> #
    >>> from techminer2.packages.networks.co_occurrence.author_keywords import NetworkMetrics
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
    FINTECH                      18     0.701977   0.950000  0.235612
    FINANCIAL_SERVICE             8     0.053718   0.633333  0.072599
    INNOVATION                    7     0.033055   0.612903  0.084031
    TECHNOLOGIES                  6     0.023308   0.593750  0.045900
    BLOCKCHAIN                    5     0.014620   0.558824  0.048082
    FINANCIAL_INSTITUTION         5     0.014676   0.575758  0.034275
    FINANCE                       5     0.015316   0.575758  0.036884
    ROBOTS                        5     0.011696   0.558824  0.037662
    REGTECH                       5     0.013701   0.575758  0.040572
    BUSINESS_MODEL                4     0.001949   0.558824  0.044621
    FINANCIAL_TECHNOLOGIES        4     0.001949   0.558824  0.033433
    BANKING                       4     0.000000   0.431818  0.034247
    MARKETPLACE_LENDING           3     0.000000   0.527778  0.045739
    CASE_STUDIES                  3     0.002924   0.527778  0.029823
    ARTIFICIAL_INTELLIGENCE       3     0.000000   0.527778  0.025308





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
            .with_field("author_keywords")
            .run()
        )
