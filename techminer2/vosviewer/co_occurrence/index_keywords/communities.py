# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
.. _index_keywords_communities:

Communities
===============================================================================


>>> from techminer2 import vosviewer
>>> root_dir = "data/regtech/"
>>> vosviewer.co_occurrence.index_keywords.communities(
...     root_dir=root_dir,
...     top_n=20, 
... )
                                   CL_0  ...                      CL_2
0           FINANCIAL_INSTITUTIONS 6:09  ...  INFORMATION_SYSTEMS 2:14
1            ANTI_MONEY_LAUNDERING 3:10  ...      INFORMATION_USE 2:14
2                          FINTECH 3:08  ...    SOFTWARE_SOLUTION 2:14
3                       LAUNDERING 2:09  ...                          
4                          BANKING 2:08  ...                          
5                 FINANCIAL_CRISIS 2:07  ...                          
6                  RISK_MANAGEMENT 2:05  ...                          
7                         COMMERCE 2:04  ...                          
8  CLASSIFICATION (OF_INFORMATION) 2:03  ...                          
9          ARTIFICIAL_INTELLIGENCE 2:02  ...                          
<BLANKLINE>
[10 rows x 3 columns]


"""
from ...nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ...nx_extract_communities_as_data_frame import nx_extract_communities_as_data_frame

FIELD = "index_keywords"


def communities(
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
    # LAYOUT:
    nx_k=None,
    nx_iterations=10,
    nx_random_state=0,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    #
    # TODO: REMOVE DEPENDENCES:
    color = "#7793a5"
    node_size_min = 30
    node_size_max = 70
    edge_width_min = 0.8
    edge_width_max = 3.0
    textfont_size_min = 10
    textfont_size_max = 20

    nx_graph = nx_create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=FIELD,
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
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
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

    return nx_extract_communities_as_data_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
