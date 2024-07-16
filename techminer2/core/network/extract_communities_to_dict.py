# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements

import numpy as np


def extract_communities_to_dict(
    nx_graph,
    conserve_counters,
):
    """Gets communities from a networkx graph as a dictionary."""

    communities = {}

    n_clusters = len(set(nx_graph.nodes[node]["group"] for node in nx_graph.nodes()))
    if n_clusters > 1:
        n_zeros = int(np.log10(n_clusters - 1)) + 1
    else:
        n_zeros = 1
    fmt = "CL_{:0" + str(n_zeros) + "d}"

    for node, data in nx_graph.nodes(data=True):
        text = fmt.format(data["group"])
        if text not in communities:
            communities[text] = []
        if conserve_counters is False:
            node = " ".join(node.split(" ")[:-1])
        communities[text].append(node)

    return communities
