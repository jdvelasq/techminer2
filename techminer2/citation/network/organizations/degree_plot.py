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

>>> from techminer2.citation.network.organizations import degree_plot
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
>>> plot.fig_.write_html("sphinx/_static/citation/network/organizations/degree_plot.html")

.. raw:: html

    <iframe src="../../../../_static/citation/network/organizations/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> plot.df_.head()
   Node                                               Name  Degree
0     0                            Politec di Milano (ITA)      25
1     1                             Kingston Bus Sch (GBR)      11
2     2                        FinTech HK, Hong Kong (HKG)      10
3     3                            Univ of Hong Kong (HKG)      10
4     4  ctr for Law, Markets & Regulation, UNSW Austra...      10



>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                                               |   Degree |
|---:|-------:|:-------------------------------------------------------------------|---------:|
|  0 |      0 | Politec di Milano (ITA)                                            |       25 |
|  1 |      1 | Kingston Bus Sch (GBR)                                             |       11 |
|  2 |      2 | FinTech HK, Hong Kong (HKG)                                        |       10 |
|  3 |      3 | Univ of Hong Kong (HKG)                                            |       10 |
|  4 |      4 | ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |       10 |
|  5 |      5 | Dublin City Univ (IRL)                                             |        8 |
|  6 |      6 | Duke Univ Sch of Law (USA)                                         |        7 |
|  7 |      7 | European Central B (DEU)                                           |        6 |
|  8 |      8 | Harvard Univ Weatherhead ctr for International Affairs (USA)       |        6 |
|  9 |      9 | KS Strategic, London, United Kingdom (GBR)                         |        6 |
| 10 |     10 | Panepistemio Aigaiou, Chios, Greece (GRC)                          |        6 |
| 11 |     11 | Sch of Eng (CHE)                                                   |        6 |
| 12 |     12 | Univ Coll Cork (IRL)                                               |        5 |
| 13 |     13 | Ahlia Univ (BHR)                                                   |        4 |
| 14 |     14 | Mutah Univ (JOR)                                                   |        4 |
| 15 |     15 | Zayed Univ (ARE)                                                   |        4 |
| 16 |     16 | Coventry Univ (GBR)                                                |        2 |
| 17 |     17 | Univ of Westminster (GBR)                                          |        2 |
| 18 |     18 | Hebei Univ of Technol (CHN)                                        |        2 |
| 19 |     19 | Jiangsu Univ (CHN)                                                 |        2 |
| 20 |     20 | Shanghai Univ (CHN)                                                |        2 |
| 21 |     21 | Tokai Univ (JPN)                                                   |        2 |
| 22 |     22 | Tongji Univ (CHN)                                                  |        2 |
| 23 |     23 | Univ of Johannesburg (ZAF)                                         |        2 |
| 24 |     24 | FinTech HK, China (CHN)                                            |        1 |
| 25 |     25 | Heinrich-Heine-Univ (DEU)                                          |        1 |
| 26 |     26 | UNSW Sydney, Kensington, Australia (AUS)                           |        1 |
| 27 |     27 | UNSW, Australia (AUS)                                              |        1 |
| 28 |     28 | Univ of Luxembourg (LUX)                                           |        1 |
| 29 |     29 | Univ of Zurich (CHE)                                               |        1 |
```
<BLANKLINE>



"""
from ....nx_create_citation_graph import nx_create_citation_graph
from ....nx_create_degree_plot import nx_create_degree_plot

UNIT_OF_ANALYSIS = "organizations"


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
