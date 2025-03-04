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


>>> from techminer2.pkgs.networks.co_authorship.organizations import NetworkMetrics
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
... ).head()
                                                    Degree  ...  PageRank
Columbia Grad Sch of Bus (USA) 1:0390                    3  ...  0.063492
Goethe Univ Frankfurt (DEU) 2:1065                       3  ...  0.063492
Pennsylvania State Univ (USA) 1:0576                     3  ...  0.063492
Singapore Manag Univ (SMU) (SGP) 1:0576                  3  ...  0.063492
Stanford GSB and the Hoover Institution, United...       3  ...  0.063492
<BLANKLINE>
[5 rows x 4 columns]




"""
from ....._internals.mixins import ParamsMixin
from ...co_occurrence.user.network_metrics import NetworkMetrics as UserNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def run(self):
        """:meta private:"""

        return (
            UserNetworkMetrics()
            .update(**self.params.__dict__)
            .with_field("organizations")
            .run()
        )
