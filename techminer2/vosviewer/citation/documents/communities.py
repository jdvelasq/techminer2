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
>>> vosviewer.citation.documents.communities(
...     root_dir=root_dir,
...     top_n=20, 
... )
                                                 CL_0  ...                                               CL_4
0   Becker M, 2020, INTELL SYST ACCOUNT FINANCE M,...  ...                         Turki M, 2020, HELIYON, V6
1   Chirulli P, 2021, ROUTLEDGE HANDBFINANCIAL TEC...  ...         von Solms J, 2021, J BANK REGUL, V22, P152
2         Gasparri G, 2019, FRONTIER ARTIF INTELL, V2  ...     Ghanem S, 2021, STUD COMPUT INTELL, V954, P139
3   Firmansyah B, 2022, INT CONF INF TECHNOL SYST ...  ...  Turki M, 2021, ADV INTELL SYS COMPUT, V1141, P349
4   Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43...  ...                Teichmann F, 2023, TECHNOL SOC, V72
5   Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219  ...                                                   
6                       Kurum E, 2020, J FINANC CRIME  ...                                                   
7      Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135  ...                                                   
8           Siering M, 2022, DECIS SUPPORT SYST, V158  ...                                                   
9                      Gu M, 2022, J CORP FINANC, V76  ...                                                   
10  Kristanto AD, 2022, INT CONF INF TECHNOL SYST ...  ...                                                   
<BLANKLINE>
[11 rows x 5 columns]


"""
from ....nx_create_citation_graph import nx_create_citation_graph
from ....nx_extract_communities_as_data_frame import nx_extract_communities_as_data_frame

UNIT_OF_ANALYSIS = "article"


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
