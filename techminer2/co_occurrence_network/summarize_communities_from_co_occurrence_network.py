# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Communities Summary
===============================================================================


>>> from techminer2.co_occurrence_network import summarize_communities_from_co_occurrence_network
>>> summarize_communities_from_co_occurrence_network(
...     #
...     # PARAMS:
...     field='author_keywords',
...     #
...     # SUMMARY PARAMS:
...     conserve_counters=False,
...     #
...     # FILTER PARAMS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     association_index="association",
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
  Cluster  ...                                              Terms
0    CL_0  ...  FINTECH; FINANCIAL_INCLUSION; CROWDFUNDING; BU...
1    CL_1  ...  INNOVATION; FINANCIAL_SERVICES; FINANCIAL_TECH...
2    CL_2  ...  MARKETPLACE_LENDING; LENDINGCLUB; PEER_TO_PEER...
3    CL_3  ...           ARTIFICIAL_INTELLIGENCE; FINANCE; ROBOTS
<BLANKLINE>
[4 rows x 4 columns]



"""
from .._core.nx.nx_cluster_graph import nx_cluster_graph
from .._core.nx.nx_summarize_communities import nx_summarize_communities
from ._create_co_occurrence_nx_graph import _create_co_occurrence_nx_graph


def summarize_communities_from_co_occurrence_network(
    #
    # PARAMS:
    field,
    #
    # SUMMARY PARAMS:
    conserve_counters=False,
    #
    # COLUMN PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    association_index="association",
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    nx_graph = _create_co_occurrence_nx_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=field,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # NETWORK PARAMS:
        association_index=association_index,
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

    return nx_summarize_communities(
        #
        # SUMMARY PARAMS:
        nx_graph=nx_graph,
        conserve_counters=conserve_counters,
    )
