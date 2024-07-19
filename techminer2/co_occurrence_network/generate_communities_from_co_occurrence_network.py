# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Communities
===============================================================================


>>> from techminer2.co_occurrence_network import generate_communities_from_co_occurrence_network
>>> generate_communities_from_co_occurrence_network(
...     #
...     # PARAMS:
...     field='author_keywords',
...     #
...     # COLUMN PARAMS:
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
                          CL_0  ...                             CL_3
0              FINTECH 31:5168  ...  ARTIFICIAL_INTELLIGENCE 02:0327
1  FINANCIAL_INCLUSION 03:0590  ...                  FINANCE 02:0309
2         CROWDFUNDING 03:0335  ...                   ROBOTS 02:0289
3      BUSINESS_MODELS 02:0759  ...                                 
4       CYBER_SECURITY 02:0342  ...                                 
5           CASE_STUDY 02:0340  ...                                 
6           BLOCKCHAIN 02:0305  ...                                 
7              REGTECH 02:0266  ...                                 
<BLANKLINE>
[8 rows x 4 columns]


"""
from .._core.nx.nx_cluster_graph import nx_cluster_graph
from .._core.nx.nx_extract_communities_to_frame import nx_extract_communities_to_frame
from ._create_co_occurrence_nx_graph import _create_co_occurrence_nx_graph


def generate_communities_from_co_occurrence_network(
    #
    # PARAMS:
    field,
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

    return nx_extract_communities_to_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
