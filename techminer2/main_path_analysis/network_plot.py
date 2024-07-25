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

>>> from techminer2.main_path_analysis import network_plot
>>> chart = network_plot(
...     #
...     # COLUMN PARAMS:
...     top_n=None,
...     citations_threshold=0,
...     #
...     # LAYOUT:
...     nx_k=None,
...     nx_iterations=30,
...     nx_random_state=0,
...     #
...     # NODES:
...     node_size_range=(30, 70),
...     textfont_size_range=(10, 20),
...     textfont_opacity_range=(0.35, 1.00),
...     #
...     # EDGES:
...     edge_color="#7793a5",
...     edge_width_range=(0.8, 3.0),
...     #
...     # DATABASE PARAMS:
...     root_dir="example/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
--INFO-- Paths computed.
--INFO-- Points per link computed.
--INFO-- Points per path computed.
>>> # chart.write_html("sphinx/_static/main_path_analysis/network_plot.html")

.. raw:: html

    <iframe src="../_static/main_path_analysis/network_plot.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import networkx as nx  # type: ignore

from .._core.nx.nx_assign_constant_color_to_nodes import nx_assign_constant_color_to_nodes
from .._core.nx.nx_assign_opacity_to_text_based_on_citations import nx_assign_opacity_to_text_based_on_citations
from .._core.nx.nx_assign_sizes_to_nodes_based_on_citations import nx_assign_sizes_to_nodes_based_on_citations
from .._core.nx.nx_assign_text_positions_to_nodes_by_quadrants import nx_assign_text_positions_to_nodes_by_quadrants
from .._core.nx.nx_assign_textfont_sizes_to_nodes_based_on_citations import nx_assign_textfont_sizes_to_nodes_based_on_citations
from .._core.nx.nx_assign_uniform_color_to_edges import nx_assign_uniform_color_to_edges
from .._core.nx.nx_assign_widths_to_edges_based_on_weight import nx_assign_widths_to_edges_based_on_weight
from .._core.nx.nx_compute_spring_layout_positions import nx_compute_spring_layout_positions
from .._core.nx.nx_network_plot import nx_network_plot
from .network_edges_frame import network_edges_frame


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
    nx_graph = nx_assign_constant_color_to_nodes(nx_graph, "#7793a5")
    nx_graph = nx_compute_spring_layout_positions(nx_graph, nx_k, nx_iterations, nx_random_state)
    nx_graph = nx_assign_sizes_to_nodes_based_on_citations(nx_graph, node_size_range)
    nx_graph = nx_assign_textfont_sizes_to_nodes_based_on_citations(nx_graph, textfont_size_range)
    nx_graph = nx_assign_opacity_to_text_based_on_citations(nx_graph, textfont_opacity_range)

    #
    # Sets the edge attributes
    nx_graph = nx_assign_widths_to_edges_based_on_weight(nx_graph, edge_width_range)
    nx_graph = nx_assign_text_positions_to_nodes_by_quadrants(nx_graph)
    nx_graph = nx_assign_uniform_color_to_edges(nx_graph, edge_color)

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    return nx_network_plot(
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
