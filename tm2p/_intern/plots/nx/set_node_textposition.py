import networkx as nx  # type: ignore
import numpy as np


def set_node_textposition(
    nx_graph: nx.Graph,
) -> nx.Graph:

    node_x = [data["x"] for _, data in nx_graph.nodes(data=True)]
    node_y = [data["y"] for _, data in nx_graph.nodes(data=True)]

    x_mean = np.mean(node_x)
    y_mean = np.mean(node_y)

    for node in nx_graph.nodes():
        x_pos = nx_graph.nodes[node]["x"]
        y_pos = nx_graph.nodes[node]["y"]

        if x_pos >= x_mean and y_pos >= y_mean:
            nx_graph.nodes[node]["textposition"] = "top right"
            continue

        if x_pos <= x_mean and y_pos >= y_mean:
            nx_graph.nodes[node]["textposition"] = "top left"
            continue
        if x_pos <= x_mean and y_pos <= y_mean:
            nx_graph.nodes[node]["textposition"] = "bottom left"
            continue

        nx_graph.nodes[node]["textposition"] = "bottom right"

    return nx_graph
