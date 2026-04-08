def create_cluster_to_items_mapping(
    nx_graph,
):

    mapping = {}

    for node, data in nx_graph.nodes(data=True):
        cluster = data["group"]
        if cluster not in mapping:
            mapping[cluster] = []
        mapping[cluster].append(node)

    return mapping
