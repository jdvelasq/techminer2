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


>>> from techminer2 import vosviewer
>>> root_dir = "data/regtech/"
>>> vosviewer.citation.organizations.communities(
...     root_dir=root_dir,
...     top_n=20, 
... )
                                       CL_0                                               CL_1
0                          Ahlia Univ (BHR)                             Dublin City Univ (IRL)
1                    Kingston Bus Sch (GBR)  Harvard Univ Weatherhead ctr for International...
2                  European Central B (DEU)         KS Strategic, London, United Kingdom (GBR)
3                   Politec di Milano (ITA)          Panepistemio Aigaiou, Chios, Greece (GRC)
4                 Heinrich-Heine-Univ (DEU)                                   Sch of Eng (CHE)
5  UNSW Sydney, Kensington, Australia (AUS)                               Univ Coll Cork (IRL)
6                   Univ of Hong Kong (HKG)                                                   
7                  Univ of Luxembourg (LUX)                                                   
8                      Univ of Zurich (CHE)                                                   



"""
from ...nx_create_citation_graph import nx_create_citation_graph
from ...nx_extract_communities_as_data_frame import nx_extract_communities_as_data_frame

UNIT_OF_ANALYSIS = "organizations"


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
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    # --------------------------------------------------------------------------
    # TODO: REMOVE DEPENDENCES:
    #
    # NODES:
    node_size = 30
    textfont_size = 10
    textfont_opacity = 0.35
    #
    # EDGES:
    edge_color = "#7793a5"
    edge_width_min = 0.8
    edge_width_max = 3.0
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
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # NETWORK CLUSTERING:
        association_index=association_index,
        algorithm_or_dict=algorithm_or_dict,
        #
        # LAYOUT:
        nx_k=nx_k,
        nx_iterations=nx_iterations,
        nx_random_state=nx_random_state,
        #
        # NODES:
        node_size=node_size,
        textfont_size=textfont_size,
        textfont_opacity=textfont_opacity,
        #
        # EDGES:
        edge_color=edge_color,
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