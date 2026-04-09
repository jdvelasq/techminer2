import networkx as nx  # type: ignore

from tm2p._intern import Params


def spring_layout(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    pos = nx.spring_layout(
        nx_graph,
        k=params.spring_layout_k,
        iterations=params.spring_layout_iterations,
        seed=params.spring_layout_seed,
    )

    for node in nx_graph.nodes():
        nx_graph.nodes[node]["x"] = pos[node][0]
        nx_graph.nodes[node]["y"] = pos[node][1]

    return nx_graph
