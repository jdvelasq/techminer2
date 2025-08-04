# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Metrics
===============================================================================


Example:
    >>> from techminer2.packages.networks.coupling.organizations import NetworkMetrics
    >>> (
    ...     NetworkMetrics()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(True)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                                                        Degree  ...  PageRank
    Goethe Univ Frankfurt (DEU) 2:1065                       4  ...  0.120134
    Univ of Sydney (AUS) 2:0300                              4  ...  0.075018
    Pennsylvania State Univ (USA) 1:0576                     4  ...  0.120134
    Singapore Manag Univ (SMU) (SGP) 1:0576                  4  ...  0.120134
    Univ of Delaware (USA) 1:0576                            4  ...  0.120134
    Fed Reserv Bank of Philadelphia (USA) 3:0317             1  ...  0.111111
    Max Planck Inst for Innovation and Competition ...       1  ...  0.111111
    Sungkyunkwan Univ (KOR) 2:0307                           1  ...  0.111111
    Fed Reserv Bank of Chicago (USA) 2:0253                  1  ...  0.111111
    <BLANKLINE>
    [9 rows x 4 columns]



    >>> from techminer2.packages.networks.coupling.organizations import NetworkMetrics
    >>> (
    ...     NetworkMetrics()
    ...     #
    ...     # UNIT OF ANALYSIS:
    ...     .having_terms_in_top(20)
    ...     .having_terms_ordered_by("OCC")
    ...     .having_citation_threshold(0)
    ...     .having_occurrence_threshold(2)
    ...     .having_terms_in(None)
    ...     #
    ...     # COUNTERS:
    ...     .using_term_counters(False)
    ...     #
    ...     # DATABASE:
    ...     .where_root_directory_is("examples/fintech/")
    ...     .where_database_is("main")
    ...     .where_record_years_range_is(None, None)
    ...     .where_record_citations_range_is(None, None)
    ...     .where_records_match(None)
    ...     #
    ...     .run()
    ... ).head(15)
                                                        Degree  ...  PageRank
    Goethe Univ Frankfurt (DEU)                              4  ...  0.120134
    Univ of Sydney (AUS)                                     4  ...  0.075018
    Pennsylvania State Univ (USA)                            4  ...  0.120134
    Singapore Manag Univ (SMU) (SGP)                         4  ...  0.120134
    Univ of Delaware (USA)                                   4  ...  0.120134
    Fed Reserv Bank of Philadelphia (USA)                    1  ...  0.111111
    Max Planck Inst for Innovation and Competition ...       1  ...  0.111111
    Sungkyunkwan Univ (KOR)                                  1  ...  0.111111
    Fed Reserv Bank of Chicago (USA)                         1  ...  0.111111
    <BLANKLINE>
    [9 rows x 4 columns]





"""
from ....._internals.mixins import ParamsMixin
from .._internals.from_others.network_metrics import InternalNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        return (
            InternalNetworkMetrics()
            .update(**self.params.__dict__)
            .unit_of_analysis("organizations")
            .run()
        )
