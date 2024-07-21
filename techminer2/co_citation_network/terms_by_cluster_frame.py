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


>>> from techminer2.co_citation_network import terms_by_cluster_frame
>>> terms_by_cluster_frame(
...     unit_of_analysis="cited_sources", # "cited_sources", 
...                                       # "cited_references",
...                                       # "cited_authors"
...     #
...     # COLUMN PARAMS:
...     top_n=None, 
...     citations_threshold=None,
...     custom_terms=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... ).head()
                                0  ...                                     9
0          J MANAGE INF SYST 1:31  ...           AGROINDUSTRIES FOR DEV 1:01
1  MIS QUART MANAGE INF SYST 1:47  ...                  DEV LEARN ORGAN 1:01
2                 INF MANAGE 1:06  ...  EURASIA J MATH SCI TECHNOL EDUC 1:01
3        INT REV FINANC ANAL 1:04  ...                   FINTECH IN GER 1:01
4                 J SERV RES 1:06  ...      INT FOOD AGRIBUS MANAGE REV 1:01
<BLANKLINE>
[5 rows x 10 columns]


"""
from .._core.nx.nx_cluster_graph import nx_cluster_graph
from .._core.nx.nx_extract_communities_to_frame import nx_extract_communities_to_frame
from ._create_co_citation_nx_graph import _create_co_citation_nx_graph


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

    nx_graph = nx_cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    return nx_extract_communities_to_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
