# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
"""
Radial Diagram
===============================================================================

A radial diagram is a visualization technique that displays the associations
between a term and other terms in a co-occurrence matrix. The radial diagram
is a network graph in which the nodes are the terms and the edges are the
co-occurrence between the terms. The radial diagram is a useful tool for
identifying the most relevant terms associated with a given term.


# >>> from techminer2.co_occurrence_analysis.associations.graphs import radial_diagram
# >>> radial_diagram(
# ...     #
# ...     # FUNCTION PARAMS:
# ...     item="REGTECH", 
# ...     #
# ...     # CO-OCC PARAMS:
# ...     columns='author_keywords',
# ...     rows=None,
# ...     #
# ...     # LAYOUT:
# ...     nx_k=None,
# ...     nx_iterations=30,
# ...     nx_random_state=0,
# ...     #
# ...     # NODES:
# ...     node_size_min=30,
# ...     node_size_max=70,
# ...     textfont_size_min=10,
# ...     textfont_size_max=20,
# ...     textfont_opacity_min=0.35,
# ...     textfont_opacity_max=1.00,
# ...     #
# ...     # EDGES:
# ...     edge_color="#7793a5",
# ...     edge_width_min=0.8,
# ...     edge_width_max=3.0,
# ...     #
# ...     # AXES:
# ...     xaxes_range=None,
# ...     yaxes_range=None,
# ...     show_axes=False,
# ...     #
# ...     # COLUMN PARAMS:
# ...     col_top_n=20,
# ...     col_occ_range=(None, None),
# ...     col_gc_range=(None, None),
# ...     col_custom_items=None,
# ...     #
# ...     # ROW PARAMS:
# ...     row_top_n=None,
# ...     row_occ_range=(None, None),
# ...     row_gc_range=(None, None),
# ...     row_custom_items=None,
# ...     #
# ...     # DATABASE PARAMS:
# ...     root_dir="example/", 
# ...     database="main",
# ...     year_filter=(None, None),
# ...     cited_by_filter=(None, None),
# ... ).write_html("sphinx/_static/co_occurrence_analysis/associations/radial_diagram.html")

# .. raw:: html

#     <iframe src="../../../../../../_static/co_occurrence_analysis/associations/radial_diagram.html" 
#     height="600px" width="100%" frameBorder="0"></iframe>


"""
import networkx as nx

from ...tools.associations.item_associations import item_associations
from .assign_opacity_to_text_based_on_frequency import assign_opacity_to_text_based_on_frequency
from .assign_sizes_to_nodes_based_on_occurrences import assign_sizes_to_nodes_based_on_occurrences
from .assign_text_positions_to_nodes_by_quadrants import assign_text_positions_to_nodes_by_quadrants
from .assign_textfont_sizes_to_nodes_based_on_occurrences import assign_textfont_sizes_to_nodes_based_on_occurrences
from .assign_uniform_color_to_edges import assign_uniform_color_to_edges
from .assign_widths_to_edges_based_on_weight import assign_widths_to_edges_based_on_weight
from .compute_spring_layout_positions import compute_spring_layout_positions
from .plot_networkx_graph import plot_networkx_graph


def nx_radial_diagram(
    #
    # FUNCTION PARAMS:
    item,
    #
    # CO-OCC PARAMS:
    columns,
    rows=None,
    #
    # LAYOUT:
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    #
    # NODES:
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    textfont_opacity_min=0.35,
    textfont_opacity_max=1.00,
    #
    # EDGES:
    edge_color="#7793a5",
    edge_width_min=0.8,
    edge_width_max=3.0,
    #
    # AXES:
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Plots a radial diagram.

    :meta private:
    """

    associations = item_associations(
        #
        # FUNCTION PARAMS:
        item=item,
        #
        # CO-OCC PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    ).df_

    #
    # Create the networkx graph
    nx_graph = nx.Graph()
    nx_graph = __add_nodes_from(nx_graph, associations)
    nx_graph = __add_weighted_edges_from(nx_graph, associations)

    #
    # Sets the layout
    nx_graph = compute_spring_layout_positions(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    # nx_graph = nx_set_node_color_from_group_attr(nx_graph)
    nx_graph = assign_sizes_to_nodes_based_on_occurrences(nx_graph, node_size_min, node_size_max)
    nx_graph = assign_textfont_sizes_to_nodes_based_on_occurrences(nx_graph, textfont_size_min, textfont_size_max)
    nx_graph = assign_opacity_to_text_based_on_frequency(nx_graph, textfont_opacity_min, textfont_opacity_max)

    #
    # Sets the edge attributes
    nx_graph = assign_widths_to_edges_based_on_weight(nx_graph, edge_width_min, edge_width_max)
    nx_graph = assign_text_positions_to_nodes_by_quadrants(nx_graph)
    nx_graph = assign_uniform_color_to_edges(nx_graph, edge_color)

    return plot_networkx_graph(
        #
        # FUNCTION PARAMS:
        nx_graph=nx_graph,
        #
        # NETWORK PARAMS:
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
        show_axes=show_axes,
    )


def __add_nodes_from(
    nx_graph,
    associations,
):
    associations = associations.copy()

    #
    # Adds the rows with  group=0
    nodes = associations.index.tolist()
    nx_graph.add_nodes_from(nodes, group=0, node_color="#7793a5")

    #
    # Adds the column with  group=1
    node = [associations.columns[0]]
    nx_graph.add_nodes_from(node, group=1, node_color="#465c6b")

    #
    # sets the labels of nodes
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["text"] = node

    return nx_graph


def __add_weighted_edges_from(
    nx_graph,
    associations,
):
    associations = associations.copy()
    item = associations.columns[0]

    for row in associations.index.tolist():
        weight = associations.loc[row][0]
        nx_graph.add_weighted_edges_from(
            ebunch_to_add=[(row, item, weight)],
            dash="solid",
        )

    return nx_graph
