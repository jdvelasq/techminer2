import networkx as nx  # type: ignore
import pandas as pd  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import Params

from ..nx import (
    add_node_labels,
    build_network_figure,
    build_scatter_edge_traces,
    build_scatter_node_trace,
    configure_figure_axes,
    keep_top_k_edges_per_node,
    remove_isolated_nodes,
    remove_selfloop_edges,
    remove_weak_nodes,
    scale_edge_weight,
    scale_edge_width,
    scale_node_size,
    scale_textfont_opacity,
    scale_textfont_size,
    set_node_textposition,
    set_top_n_node_labels,
    set_uniform_edge_color,
    set_uniform_edge_line_style,
    set_uniform_node_color,
    spring_layout,
)


def build_co_occ_matrix_plot(
    params: Params,
    matrix: pd.DataFrame,
) -> go.Figure:

    nx_graph = nx.from_pandas_adjacency(matrix)

    nx_graph = remove_selfloop_edges(nx_graph)
    nx_graph = remove_isolated_nodes(nx_graph)
    nx_graph = keep_top_k_edges_per_node(params, nx_graph)
    nx_graph = remove_weak_nodes(params, nx_graph)

    nx_graph = set_top_n_node_labels(
        nx_graph,
        matrix.columns.to_list(),
        params.max_node_labels,
    )

    nx_graph = scale_edge_weight(params, nx_graph)
    nx_graph = spring_layout(params, nx_graph)
    nx_graph = scale_node_size(params, nx_graph)
    nx_graph = scale_textfont_size(params, nx_graph)
    nx_graph = scale_textfont_opacity(params, nx_graph)
    nx_graph = set_uniform_node_color(params, nx_graph)
    nx_graph = set_uniform_edge_color(params, nx_graph)
    nx_graph = scale_edge_width(params, nx_graph)
    nx_graph = set_node_textposition(nx_graph)

    nx_graph = set_uniform_edge_line_style(nx_graph, "solid")

    node_trace = build_scatter_node_trace(nx_graph)
    edge_traces = build_scatter_edge_traces(nx_graph)

    fig = build_network_figure(edge_traces, node_trace)
    fig = configure_figure_axes(params, fig)
    fig = add_node_labels(fig, nx_graph)

    return fig
