import math
from collections import defaultdict

import networkx as nx  # type: ignore


def compute_clustered_spring_layout_positions(
    params,
    nx_graph,
):

    nodes_by_group, cluster_pos = compute_cluster_positions(params, nx_graph)
    pos = compute_node_positions(params, nx_graph, nodes_by_group, cluster_pos)

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["x"] = pos[node][0]
        nx_graph.nodes[node]["y"] = pos[node][1]

    return nx_graph


def compute_node_positions(params, nx_graph, nodes_by_group, cluster_pos):
    final_pos = {}

    max_cluster_size = max(len(nodes) for nodes in nodes_by_group.values())

    for group, group_nodes in nodes_by_group.items():
        subgraph = nx_graph.subgraph(group_nodes).copy()

        if len(group_nodes) == 1:
            local_pos = {group_nodes[0]: (0.0, 0.0)}
        else:
            local_pos = nx.spring_layout(
                subgraph,
                k=params.spring_layout_k,
                iterations=params.spring_layout_iterations,
                seed=params.spring_layout_seed,
                weight="weight",
            )

        #
        # 4) Scale local coordinates and translate to cluster center
        #
        cx, cy = cluster_pos[group]

        #
        # optional: radius proportional to sqrt(cluster size)
        #
        radius = params.spring_layout_intra_scale * math.sqrt(
            len(group_nodes) / max_cluster_size
        )

        for node, (x, y) in local_pos.items():
            final_pos[node] = (
                params.spring_layout_cluster_scale * cx + radius * x,
                params.spring_layout_cluster_scale * cy + radius * y,
            )

    return final_pos


def compute_cluster_positions(params, nx_graph):
    groups = {node: nx_graph.nodes[node]["group"] for node in nx_graph.nodes()}

    nodes_by_group = defaultdict(list)
    for node, group in groups.items():
        nodes_by_group[group].append(node)

    #
    # 1) Build cluster meta-graph
    #
    cluster_graph = nx.Graph()
    cluster_graph.add_nodes_from(nodes_by_group.keys())

    inter_weights = defaultdict(float)

    for u, v, data in nx_graph.edges(data=True):
        gu = groups[u]
        gv = groups[v]
        w = float(data.get("weight", 1.0))

        if gu == gv:
            continue

        edge = tuple(sorted((gu, gv)))
        inter_weights[edge] += w

    for (gu, gv), w in inter_weights.items():
        cluster_graph.add_edge(gu, gv, weight=w)

    #
    # 2) Layout clusters
    #

    cluster_pos = nx.spring_layout(
        cluster_graph,
        k=params.spring_layout_k,
        iterations=params.spring_layout_iterations,
        seed=params.spring_layout_seed,
        weight="weight",
    )

    return nodes_by_group, cluster_pos
