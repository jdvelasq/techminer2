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

>>> from techminer2.science_mapping.co_citation.cited_sources import degree_plot
>>> plot = degree_plot(
...     #
...     # COLUMN PARAMS:
...     top_n=30, 
...     citations_threshold=None,
...     custom_terms=None,
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
...     root_dir="example/", 
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> plot.fig_.write_html("sphinx/_static/analyze/co_citation/cited_sources/degree_plot.html")

.. raw:: html

    <iframe src="../../../../../_static/analyze/co_citation/cited_sources/degree_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>

>>> plot.df_.head()
   Node                            Name  Degree
0     0  MIS QUART MANAGE INF SYST 1:47      26
1     1      ELECT COMMER RES APPL 1:32      25
2     2          J MANAGE INF SYST 1:31      25
3     3                 MANAGE SCI 1:33      25
4     4               INF SYST RES 1:18      25


>>> print(plot.prompt_) # doctest: +ELLIPSIS
Your task is ...


"""
from ..._core.nx.nx_create_co_citation_graph import nx_create_co_citation_graph
from ..._core.nx.nx_generate_node_degree_distribution_chart import nx_generate_node_degree_distribution_chart

UNIT_OF_ANALYSIS = "cited_sources"


def plot_node_degree_from_cited_sources_network(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    custom_terms=None,
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
    # NODES:
    node_size_range = (30, 70)
    textfont_size_range = (10, 20)
    textfont_opacity_range = (0.35, 1.00)
    #
    # EDGES:
    edge_color = "#7793a5"
    edge_width_range = (0.8, 3.0)
    #
    # LAYOUT:
    nx_k = None
    nx_iterations = 10
    nx_random_state = 0
    # --------------------------------------------------------------------------

    nx_graph = nx_create_co_citation_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=UNIT_OF_ANALYSIS,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
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

    return nx_generate_node_degree_distribution_chart(
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
