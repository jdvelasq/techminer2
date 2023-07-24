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


>>> from techminer2.network_analysis.co_authorship.countries import degree_plot
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
>>> plot.fig_.write_html("sphinx/_static/network_analysis/co_authorship/countries/degree_plot.html")

.. raw:: html

    <iframe src="../../../../../../_static/network_analysis/co_authorship/countries/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                  Name  Degree
0     0     Switzerland 4:045       8
1     1         Germany 4:051       7
2     2  United Kingdom 7:199       6
3     3       Australia 7:199       5
4     4   United States 6:059       5

>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                       |   Degree |
|---:|-------:|:---------------------------|---------:|
|  0 |      0 | Switzerland 4:045          |        8 |
|  1 |      1 | Germany 4:051              |        7 |
|  2 |      2 | United Kingdom 7:199       |        6 |
|  3 |      3 | Australia 7:199            |        5 |
|  4 |      4 | United States 6:059        |        5 |
|  5 |      5 | Hong Kong 3:185            |        5 |
|  6 |      6 | China 5:027                |        4 |
|  7 |      7 | Luxembourg 2:034           |        4 |
|  8 |      8 | Greece 1:021               |        4 |
|  9 |      9 | Italy 5:005                |        2 |
| 10 |     10 | Bahrain 4:019              |        2 |
| 11 |     11 | United Arab Emirates 2:013 |        2 |
| 12 |     12 | Jordan 1:011               |        2 |
| 13 |     13 | Ireland 5:055              |        1 |
| 14 |     14 | Japan 1:013                |        1 |
| 15 |     15 | Spain 2:004                |        0 |
| 16 |     16 | Indonesia 2:000            |        0 |
| 17 |     17 | South Africa 1:011         |        0 |
| 18 |     18 | Ukraine 1:004              |        0 |
| 19 |     19 | Malaysia 1:003             |        0 |
```
<BLANKLINE>

"""
from ....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ....nx_create_degree_plot import nx_create_degree_plot

FIELD = "countries"


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
