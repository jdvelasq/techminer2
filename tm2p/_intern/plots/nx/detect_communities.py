from cdlib import algorithms  # type: ignore


def detect_communities(
    params,
    nx_graph,
):

    clustering = params.clustering

    if isinstance(clustering, str):
        nx_graph = _apply_cdlib_algorithm(params, nx_graph, clustering)

    if isinstance(clustering, dict):
        #
        # The group is assigned using and external algorithm. It is designed
        # to provide analysis capabilities to the system when other types of
        # analysis are conducted, for example, factor analysis.
        #
        for node, group in clustering.items():
            nx_graph.nodes[node]["group"] = group

    return nx_graph


def _apply_cdlib_algorithm(
    params,
    nx_graph,
    algorithm,
):
    """Network community detection."""

    cdlib_algorithm = {
        "INFOMAP": algorithms.infomap,
        "LEIDEN": algorithms.leiden,
        "LOUVAIN": algorithms.louvain,
        "WALKTRAP": algorithms.walktrap,
    }[algorithm]

    kwargs = {}

    if algorithm in [
        "LOUVAIN",
    ]:
        kwargs["weight"] = "weight"
        kwargs["randomize"] = False

    if algorithm in [
        "LEIDEN",
    ]:
        kwargs["weights"] = "weight"
        kwargs["seed"] = 0

    final_communities = cdlib_algorithm(nx_graph, **kwargs).communities

    for _ in range(2, params.max_recursive_clustering_depth + 1):

        min_size = min(len(c) for c in final_communities)

        if min_size > params.min_recursive_cluster_size:

            new_communities = []

            for community in final_communities:

                subgraph = nx_graph.subgraph(community).copy()

                sub_communities = cdlib_algorithm(subgraph, **kwargs).communities
                min_size = min(len(c) for c in sub_communities)
                if min_size > params.min_recursive_cluster_size:
                    new_communities.extend(sub_communities)
                else:
                    new_communities.append(community)

            final_communities = new_communities

    final_communities = sorted(final_communities, key=len, reverse=True)
    for i_community, community in enumerate(final_communities):
        for node in community:
            nx_graph.nodes[node]["group"] = i_community

    return nx_graph
