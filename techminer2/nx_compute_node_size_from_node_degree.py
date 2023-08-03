# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

#
# In networkx, the size of the node is specified by the 'node_size' parameter.
# Example: nx.draw_networkx_nodes(G, pos, node_size=node_sizes)
import numpy as np


def nx_compute_node_size_from_node_degree(
    nx_graph,
    node_size_min,
    node_size_max,
):
    #
    # Compute node degree
    degrees = []
    for node in nx_graph.nodes():
        degrees.append(nx_graph.nodes[node]["degree"])
    degrees = np.array([float(degree) for degree in degrees])

    #
    # Set the lower value of the node size to node_size_min
    min_degree = min(degrees)
    node_sizes = degrees - min_degree + node_size_min

    #
    # Checks if node_sizes.max() > node_size_max and, if so, rescales
    if node_sizes.max() > node_size_max:
        #
        # Scales the node size to the range [node_size_min, node_size_max]
        node_sizes -= node_size_min
        node_sizes /= node_sizes.max() - node_size_min
        node_sizes *= node_size_max - node_size_min
        node_sizes += node_size_min

    #
    # Sets the value of node_size
    for size, node in zip(node_sizes, nx_graph.nodes()):
        nx_graph.nodes[node]["node_size"] = size

    return nx_graph
