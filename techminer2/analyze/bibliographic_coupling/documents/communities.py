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


>>> from techminer2.analyze.bibliographic_coupling.documents import communities
>>> communities(
...     #
...     # COLUMN PARAMS:
...     top_n=30, 
...     citations_min=None,
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
                                             CL_0  ...                                  CL_4
0                  Grassi L, 2022, J IND BUS ECON  ...         Singh C, 2022, J FINANC CRIME
1   Becker M, 2020, INTELL SYST ACCOUNT FINANCE M  ...  Singh C, 2020, J MONEY LAUND CONTROL
2     Goul M, 2019, PROC - IEEE WORLD CONGR SERV,  ...                                      
3                   Kurum E, 2020, J FINANC CRIME  ...                                      
4                Muganyi T, 2022, FINANCIAL INNOV  ...                                      
5            Muzammil M, 2020, CEUR WORKSHOP PROC  ...                                      
6       Nasir F, 2019, J ADV RES DYN CONTROL SYST  ...                                      
7             Siering M, 2022, DECIS SUPPORT SYST  ...                                      
8                          Turki M, 2020, HELIYON  ...                                      
9                 von Solms J, 2021, J BANK REGUL  ...                                      
10                 Buckley RP, 2020, J BANK REGUL  ...                                      
11                 Waye V, 2020, ADELAIDE LAW REV  ...                                      
<BLANKLINE>
[12 rows x 5 columns]



"""
from ....nx_create_bibliographic_coupling_graph import nx_create_bibliographic_coupling_graph
from ....nx_extract_communities_as_data_frame import nx_extract_communities_as_data_frame

UNIT_OF_ANALYSIS = "article"


def communities(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_min=0,
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
    # TODO: REMOVE DEPENDENCES:
    #
    # NODES:
    node_size_min = 30
    node_size_max = 70
    textfont_size_min = 10
    textfont_size_max = 20
    textfont_opacity_min = 0.35
    textfont_opacity_max = 1.00
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

    nx_graph = nx_create_bibliographic_coupling_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=UNIT_OF_ANALYSIS,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_min=citations_min,
        documents_min=None,
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
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        textfont_opacity_min=textfont_opacity_min,
        textfont_opacity_max=textfont_opacity_max,
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
