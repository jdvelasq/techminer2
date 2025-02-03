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

## >>> from techminer2.analyze.main_path_analysis import NetworkPlot
## >>> plot = (
## ...     NetworkPlot()
## ...     .set_analysis_params(
## ...         top_n=None,
## ...         citations_threshold=0,
## ...     .using_xaxes_range=(None, None)
## ...     .using_yaxes_range=(None, None)
## ...     .using_axes_visible(False)

## ...     #
## ...     .using_node_size_range(30, 70)
## ...     .using_textfont_size_range(10, 20)
## ...     .using_textfont_opacity_range(0.35, 1.00)
## ...         edge_color="#7793a5",
## ...         edge_width_range=(0.8, 3.0),
## ...     #
## ...     # DATABASE:
## ...     .where_directory_is("example/")
## ...     .where_database_is("main")
## ...     .where_record_years_between(None, None)
## ...     .where_record_citations_between(None, None)
## ...     .where_records_match(None)
## ...     #
## ...     .build()
## ... )
--INFO-- Paths computed.
--INFO-- Points per link computed.
--INFO-- Points per path computed.
## >>> # chart.write_html("sphinx/_static/main_path_analysis/network_plot.html")

.. raw:: html

    <iframe src="../_static/main_path_analysis/network_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import networkx as nx  # type: ignore

from ....internals.nx.assign_constant_to_edge_colors import (
    internal__assign_constant_to_edge_colors,
)
from ....internals.nx.assign_constant_to_node_colors import (
    internal__assign_constant_to_node_colors,
)
from ....internals.nx.assign_edge_widths_based_on_weight import (
    internal__assign_edge_widths_based_on_weight,
)
from ....internals.nx.assign_node_sizes_based_on_citations import (
    internal__assign_node_sizes_based_on_citations,
)
from ....internals.nx.assign_text_positions_based_on_quadrants import (
    internal__assign_text_positions_based_on_quadrants,
)
from ....internals.nx.assign_textfont_opacity_based_on_citations import (
    internal__assign_textfont_opacity_based_on_citations,
)
from ....internals.nx.assign_textfont_sizes_based_on_citations import (
    internal__assign_textfont_sizes_based_on_citations,
)
from ....internals.nx.compute_spring_layout_positions import (
    internal__compute_spring_layout_positions,
)
from ....internals.nx.create_network_plot import internal__create_network_plot
from .network_edges_dataframe import network_edges_frame


def network_plot(
    #
    # COLUMN PARAMS:
    top_n=None,
    citations_threshold=0,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_range=(30, 70),
    textfont_size_range=(10, 20),
    textfont_opacity_range=(0.35, 1.00),
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_range=(0.8, 3.0),
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    #
    # Creates a table with citing and cited articles
    data_frame = network_edges_frame(
        #
        # COLUMN PARAMS:
        top_n=top_n,
        citations_threshold=citations_threshold,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Create the networkx graph
    nx_graph = nx.Graph()

    #
    # Adds the links to the network:
    for _, row in data_frame.iterrows():
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row.citing_article, row.cited_article, row.points)],
            dash="solid",
        )

    #
    # Sets the layout
    nx_graph = internal__assign_constant_to_node_colors(nx_graph, "#7793a5")

    nx_graph = internal__compute_spring_layout_positions(
        nx_graph, nx_k, nx_iterations, nx_random_state
    )

    nx_graph = internal__assign_node_sizes_based_on_citations(nx_graph, node_size_range)
    nx_graph = internal__assign_textfont_sizes_based_on_citations(
        nx_graph, textfont_size_range
    )
    nx_graph = internal__assign_textfont_opacity_based_on_citations(
        nx_graph, textfont_opacity_range
    )

    #
    # Sets the edge attributes
    nx_graph = internal__assign_edge_widths_based_on_weight(nx_graph, edge_width_range)
    nx_graph = internal__assign_text_positions_based_on_quadrants(nx_graph)
    nx_graph = internal__assign_constant_to_edge_colors(nx_graph, edge_color)

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    return internal__create_network_plot(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        xaxes_range=None,
        yaxes_range=None,
        show_axes=False,
        #
        # ARROWS:
        draw_arrows=True,
    )
