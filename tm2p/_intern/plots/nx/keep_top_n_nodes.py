import networkx as nx  # type: ignore

from tm2p._intern import Params


def keep_top_n_nodes(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    nodes = list(dict(nx_graph.degree()))

    def f(x):
        counters = x.split(" ")[-1]
        occ = counters.split(":")[0]
        gcs = counters.split(":")[1]
        return int(occ), int(gcs), x

    nodes = sorted(nodes, key=f, reverse=True)
    nodes_to_keep = nodes[: params.top_n_nodes]
    nodes_to_remove = [node for node in nx_graph.nodes() if node not in nodes_to_keep]
    nx_graph.remove_nodes_from(nodes_to_remove)

    return nx_graph
