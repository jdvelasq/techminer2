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


>>> from techminer2.analyze.co_citation_network import NetworkMetrics
>>> (
...     NetworkMetrics()
...     .set_analysis_params(
...         unit_of_analysis="cited_sources", # "cited_sources", 
...                                           # "cited_references",
...                                           # "cited_authors"
...         top_n=30, 
...         citations_threshold=None,
...         custom_terms=None,
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
... ).head()
                                Degree  Betweenness  Closeness  PageRank
ELECT COMMER RES APPL 1:32          27     0.077741   0.935484  0.047163
J MANAGE INF SYST 1:27              26     0.017028   0.906250  0.042947
MIS QUART MANAGE INF SYST 1:47      26     0.017028   0.906250  0.042947
COMMUN ACM 1:12                     25     0.070961   0.878788  0.044207
MANAGE SCI 1:30                     25     0.016051   0.878788  0.041488

"""
from ....internals.nx.internal__compute_network_metrics import (
    internal__compute_network_metrics,
)
from .internals.create_co_citation_nx_graph import _create_co_citation_nx_graph


def network_metrics(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    nx_graph = _create_co_citation_nx_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return internal__compute_network_metrics(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
    )
