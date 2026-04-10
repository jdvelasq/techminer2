def nodes_to_clusters(
    nx_graph,
):

    n2c = {}
    for node, data in nx_graph.nodes(data=True):
        cluster = data["group"]
        n2c[node] = cluster

    return n2c
