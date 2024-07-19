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


>>> from techminer2.science_mapping.citation.network.organizations import communities
>>> communities(
...     #
...     # COLUMN PARAMS:
...     top_n=30, 
...     citations_threshold=0,
...     occurrence_threshold=2,
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
                                               CL_0  ...                            CL_2
0       Federal Reserve Bank of Chicago (USA) 2:253  ...          Pace Univ. (USA) 2:323
1  Federal Reserve Bank of Philadelphia (USA) 3:317  ...  Sungkyunkwan Univ. (KOR) 2:307
<BLANKLINE>
[2 rows x 3 columns]


    
"""
from ..._core.nx.nx_create_citation_graph import nx_create_citation_graph
from ..._core.nx.nx_extract_communities_to_frame import nx_extract_communities_to_frame

UNIT_OF_ANALYSIS = "organizations"


def generate_communities_from_organizations_citation_network(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    occurrence_threshold=None,
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

    nx_graph = nx_create_citation_graph(
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
