"""
Network
===============================================================================

Builds a network from a matrix

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> coc_matrix = co_occurrence_matrix(column='author_keywords', min_occ=8, directory=directory)
>>> network(coc_matrix).keys()
dict_keys(['nodes', 'edges', 'G', 'indicators', 'communities', 'manifold_data'])


"""
import numpy as np
import pandas as pd
from cdlib import algorithms
from sklearn.manifold import MDS

import networkx as nx


def network(
    matrix,
    clustering_method="louvain",
    manifold_method=None,
):

    # -------------------------------------------------------------------------
    matrix.sort_index(axis="columns", level=[0, 1, 2], inplace=True)
    matrix.sort_index(axis="index", level=[0, 1, 2], inplace=True)

    # -------------------------------------------------------------------------
    names = matrix.columns.get_level_values(0)
    n_cols = matrix.shape[1]
    edges = []
    for i_row in range(1, n_cols):
        for i_col in range(0, i_row):
            if matrix.iloc[i_row, i_col] > 0:
                edges.append(
                    {
                        "source": names[i_row],
                        "target": names[i_col],
                        "weight": matrix.iloc[i_row, i_col],
                    }
                )

    # -------------------------------------------------------------------------
    size = {name: 0 for name in names}
    for edge in edges:
        size[edge["source"]] += edge["weight"]
        size[edge["target"]] += edge["weight"]
    nodes = [(name, dict(size=size[name], group=0)) for name in size.keys()]

    # -------------------------------------------------------------------------
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_weighted_edges_from(
        [(edge["source"], edge["target"], edge["weight"]) for edge in edges]
    )

    # -------------------------------------------------------------------------
    if isinstance(clustering_method, str):
        #
        # network clustering
        #
        communities = {
            "label_propagation": algorithms.label_propagation,
            "leiden": algorithms.leiden,
            "louvain": algorithms.louvain,
            "walktrap": algorithms.walktrap,
        }[clustering_method](G, randomize=False).communities

        communities = dict(
            (member, i_community)
            for i_community, community in enumerate(communities)
            for member in community
        )

        for node in nodes:
            node[1]["group"] = communities[node[0]]

    else:
        #
        # sklearn matrix clustering
        #
        clustering_method.fit(matrix)
        communities = dict(zip(matrix.columns, clustering_method.labels_))

        for node in nodes:
            node[1]["group"] = communities[node[0]]

    # -------------------------------------------------------------------------
    if manifold_method is None:
        manifold_method = MDS(n_components=2)

    transformed_matrix = manifold_method.fit_transform(matrix)

    manifold_data = pd.DataFrame(
        {
            "node": matrix.index.get_level_values(0),
            "num_documents": matrix.index.get_level_values(1),
            "global_citations": matrix.index.get_level_values(2),
        }
    )

    manifold_data["Dim-0"] = transformed_matrix[:, 0]
    manifold_data["Dim-1"] = transformed_matrix[:, 1]
    node2cluster = {node[0]: node[1]["group"] for node in nodes}
    manifold_data["cluster"] = manifold_data.node.map(node2cluster)
    name2degree = {name: val for (name, val) in G.degree()}
    manifold_data["degree"] = manifold_data.node.map(name2degree)

    # -------------------------------------------------------------------------
    indicators_table = pd.DataFrame(
        {
            "node": matrix.index.get_level_values(0),
            "num_documents": matrix.index.get_level_values(1),
            "global_citations": matrix.index.get_level_values(2),
        }
    )

    ## node2cluster = {node[0]: node[1]["group"] for node in nodes}
    indicators_table["cluster"] = indicators_table.node.map(node2cluster)

    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)
    pagerank = nx.pagerank(G)

    indicators_table["betweenness"] = indicators_table.node.map(betweenness)
    indicators_table["closeness"] = indicators_table.node.map(closeness)
    indicators_table["pagerank"] = indicators_table.node.map(pagerank)

    # -------------------------------------------------------------------------
    cluster_members = indicators_table.copy()
    cluster_members = cluster_members.sort_values(by=["cluster", "num_documents"])
    cluster_members = cluster_members.assign(
        rn=cluster_members.groupby("cluster").cumcount(())
    )

    num_docs = cluster_members.num_documents.values
    cited_by = cluster_members.global_citations.values
    n_zeros_docs = int(np.log10(max(num_docs))) + 1
    n_zeros_cited_by = int(np.log10(max(cited_by))) + 1

    fmt = "{} {:0" + str(n_zeros_docs) + "d}:{:0" + str(n_zeros_cited_by) + "d}"
    text = [
        fmt.format(name, int(nd), int(tc))
        for name, nd, tc in zip(cluster_members.node, num_docs, cited_by)
    ]

    cluster_members = cluster_members.assign(node=text)
    cluster_members = cluster_members.assign(
        cluster=cluster_members.cluster.map(lambda x: "CLUST_{:0d}".format(x))
    )
    cluster_members = cluster_members[["rn", "node", "cluster"]]
    cluster_members = cluster_members.pivot(
        index="rn", columns="cluster", values="node"
    )
    cluster_members = cluster_members.fillna("")

    # -------------------------------------------------------------------------

    return {
        "nodes": nodes,
        "edges": edges,
        "G": G,
        "indicators": indicators_table,
        "communities": cluster_members,
        "manifold_data": manifold_data,
    }
