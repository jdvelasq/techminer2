import numpy as np

from tm2p.enum import Scaling


def set_node_size_by_occ(
    params,
    nx_graph,
):
    node_size_range = params.node_size_range

    occ = list(nx_graph.nodes())
    occ = [node.split(" ")[-1] for node in occ]
    occ = [node.split(":")[0] for node in occ]
    occ = np.array([float(node) for node in occ])

    if max(occ) == min(occ):
        node_sizes = np.array([node_size_range[0]] * len(occ))
    else:

        #
        # Node scaling
        if params.node_scaling == Scaling.SQRT:
            occ = np.sqrt(occ)
        if params.node_scaling == Scaling.LOG:
            occ = np.log1p(occ)

        width = node_size_range[1] - node_size_range[0]
        prop = (occ - occ.min()) / (occ.max() - occ.min())
        node_sizes = node_size_range[0] + prop * width

    #
    # Sets the value of node_size
    for size, node in zip(node_sizes, nx_graph.nodes()):
        nx_graph.nodes[node]["node_size"] = size

    return nx_graph
