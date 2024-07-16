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


>>> from techminer2.tech_mining.research_agenda.network import degree_plot
>>> plot = degree_plot(
...     #
...     # FUNCTION PARAMS:
...     field='author_keywords',
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> plot.fig_.write_html("sphinx/_static/analyze/research_agenda/network/degree_plot.html")

.. raw:: html

    <iframe src="../../../_static/analyze/research_agenda/network/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                          Name  Degree
0     0               FINTECH 31:5168      19
1     1    FINANCIAL_SERVICES 04:0667       8
2     2  PEER_TO_PEER_LENDING 03:0324       6
3     3               REGTECH 02:0266       6
4     4  FINANCIAL_TECHNOLOGY 04:0551       5


>>> print(plot.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
from ..core.network.create_co_occurrence_graph import create_co_occurrence_graph
from ..core.network.generate_node_degree_distribution_chart import generate_node_degree_distribution_chart
from ..metrics.performance_metrics import performance_metrics


def degree_plot(
    #
    # FUNCTION PARAMS:
    field,
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
    node_size_range = (30, 70)
    textfont_size_range = (10, 20)
    textfont_opacity_range = (0.30, 1.00)
    #
    # EDGES:
    edge_color = "#7793a5"
    edge_width_range = (0.8, 3.0)
    #
    # --------------------------------------------------------------------------

    #
    # Computes performance metrics
    metrics = performance_metrics(
        #
        # PERFORMANCE PARAMS:
        field=field,
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

    nx_graph = create_co_occurrence_graph(
        #
        # FUNCTION PARAMS:
        rows_and_columns=field,
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
        node_size_range=node_size_range,
        textfont_size_range=textfont_size_range,
        textfont_opacity_range=textfont_opacity_range,
        #
        # EDGES:
        edge_color=edge_color,
        edge_width_range=edge_width_range,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return generate_node_degree_distribution_chart(
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
