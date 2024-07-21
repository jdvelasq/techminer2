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


>>> from techminer2.co_citation_network import network_metrics
>>> network_metrics(
...     unit_of_analysis="cited_sources", # "cited_sources", 
...                                       # "cited_references",
...                                       # "cited_authors"
...     #
...     # COLUMN PARAMS:
...     top_n=30, 
...     citations_threshold=None,
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                                Degree  Betweenness  Closeness  PageRank
ELECT COMMER RES APPL 1:32          26     0.055089   0.933333  0.045030
J MANAGE INF SYST 1:31              26     0.015935   0.933333  0.043009
MIS QUART MANAGE INF SYST 1:47      26     0.015935   0.933333  0.043009
INF SYST RES 1:18                   25     0.013700   0.903226  0.041529
MANAGE SCI 1:33                     25     0.015093   0.903226  0.041559


"""
from .._core.nx.nx_compute_metrics import nx_compute_metrics
from ._create_co_citation_nx_graph import _create_co_citation_nx_graph


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

    return nx_compute_metrics(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
    )
