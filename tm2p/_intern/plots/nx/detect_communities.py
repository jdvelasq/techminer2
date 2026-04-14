from cdlib import algorithms  # type: ignore


def detect_communities(
    params,
    nx_graph,
):

    clustering = params.clustering

    if isinstance(clustering, str):
        nx_graph = _apply_cdlib_algorithm(nx_graph, clustering)

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

    communities = cdlib_algorithm(nx_graph, **kwargs).communities

    for i_community, community in enumerate(communities):
        for node in community:
            nx_graph.nodes[node]["group"] = i_community

    return nx_graph
