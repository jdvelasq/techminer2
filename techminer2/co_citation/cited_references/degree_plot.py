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

>>> from techminer2.co_citation.cited_references import degree_plot
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
>>> plot.fig_.write_html("sphinx/_static/co_citation/cited_references/degree_plot.html")

.. raw:: html

    <iframe src="../../../_static/co_citation/cited_references/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                                           Name  Degree
0     0  Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL      28
1     1       Arner DW, 2017, NORTHWEST J INTL LAW BUS      28
2     2            Anagnostopoulos I, 2018, J ECON BUS      27
3     3              Kavassalis P, 2018, J RISK FINANC      27
4     4          Yang D, 2018, EMERG MARK FINANC TRADE      27


>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                               |   Degree |
|---:|-------:|:---------------------------------------------------|---------:|
|  0 |      0 | Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL      |       28 |
|  1 |      1 | Arner DW, 2017, NORTHWEST J INTL LAW BUS           |       28 |
|  2 |      2 | Anagnostopoulos I, 2018, J ECON BUS                |       27 |
|  3 |      3 | Kavassalis P, 2018, J RISK FINANC                  |       27 |
|  4 |      4 | Yang D, 2018, EMERG MARK FINANC TRADE              |       27 |
|  5 |      5 | Baxter LG, 2016, DUKE LAW J                        |       27 |
|  6 |      6 | Micheler E, 2020, EUR BUS ORG LAW REV              |       26 |
|  7 |      7 | Buckley RP, 2020, J BANK REGUL                     |       26 |
|  8 |      8 | Sheridan I, 2017, CAP MARK LAW J                   |       26 |
|  9 |      9 | von Solms J, 2021, J BANK REGUL                    |       26 |
| 10 |     10 | Arner DW, 2019, EUR BUS ORG LAW REV                |       25 |
| 11 |     11 | Williams JW, 2013, ACCOUNT ORGAN SOC               |       25 |
| 12 |     12 | Brand V, 2020, UNIV NEW SOUTH WALES LAW J          |       25 |
| 13 |     13 | Kurum E, 2020, J FINANC CRIME                      |       25 |
| 14 |     14 | Lee J, 2020, EUR BUS ORG LAW REV                   |       25 |
| 15 |     15 | Muzammil M, 2020, CEUR WORKSHOP PROC               |       25 |
| 16 |     16 | Omarova ST, 2020, J FINANC REGUL                   |       25 |
| 17 |     17 | Parra Moyano J, 2017, BUSIN INFO SYS ENG           |       24 |
| 18 |     18 | Gomber P, 2018, J MANAGE INF SYST                  |       24 |
| 19 |     19 | Gozman DP, 2020, MIS Q EXEC                        |       23 |
| 20 |     20 | Lui A, 2018, INF COMMUN TECHNOL LAW                |       23 |
| 21 |     21 | Arner DW, 2017, HANDBBLOCKCHAIN                    |       23 |
| 22 |     22 | Butler T, 2018, J RISK MANG FINANCIAL INST         |       23 |
| 23 |     23 | Ryan P, 2020, ICEIS - PROC INT CONF ENTERP         |       23 |
| 24 |     24 | Nicholls R, 2021, J ANTITRUST ENFORC               |       23 |
| 25 |     25 | Currie WL, 2018, J INF TECHNOL                     |       18 |
| 26 |     26 | Romanova I, 2016, CONTEMP STUD ECON FINANC ANAL    |       11 |
| 27 |     27 | Kroll JA, 2017, UNIV PA LAW REV                    |        9 |
| 28 |     28 | Hildebrandt M, 2018, PHILOS TRANS R SOC A MATH PHY |        6 |
| 29 |     29 | Bamberger KA, 2010, TEX LAW REV                    |        5 |
```
<BLANKLINE>


"""
from ...nx_create_co_citation_graph import nx_create_co_citation_graph
from ...nx_create_degree_plot import nx_create_degree_plot

UNIT_OF_ANALYSIS = "cited_references"


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
