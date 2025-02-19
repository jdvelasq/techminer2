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
...     .where_directory_is("example/")
...     .where_database_is("main")
...     .where_record_years_between(None, None)
...     .where_record_citations_between(None, None)
...     .where_records_match(None)
...     #
...     .build()
... ).head()
                           Degree  Betweenness  Closeness  PageRank
FINANCE 10:1866                17     0.329142   0.904762  0.157519
FINTECH 10:1412                16     0.210721   0.826087  0.142697
FINANCIAL_SERVICE 04:1036      11     0.056043   0.678571  0.073621
CYBER_SECURITY 02:0342          8     0.015595   0.612903  0.046725
COMMERCE 03:0846                7     0.042885   0.612903  0.049157


"""
from ....._internals.mixins import ParamsMixin
from ...co_occurrence.user.network_metrics import NetworkMetrics as UserNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        """:meta private:"""

        return (
            UserNetworkMetrics()
            .update(**self.params.__dict__)
            .with_field("organizations")
            .build()
        )
