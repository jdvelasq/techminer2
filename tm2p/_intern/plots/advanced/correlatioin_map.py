import networkx as nx  # type: ignore
import pandas as pd  # type: ignore
import plotly.graph_objects as go  # type: ignore
from sklearn.metrics.pairwise import cosine_similarity  # type: ignore

from tm2p._intern import Params
from tm2p.enum import Correlation

from ..nx import (
    add_node_labels,
    build_network_figure,
    build_scatter_edge_traces,
    build_scatter_node_trace,
    configure_figure_axes,
    keep_top_k_edges_per_node,
    remove_edges_below_similarity_threshold,
    remove_isolated_nodes,
    remove_selfloop_edges,
    remove_weak_nodes,
    scale_edge_weight,
    scale_node_size_by_occ,
    scale_textfont_opacity_by_occ,
    scale_textfont_size_by_occ,
    set_node_textposition,
    set_top_n_node_labels,
    set_uniform_node_color,
    spring_layout,
    style_edges_by_weight_bins,
)


def build_correlation_map(
    params: Params,
    matrix: pd.DataFrame,
) -> go.Figure:

    if params.correlation_method != Correlation.COSINE:

        matrix = pd.DataFrame(
            cosine_similarity(matrix),
            index=matrix.index,
            columns=matrix.columns,
        )

    nx_graph = nx.from_pandas_adjacency(matrix)

    nx_graph = remove_selfloop_edges(nx_graph)
    nx_graph = remove_isolated_nodes(nx_graph)
    nx_graph = remove_edges_below_similarity_threshold(params, nx_graph)
    nx_graph = keep_top_k_edges_per_node(params, nx_graph)
    nx_graph = remove_weak_nodes(params, nx_graph)

    nx_graph = set_top_n_node_labels(
        nx_graph,
        matrix.columns.to_list(),
        params.max_node_labels,
    )

    nx_graph = style_edges_by_weight_bins(params, nx_graph)
    nx_graph = scale_edge_weight(params, nx_graph)
    nx_graph = spring_layout(params, nx_graph)
    nx_graph = scale_node_size_by_occ(params, nx_graph)
    nx_graph = scale_textfont_size_by_occ(params, nx_graph)
    nx_graph = scale_textfont_opacity_by_occ(params, nx_graph)
    nx_graph = set_uniform_node_color(params, nx_graph)

    nx_graph = set_node_textposition(nx_graph)

    node_trace = build_scatter_node_trace(nx_graph)
    edge_traces = build_scatter_edge_traces(nx_graph)

    fig = build_network_figure(edge_traces, node_trace)
    fig = configure_figure_axes(params, fig)
    fig = add_node_labels(fig, nx_graph)

    return fig
