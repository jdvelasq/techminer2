import networkx as nx  # type: ignore

from tm2p._intern import Params


def set_top_n_node_labels(
    params: Params,
    nx_graph: nx.Graph,
) -> nx.Graph:

    nx_graph = _initialize_node_properties(params, nx_graph)
    sorted_nodes = _get_sorted_nodes(nx_graph)
    nx_graph = _set_node_labels(params, nx_graph, sorted_nodes)

    return nx_graph


def _set_node_labels(params, nx_graph, sorted_nodes):
    n_labeled = 0
    for node in sorted_nodes:
        nx_graph.nodes[node]["labeled"] = True
        n_labeled += 1
        if n_labeled >= params.max_node_labels:
            break
    return nx_graph


def _get_sorted_nodes(nx_graph):

    nodes = list(nx_graph.nodes())

    def f(x):
        counters = x.split(" ")[-1]
        occ = counters.split(":")[0]
        gcs = counters.split(":")[1]
        return int(occ), int(gcs), x

    return sorted(nodes, key=f, reverse=True)


def _initialize_node_properties(params, nx_graph):

    for node in nx_graph.nodes():

        nx_graph.nodes[node]["labeled"] = False

        if params.use_counters:
            name = node
        else:
            name = " ".join(node.split(" ")[:-1])

        if len(name) > params.node_label_max_length:
            name = name[: params.node_label_max_length] + "…"

        nx_graph.nodes[node]["text"] = name

    return nx_graph
