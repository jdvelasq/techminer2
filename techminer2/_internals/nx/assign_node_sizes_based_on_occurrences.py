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


def internal__assign_node_sizes_based_on_occurrences(
    params,
    nx_graph,
):
    node_size_range = params.node_size_range

    #
    # Extracs occurrences from node names. Example: 'regtech 10:100' -> 10
    occ = list(nx_graph.nodes())
    occ = [node.split(" ")[-1] for node in occ]
    occ = [node.split(":")[0] for node in occ]
    occ = np.array([float(node) for node in occ])

    #
    # Set the lower value of the node size to node_size_min
    min_occ = min(occ)
    node_sizes = occ - min_occ + node_size_range[0]

    #
    # Checks if node_sizes.max() > node_size_max and, if so, rescales
    if node_sizes.max() > node_size_range[1]:
        #
        # Scales the node size to the range [node_size_min, node_size_max]
        node_sizes -= node_size_range[0]
        node_sizes /= node_sizes.max()
        node_sizes *= node_size_range[1]
        node_sizes += node_size_range[0]

    #
    # Sets the value of node_size
    for size, node in zip(node_sizes, nx_graph.nodes()):
        nx_graph.nodes[node]["node_size"] = size

    return nx_graph
