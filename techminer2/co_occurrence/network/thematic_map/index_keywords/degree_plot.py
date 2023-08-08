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



>>> from techminer2.co_occurrence.network.thematic_map.index_keywords import degree_plot
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
>>> plot.fig_.write_html("sphinx/_static/co_occurrence/network/thematic_map/index_keywords/degree_plot.html")

.. raw:: html

    <iframe src="../../../../../../../_static/co_occurrence/network/thematic_map/index_keywords/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> plot.df_.head()
   Node                         Name  Degree
0     0   REGULATORY_COMPLIANCE 9:34      14
1     1  FINANCIAL_INSTITUTIONS 6:09      12
2     2                 FINANCE 5:16      12
3     3                 REGTECH 5:15      10
4     4   ANTI_MONEY_LAUNDERING 3:10      10

>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                 |   Degree |
|---:|-------:|:-------------------------------------|---------:|
|  0 |      0 | REGULATORY_COMPLIANCE 9:34           |       14 |
|  1 |      1 | FINANCIAL_INSTITUTIONS 6:09          |       12 |
|  2 |      2 | FINANCE 5:16                         |       12 |
|  3 |      3 | REGTECH 5:15                         |       10 |
|  4 |      4 | ANTI_MONEY_LAUNDERING 3:10           |       10 |
|  5 |      5 | FINTECH 3:08                         |        8 |
|  6 |      6 | COMMERCE 2:04                        |        8 |
|  7 |      7 | ARTIFICIAL_INTELLIGENCE 2:02         |        8 |
|  8 |      8 | LAUNDERING 2:09                      |        7 |
|  9 |      9 | BANKING 2:08                         |        7 |
| 10 |     10 | SANDBOXES 2:12                       |        6 |
| 11 |     11 | FINANCIAL_REGULATION 2:11            |        6 |
| 12 |     12 | FINANCIAL_SERVICES_INDUSTRY 2:11     |        6 |
| 13 |     13 | RISK_MANAGEMENT 2:05                 |        6 |
| 14 |     14 | CLASSIFICATION (OF_INFORMATION) 2:03 |        5 |
| 15 |     15 | FINANCIAL_CRISIS 2:07                |        4 |
| 16 |     16 | INFORMATION_SYSTEMS 2:14             |        3 |
| 17 |     17 | INFORMATION_USE 2:14                 |        3 |
| 18 |     18 | SOFTWARE_SOLUTION 2:14               |        3 |
| 19 |     19 | BLOCKCHAIN 2:02                      |        2 |
```
<BLANKLINE>



"""
from .....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from .....nx_create_degree_plot import nx_create_degree_plot

FIELD = "index_keywords"


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
