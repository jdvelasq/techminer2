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
>>> plot = vosviewer.thematic_map.title_nlp_phrases.degree_plot(
...     root_dir=root_dir,
...     top_n=20, 
... )
>>> plot.fig_.write_html("sphinx/_static/vosviewer/thematic_map/title_nlp_phrases_degree_plot.html")

.. raw:: html

    <iframe src="../../../../../_static/vosviewer/thematic_map/title_nlp_phrases_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                           Name  Degree
0     0          FINANCIAL_CRIME 2:012       3
1     1    REGULATORY_TECHNOLOGY 3:020       2
2     2  ARTIFICIAL_INTELLIGENCE 3:017       2
3     3            BANK_TREASURY 1:011       2
4     4   DIGITAL_TRANSFORMATION 1:011       2

>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                       |   Degree |
|---:|-------:|:-------------------------------------------|---------:|
|  0 |      0 | FINANCIAL_CRIME 2:012                      |        3 |
|  1 |      1 | REGULATORY_TECHNOLOGY 3:020                |        2 |
|  2 |      2 | ARTIFICIAL_INTELLIGENCE 3:017              |        2 |
|  3 |      3 | BANK_TREASURY 1:011                        |        2 |
|  4 |      4 | DIGITAL_TRANSFORMATION 1:011               |        2 |
|  5 |      5 | AML_COMPLIANCE 1:010                       |        2 |
|  6 |      6 | REGTECH_SOLUTIONS 1:010                    |        2 |
|  7 |      7 | EFFECTIVE_SOLUTIONS 1:014                  |        1 |
|  8 |      8 | MODERN_INFORMATION_TECHNOLOGY 1:005        |        1 |
|  9 |      9 | REGULATORY_AFFAIRS 1:005                   |        1 |
| 10 |     10 | FINANCIAL_STABILITY 1:004                  |        1 |
| 11 |     11 | TRADITIONAL_FINANCIAL_INTERMEDIATION 1:004 |        1 |
| 12 |     12 | FINANCIAL_REGULATION 2:180                 |        0 |
| 13 |     13 | EUROPEAN_UNION 1:024                       |        0 |
| 14 |     14 | FINANCIAL_RISK 1:021                       |        0 |
| 15 |     15 | FINANCIAL_DEVELOPMENT 1:013                |        0 |
| 16 |     16 | REGULATORY_TECHNOLOGY_REGTECH 1:011        |        0 |
| 17 |     17 | FINANCIAL_SYSTEM 1:011                     |        0 |
| 18 |     18 | SMART_REGULATION 1:004                     |        0 |
| 19 |     19 | CHARITABLE_ORGANISATIONS 1:003             |        0 |
```
<BLANKLINE>




"""
from ....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ....nx_create_degree_plot import nx_create_degree_plot

FIELD = "title_nlp_phrases"


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
        association_index="association",
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
