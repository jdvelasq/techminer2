import networkx as nx  # type: ignore
import pandas as pd  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import Params

from ..nx import (
    add_node_labels,
    build_density_plot,
    build_heatmap_trace,
    configure_figure_axes,
    keep_top_k_edges_per_node,
    keep_top_n_edges,
    keep_top_n_nodes,
    remove_isolated_nodes,
    remove_selfloop_edges,
    remove_weak_nodes,
    scale_edge_weight,
    scale_textfont_opacity,
    scale_textfont_size,
    set_density_textposition,
    set_node_group,
    set_node_size_properties,
    set_top_n_node_labels,
    spring_layout,
)


def build_co_occ_density_plot(
    params: Params,
    similarity_matrix: pd.DataFrame,
    co_occurrence_matrix: pd.DataFrame,
    i2c: dict[str, int],
) -> go.Figure:

    nx_graph = nx.from_pandas_adjacency(similarity_matrix)
    nx_graph = remove_selfloop_edges(nx_graph)
    nx_graph = set_node_size_properties(params, nx_graph, co_occurrence_matrix)
    nx_graph = set_node_group(nx_graph, i2c)

    nx_graph = remove_isolated_nodes(nx_graph)
    nx_graph = keep_top_k_edges_per_node(params, nx_graph)
    nx_graph = keep_top_n_edges(params, nx_graph)
    nx_graph = remove_weak_nodes(params, nx_graph)
    nx_graph = keep_top_n_nodes(params, nx_graph)

    nx_graph = set_top_n_node_labels(
        params=params,
        nx_graph=nx_graph,
    )

    nx_graph = scale_edge_weight(params, nx_graph)
    nx_graph = spring_layout(params, nx_graph)

    nx_graph = scale_textfont_size(params, nx_graph)
    nx_graph = scale_textfont_opacity(params, nx_graph)

    nx_graph = set_density_textposition(nx_graph)

    contour_trace = build_heatmap_trace(params, nx_graph)

    fig = build_density_plot(contour_trace)
    fig = configure_figure_axes(params, fig)
    fig = add_node_labels(fig, nx_graph)

    return fig
