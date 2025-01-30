# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Terms by Cluster Frame
===============================================================================


## >>> from techminer2.analyze.co_citation_network import terms_by_cluster_frame
## >>> terms_by_cluster_frame(
## ...     .set_analysis_params(
## ...         unit_of_analysis="cited_sources", # "cited_sources", 
## ...                                           # "cited_references",
## ...                                           # "cited_authors"
## ...         top_n=30, 
## ...         citations_threshold=None,
## ...         custom_terms=None,
## ...         algorithm_or_dict="louvain",
## ...     #
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     #
## ...     ).build()
## ... ).head()
                                0  ...                                     9
0  MIS QUART MANAGE INF SYST 1:47  ...           AGROINDUSTRIES FOR DEV 1:01
1               INF SYST RES 1:18  ...                  DEV LEARN ORGAN 1:01
2         INT J ELECT COMMER 1:09  ...  EURASIA J MATH SCI TECHNOL EDUC 1:01
3                 INF MANAGE 1:06  ...                   FINTECH IN GER 1:01
4           COMPUT HUM BEHAV 1:09  ...      INT FOOD AGRIBUS MANAGE REV 1:01
<BLANKLINE>
[5 rows x 10 columns]


"""
from ...internals.nx.internal__cluster_graph import internal__cluster_graph
from ...internals.nx.internal__extract_communities_to_frame import (
    internal__extract_communities_to_frame,
)
from .internals.create_co_citation_nx_graph import _create_co_citation_nx_graph


def terms_by_cluster_frame(
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    custom_terms=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
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

    nx_graph = internal__cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    return internal__extract_communities_to_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
