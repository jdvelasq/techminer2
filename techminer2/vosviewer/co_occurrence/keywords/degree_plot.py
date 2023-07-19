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
>>> plot = vosviewer.co_occurrence.keywords.degree_plot(
...     root_dir=root_dir,
...     top_n=20, 
... )
>>> plot.fig_.write_html("sphinx/_static/vosviewer/co_occurrence/keywords_degree_plot.html")

.. raw:: html

    <iframe src="../../../../../_static/vosviewer/co_occurrence/keywords_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                           Name  Degree
0     0                 REGTECH 28:329      19
1     1                 FINTECH 12:249      17
2     2              REGULATION 05:164      14
3     3         RISK_MANAGEMENT 05:019      14
4     4  FINANCIAL_INSTITUTIONS 06:009      13

>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                           |   Degree |
|---:|-------:|:-------------------------------|---------:|
|  0 |      0 | REGTECH 28:329                 |       19 |
|  1 |      1 | FINTECH 12:249                 |       17 |
|  2 |      2 | REGULATION 05:164              |       14 |
|  3 |      3 | RISK_MANAGEMENT 05:019         |       14 |
|  4 |      4 | FINANCIAL_INSTITUTIONS 06:009  |       13 |
|  5 |      5 | FINANCE 07:017                 |       12 |
|  6 |      6 | REGULATORY_COMPLIANCE 09:034   |       11 |
|  7 |      7 | ARTIFICIAL_INTELLIGENCE 06:025 |       11 |
|  8 |      8 | REGULATORY_TECHNOLOGY 08:037   |       10 |
|  9 |      9 | COMPLIANCE 07:030              |       10 |
| 10 |     10 | ANTI_MONEY_LAUNDERING 06:035   |       10 |
| 11 |     11 | SUPTECH 03:004                 |       10 |
| 12 |     12 | FINANCIAL_REGULATION 05:035    |        9 |
| 13 |     13 | INNOVATION 03:012              |        9 |
| 14 |     14 | FINANCIAL_SERVICES 04:168      |        8 |
| 15 |     15 | BLOCKCHAIN 03:005              |        6 |
| 16 |     16 | SEMANTIC_TECHNOLOGIES 02:041   |        4 |
| 17 |     17 | SMART_CONTRACTS 03:023         |        3 |
| 18 |     18 | DATA_PROTECTION 02:027         |        3 |
| 19 |     19 | CHARITYTECH 02:017             |        3 |
```
<BLANKLINE>



"""
from ...nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ...nx_create_degree_plot import nx_create_degree_plot

FIELD = "keywords"


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
