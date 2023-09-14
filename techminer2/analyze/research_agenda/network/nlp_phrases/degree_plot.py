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


>>> from techminer2.agenda.network.nlp_phrases import degree_plot
>>> plot = degree_plot(
...     #
...     # AGENDA PARAMS:
...     occ_range=(2, None),
...     gc_range=(None, None),
...     time_window=2,
...     growth_percentage_min=50,
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
>>> plot.fig_.write_html("sphinx/_static/agenda/network/nlp_phrases/degree_plot.html")

.. raw:: html

    <iframe src="../../../../_static/agenda/network/nlp_phrases/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                                      Name  Degree
0     0                   MACHINE_LEARNING 04:007       9
1     1            GLOBAL_FINANCIAL_CRISIS 06:177       5
2     2           INTERNATIONAL_REGULATION 02:017       4
3     3                       MAJOR_IMPACT 02:017       4
4     4  POTENTIAL_TECHNOLOGICAL_SOLUTIONS 02:017       4


>>> print(plot.prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                     |   Degree |
|---:|-------:|:-----------------------------------------|---------:|
|  0 |      0 | MACHINE_LEARNING 04:007                  |        9 |
|  1 |      1 | GLOBAL_FINANCIAL_CRISIS 06:177           |        5 |
|  2 |      2 | INTERNATIONAL_REGULATION 02:017          |        4 |
|  3 |      3 | MAJOR_IMPACT 02:017                      |        4 |
|  4 |      4 | POTENTIAL_TECHNOLOGICAL_SOLUTIONS 02:017 |        4 |
|  5 |      5 | REGULATORY_COMPLIANCE_CHALLENGE 02:017   |        4 |
|  6 |      6 | FINANCIAL_MARKETS 04:151                 |        3 |
|  7 |      7 | PRIMARY_DATA 02:012                      |        3 |
|  8 |      8 | EXCLUSIVE_LICENSE 02:001                 |        3 |
|  9 |      9 | REGULATION_TECHNOLOGY 02:001             |        3 |
| 10 |     10 | SUPERVISOR_AND_OR_REGULATOR 02:000       |        3 |
| 11 |     11 | REGTECH_DEVELOPMENTS 02:150              |        2 |
| 12 |     12 | SUPERVISORY_TECHNOLOGY 02:000            |        2 |
| 13 |     13 | MARKET_PARTICIPANT 02:154                |        1 |
| 14 |     14 | REGULATORY_ENFORCEMENT 02:004            |        1 |
| 15 |     15 | NEW_REGULATORY_TECHNOLOGIES 02:003       |        1 |
| 16 |     16 | FINTECH_SECTOR 02:014                    |        0 |
| 17 |     17 | REGULATORY_APPROACHES 02:011             |        0 |
```
<BLANKLINE>



"""
from .....nx_create_co_occurrence_graph import nx_create_co_occurrence_graph
from .....nx_create_degree_plot import nx_create_degree_plot
from ....performance_metrics import performance_metrics

UNIT_OF_ANALYSIS = "nlp_phrases"


def degree_plot(
    #
    # AGENDA PARAMS:
    occ_range=(None, None),
    gc_range=(None, None),
    time_window=2,
    growth_percentage_min=50,
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
    textfont_opacity_min = 0.30
    textfont_opacity_max = 1.00
    #
    # EDGES:
    edge_color = "#7793a5"
    edge_width_min = 0.8
    edge_width_max = 3.0
    #
    # --------------------------------------------------------------------------

    #
    # Computes performance metrics
    metrics = performance_metrics(
        #
        # PERFORMANCE PARAMS:
        field=UNIT_OF_ANALYSIS,
        metric="OCC",
        #
        # ITEM FILTERS:
        top_n=None,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=None,
        #
        # TREND ANALYSIS:
        time_window=time_window,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).df_

    #
    # Selects only the items with growth rate >= growth_percentage_min
    metrics = metrics[metrics["growth_percentage"] >= growth_percentage_min]

    #
    # Obtains emergent items
    custom_items = metrics.index.tolist()

    nx_graph = nx_create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=UNIT_OF_ANALYSIS,
        #
        # COLUMN PARAMS:
        top_n=None,
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
