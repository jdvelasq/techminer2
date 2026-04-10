import networkx as nx  # type: ignore

from tm2p._intern import Params


def set_cluster_names(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:
    for node in nx_graph.nodes():
        text = nx_graph.nodes[node]["text"]
        index = text.split(" ")[0]
        counters = text.split(" ")[-1]
        cluster = int(index)
        name = params.cluster_names[cluster]  # type: ignore
        name = f"{name} {counters}"
        nx_graph.nodes[node]["text"] = name
    return nx_graph
