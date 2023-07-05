# flake8: noqa
# pylint: disable=line-too-long
"""
.. _auto_correlation_map:

Auto-correlation Map
===============================================================================

Creates an Auto-correlation Map.

* Preparation

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p


* Object oriented interface

>>> fig = (
...     tm2p.records(root_dir=root_dir)
...     .auto_correlation_matrix(
...         rows_and_columns='authors',
...         occ_range=(2, None),
...     )
...     .auto_correlation_map()
... )


* Functional interface

>>> auto_corr_matrix = tm2p.auto_correlation_matrix(
...     rows_and_columns='authors',
...     occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> fig =  tm2p.auto_correlation_map(
...     auto_corr_matrix,
...     color="#1f77b4", # tab:blue
... )

* Results    

>>> file_name = "sphinx/_static/auto_correlation_map.html"
>>> fig.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/auto_correlation_map.html" height="600px" width="100%" frameBorder="0"></iframe>


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
def auto_correlation_map(
    #
    # FUNCTION PARAMS:
    auto_corr_matrix,
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
    """Auto-correlation Map."""

    graph = nx_create_graph_from_matrix(
        auto_corr_matrix,
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
