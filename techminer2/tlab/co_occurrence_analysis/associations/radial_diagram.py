# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Radial Diagram
===============================================================================

A radial diagram is a visualization technique that displays the associations
between a term and other terms in a co-occurrence matrix. The radial diagram
is a network graph in which the nodes are the terms and the edges are the
co-occurrence between the terms. The radial diagram is a useful tool for
identifying the most relevant terms associated with a given term.


>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"
>>> tm2.radial_diagram(
...     item="REGTECH", 
...     columns='author_keywords',
...     col_top_n=20,
...     root_dir=root_dir,
... ).write_html("sphinx/_static/radial_diagram.html")

.. raw:: html

    <iframe src="../../../../../_static/radial_diagram.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import networkx as nx

from ...._network_lib import (
    nx_compute_node_property_from_occ,
    nx_compute_spring_layout,
    nx_create_node_occ_property_from_node_name,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)
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
    # CHART PARAMS:
    n_labels=None,
    nx_k=None,
    nx_iterations=30,
    nx_random_state=0,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
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

    def create_graph(
        name,
        series,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    ):
        """Creates a networkx graph."""
        graph = nx.Graph()

        # Adds the central item
        nodes = [
            (name, {"group": 0, "color": "#556f81", "textfont_color": "black"})
        ]

        # Adds the items in the column as nodes
        nodes += [
            (
                index,
                {"group": 1, "color": "#8da4b4", "textfont_color": "black"},
            )
            for index in series.index.to_list()
        ]
        graph.add_nodes_from(nodes)

        # Sets node properties
        graph = nx_create_node_occ_property_from_node_name(graph)
        graph = nx_compute_node_property_from_occ(
            graph, "node_size", node_size_min, node_size_max
        )
        graph = nx_compute_node_property_from_occ(
            graph, "textfont_size", textfont_size_min, textfont_size_max
        )

        for index, value in series.items():
            graph.add_edges_from(
                [(name, index)],
                value=value,
                width=2,
                dash="solid",
                color="#8da4b4",
            )

        return graph

    #
    # MAIN CODE:
    #
    data_frame = item_associations_table(
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
    )

    series = data_frame.iloc[:, 0].copy()
    name = series.name

    graph = create_graph(
        name=name,
        series=series,
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
    )

    graph = nx_compute_spring_layout(
        graph, nx_k, nx_iterations, nx_random_state
    )

    node_trace = px_create_node_trace(graph)
    edge_traces = px_create_edge_traces(graph)

    fig = px_create_network_fig(
        edge_traces,
        node_trace,
        xaxes_range,
        yaxes_range,
        show_axes,
    )

    fig = px_add_names_to_fig_nodes(fig, graph, n_labels, is_article=False)

    return fig
