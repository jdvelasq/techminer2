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
>>> plot = vosviewer.co_occurrence.nlp_phrases.degree_plot(
...     root_dir=root_dir,
...     top_n=20, 
... )
>>> plot.fig_.write_html("sphinx/_static/vosviewer/co_occurrence/nlp_phrases_degree_plot.html")

.. raw:: html

    <iframe src="../../../../../_static/vosviewer/co_occurrence/nlp_phrases_degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                                Name  Degree
0     0        REGULATORY_TECHNOLOGY 18:273      19
1     1       FINANCIAL_INSTITUTIONS 15:194      17
2     2  FINANCIAL_SERVICES_INDUSTRY 05:315      15
3     3        REGULATORY_COMPLIANCE 07:198      14
4     4         FINANCIAL_REGULATION 07:360      13

>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                |   Degree |
|---:|-------:|:------------------------------------|---------:|
|  0 |      0 | REGULATORY_TECHNOLOGY 18:273        |       19 |
|  1 |      1 | FINANCIAL_INSTITUTIONS 15:194       |       17 |
|  2 |      2 | FINANCIAL_SERVICES_INDUSTRY 05:315  |       15 |
|  3 |      3 | REGULATORY_COMPLIANCE 07:198        |       14 |
|  4 |      4 | FINANCIAL_REGULATION 07:360         |       13 |
|  5 |      5 | FINANCIAL_SECTOR 07:169             |       13 |
|  6 |      6 | ARTIFICIAL_INTELLIGENCE 07:033      |       13 |
|  7 |      7 | FINANCIAL_SYSTEM 05:189             |       13 |
|  8 |      8 | INFORMATION_TECHNOLOGY 05:177       |       13 |
|  9 |      9 | DIGITAL_INNOVATION 03:164           |       13 |
| 10 |     10 | SYSTEMATIC_LITERATURE_REVIEW 03:004 |       12 |
| 11 |     11 | FINANCIAL_TECHNOLOGY 05:173         |       11 |
| 12 |     12 | RISK_MANAGEMENT 04:015              |       11 |
| 13 |     13 | FINANCIAL_CRISIS 06:058             |       10 |
| 14 |     14 | GLOBAL_FINANCIAL_CRISIS 06:177      |        9 |
| 15 |     15 | REGTECH_SOLUTIONS 05:018            |        9 |
| 16 |     16 | FINANCIAL_MARKETS 04:151            |        9 |
| 17 |     17 | MACHINE_LEARNING 04:007             |        9 |
| 18 |     18 | NEW_TECHNOLOGIES 04:012             |        8 |
| 19 |     19 | REGTECH 04:037                      |        5 |
```
<BLANKLINE>



"""
from ....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from ....nx_create_degree_plot import nx_create_degree_plot

FIELD = "nlp_phrases"


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
