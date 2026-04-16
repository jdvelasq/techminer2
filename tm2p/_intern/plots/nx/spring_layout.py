# import math
# from collections import defaultdict

import networkx as nx  # type: ignore

from tm2p._intern import Params


def spring_layout(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    graph = nx_graph.copy()

    _apply_layout_weights(graph)

    pos = nx.spring_layout(
        graph,
        k=params.spring_layout_k,
        iterations=params.spring_layout_iterations,
        seed=params.spring_layout_seed,
        weight="layout_weight",
        scale=1.0,
    )

    pos = _apply_cluster_cohesion(
        nx_graph=graph,
        pos=pos,
    )

    for node, (x, y) in pos.items():
        nx_graph.nodes[node]["x"] = float(x)
        nx_graph.nodes[node]["y"] = float(y)

    return nx_graph


def _apply_layout_weights(nx_graph):
    for _, _, data in nx_graph.edges(data=True):
        data["layout_weight"] = _layout_weight(data.get("weight", 1.0))


def _layout_weight(weight):
    return max(float(weight), 0.0) ** 0.5


def _apply_cluster_cohesion(nx_graph, pos):

    nodes_by_group = _group_nodes(nx_graph)

    if len(nodes_by_group) <= 1:
        return pos

    pos = {node: (float(x), float(y)) for node, (x, y) in pos.items()}

    alpha = 0.1
    n_iterations = 5

    weighted_degree = {
        node: nx_graph.degree(node, weight="weight") for node in nx_graph.nodes()
    }

    for _ in range(n_iterations):

        centroids = _compute_group_centroids(nodes_by_group, pos)

        new_pos = {}

        for node, (x, y) in pos.items():

            group = nx_graph.nodes[node]["group"]
            cx, cy = centroids[group]

            node_alpha = alpha / (1.0 + weighted_degree[node] ** 0.5)

            new_pos[node] = (
                (1.0 - node_alpha) * x + node_alpha * cx,
                (1.0 - node_alpha) * y + node_alpha * cy,
            )

        pos = new_pos

    return pos


# def _apply_cluster_cohesion(nx_graph, pos):

#     nodes_by_group = _group_nodes(nx_graph)

#     if len(nodes_by_group) <= 1:
#         return pos

#     pos = {node: (float(x), float(y)) for node, (x, y) in pos.items()}

#     alpha = 0.08
#     n_iterations = 6

#     for _ in range(n_iterations):

#         centroids = _compute_group_centroids(nodes_by_group, pos)

#         new_pos = {}

#         for node, (x, y) in pos.items():

#             group = nx_graph.nodes[node]["group"]
#             cx, cy = centroids[group]

#             new_pos[node] = (
#                 (1.0 - alpha) * x + alpha * cx,
#                 (1.0 - alpha) * y + alpha * cy,
#             )

#         pos = new_pos

#     return pos


def _group_nodes(nx_graph):
    nodes_by_group = {}
    for node, data in nx_graph.nodes(data=True):
        group = data["group"]
        if group not in nodes_by_group:
            nodes_by_group[group] = []
        nodes_by_group[group].append(node)
    return nodes_by_group


def _compute_group_centroids(nodes_by_group, pos):

    centroids = {}

    for group, nodes in nodes_by_group.items():

        x_sum = 0.0
        y_sum = 0.0

        for node in nodes:
            x, y = pos[node]
            x_sum += x
            y_sum += y

        n = len(nodes)

        centroids[group] = (
            x_sum / n,
            y_sum / n,
        )

    return centroids


# def spring_layout(
#     params: Params,
#     nx_graph: nx.Graph,
# ) -> nx.Graph:

#     nodes_by_group = _group_nodes(nx_graph)

#     cluster_graph = _build_cluster_graph(nx_graph, nodes_by_group)

#     cluster_pos = _compute_cluster_positions(params, cluster_graph)

#     pos = _compute_node_positions(
#         params=params,
#         nx_graph=nx_graph,
#         nodes_by_group=nodes_by_group,
#         cluster_pos=cluster_pos,
#     )

#     pos = _refine_global_layout(
#         params=params,
#         nx_graph=nx_graph,
#         pos=pos,
#         nodes_by_group=nodes_by_group,
#     )

#     for node, (x, y) in pos.items():
#         nx_graph.nodes[node]["x"] = float(x)
#         nx_graph.nodes[node]["y"] = float(y)

#     return nx_graph


# def _group_nodes(nx_graph):
#     nodes_by_group = defaultdict(list)
#     for node, data in nx_graph.nodes(data=True):
#         nodes_by_group[data["group"]].append(node)
#     return dict(nodes_by_group)


# def _build_cluster_graph(nx_graph, nodes_by_group):

#     cluster_graph = nx.Graph()
#     cluster_graph.add_nodes_from(nodes_by_group.keys())

#     inter_weights = defaultdict(float)

#     for u, v, data in nx_graph.edges(data=True):

#         gu = nx_graph.nodes[u]["group"]
#         gv = nx_graph.nodes[v]["group"]

#         if gu == gv:
#             continue

#         w = _layout_weight(data.get("weight", 1.0))

#         edge = tuple(sorted((gu, gv)))
#         inter_weights[edge] += w

#     for (gu, gv), w in inter_weights.items():
#         cluster_graph.add_edge(gu, gv, weight=w)

#     return cluster_graph


# def _compute_cluster_positions(params, cluster_graph):

#     if cluster_graph.number_of_nodes() == 1:
#         g = next(iter(cluster_graph.nodes()))
#         return {g: (0.0, 0.0)}

#     pos = nx.spring_layout(
#         cluster_graph,
#         k=1.5 * params.spring_layout_k,
#         iterations=params.spring_layout_iterations,
#         seed=params.spring_layout_seed,
#         weight="weight",
#         scale=1.0,
#     )

#     pos = _normalize_positions(pos)

#     return {
#         group: (
#             params.spring_layout_cluster_scale * x,
#             params.spring_layout_cluster_scale * y,
#         )
#         for group, (x, y) in pos.items()
#     }


# def _compute_node_positions(params, nx_graph, nodes_by_group, cluster_pos):

#     final_pos = {}

#     max_size = max(len(nodes) for nodes in nodes_by_group.values())

#     for group, group_nodes in nodes_by_group.items():

#         cx, cy = cluster_pos[group]

#         if len(group_nodes) == 1:
#             final_pos[group_nodes[0]] = (cx, cy)
#             continue

#         subgraph = nx_graph.subgraph(group_nodes).copy()
#         _apply_layout_weights(subgraph)

#         local_pos = nx.spring_layout(
#             subgraph,
#             k=params.spring_layout_k,
#             iterations=params.spring_layout_iterations,
#             seed=params.spring_layout_seed,
#             weight="layout_weight",
#             scale=1.0,
#         )

#         local_pos = _normalize_positions(local_pos)

#         density = nx.density(subgraph)
#         size_factor = math.sqrt(len(group_nodes) / max_size)
#         density_factor = 1.0 - min(max(density, 0.0), 1.0)

#         radius = (
#             params.spring_layout_intra_scale
#             * size_factor
#             * (0.85 + 0.35 * density_factor)
#         )

#         for node, (x, y) in local_pos.items():
#             final_pos[node] = (
#                 cx + radius * x,
#                 cy + radius * y,
#             )

#     return final_pos


# def _refine_global_layout(params, nx_graph, pos, nodes_by_group):

#     graph = nx_graph.copy()
#     _apply_layout_weights(graph)

#     fixed_nodes = _select_anchor_nodes(graph, nodes_by_group)

#     return nx.spring_layout(
#         graph,
#         pos=pos,
#         fixed=fixed_nodes,
#         k=0.18 * params.spring_layout_k,
#         iterations=6,
#         seed=params.spring_layout_seed,
#         weight="layout_weight",
#         scale=None,
#     )


# def _select_anchor_nodes(nx_graph, nodes_by_group):

#     anchors = []

#     for group_nodes in nodes_by_group.values():
#         ranked_nodes = sorted(
#             group_nodes,
#             key=lambda node: nx_graph.degree(node, weight="weight"),
#             reverse=True,
#         )
#         anchors.extend(ranked_nodes[: min(3, len(ranked_nodes))])

#     return anchors


# def _apply_layout_weights(nx_graph):
#     for _, _, data in nx_graph.edges(data=True):
#         data["layout_weight"] = _layout_weight(data.get("weight", 1.0))


# def _layout_weight(weight):
#     return math.sqrt(max(float(weight), 0.0))


# def _normalize_positions(pos):

#     if not pos:
#         return pos

#     xs = [x for x, _ in pos.values()]
#     ys = [y for _, y in pos.values()]

#     min_x = min(xs)
#     max_x = max(xs)
#     min_y = min(ys)
#     max_y = max(ys)

#     span_x = max_x - min_x
#     span_y = max_y - min_y
#     span = max(span_x, span_y, 1e-9)

#     cx = 0.5 * (min_x + max_x)
#     cy = 0.5 * (min_y + max_y)

#     return {node: ((x - cx) / span, (y - cy) / span) for node, (x, y) in pos.items()}


# def spring_layout(
#     params: Params,
#     nx_graph: nx.Graph,
# ) -> nx.Graph:

#     pos = nx.spring_layout(
#         nx_graph,
#         k=params.spring_layout_k,
#         iterations=params.spring_layout_iterations,
#         seed=params.spring_layout_seed,
#     )

#     for node in nx_graph.nodes():
#         nx_graph.nodes[node]["x"] = pos[node][0]
#         nx_graph.nodes[node]["y"] = pos[node][1]

#     return nx_graph
