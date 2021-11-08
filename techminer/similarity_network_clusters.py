"""
Similarity network --- clusters
===============================================================================

Computes the co-occurrence network map clusters using network clustering algorithms.


"""
import networkx as nx
import pandas as pd
from cdlib import algorithms


def similarity_network_clusters(
    similarity_matrix,
    algorithm="louvain",
):
    matrix = similarity_matrix.copy()
    melted_matrix = pd.melt(
        matrix,
        var_name="to",
        value_name="value",
        ignore_index=False,
    )
    melted_matrix = melted_matrix.reset_index()
    melted_matrix = melted_matrix.rename(columns={melted_matrix.columns[0]: "from"})

    ## terms
    terms = melted_matrix.to.copy()
    terms = terms.drop_duplicates()

    ## Network
    G = nx.Graph()
    G.add_nodes_from(terms.tolist())
    G.add_edges_from(
        [
            (u, v, {"weight": l})
            for u, v, l in zip(
                melted_matrix["from"], melted_matrix["to"], melted_matrix["value"]
            )
            if l > 0
        ]
    )
    communities = {
        "label_propagation": algorithms.label_propagation,
        "leiden": algorithms.leiden,
        "louvain": algorithms.louvain,
        "walktrap": algorithms.walktrap,
    }[algorithm](G).communities

    communities = [
        (member, i_community)
        for i_community, community in enumerate(communities)
        for member in community
    ]
    cluster_members = pd.DataFrame(communities, columns=["term", "cluster"])
    cluster_members = cluster_members.set_index("term")
    cluster_members = cluster_members.sort_values(by="cluster", ascending=True)

    return cluster_members
