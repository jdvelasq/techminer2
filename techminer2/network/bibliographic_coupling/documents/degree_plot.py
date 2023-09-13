# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Degree Plot
===============================================================================


>>> from techminer2.bibliographic_coupling.documents import degree_plot
>>> plot = degree_plot(
...     #
...     # COLUMN PARAMS:
...     top_n=20, 
...     citations_min=0,
...     documents_min=2,
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     #
...     # DEGREE PLOT:
...     textfont_size=10,
...     marker_size=7,
...     line_color="black",
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> plot.fig_.write_html("sphinx/_static/bibliographic_coupling/documents/degree_plot.html")

.. raw:: html

    <iframe src="../../../../../_static/bibliographic_coupling/documents/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> plot.df_.head()
   Node                                           Name  Degree
0     0  Becker M, 2020, INTELL SYST ACCOUNT FINANCE M      10
1     1                  Kurum E, 2020, J FINANC CRIME       9
2     2                         Turki M, 2020, HELIYON       8
3     3              Kavassalis P, 2018, J RISK FINANC       7
4     4             Das SR, 2019, J FINANCIAL DATA SCI       6


>>> print(plot.prompt_)                                         
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                          |   Degree |
|---:|-------:|:----------------------------------------------|---------:|
|  0 |      0 | Becker M, 2020, INTELL SYST ACCOUNT FINANCE M |       10 |
|  1 |      1 | Kurum E, 2020, J FINANC CRIME                 |        9 |
|  2 |      2 | Turki M, 2020, HELIYON                        |        8 |
|  3 |      3 | Kavassalis P, 2018, J RISK FINANC             |        7 |
|  4 |      4 | Das SR, 2019, J FINANCIAL DATA SCI            |        6 |
|  5 |      5 | Gasparri G, 2019, FRONTIER ARTIF INTELL       |        6 |
|  6 |      6 | Nicholls R, 2021, J ANTITRUST ENFORC          |        6 |
|  7 |      7 | Muganyi T, 2022, FINANCIAL INNOV              |        4 |
|  8 |      8 | von Solms J, 2021, J BANK REGUL               |        4 |
|  9 |      9 | Anagnostopoulos I, 2018, J ECON BUS           |        3 |
| 10 |     10 | Goul M, 2019, PROC - IEEE WORLD CONGR SERV,   |        2 |
| 11 |     11 | Arner DW, 2017, NORTHWEST J INTL LAW BUS      |        1 |
| 12 |     12 | Butler T, 2018, J RISK MANG FINANCIAL INST    |        1 |
| 13 |     13 | Ryan P, 2020, ICEIS - PROC INT CONF ENTERP    |        1 |
```
<BLANKLINE>




"""
from ....nx_create_bibliographic_coupling_graph import nx_create_bibliographic_coupling_graph
from ....nx_create_degree_plot import nx_create_degree_plot

UNIT_OF_ANALYSIS = "article"


def degree_plot(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_min=0,
    documents_min=2,
    custom_items=None,
    #
    # NETWORK PARAMS:
    algorithm_or_dict="louvain",
    #
    # DEGREE PLOT:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
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
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
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
        documents_min=documents_min,
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

    return nx_create_degree_plot(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # DEGREE PLOT PARAMS:
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )
