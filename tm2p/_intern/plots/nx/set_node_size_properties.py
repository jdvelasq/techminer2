import networkx as nx  # type: ignore
import pandas as pd  # type: ignore

from tm2p._intern import Params
from tm2p.enum import NodeSizeMetric


def set_node_size_properties(
    params: Params,
    nx_graph: nx.Graph,
    co_occurrence_matrix: pd.DataFrame,
) -> nx.Graph:

    matrix = co_occurrence_matrix.copy()
    matrix = _set_diagonal_to_zero(matrix)

    nx_graph = _set_occurrences(nx_graph)
    nx_graph = _set_links(nx_graph, matrix)
    nx_graph = _set_tls(nx_graph, matrix)

    nx_graph = _set_node_raw_size(params, nx_graph)

    return nx_graph


def _set_node_raw_size(params, nx_graph):

    if "node_size_metric" not in params.__dict__:
        return nx_graph

    if params.node_size_metric == NodeSizeMetric.OCC:
        metric = "OCC"
    elif params.node_size_metric == NodeSizeMetric.LINKS:
        metric = "LINKS"
    elif params.node_size_metric == NodeSizeMetric.TLS:
        metric = "TLS"
    else:
        raise ValueError(f"Unsupported node size metric: {params.node_size_metric}")

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["raw_node_size"] = nx_graph.nodes[node][metric]

    return nx_graph


def _set_tls(nx_graph, matrix):

    tls = matrix.sum(axis=1).to_dict()
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["TLS"] = tls[node]

    return nx_graph


def _set_links(nx_graph, matrix):

    matrix = matrix.copy()
    matrix = matrix.map(lambda x: 1 if x > 0 else 0)
    links = matrix.sum(axis=1).to_dict()
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["LINKS"] = links[node]
    return nx_graph


def _set_occurrences(nx_graph):
    for node in nx_graph.nodes():
        occ = int(node.split(" ")[-1].split(":")[0])
        nx_graph.nodes[node]["OCC"] = occ
    return nx_graph


def _set_diagonal_to_zero(matrix):
    for col in matrix.columns:
        matrix.loc[col, col] = 0
    return matrix
