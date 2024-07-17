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


>>> from techminer2.science_mapping.bibliographic_coupling.sources import communities
>>> communities(
...     #
...     # COLUMN PARAMS:
...     top_n=20, 
...     citations_threshold=0,
...     occurrence_threshold=1,
...     custom_items=None,
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
                      CL_0  ...                       CL_3
0        Bus. Horiz. 1:557  ...  Ind Manage Data Sys 2:386
1      J. Bus. Econ. 1:489  ...             Symmetry 1:176
2   Small Bus. Econ. 1:258  ...                           
3  J Manage Inf Syst 2:696  ...                           
4   Financial Innov. 2:190  ...                           
<BLANKLINE>
[5 rows x 4 columns]








"""
from ....core.nx.nx_create_coupling_graph import nx_create_coupling_graph
from ....core.nx.nx_extract_communities_to_frame import nx_extract_communities_to_frame

UNIT_OF_ANALYSIS = "abbr_source_title"


def generate_communities_from_sources_coupling_network(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    occurrence_threshold=2,
    custom_items=None,
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
    """
    :meta private:
    """
    # --------------------------------------------------------------------------
    # NODES:
    node_size_range = (30, 70)
    textfont_size_range = (10, 20)
    textfont_opacity_range = (0.35, 1.00)
    #
    # EDGES:
    edge_color = "#7793a5"
    edge_width_range = (0.8, 3.0)
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    #
    # --------------------------------------------------------------------------

    nx_graph = nx_create_coupling_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=UNIT_OF_ANALYSIS,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_items=custom_items,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        textfont_opacity_range=textfont_opacity_range,
        #
        # EDGES:
        edge_color=edge_color,
        edge_width_range=edge_width_range,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return nx_extract_communities_to_frame(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        conserve_counters=True,
    )
