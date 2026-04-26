import contextlib
import io
import sys


@contextlib.contextmanager
def suppress_stdout():
    old = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield
    finally:
        sys.stdout = old


def cluster_nx_graph(
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

        for node, group in clustering.items():
            nx_graph.nodes[node]["group"] = group

    for node in nx_graph.nodes:
        nx_graph.nodes[node]["top_n"] = False

    clusters = {}
    for node in nx_graph.nodes:
        group = nx_graph.nodes[node]["group"]
        if group not in clusters:
            clusters[group] = []
        clusters[group].append(node)

    for _, value in clusters.items():
        sorted_value = sorted(
            value,
            key=lambda x: int(x.split(" ")[-1].split(":")[0]),
            reverse=False,
        )
        for node in sorted_value[: params.node_n_labels]:
            nx_graph.nodes[node]["labeled"] = True

    return nx_graph


def _apply_cdlib_algorithm(
    nx_graph,
    algorithm,
):
    """Network community detection."""

    with suppress_stdout():
        from cdlib import algorithms  # type: ignore

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

    with suppress_stdout():
        communities = cdlib_algorithm(nx_graph, **kwargs).communities

    for i_community, community in enumerate(communities):
        for node in community:
            nx_graph.nodes[node]["group"] = i_community

    return nx_graph
