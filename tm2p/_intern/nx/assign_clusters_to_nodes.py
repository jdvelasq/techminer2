def assign_clusters_to_nodes(params, nx_graph, item2cluster):

    for node, group in item2cluster.items():
        nx_graph.nodes[node]["group"] = group

    for node in nx_graph.nodes:
        nx_graph.nodes[node]["top_n"] = False
        nx_graph.nodes[node]["text"] = node
        nx_graph.nodes[node]["labeled"] = False

    clusters = {}
    for node in nx_graph.nodes:
        group = nx_graph.nodes[node]["group"]
        if group not in clusters:
            clusters[group] = []
        clusters[group].append(node)

    def _generate_sorting_key(node):
        text = node.split(" ")
        occ = int(text[-1].split(":")[0])
        gcs = int(text[-1].split(":")[1])
        return (occ, gcs, node)

    for _, value in clusters.items():
        sorted_value = sorted(
            value,
            key=_generate_sorting_key,
            reverse=True,
        )
        for node in sorted_value[: params.node_n_labels]:
            nx_graph.nodes[node]["labeled"] = True

    for edge in nx_graph.edges():
        nx_graph.edges[edge]["dash"] = "solid"

    return nx_graph
