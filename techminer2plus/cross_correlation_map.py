# flake8: noqa
# pylint: disable=line-too-long
"""
.. _cross_correlation_map:

Cross-correlation Map
===============================================================================

Creates an Cross-correlation Map.

* Preparation

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p


* Object oriented interface

>>> fig = (
...     tm2p.records(root_dir=root_dir)
...     .cross_correlation_matrix(
...         rows_and_columns='authors', 
...         cross_with='countries',
...         top_n=10,
...     )
...     .cross_correlation_map(
...         color="#1f77b4", # tab:blue
...     )
...     .write_html("sphinx/_static/cross_correlation_map_0.html")
... )

.. raw:: html

    <iframe src="../../_static/cross_correlation_map_0.html" height="600px" width="100%" frameBorder="0"></iframe>



* Functional interface

>>> file_name = "sphinx/_static/cross_correlation_map.html"


>>> cross_corr_matrix = tm2p.cross_correlation_matrix(
...     rows_and_columns='authors', 
...     cross_with='countries',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> tm2p.cross_correlation_map(
...     cross_corr_matrix,
...     color="#1f77b4", # tab:blue
... ).write_html("sphinx/_static/cross_correlation_map_1.html")

.. raw:: html

    <iframe src="../../_static/cross_correlation_map_1.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ._network_lib import (
    nx_compute_spring_layout,
    nx_create_graph_from_matrix,
    nx_set_edge_properties_for_corr_maps,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def cross_correlation_map(
    cross_corr_matrix,
    #
    # Map params:
    n_labels=None,
    color="#8da4b4",
    nx_k=None,
    nx_iterations=10,
    nx_random_state=0,
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
    show_axes=False,
):
    """Correlation map."""

    graph = nx_create_graph_from_matrix(
        cross_corr_matrix,
        node_size_min,
        node_size_max,
        textfont_size_min,
        textfont_size_max,
    )

    for node in graph.nodes():
        graph.nodes[node]["color"] = color

    graph = nx_set_edge_properties_for_corr_maps(graph, color)

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
