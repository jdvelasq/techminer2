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

>>> from techminer2.citation.network.documents import degree_plot
>>> plot = degree_plot(
...     #
...     # COLUMN PARAMS:
...     top_n=30,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # NETWORK PARAMS:
...     algorithm_or_dict="louvain",
...     association_index="association",
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
>>> plot.fig_.write_html("sphinx/_static/citation/network/documents/degree_plot.html")

.. raw:: html

    <iframe src="../../../../_static/citation/network/documents/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                                               Name  Degree
0     0                Anagnostopoulos I, 2018, J ECON BUS      16
1     1           Arner DW, 2017, NORTHWEST J INTL LAW BUS      16
2     2                     Grassi L, 2022, J IND BUS ECON      16
3     3      Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL      14
4     4  Kristanto AD, 2022, INT CONF INF TECHNOL SYST INN      14



>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                              |   Degree |
|---:|-------:|:--------------------------------------------------|---------:|
|  0 |      0 | Anagnostopoulos I, 2018, J ECON BUS               |       16 |
|  1 |      1 | Arner DW, 2017, NORTHWEST J INTL LAW BUS          |       16 |
|  2 |      2 | Grassi L, 2022, J IND BUS ECON                    |       16 |
|  3 |      3 | Butler T, 2019, PALGRAVE STUD DIGIT BUS ENABL     |       14 |
|  4 |      4 | Kristanto AD, 2022, INT CONF INF TECHNOL SYST INN |       14 |
|  5 |      5 | Firmansyah B, 2022, INT CONF INF TECHNOL SYST INN |       13 |
|  6 |      6 | Kavassalis P, 2018, J RISK FINANC                 |       10 |
|  7 |      7 | Baxter LG, 2016, DUKE LAW J                       |        8 |
|  8 |      8 | Teichmann F, 2023, TECHNOL SOC                    |        7 |
|  9 |      9 | Becker M, 2020, INTELL SYST ACCOUNT FINANCE M     |        5 |
| 10 |     10 | Butler T, 2018, J RISK MANG FINANCIAL INST        |        5 |
| 11 |     11 | Kurum E, 2020, J FINANC CRIME                     |        5 |
| 12 |     12 | Muzammil M, 2020, CEUR WORKSHOP PROC              |        5 |
| 13 |     13 | Nicholls R, 2021, J ANTITRUST ENFORC              |        5 |
| 14 |     14 | von Solms J, 2021, J BANK REGUL                   |        5 |
| 15 |     15 | Miglionico A, 2020, EUR BUS LAW REV               |        5 |
| 16 |     16 | Ryan P, 2021, LECT NOTES BUS INF PROCESS          |        5 |
| 17 |     17 | Battanta L, 2020, PROC EUR CONF INNOV ENTREPREN   |        4 |
| 18 |     18 | Boitan IA, 2020, FOSTER INNOVCOMPET WITH FINTE    |        4 |
| 19 |     19 | Buckley RP, 2020, J BANK REGUL                    |        4 |
| 20 |     20 | Ryan P, 2020, ICEIS - PROC INT CONF ENTERP        |        4 |
| 21 |     21 | Turki M, 2020, HELIYON                            |        4 |
| 22 |     22 | Narang S, 2020, FOSTER INNOVCOMPET WITH FINTE     |        4 |
| 23 |     23 | Nasir F, 2019, J ADV RES DYN CONTROL SYST         |        4 |
| 24 |     24 | Gasparri G, 2019, FRONTIER ARTIF INTELL           |        3 |
| 25 |     25 | Colaert V, 2021, ROUTLEDGE HANDBFINANCIAL TECH    |        3 |
| 26 |     26 | Arner DW, 2017, HANDBBLOCKCHAIN                   |        3 |
| 27 |     27 | Brand V, 2020, UNIV NEW SOUTH WALES LAW J         |        3 |
| 28 |     28 | Ghanem S, 2021, STUD COMPUT INTELL                |        3 |
| 29 |     29 | Singh C, 2020, J MONEY LAUND CONTROL              |        3 |
| 30 |     30 | Campbell-Verduyn M, 2022, NEW POLIT ECON          |        2 |
| 31 |     31 | Chirulli P, 2021, ROUTLEDGE HANDBFINANCIAL TECH   |        2 |
| 32 |     32 | Das SR, 2019, J FINANCIAL DATA SCI                |        2 |
| 33 |     33 | Goul M, 2019, PROC - IEEE WORLD CONGR SERV,       |        2 |
| 34 |     34 | Siering M, 2022, DECIS SUPPORT SYST               |        2 |
| 35 |     35 | Muganyi T, 2022, FINANCIAL INNOV                  |        2 |
| 36 |     36 | Singh C, 2022, J FINANC CRIME                     |        2 |
| 37 |     37 | Waye V, 2020, ADELAIDE LAW REV                    |        2 |
| 38 |     38 | McCarthy J, 2022, J FINANC REGUL COMPLIANCE       |        2 |
| 39 |     39 | Turki M, 2021, ADV INTELL SYS COMPUT              |        1 |
| 40 |     40 | Gu M, 2022, J CORP FINANC                         |        1 |
| 41 |     41 | Hee Jung JH, 2019, FINTECH: LAWREGULATION         |        1 |
| 42 |     42 | Mohamed H, 2021, STUD COMPUT INTELL               |        1 |
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
