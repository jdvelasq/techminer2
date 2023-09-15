# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Metrics
===============================================================================


>>> from techminer2.analyze.bibliographic_coupling.documents import metrics
>>> metrics(
...     #
...     # COLUMN PARAMS:
...     top_n=20, 
...     citations_min=0,
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
                                               Degree  ...  PageRank
Becker M, 2020, INTELL SYST ACCOUNT FINANCE M      10  ...  0.148655
Kurum E, 2020, J FINANC CRIME                       9  ...  0.132326
Turki M, 2020, HELIYON                              8  ...  0.109986
Kavassalis P, 2018, J RISK FINANC                   7  ...  0.099831
Das SR, 2019, J FINANCIAL DATA SCI                  6  ...  0.069294
Gasparri G, 2019, FRONTIER ARTIF INTELL             6  ...  0.069294
Nicholls R, 2021, J ANTITRUST ENFORC                6  ...  0.080003
Muganyi T, 2022, FINANCIAL INNOV                    4  ...  0.049722
von Solms J, 2021, J BANK REGUL                     4  ...  0.049722
Anagnostopoulos I, 2018, J ECON BUS                 3  ...  0.076273
Goul M, 2019, PROC - IEEE WORLD CONGR SERV,         2  ...  0.029807
Arner DW, 2017, NORTHWEST J INTL LAW BUS            1  ...  0.032327
Butler T, 2018, J RISK MANG FINANCIAL INST          1  ...  0.032327
Ryan P, 2020, ICEIS - PROC INT CONF ENTERP          1  ...  0.020434
<BLANKLINE>
[14 rows x 4 columns]



"""
from ....nx_compute_metrics import nx_compute_metrics
from ....nx_create_bibliographic_coupling_graph import nx_create_bibliographic_coupling_graph

UNIT_OF_ANALYSIS = "article"


def metrics(
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

    return nx_compute_metrics(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
    )
