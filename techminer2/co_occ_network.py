"""
Co-occurrence Network
===============================================================================

Builds a network from a matrix

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> matrix_list = co_occ_matrix_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> co_occ_network(matrix_list) # doctest: +ELLIPSIS
<networkx.classes.graph.Graph ...

"""
import networkx as nx


def co_occ_network(
    matrix_list,
):
    """Transforms a co-occurrence matrix list into a networkx graph."""

    graph = nx.Graph()
    graph = _create_nodes(graph, matrix_list)
    graph = _create_edges(graph, matrix_list)
    return graph


#####
def _create_edges(graph, matrix_list):
    edges = []
    for _, row in matrix_list.iterrows():
        if row["row"] != row["column"]:
            edges.append((row[0], row[1], row[2]))
    graph.add_weighted_edges_from(edges)
    return graph


def _create_nodes(graph, matrix_list):
    matrix_list = matrix_list.copy()
    matrix_list = matrix_list[matrix_list["row"] == matrix_list["column"]]
    nodes = [
        (node, dict(size=occ, group=0))
        for node, occ in zip(matrix_list["row"], matrix_list["OCC"])
    ]
    graph.add_nodes_from(nodes)
    return graph


# def old():

#     # -------------------------------------------------------------------------
#     names = matrix.columns.get_level_values(0)
#     n_cols = matrix.shape[1]
#     edges = []
#     for i_row in range(1, n_cols):
#         for i_col in range(0, i_row):
#             if matrix.iloc[i_row, i_col] > 0:
#                 edges.append(
#                     {
#                         "source": names[i_row],
#                         "target": names[i_col],
#                         "weight": matrix.iloc[i_row, i_col],
#                     }
#                 )

#     # -------------------------------------------------------------------------
#     size = {name: 0 for name in names}
#     for edge in edges:
#         size[edge["source"]] += edge["weight"]
#         size[edge["target"]] += edge["weight"]
#     nodes = [(name, dict(size=size[name], group=0)) for name in size.keys()]

#     # -------------------------------------------------------------------------
#     G = nx.Graph()
#     G.add_nodes_from(nodes)
#     G.add_weighted_edges_from(
#         [(edge["source"], edge["target"], edge["weight"]) for edge in edges]
#     )

#     # -------------------------------------------------------------------------
#     if isinstance(clustering_method, str):
#         #
#         # network clustering
#         #
#         communities = {
#             "label_propagation": algorithms.label_propagation,
#             "leiden": algorithms.leiden,
#             "louvain": algorithms.louvain,
#             "walktrap": algorithms.walktrap,
#         }[clustering_method](G, randomize=False).communities

#         communities = dict(
#             (member, i_community)
#             for i_community, community in enumerate(communities)
#             for member in community
#         )

#         for node in nodes:
#             node[1]["group"] = communities[node[0]]

#     else:
#         #
#         # sklearn matrix clustering
#         #
#         clustering_method.fit(matrix)
#         communities = dict(zip(matrix.columns, clustering_method.labels_))

#         for node in nodes:
#             node[1]["group"] = communities[node[0]]

#     # -------------------------------------------------------------------------
#     if manifold_method is None:
#         manifold_method = MDS(n_components=2)

#     transformed_matrix = manifold_method.fit_transform(matrix)

#     manifold_data = pd.DataFrame(
#         {
#             "node": matrix.index.get_level_values(0),
#             "num_documents": matrix.index.get_level_values(1),
#             "global_citations": matrix.index.get_level_values(2),
#         }
#     )

#     manifold_data["Dim-0"] = transformed_matrix[:, 0]
#     manifold_data["Dim-1"] = transformed_matrix[:, 1]
#     node2cluster = {node[0]: node[1]["group"] for node in nodes}
#     manifold_data["cluster"] = manifold_data.node.map(node2cluster)
#     name2degree = {name: val for (name, val) in G.degree()}
#     manifold_data["degree"] = manifold_data.node.map(name2degree)

