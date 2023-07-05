# flake8: noqa
# pylint: disable=line-too-long
"""
Radial Diagram
===============================================================================

A radial diagram is a visualization technique that displays the associations
between a term and other terms in a co-occurrence matrix. The radial diagram
is a network graph in which the nodes are the terms and the edges are the
co-occurrence between the terms. The radial diagram is a useful tool for
identifying the most relevant terms associated with a given term.


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"


* Object oriented interface

>>> fig = (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .item_associations(item="REGTECH") 
...     .radial_diagram()
... )

* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> associations = tm2p.item_associations(
...     item="REGTECH", 
...     cooc_matrix=cooc_matrix,
... )
>>> fig = tm2p.radial_diagram(associations)


* Results:

>>> fig.write_html("sphinx/_static/radial_diagram.html")

.. raw:: html

    <iframe src="../../_static/radial_diagram.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import networkx as nx

from ._network_lib import (
    nx_compute_node_property_from_occ,
    nx_compute_spring_layout,
    nx_create_node_occ_property_from_node_name,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def radial_diagram(
    item_associations,
    #
    # Figure params:
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
    series = item_associations.df_.iloc[:, 0].copy()
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
