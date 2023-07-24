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
>>> plot = vosviewer.citation.documents.degree_plot(
...     root_dir=root_dir,
...     top_n=20, 
... )
>>> plot.fig_.write_html("sphinx/_static/vosviewer/citation/documents/degree_plot.html")

.. raw:: html

    <iframe src="../../../../../_static/vosviewer/citation/documents/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                                               Name  Degree
0     0      Anagnostopoulos I, 2018, J ECON BUS, V100, P7      16
1     1  Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL,...      14
2     2  Firmansyah B, 2022, INT CONF INF TECHNOL SYST ...      14
3     3          Grassi L, 2022, J IND BUS ECON, V49, P441      14
4     4  Kristanto AD, 2022, INT CONF INF TECHNOL SYST ...      14

>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                                                   |   Degree |
|---:|-------:|:-----------------------------------------------------------------------|---------:|
|  0 |      0 | Anagnostopoulos I, 2018, J ECON BUS, V100, P7                          |       16 |
|  1 |      1 | Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL, P85                     |       14 |
|  2 |      2 | Firmansyah B, 2022, INT CONF INF TECHNOL SYST INN, P310                |       14 |
|  3 |      3 | Grassi L, 2022, J IND BUS ECON, V49, P441                              |       14 |
|  4 |      4 | Kristanto AD, 2022, INT CONF INF TECHNOL SYST INN, P300                |       14 |
|  5 |      5 | Kavassalis P, 2018, J RISK FINANC, V19, P39                            |        8 |
|  6 |      6 | Teichmann F, 2023, TECHNOL SOC, V72                                    |        7 |
|  7 |      7 | Becker M, 2020, INTELL SYST ACCOUNT FINANCE M, V27, P161               |        6 |
|  8 |      8 | Butler T, 2018, J RISK MANG FINANCIAL INST, V11, P19                   |        5 |
|  9 |      9 | Buckley RP, 2020, J BANK REGUL, V21, P26                               |        5 |
| 10 |     10 | Muzammil M, 2020, CEUR WORKSHOP PROC, V2815, P382                      |        5 |
| 11 |     11 | Turki M, 2020, HELIYON, V6                                             |        5 |
| 12 |     12 | von Solms J, 2021, J BANK REGUL, V22, P152                             |        5 |
| 13 |     13 | Narang S, 2020, FOSTER INNOVCOMPET WITH FINTE, P61                     |        5 |
| 14 |     14 | Ryan P, 2021, LECT NOTES BUS INF PROCESS, V417, P905                   |        5 |
| 15 |     15 | Boitan IA, 2020, FOSTER INNOVCOMPET WITH FINTE, P1                     |        4 |
| 16 |     16 | Kurum E, 2020, J FINANC CRIME                                          |        4 |
| 17 |     17 | Ryan P, 2020, ICEIS - PROC INT CONF ENTERP , V2, P787                  |        4 |
| 18 |     18 | Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN, V2020-September, P112 |        3 |
| 19 |     19 | Arner DW, 2017, HANDBBLOCKCHAIN, DIGIT FINANC, P359                    |        3 |
| 20 |     20 | Brand V, 2020, UNIV NEW SOUTH WALES LAW J, V43, P801                   |        3 |
| 21 |     21 | Nicholls R, 2021, J ANTITRUST ENFORC, V9, P135                         |        3 |
| 22 |     22 | Ghanem S, 2021, STUD COMPUT INTELL, V954, P139                         |        3 |
| 23 |     23 | Singh C, 2020, J MONEY LAUND CONTROL, V24, P464                        |        3 |
| 24 |     24 | Miglionico A, 2020, EUR BUS LAW REV, V31, P641                         |        3 |
| 25 |     25 | Nasir F, 2019, J ADV RES DYN CONTROL SYST, V11, P912                   |        3 |
| 26 |     26 | Gasparri G, 2019, FRONTIER ARTIF INTELL, V2                            |        2 |
| 27 |     27 | Colaert V, 2021, ROUTLEDGE HANDBFINANCIAL TECH, P431                   |        2 |
| 28 |     28 | Goul M, 2019, PROC - IEEE WORLD CONGR SERV,, P219                      |        2 |
| 29 |     29 | Siering M, 2022, DECIS SUPPORT SYST, V158                              |        2 |
| 30 |     30 | Muganyi T, 2022, FINANCIAL INNOV, V8                                   |        2 |
| 31 |     31 | Singh C, 2022, J FINANC CRIME, V29, P45                                |        2 |
| 32 |     32 | Waye V, 2020, ADELAIDE LAW REV, V40, P363                              |        2 |
| 33 |     33 | Campbell-Verduyn M, 2022, NEW POLIT ECON                               |        1 |
| 34 |     34 | Chirulli P, 2021, ROUTLEDGE HANDBFINANCIAL TECH, P447                  |        1 |
| 35 |     35 | Turki M, 2021, ADV INTELL SYS COMPUT, V1141, P349                      |        1 |
| 36 |     36 | Das SR, 2019, J FINANCIAL DATA SCI, V1, P8                             |        1 |
| 37 |     37 | Gu M, 2022, J CORP FINANC, V76                                         |        1 |
| 38 |     38 | McCarthy J, 2022, J FINANC REGUL COMPLIANCE                            |        1 |
```
<BLANKLINE>

"""
from ....nx_create_citation_graph import nx_create_citation_graph
from ....nx_create_degree_plot import nx_create_degree_plot

UNIT_OF_ANALYSIS = "article"


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
