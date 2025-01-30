# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Network Plot
===============================================================================

## >>> # abbr_source_title, authors, organizations, countries:
## >>> from techminer2.analyze.citation_network import NetworkPlot
## >>> plot = (
## ...     NetworkPlot()
## ...     .set_analysis_params(
## ...         unit_of_analysis='abbr_source_title',
## ...         top_n=30,
## ...         citations_threshold=0,
## ...         occurrence_threshold=2,
## ...         custom_terms=None,
## ...     #
## ...     # NETWORK CLUSTERING:
## ...     algorithm_or_dict="louvain",
## ...     #
## ...     ).set_nx_params(
## ...         nx_k=None,
## ...         nx_iterations=30,
## ...         nx_random_state=0,
## ...     ).set_plot_params(
## ...         node_size_range=(30, 70),
## ...         textfont_size_range=(10, 20),
## ...         textfont_opacity_range=(0.35, 1.00),
## ...         edge_color="#7793a5",
## ...         edge_width_range=(0.8, 3.0),
## ...     ).set_axes_params(
## ...         xaxes_range=None,
## ...         yaxes_range=None,
## ...         show_axes=False,
## ...     ).set_database_params(
## ...         root_dir="example/", 
## ...         database="main",
## ...         year_filter=(None, None),
## ...         cited_by_filter=(None, None),
## ...     ).build()
## ... )
## >>> # plot.write_html("sphinx/_static/citation_network/others_network_plot.html")

.. raw:: html

    <iframe src="../_static/citation_network/others_network_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>



"""
from ....internals.nx.internal__assign_colors_to_nodes_by_group_attribute import (
    internal__assign_colors_to_nodes_by_group_attribute,
)
from ....internals.nx.internal__assign_opacity_to_text_by_frequency import (
    internal__assign_opacity_to_text_by_frequency,
)
from ....internals.nx.internal__assign_sizes_to_nodes_by_occurrences import (
    internal__assign_sizes_to_nodes_by_occurrences,
)
from ....internals.nx.internal__assign_text_positions_to_nodes_by_quadrants import (
    internal__assign_text_positions_to_nodes_by_quadrants,
)
from ....internals.nx.internal__assign_textfont_sizes_to_nodes_by_occurrences import (
    nx_assign_textfont_sizes_to_nodes_by_occurrences,
)
from ....internals.nx.internal__assign_uniform_color_to_edges import (
    internal__assign_uniform_color_to_edges,
)
from ....internals.nx.internal__assign_widths_to_edges_by_weight import (
    internal__assign_widths_to_edges_by_weight,
)
from ....internals.nx.internal__cluster_graph import internal__cluster_graph
from ....internals.nx.internal__compute_spring_layout_positions import (
    internal__compute_spring_layout_positions,
)
from ....internals.nx.internal__create_network_plot import internal__create_network_plot
from .internals.create_citation_nx_graph import _create_citation_nx_graph

UNIT_OF_ANALYSIS = "abbr_source_title"


def _network_plot(
    #
    # FIELD PARAMS:
    unit_of_analysis,
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=None,
    occurrence_threshold=None,
    custom_terms=None,
    #
    # NETWORK CLUSTERING:
    algorithm_or_dict="louvain",
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_range=(20, 70),
    textfont_size_range=(9, 12),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_range=(0.8, 3.0),
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    nx_graph = _create_citation_nx_graph(
        #
        # FUNCTION PARAMS:
        unit_of_analysis=unit_of_analysis,
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        occurrence_threshold=occurrence_threshold,
        custom_terms=custom_terms,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    nx_graph = internal__cluster_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK CLUSTERING:
        algorithm_or_dict=algorithm_or_dict,
    )

    nx_graph = internal__compute_spring_layout_positions(
        nx_graph=nx_graph,
        k=nx_k,
        iterations=nx_iterations,
        seed=nx_random_state,
    )

    #
    # Sets the node attributes
    nx_graph = internal__assign_colors_to_nodes_by_group_attribute(nx_graph)
    #
    nx_graph = internal__assign_sizes_to_nodes_by_occurrences(nx_graph, node_size_range)
    nx_graph = nx_assign_textfont_sizes_to_nodes_by_occurrences(
        nx_graph, textfont_size_range
    )
    nx_graph = internal__assign_opacity_to_text_by_frequency(
        nx_graph, textfont_opacity_range
    )

    #
    # Sets the edge attributes
    nx_graph = internal__assign_widths_to_edges_by_weight(nx_graph, edge_width_range)
    nx_graph = internal__assign_text_positions_to_nodes_by_quadrants(nx_graph)
    nx_graph = internal__assign_uniform_color_to_edges(nx_graph, edge_color)

    return internal__create_network_plot(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )
