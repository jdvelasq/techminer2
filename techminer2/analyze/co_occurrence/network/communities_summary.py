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


>>> from techminer2.analyze.co_occurrence.network import communities_summary
>>> communities_summary(
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
0    CL_0  ...  FINTECH; FINANCIAL_INCLUSION; CASE_STUDIES; BL...
1    CL_1  ...  INNOVATION; DIGITAL; BANKING; FINANCIAL_INSTIT...
2    CL_2  ...  FINANCIAL_SERVICES; FINANCIAL_TECHNOLOGY; BUSI...
3    CL_3  ...  SHADOW_BANKING; PEER_TO_PEER_LENDING; MARKETPL...
<BLANKLINE>
[4 rows x 4 columns]


"""
from ...._common.nx_communities_summary import nx_communities_summary
from ...._common.nx_create_co_occurrence_graph import nx_create_co_occurrence_graph


def communities_summary(
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
    """
    :meta private:
    """
    # --------------------------------------------------------------------------
    # TODO: REMOVE DEPENDENCES:
    #
    #
    # NODES:
    node_size_range = (30, 70)
    textfont_size_range = (10, 20)
    #
    # EDGES:
    edge_width_min = 0.8
    edge_width_max = 3.0
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    #
    # --------------------------------------------------------------------------

    nx_graph = nx_create_co_occurrence_graph(
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
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
        association_index=association_index,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        #
        # EDGES:
        edge_width_min=edge_width_min,
        edge_width_max=edge_width_max,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return nx_communities_summary(
        #
        # SUMMARY PARAMS:
        nx_graph=nx_graph,
        conserve_counters=conserve_counters,
    )
