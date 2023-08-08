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


>>> from techminer2.co_authorship.network.organizations import degree_plot
>>> plot = degree_plot(
...     #
...     # COLUMN PARAMS:
...     top_n=20,
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
>>> plot.fig_.write_html("sphinx/_static/co_authorship/network/organizations/degree_plot.html")

.. raw:: html

    <iframe src="../../../../../../_static/co_authorship/network/organizations/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> plot.df_.head()
   Node                                            Name  Degree
0     0                   Univ of Hong Kong (HKG) 3:185       6
1     1                 Heinrich-Heine-Univ (DEU) 1:024       4
2     2  UNSW Sydney, Kensington, Australia (AUS) 1:024       4
3     3                  Univ of Luxembourg (LUX) 1:024       4
4     4                      Univ of Zurich (CHE) 1:024       4


>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                                                     |   Degree |
|---:|-------:|:-------------------------------------------------------------------------|---------:|
|  0 |      0 | Univ of Hong Kong (HKG) 3:185                                            |        6 |
|  1 |      1 | Heinrich-Heine-Univ (DEU) 1:024                                          |        4 |
|  2 |      2 | UNSW Sydney, Kensington, Australia (AUS) 1:024                           |        4 |
|  3 |      3 | Univ of Luxembourg (LUX) 1:024                                           |        4 |
|  4 |      4 | Univ of Zurich (CHE) 1:024                                               |        4 |
|  5 |      5 | European Central B (DEU) 1:021                                           |        4 |
|  6 |      6 | Harvard Univ Weatherhead ctr for International Affairs (USA) 1:021       |        4 |
|  7 |      7 | KS Strategic, London, United Kingdom (GBR) 1:021                         |        4 |
|  8 |      8 | Panepistemio Aigaiou, Chios, Greece (GRC) 1:021                          |        4 |
|  9 |      9 | Sch of Eng (CHE) 1:021                                                   |        4 |
| 10 |     10 | FinTech HK, Hong Kong (HKG) 1:150                                        |        2 |
| 11 |     11 | ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150 |        2 |
| 12 |     12 | Coventry Univ (GBR) 2:017                                                |        1 |
| 13 |     13 | Univ of Westminster (GBR) 2:017                                          |        1 |
| 14 |     14 | Univ Coll Cork (IRL) 3:041                                               |        0 |
| 15 |     15 | Ahlia Univ (BHR) 3:019                                                   |        0 |
| 16 |     16 | Dublin City Univ (IRL) 2:014                                             |        0 |
| 17 |     17 | Politec di Milano (ITA) 2:002                                            |        0 |
| 18 |     18 | Kingston Bus Sch (GBR) 1:153                                             |        0 |
| 19 |     19 | Duke Univ Sch of Law (USA) 1:030                                         |        0 |
```
<BLANKLINE>


"""
from ....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ....nx_create_degree_plot import nx_create_degree_plot

FIELD = "organizations"


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
    #
    # EDGES:
    edge_width_min = 0.8
    edge_width_max = 3.0
    #
    # --------------------------------------------------------------------------

    nx_graph = nx_create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=FIELD,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
        association_index=association_index,
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
        #
        # EDGES:
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
