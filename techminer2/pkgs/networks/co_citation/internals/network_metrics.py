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


## >>> from techminer2.pkgs.co_citation_network import NetworkMetrics
## >>> (
## ...     NetworkMetrics()
## ...     #
## ...     # UNIT OF ANALYSIS:
## ...         unit_of_analysis="cited_sources", # "cited_sources", 
## ...                                           # "cited_references",
## ...                                           # "cited_authors"
## ...     .having_terms_in_top(30)
## ...     .having_citation_threshold(0)
## ...     .having_terms_in(None)
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... ).head()
                                Degree  Betweenness  Closeness  PageRank
ELECT COMMER RES APPL 1:32          27     0.077741   0.935484  0.047163
J MANAGE INF SYST 1:27              26     0.017028   0.906250  0.042947
MIS QUART MANAGE INF SYST 1:47      26     0.017028   0.906250  0.042947
COMMUN ACM 1:12                     25     0.070961   0.878788  0.044207
MANAGE SCI 1:30                     25     0.016051   0.878788  0.041488

"""
from .....internals.mixins import ParamsMixin
from .....internals.nx.compute_network_metrics import internal__compute_network_metrics
from .create_nx_graph import internal__create_nx_graph


class NetworkMetrics(
    ParamsMixin,
):
    """:meta private:"""

    def build(self):
        nx_graph = internal__create_nx_graph(self.params)
        return internal__compute_network_metrics(nx_graph=nx_graph)
