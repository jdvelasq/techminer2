# """
# Ego Network
# ===============================================================================

# # >>> from techminer2 import *
# # >>> directory = "data/regtech/"
# # >>> file_name = "sphinx/images/ego_network.png"
# # >>> ego_network(
# # ...     'block-chain',
# # ...     'author_keywords',
# # ...      min_occ=5,
# # ...      directory=directory
# # ... ).savefig(file_name)

# # .. image:: images/ego_network.png
# #     :width: 700px
# #     :align: center


# """

# import networkx as nx

# # from .co_occurrence_matrix import co_occurrence_matrix
# # from .network_plot import network_plot


# def ego_network(
#     topic,
#     column,
#     min_occ=1,
#     directory="./",
#     figsize=(7, 7),
#     k=0.20,
#     iterations=50,
#     max_labels=50,
#     plot=True,
# ):
#     matrix = co_occurrence_matrix(
#         column,
#         min_occ=min_occ,
#         max_occ=None,
#         normalization=None,
#         scheme=None,
#         directory=directory,
#     )

#     matrix = matrix.iloc[
#         matrix.iloc[:, matrix.columns.get_level_values(0) == topic].values > 0,
#         :,
#     ]
#     matrix = matrix.transpose()
#     matrix = matrix.iloc[
#         matrix.iloc[:, matrix.columns.get_level_values(0) == topic].values > 0,
#         :,
#     ]

#     if plot is False:
#         return matrix

#     # -------------------------------------------------------------------------
#     matrix.sort_index(axis="columns", level=[0, 1, 2], inplace=True)
#     matrix.sort_index(axis="index", level=[0, 1, 2], inplace=True)

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
#     nodes = [
#         (name, dict(size=size[name], group=(1 if name == topic else 0)))
#         for name in size.keys()
#     ]

#     # -------------------------------------------------------------------------
#     G = nx.Graph()
#     G.add_nodes_from(nodes)
#     G.add_weighted_edges_from(
#         [(edge["source"], edge["target"], edge["weight"]) for edge in edges]
#     )

#     network_ = {
#         "nodes": nodes,
#         "edges": edges,
#         "G": G,
#     }

#     return network_plot(
#         network_,
#         figsize=figsize,
#         k=k,
#         iterations=iterations,
#         max_labels=max_labels,
#     )
