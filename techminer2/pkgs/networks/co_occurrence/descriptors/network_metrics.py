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


>>> from techminer2.pkgs.networks.co_occurrence.descriptors import NetworkMetrics
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
FINTECH 46:7183                              19  ...  0.126764
FINANCE 21:3481                              19  ...  0.067794
INNOVATION 16:2845                           19  ...  0.062823
TECHNOLOGIES 15:1810                         19  ...  0.067053
FINANCIAL_SERVICE 12:2100                    19  ...  0.057449
BANKS 09:1133                                19  ...  0.046195
REGULATORS 08:0974                           19  ...  0.042814
FINANCIAL_TECHNOLOGIES 18:2455               18  ...  0.073041
THIS_STUDY 14:1737                           18  ...  0.057493
THE_AUTHOR 07:0828                           18  ...  0.041990
THIS_PAPER 14:2240                           17  ...  0.058869
THE_DEVELOPMENT 08:1173                      17  ...  0.040103
BANKING 07:0851                              17  ...  0.040151
INVESTMENT 06:1294                           17  ...  0.033589
THE_FINANCIAL_SERVICES_INDUSTRY 06:1237      17  ...  0.037560
<BLANKLINE>
[15 rows x 4 columns]



>>> from techminer2.pkgs.networks.co_occurrence.descriptors import NetworkMetrics
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
FINTECH                              19     0.010451   1.000000  0.126764
FINANCE                              19     0.010451   1.000000  0.067794
INNOVATION                           19     0.010451   1.000000  0.062823
TECHNOLOGIES                         19     0.010451   1.000000  0.067053
FINANCIAL_SERVICE                    19     0.010451   1.000000  0.057449
BANKS                                19     0.010451   1.000000  0.046195
REGULATORS                           19     0.010451   1.000000  0.042814
FINANCIAL_TECHNOLOGIES               18     0.006774   0.950000  0.073041
THIS_STUDY                           18     0.004798   0.950000  0.057493
THE_AUTHOR                           18     0.004798   0.950000  0.041990
THIS_PAPER                           17     0.001121   0.904762  0.058869
THE_DEVELOPMENT                      17     0.004043   0.904762  0.040103
BANKING                              17     0.005369   0.904762  0.040151
INVESTMENT                           17     0.001121   0.904762  0.033589
THE_FINANCIAL_SERVICES_INDUSTRY      17     0.001121   0.904762  0.037560




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
