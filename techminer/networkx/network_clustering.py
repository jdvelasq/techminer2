import pandas as pd
from cdlib import algorithms

import networkx as nx


def network_clustering(
    nodes,
    edges,
    algorithm,
):
    """
    Network clustering.

    nodes: pandas.DataFrame
    - name
    - ...

    edges: pandas.DataFrame
    - source
    - target
    - value
    - ....

    """
    nodes = nodes.copy()
    edges = edges.copy()

    # creates a networkx graph
    G = nx.Graph()

    # add nodes
    for _, row in nodes.iterrows():
        G.add_node(
            row["name"],
            size=row["size"],
        )

    # add edges
    for _, row in edges.iterrows():
        G.add_weighted_edges_from(
            [
                (row["source"], row["target"], row["value"]),
            ]
        )

    communities = {
        "label_propagation": algorithms.label_propagation,
        "leiden": algorithms.leiden,
        "louvain": algorithms.louvain,
        "walktrap": algorithms.walktrap,
    }[algorithm](G).communities

    communities = dict(
        [
            (member, i_community)
            for i_community, community in enumerate(communities)
            for member in community
        ]
    )

    nodes["group"] = nodes.name.map(communities)

    # color for edges
    node_sizes = dict(zip(nodes.name, nodes["size"]))
    edges["group"] = [
        source if node_sizes[source] > node_sizes[target] else target
        for source, target in zip(edges.source, edges.target)
    ]
    edges["group"] = edges.group.map(communities)

    return nodes, edges
