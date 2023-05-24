"""
Co-occurrence map
===============================================================================




"""
from dataclasses import dataclass

from ... import network_utils
from ..analyze.list_cells_in_matrix import list_cells_in_matrix


@dataclass(init=False)
class _Chart:
    plot_: None
    graph_: None
    table_: None
    prompt_: None


def co_occ_map(
    matrix,
    method="louvain",
    nx_k=0.5,
    nx_iterations=10,
    node_min_size=30,
    node_max_size=70,
    textfont_size_min=10,
    textfont_size_max=20,
    seed=0,
):
    """Creates and clustering a co-occurrence network."""

    matrix_list = list_cells_in_matrix(matrix)

    graph = network_utils.create_graph(
        matrix_list,
        node_min_size,
        node_max_size,
        textfont_size_min,
        textfont_size_max,
    )

    graph = network_utils.compute_spring_layout(
        graph, nx_k, nx_iterations, seed
    )

    graph = network_utils.apply_community_detection_method(graph, method)

    node_trace = network_utils.create_node_trace(graph)
    text_trace = network_utils.create_text_trace(graph)
    edge_traces = network_utils.create_edge_traces(graph)

    delta = 0
    fig = network_utils.create_network_graph(
        edge_traces, node_trace, text_trace, delta
    )
