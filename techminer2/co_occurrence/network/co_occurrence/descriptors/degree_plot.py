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



>>> from techminer2.co_occurrence.network.co_occurrence.descriptors import degree_plot
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
>>> plot.fig_.write_html("sphinx/_static/co_occurrence/network/co_occurrence/descriptors/degree_plot.html")

.. raw:: html

    <iframe src="../../../../../../../_static/co_occurrence/network/co_occurrence/descriptors/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


>>> plot.df_.head()
   Node                           Name  Degree
0     0                 REGTECH 29:330      19
1     1   REGULATORY_TECHNOLOGY 20:274      19
2     2  FINANCIAL_INSTITUTIONS 16:198      19
3     3   REGULATORY_COMPLIANCE 15:232      18
4     4    FINANCIAL_REGULATION 12:395      18


>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                               |   Degree |
|---:|-------:|:-----------------------------------|---------:|
|  0 |      0 | REGTECH 29:330                     |       19 |
|  1 |      1 | REGULATORY_TECHNOLOGY 20:274       |       19 |
|  2 |      2 | FINANCIAL_INSTITUTIONS 16:198      |       19 |
|  3 |      3 | REGULATORY_COMPLIANCE 15:232       |       18 |
|  4 |      4 | FINANCIAL_REGULATION 12:395        |       18 |
|  5 |      5 | FINTECH 12:249                     |       17 |
|  6 |      6 | FINANCE 07:017                     |       17 |
|  7 |      7 | GLOBAL_FINANCIAL_CRISIS 06:177     |       17 |
|  8 |      8 | FINANCIAL_SYSTEM 06:339            |       16 |
|  9 |      9 | INFORMATION_TECHNOLOGY 06:177      |       16 |
| 10 |     10 | ARTIFICIAL_INTELLIGENCE 08:036     |       15 |
| 11 |     11 | COMPLIANCE_COSTS 06:033            |       15 |
| 12 |     12 | FINANCIAL_CRISIS 07:058            |       14 |
| 13 |     13 | TECHNOLOGICAL_SOLUTIONS 06:016     |       14 |
| 14 |     14 | FINANCIAL_SERVICES_INDUSTRY 05:315 |       14 |
| 15 |     15 | FINANCIAL_SECTOR 07:169            |       13 |
| 16 |     16 | FINANCIAL_TECHNOLOGY 06:173        |       13 |
| 17 |     17 | COMPLIANCE 07:030                  |       12 |
| 18 |     18 | FINANCIAL_SERVICES 06:195          |       12 |
| 19 |     19 | ANTI_MONEY_LAUNDERING 06:035       |       10 |
```
<BLANKLINE>


"""
from .....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from .....nx_create_degree_plot import nx_create_degree_plot

FIELD = "descriptors"


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
