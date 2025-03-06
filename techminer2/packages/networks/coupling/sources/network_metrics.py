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

>>> from techminer2.packages.networks.coupling.sources import NetworkMetrics
>>> (
...     NetworkMetrics()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(20)
...     .having_citation_threshold(0)
...     .having_occurrence_threshold(2)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(True)
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
Electronic Markets 2:287                              5  ...  0.231592
Journal of Economics and Business 3:422               4  ...  0.177251
Industrial Management and Data Systems 2:386          3  ...  0.111571
Symmetry 1:176                                        3  ...  0.110623
Journal of Management Information Systems 2:696       2  ...  0.135259
Sustainability (Switzerland) 2:150                    2  ...  0.106338
Journal of Innovation Management 1:226                2  ...  0.078484
Financial Management 2:161                            1  ...  0.048882
<BLANKLINE>
[8 rows x 4 columns]



>>> (
...     NetworkMetrics()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(20)
...     .having_citation_threshold(0)
...     .having_occurrence_threshold(2)
...     .having_terms_in(None)
...     #
...     # COUNTERS:
...     .using_term_counters(False)
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
Electronic Markets                              5  ...  0.231592
Journal of Economics and Business               4  ...  0.177251
Industrial Management and Data Systems          3  ...  0.111571
Symmetry                                        3  ...  0.110623
Journal of Management Information Systems       2  ...  0.135259
Sustainability (Switzerland)                    2  ...  0.106338
Journal of Innovation Management                2  ...  0.078484
Financial Management                            1  ...  0.048882
<BLANKLINE>
[8 rows x 4 columns]



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
            .unit_of_analysis("source_title")
            .run()
        )
