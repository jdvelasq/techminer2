# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import networkx as nx


def nx_compute_spring_layout(nx_graph, k, iterations, seed):
    """Computes the layout of a networkx graph."""

    pos = nx.spring_layout(nx_graph, k=k, iterations=iterations, seed=seed)
    for node in nx_graph.nodes():
        nx_graph.nodes[node]["x"] = pos[node][0]
        nx_graph.nodes[node]["y"] = pos[node][1]
    return nx_graph
