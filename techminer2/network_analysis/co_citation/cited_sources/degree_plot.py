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

>>> from techminer2.network_analysis.co_citation.cited_sources import degree_plot
>>> plot = degree_plot(
...     #
...     # COLUMN PARAMS:
...     top_n=30, 
...     citations_min=None,
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
>>> plot.fig_.write_html("sphinx/_static/network_analysis/co_citation/cited_sources/degree_plot.html")

.. raw:: html

    <iframe src="../../../../_static/network_analysis/co_citation/cited_sources/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                Name  Degree
0     0           J BUS RES      28
1     1  DECIS SUPPORT SYST      28
2     2          J ECON BUS      28
3     3  BUSIN INFO SYS ENG      28
4     4   J MANAGE INF SYST      28


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
|  0 |      0 | J BUS RES                     |       28 |
|  1 |      1 | DECIS SUPPORT SYST            |       28 |
|  2 |      2 | J ECON BUS                    |       28 |
|  3 |      3 | BUSIN INFO SYS ENG            |       28 |
|  4 |      4 | J MANAGE INF SYST             |       28 |
|  5 |      5 | NORTHWEST J INTL LAW BUS      |       27 |
|  6 |      6 | PALGRAVE STUD DIGIT BUS ENABL |       27 |
|  7 |      7 | FINANCIAL INNOV               |       26 |
|  8 |      8 | J RISK FINANC                 |       26 |
|  9 |      9 | J BANK FINANC                 |       25 |
| 10 |     10 | CEUR WORKSHOP PROC            |       25 |
| 11 |     11 | HANDBBLOCKCHAIN               |       25 |
| 12 |     12 | EMERG MARK FINANC TRADE       |       25 |
| 13 |     13 | ACCOUNT ORGAN SOC             |       25 |
| 14 |     14 | DUKE LAW J                    |       25 |
| 15 |     15 | J BANK REGUL                  |       23 |
| 16 |     16 | CAP MARK LAW J                |       23 |
| 17 |     17 | J FINANC                      |       22 |
| 18 |     18 | EUR BUS ORG LAW REV           |       22 |
| 19 |     19 | J FINANC CRIME                |       22 |
| 20 |     20 | J FINANC REGUL COMPLIANCE     |       22 |
| 21 |     21 | J FINANC REGUL                |       22 |
| 22 |     22 | J MONEY LAUND CONTROL         |       22 |
| 23 |     23 | J FINANC ECON                 |       20 |
| 24 |     24 | NEW POLIT ECON                |       20 |
| 25 |     25 | REV FINANC STUD               |       15 |
| 26 |     26 | MIS QUART MANAGE INF SYST     |       14 |
| 27 |     27 | LECT NOTES COMPUT SCI         |       13 |
| 28 |     28 | EXPERT SYS APPL               |       12 |
| 29 |     29 | TECHNOL SOC                   |        4 |
```
<BLANKLINE>


"""
from ....nx_create_co_citation_graph import nx_create_co_citation_graph
from ....nx_create_degree_plot import nx_create_degree_plot

UNIT_OF_ANALYSIS = "cited_sources"


def degree_plot(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_min=None,
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

    nx_graph = nx_create_co_citation_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=UNIT_OF_ANALYSIS,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_min=citations_min,
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
