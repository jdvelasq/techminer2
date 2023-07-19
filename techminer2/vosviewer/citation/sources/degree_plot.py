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

>>> from techminer2 import vosviewer
>>> root_dir = "data/regtech/"
>>> plot = vosviewer.citation.sources.degree_plot(
...     root_dir=root_dir,
...     top_n=20, 
... )
>>> plot.fig_.write_html("sphinx/_static/vosviewer/citation/sources/degree_plot.html")

.. raw:: html

    <iframe src="../../../../../_static/vosviewer/citation/sources/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                           Name  Degree
0     0  INT CONF INF TECHNOL SYST INN       8
1     1                     J ECON BUS       7
2     2                  J RISK FINANC       5
3     3  INTELL SYST ACCOUNT FINANCE M       4
4     4                 J FINANC CRIME       4

>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                          |   Degree |
|---:|-------:|:------------------------------|---------:|
|  0 |      0 | INT CONF INF TECHNOL SYST INN |        8 |
|  1 |      1 | J ECON BUS                    |        7 |
|  2 |      2 | J RISK FINANC                 |        5 |
|  3 |      3 | INTELL SYST ACCOUNT FINANCE M |        4 |
|  4 |      4 | J FINANC CRIME                |        4 |
|  5 |      5 | FOSTER INNOVCOMPET WITH FINTE |        3 |
|  6 |      6 | ICEIS - PROC INT CONF ENTERP  |        3 |
|  7 |      7 | J RISK MANG FINANCIAL INST    |        2 |
|  8 |      8 | FINANCIAL INNOV               |        2 |
|  9 |      9 | HELIYON                       |        2 |
| 10 |     10 | J BANK REGUL                  |        2 |
| 11 |     11 | ROUTLEDGE HANDBFINANCIAL TECH |        2 |
| 12 |     12 | STUD COMPUT INTELL            |        2 |
| 13 |     13 | ADELAIDE LAW REV              |        1 |
| 14 |     14 | PALGRAVE STUD DIGIT BUS ENABL |        1 |
```
<BLANKLINE>



"""
from ...nx_create_citation_graph import nx_create_citation_graph
from ...nx_create_degree_plot import nx_create_degree_plot

UNIT_OF_ANALYSIS = "source_abbr"


def degree_plot(
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
    # --------------------------------------------------------------------------
    # TODO: REMOVE DEPENDENCES:
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    #
    # NODES:
    node_size = 30
    # textfont_size=10,
    textfont_opacity = 0.35
    #
    # EDGES:
    edge_color = "#7793a5"
    edge_width_min = 0.8
    edge_width_max = 3.0
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
