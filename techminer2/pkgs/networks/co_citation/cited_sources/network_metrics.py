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


>>> from techminer2.pkgs.networks.co_citation.cited_sources import NetworkMetrics
>>> (
...     NetworkMetrics()
...     #
...     # UNIT OF ANALYSIS:
...     .having_terms_in_top(30)
...     .having_citation_threshold(0)
...     .having_terms_in(None)
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
ELECT COMMER RES APPL 1:32          27     0.074517   0.935484  0.046446
MIS QUART MANAGE INF SYST 1:47      26     0.014924   0.906250  0.042254
COMMUN ACM 1:12                     25     0.068477   0.878788  0.043568
INF SYST RES 1:18                   25     0.012996   0.878788  0.040796
MANAGE SCI 1:30                     25     0.014031   0.878788  0.040817



"""
from ....._internals.mixins import ParamsMixin
from .._internals.network_metrics import NetworkMetrics as InternalNetworkMetrics


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        return (
            InternalNetworkMetrics()
            .update(**self.params.__dict__)
            .unit_of_analysis("cited_sources")
            .build()
        )
