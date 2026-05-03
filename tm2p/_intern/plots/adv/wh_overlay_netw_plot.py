import networkx as nx  # type: ignore
import pandas as pd  # type: ignore
import plotly.graph_objects as go  # type: ignore

from tm2p._intern import Params
from tm2p._intern.helpers import color
from tm2p._intern.helpers.mtx_to_mtx_list import matrix_to_matrix_list

from ..nx import (
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
    set_edge_invisible,
    set_edge_width_from_pandas_adjacency,
    set_node_color_by_group,
    set_node_group,
    set_node_opacity,
    set_node_size_properties,
    set_node_textposition,
    set_top_n_node_labels,
    set_uniform_edge_color,
    set_uniform_edge_line_style,
    spring_layout,
)


def build_wh_overlay_network_plot(
    params: Params,
    similarity_matrix: pd.DataFrame,
    co_occurrence_matrix: pd.DataFrame,
    white_space_matrix: pd.DataFrame,
    i2c: dict[str, int],
) -> go.Figure:

    nx_graph = nx.from_pandas_adjacency(similarity_matrix)
    nx_graph = remove_selfloop_edges(nx_graph)
    nx_graph = set_node_size_properties(params, nx_graph, co_occurrence_matrix)
    nx_graph = set_node_group(nx_graph, i2c)

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
    nx_graph = set_node_color_by_group(params, nx_graph)
    nx_graph = set_node_opacity(params, nx_graph)
    nx_graph = set_node_textposition(nx_graph)

    #
    nx_graph = set_edge_invisible(nx_graph)
    nx_graph = set_edge_width_from_pandas_adjacency(nx_graph, white_space_matrix)
    nx_graph = set_uniform_edge_color(params, nx_graph)
    #

    nx_graph = scale_edge_width(params, nx_graph)
    nx_graph = scale_edge_opacity(params, nx_graph)
    nx_graph = set_uniform_edge_line_style(nx_graph, "solid")

    node_trace = build_scatter_node_trace(nx_graph)
    edge_traces = build_scatter_edge_traces(nx_graph)

    nx_graph = set_emergent_node_labels(nx_graph, white_space_matrix)

    fig = build_network_plot(edge_traces, node_trace)
    fig = configure_figure_axes(params, fig)
    fig = add_node_labels(fig, nx_graph)

    return fig


def set_emergent_node_labels(
    nx_graph: nx.Graph, white_space_matrix: pd.DataFrame
) -> nx.Graph:

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["labeled"] = False

    matrix_list = matrix_to_matrix_list(white_space_matrix, "WEIGHT")
    matrix_list = matrix_list.loc[matrix_list["WEIGHT"] > 0, :]
    for _, row in matrix_list.iterrows():

        node_a = row["ROWS"]
        node_b = row["COLUMNS"]
        if node_a in nx_graph.nodes():
            nx_graph.nodes[node_a]["labeled"] = True
        if node_b in nx_graph.nodes():
            nx_graph.nodes[node_b]["labeled"] = True

    return nx_graph


# def build_edge_traces(
#     params: Params,
#     nx_graph: nx.Graph,
#     white_space_matrix: pd.DataFrame,
# ) -> list[go.Scatter]:

#     edge_traces = []
#     data = []

#     matrix_list = matrix_to_matrix_list(white_space_matrix, "WEIGHT")
#     matrix_list = matrix_list.loc[matrix_list["WEIGHT"] > 0, :]

#     for _, row in matrix_list.iterrows():

#         node_a = row["ROWS"]
#         node_b = row["COLUMNS"]
#         if node_a not in nx_graph.nodes() or node_b not in nx_graph.nodes():
#             continue

#         pos_x0 = nx_graph.nodes[node_a]["x"]
#         pos_y0 = nx_graph.nodes[node_a]["y"]

#         pos_x1 = nx_graph.nodes[node_b]["x"]
#         pos_y1 = nx_graph.nodes[node_b]["y"]

#         edge = (row["ROWS"], row["COLUMNS"])

#         edge_trace = go.Scatter(
#             x=(pos_x0, pos_x1),
#             y=(pos_y0, pos_y1),
#             line={
#                 "color": "#505050",
#                 "dash": "solid",
#                 "width": 2.0,
#             },
#             hoverinfo="none",
#             mode="lines",
#             opacity=0.2,
#         )

#         data.append((edge_trace, 1.0))

#     # ---

#     # for edge in nx_graph.edges():

#     #     pos_x0 = nx_graph.nodes[edge[0]]["x"]
#     #     pos_y0 = nx_graph.nodes[edge[0]]["y"]

#     #     pos_x1 = nx_graph.nodes[edge[1]]["x"]
#     #     pos_y1 = nx_graph.nodes[edge[1]]["y"]

#     #     dash = nx_graph.edges[edge]["dash"]
#     #     width = nx_graph.edges[edge]["width"]

#     #     edge_trace = go.Scatter(
#     #         x=(pos_x0, pos_x1),
#     #         y=(pos_y0, pos_y1),
#     #         line={
#     #             "color": "gainsboro",
#     #             "dash": dash,
#     #             "width": 1.0,
#     #         },
#     #         hoverinfo="none",
#     #         mode="lines",
#     #         opacity=0.6,
#     #     )

#     #     data.append((edge_trace, width))

#     data = sorted(data, key=lambda x: x[1])
#     edge_traces = [x[0] for x in data]

#     return edge_traces
