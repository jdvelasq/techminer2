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

>>> from techminer2.network_analysis.co_citation.cited_authors import degree_plot
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
>>> plot.fig_.write_html("sphinx/_static/network_analysis/co_citation/cited_authors/degree_plot.html")

.. raw:: html

    <iframe src="../../../../_static/network_analysis/co_citation/cited_authors/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node               Name  Degree
0     0           Arner DW      28
1     1           Butler T      27
2     2  Anagnostopoulos I      23
3     3             Yang D      23
4     4         Micheler E      22

>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name              |   Degree |
|---:|-------:|:------------------|---------:|
|  0 |      0 | Arner DW          |       28 |
|  1 |      1 | Butler T          |       27 |
|  2 |      2 | Anagnostopoulos I |       23 |
|  3 |      3 | Yang D            |       23 |
|  4 |      4 | Micheler E        |       22 |
|  5 |      5 | Kavassalis P      |       22 |
|  6 |      6 | Buckley RP        |       22 |
|  7 |      7 | Das SR            |       22 |
|  8 |      8 | Sheridan I        |       22 |
|  9 |      9 | Williams JW       |       22 |
| 10 |     10 | Baxter LG         |       21 |
| 11 |     11 | von Solms J       |       21 |
| 12 |     12 | Gomber P          |       21 |
| 13 |     13 | Becker M          |       20 |
| 14 |     14 | Brand V           |       20 |
| 15 |     15 | Kurum E           |       20 |
| 16 |     16 | Lee J             |       20 |
| 17 |     17 | Gozman DP         |       19 |
| 18 |     18 | Currie WL         |       19 |
| 19 |     19 | Singh C           |       18 |
| 20 |     20 | Siering M         |       14 |
| 21 |     21 | Gabor D           |       13 |
| 22 |     22 | Allen F           |       11 |
| 23 |     23 | Kroll JA          |       11 |
| 24 |     24 | Brummer C         |       10 |
| 25 |     25 | Bamberger KA      |        8 |
| 26 |     26 | Hildebrandt M     |        7 |
| 27 |     27 | Baker A           |        4 |
| 28 |     28 | Loughran T        |        2 |
```
<BLANKLINE>


"""
from ....nx_create_co_citation_graph import nx_create_co_citation_graph
from ....nx_create_degree_plot import nx_create_degree_plot

UNIT_OF_ANALYSIS = "cited_authors"


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
