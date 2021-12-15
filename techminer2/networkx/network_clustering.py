# import pandas as pd
from cdlib import algorithms

import networkx as nx


def network_clustering(
    nodes,
    edges,
    algorithm,
    random_state=12345,
):
    """
    Network clustering.

    Parameters:
    -----------
    nodes: pandas.DataFrame
        Nodes dataframe, with the following columns:
            - name
            - size
            - ...

    edges: pandas.DataFrame
        Edges dataframe, with the following columns:
            - source
            - target
            - value
            - ...

    algorithm: str
        Clustering algorithm. Valid options are the following:
            - 'louvain'
            - 'label_propagation'
            - 'walktrap'
            - 'leiden'

    Returns:
    --------
    pandas.DataFrame
        Nodes dataframe, with the following columns:
        - name
        - size
        - group: int. Indicates the cluster assigned to the node.
        - ...

    pandas.DataFrame
        Edges dataframe, with the following columns:
        - source
        - target
        - value
        - group: int. Indicates the cluster assigned to the edge.
        - ...

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
    }[algorithm](G, randomize=random_state).communities

    communities = dict(
        (member, i_community)
        for i_community, community in enumerate(communities)
        for member in community
    )

    nodes["group"] = nodes.name.map(communities)

    # group of the each edge
    node_sizes = dict(zip(nodes.name, nodes["size"]))
    edges["cluster_source"] = edges.source.map(communities)
    edges["cluster_target"] = edges.target.map(communities)

    edges["group"] = [
        source if node_sizes[source] > node_sizes[target] else target
        for source, target in zip(edges.source, edges.target)
    ]
    edges["group"] = edges.group.map(communities)

    return nodes, edges
