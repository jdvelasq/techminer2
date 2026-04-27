from typing import Union

import networkx as nx  # type: ignore
import pandas as pd  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import Params

from ..nx import (
    add_node_colorscale,
    add_node_labels,
    build_network_plot,
    build_scatter_edge_traces,
    build_scatter_node_trace,
    configure_figure_axes,
    keep_top_k_edges_per_node,
    keep_top_n_edges,
    keep_top_n_nodes,
    remove_isolated_nodes,
    remove_selfloop_edges,
    remove_weak_nodes,
    scale_edge_opacity,
    scale_edge_weight,
    scale_edge_width,
    scale_node_size,
    scale_textfont_opacity,
    scale_textfont_size,
    set_edge_color_by_group,
    set_edge_width_from_pandas_adjacency,
    set_node_color_by_year,
    set_node_group,
    set_node_opacity,
    set_node_size_properties,
    set_node_textposition,
    set_node_year,
    set_top_n_node_labels,
    set_uniform_edge_line_style,
    spring_layout,
)


def build_co_occ_overlay_plot(
    params: Params,
    similarity_matrix: pd.DataFrame,
    co_occurrence_matrix: pd.DataFrame,
    i2c: dict[str, int],
    i2y: dict[str, Union[int, float]],
) -> go.Figure:

    nx_graph = nx.from_pandas_adjacency(similarity_matrix)
    nx_graph = remove_selfloop_edges(nx_graph)
    nx_graph = set_node_size_properties(params, nx_graph, co_occurrence_matrix)
    nx_graph = set_node_group(nx_graph, i2c)
    nx_graph = set_node_year(nx_graph, i2y)

    nx_graph = keep_top_k_edges_per_node(params, nx_graph)
    nx_graph = keep_top_n_edges(params, nx_graph)
    nx_graph = remove_weak_nodes(params, nx_graph)
    nx_graph = keep_top_n_nodes(params, nx_graph)
    nx_graph = remove_isolated_nodes(nx_graph)

    nx_graph = set_top_n_node_labels(
        params=params,
        nx_graph=nx_graph,
    )

    nx_graph = scale_edge_weight(params, nx_graph)
    nx_graph = spring_layout(params, nx_graph)
    nx_graph = scale_node_size(params, nx_graph)
    nx_graph = scale_textfont_size(params, nx_graph)
    nx_graph = scale_textfont_opacity(params, nx_graph)

    nx_graph = set_node_color_by_year(params, nx_graph)
    nx_graph = set_edge_color_by_group(params, nx_graph)

    nx_graph = set_node_opacity(params, nx_graph)

    nx_graph = set_edge_width_from_pandas_adjacency(nx_graph, co_occurrence_matrix)
    nx_graph = scale_edge_width(params, nx_graph)
    nx_graph = scale_edge_opacity(params, nx_graph)

    nx_graph = set_node_textposition(nx_graph)

    nx_graph = set_uniform_edge_line_style(nx_graph, "solid")

    node_trace = build_scatter_node_trace(nx_graph)
    edge_traces = build_scatter_edge_traces(nx_graph)

    fig = build_network_plot(edge_traces, node_trace)
    fig = configure_figure_axes(params, fig)
    fig = add_node_labels(fig, nx_graph)
    fig = add_node_colorscale(params, fig, nx_graph)

    return fig
