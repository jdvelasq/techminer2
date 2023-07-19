# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tlab_co_occurrence_analysis_word_associations_radial_diagram:

Radial Diagram
===============================================================================

A radial diagram is a visualization technique that displays the associations
between a term and other terms in a co-occurrence matrix. The radial diagram
is a network graph in which the nodes are the terms and the edges are the
co-occurrence between the terms. The radial diagram is a useful tool for
identifying the most relevant terms associated with a given term.


>>> from techminer2 import tlab
>>> root_dir = "data/regtech/"
>>> associations = tlab.co_occurrence_analysis.word_associations.radial_diagram(
...     item="REGTECH", 
...     columns='author_keywords',
...     col_top_n=20,
...     root_dir=root_dir,
... ).write_html("sphinx/_static/tlab/co_occurrence_analysis/word_associations/radial_diagram.html")

.. raw:: html

    <iframe src="../../../../../_static/tlab/co_occurrence_analysis/word_associations/radial_diagram.html" 
    height="600px" width="100%" frameBorder="0"></iframe>


"""
import networkx as nx

from ....vosviewer.nx_compute_edge_width_from_edge_weight import (
    nx_compute_edge_width_from_edge_weight,
)
from ....vosviewer.nx_compute_node_size_from_item_occ import nx_compute_node_size_from_item_occ
from ....vosviewer.nx_compute_spring_layout import nx_compute_spring_layout
from ....vosviewer.nx_compute_textfont_opacity_from_item_occ import (
    nx_compute_textfont_opacity_from_item_occ,
)
from ....vosviewer.nx_compute_textfont_size_from_item_occ import (
    nx_compute_textfont_size_from_item_occ,
)
from ....vosviewer.nx_compute_textposition_from_graph import nx_compute_textposition_from_graph
from ....vosviewer.nx_set_edge_color_to_constant import nx_set_edge_color_to_constant
from ....vosviewer.nx_visualize_graph import nx_visualize_graph
from .item_associations import item_associations


def radial_diagram(
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
    """Plots a radial diagram."""

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
    nx_graph = nx_compute_spring_layout(nx_graph, nx_k, nx_iterations, nx_random_state)

    #
    # Sets the node attributes
    # nx_graph = nx_set_node_color_from_group_attr(nx_graph)
    nx_graph = nx_compute_node_size_from_item_occ(nx_graph, node_size_min, node_size_max)
    nx_graph = nx_compute_textfont_size_from_item_occ(
        nx_graph, textfont_size_min, textfont_size_max
    )
    nx_graph = nx_compute_textfont_opacity_from_item_occ(
        nx_graph, textfont_opacity_min, textfont_opacity_max
    )

    #
    # Sets the edge attributes
    nx_graph = nx_compute_edge_width_from_edge_weight(nx_graph, edge_width_min, edge_width_max)
    nx_graph = nx_compute_textposition_from_graph(nx_graph)
    nx_graph = nx_set_edge_color_to_constant(nx_graph, edge_color)

    return nx_visualize_graph(
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
