# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _cross_correlation_map:

Cross-correlation Map
===============================================================================

Creates an Cross-correlation Map.

* Preparation

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> file_name = "sphinx/_static/cross_correlation_map.html"
>>> tm2.cross_correlation_map(
...     rows_and_columns='authors', 
...     cross_with='countries',
...     top_n=10,
...     root_dir=root_dir,
...     color="#1f77b4", # tab:blue
... ).write_html("sphinx/_static/cross_correlation_map.html")

.. raw:: html

    <iframe src="../../../../_static/cross_correlation_map.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from ...._network_lib import (
    nx_compute_spring_layout,
    nx_create_graph_from_matrix,
    nx_set_edge_properties_for_corr_maps,
    px_add_names_to_fig_nodes,
    px_create_edge_traces,
    px_create_network_fig,
    px_create_node_trace,
)
from ..matrix.cross_correlation_matrix import cross_correlation_matrix


def cross_correlation_map(
    #
    # FUNCTION PARAMS:
    rows_and_columns,
    cross_with,
    method="pearson",
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
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Correlation map."""

    cross_corr_matrix = cross_correlation_matrix(
        #
        # FUNCTION PARAMS:
        rows_and_columns=rows_and_columns,
        cross_with=cross_with,
        method=method,
        #
        # ITEM PARAMS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
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