#     # -------------------------------------------------------------------------
#     indicators_table = pd.DataFrame(
#         {
#             "node": matrix.index.get_level_values(0),
#             "num_documents": matrix.index.get_level_values(1),
#             "global_citations": matrix.index.get_level_values(2),
#         }
#     )

#     indicators_table["cluster"] = indicators_table.node.map(node2cluster)

#     betweenness = nx.betweenness_centrality(G)
#     closeness = nx.closeness_centrality(G)
#     pagerank = nx.pagerank(G)

#     indicators_table["betweenness"] = indicators_table.node.map(betweenness)
#     indicators_table["closeness"] = indicators_table.node.map(closeness)
#     indicators_table["pagerank"] = indicators_table.node.map(pagerank)

#     # -------------------------------------------------------------------------
#     cluster_members = indicators_table.copy()
#     cluster_members = cluster_members.sort_values(
#         by=["cluster", "num_documents", "global_citations", "node"]
#     )
#     cluster_members = cluster_members.assign(
#         rn=cluster_members.groupby("cluster").cumcount(())
#     )

#     num_docs = cluster_members.num_documents.values
#     cited_by = cluster_members.global_citations.values
#     n_zeros_docs = int(np.log10(max(num_docs))) + 1
#     n_zeros_cited_by = int(np.log10(max(cited_by))) + 1

#     fmt = "{} {:0" + str(n_zeros_docs) + "d}:{:0" + str(n_zeros_cited_by) + "d}"
#     text = [
#         fmt.format(name, int(nd), int(tc))
#         for name, nd, tc in zip(cluster_members.node, num_docs, cited_by)
#     ]

#     cluster_members = cluster_members.assign(node=text)
#     cluster_members = cluster_members.assign(
#         cluster=cluster_members.cluster.map(lambda x: "CL_{:02d}".format(x))
#     )
#     cluster_members = cluster_members[["rn", "node", "cluster"]]
#     cluster_members = cluster_members.pivot(
#         index="rn", columns="cluster", values="node"
#     )
#     cluster_members = cluster_members.fillna("")

#     # -------------------------------------------------------------------------

#     callon_matrix = matrix.copy()
#     callon_matrix.columns = callon_matrix.columns.get_level_values(0)
#     callon_matrix.index = callon_matrix.index.get_level_values(0)

#     callon_matrix["_CLUSTER_"] = callon_matrix.index.map(node2cluster)
#     callon_matrix = callon_matrix.groupby(["_CLUSTER_"]).sum()
#     callon_matrix = callon_matrix.transpose()
#     callon_matrix["_CLUSTER_"] = callon_matrix.index.map(node2cluster)
#     callon_matrix = callon_matrix.groupby(["_CLUSTER_"]).sum()

#     callon_matrix = callon_matrix.sort_index(axis=0)
#     callon_matrix = callon_matrix.sort_index(axis=1)

#     strategic_diagram = pd.DataFrame(
#         {"callon_centrality": callon_matrix.values.diagonal()}
#     )
#     strategic_diagram["callon_density"] = (
#         callon_matrix.sum() - callon_matrix.values.diagonal()
#     )

#     strategic_diagram["callon_centrality"] *= 10
#     strategic_diagram["callon_density"] *= 100

#     n_items_per_cluster = indicators_table["cluster"].value_counts()
#     n_items_per_cluster = n_items_per_cluster.sort_index()

#     strategic_diagram["n_items"] = n_items_per_cluster

#     strategic_diagram["callon_density"] = [
#         d / n for d, n in zip(strategic_diagram["callon_density"], n_items_per_cluster)
#     ]

#     cluster_names = cluster_members.iloc[0, :].to_list()
#     cluster_names = [" ".join(name.split(" ")[:-1]) for name in cluster_names]

#     strategic_diagram["cluster_name"] = cluster_names

#     # -------------------------------------------------------------------------

#     return {
#         "nodes": nodes,
#         "edges": edges,
#         "G": G,
#         "indicators": indicators_table,
#         "communities": cluster_members,
#         "manifold_data": manifold_data,
#         "strategic_diagram": strategic_diagram,
#     }
