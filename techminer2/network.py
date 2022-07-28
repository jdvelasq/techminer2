# """Network interface."""


# from dataclasses import dataclass

# from ._get_network_graph_communities import get_network_graph_communities
# from ._get_network_graph_degree_plot import get_network_graph_degree_plot
# from ._get_network_graph_indicators import get_network_graph_indicators
# from ._get_network_graph_manifold_plot import get_network_graph_manifold_plot
# from ._get_network_graph_plot import network_graph_plot
# from ._matrix_list_2_network_graph import matrix_list_2_network_graph
# from ._network_community_detection import network_community_detection
# from .vantagepoint__co_occ_matrix_list import vantagepoint__co_occ_matrix_list


# @dataclass(init=False)
# class _Result:
#     communities_: None
#     indicators_: None
#     plot_: None
#     degree_plot_: None
#     manifold_plot_: None


# def network(
#     column,
#     top_n=None,
#     directory="./",
#     database="documents",
#     method="louvain",
#     nx_k=0.5,
#     nx_iteratons=10,
#     delta=1.0,
# ):
#     """Network."""

#     matrix_list = vantagepoint__co_occ_matrix_list(
#         criterion=column,
#         row=None,
#         topics_length=top_n,
#         directory=directory,
#         database=database,
#     )

#     graph = matrix_list_2_network_graph(matrix_list)
#     graph = network_community_detection(graph, method=method)

#     result = _Result()
#     result.communities_ = get_network_graph_communities(graph)
#     result.indicators_ = get_network_graph_indicators(graph)
#     result.plot_ = network_graph_plot(
#         graph,
#         nx_k=nx_k,
#         nx_iterations=nx_iteratons,
#         delta=delta,
#     )
#     result.degree_plot_ = get_network_graph_degree_plot(graph)
#     result.manifold_plot_ = get_network_graph_manifold_plot(matrix_list, graph)

#     return result
