import networkx as nx  # type: ignore

from tm2p._intern import Params


def __set_top_n_node_labels_per_group(
    params: Params,
    nx_graph: nx.Graph,
    i2c: dict[str, int],
    top_n: int,
) -> nx.Graph:

    for node in nx_graph.nodes():
        if "text" not in nx_graph.nodes[node]:
            if params.use_counters:
                nx_graph.nodes[node]["text"] = node
            else:
                nx_graph.nodes[node]["text"] = " ".join(node.split(" ")[:-1])

        if "labeled" not in nx_graph.nodes[node]:
            nx_graph.nodes[node]["labeled"] = False

        if "bold" not in nx_graph.nodes[node]:
            nx_graph.nodes[node]["bold"] = False

    c2i: dict[int, list[str]] = {}
    for i, c in i2c.items():
        if c not in c2i:
            c2i[c] = []
        c2i[c].append(i)

    def f(x):
        counters = x.split(" ")[-1]
        occ = counters.split(":")[0]
        gcs = counters.split(":")[1]
        return occ, gcs, x

    for ctr, items in c2i.items():
        items = sorted(items, reverse=False)
        c2i[ctr] = sorted(items, key=f, reverse=True)

    for cluster in set(c2i.keys()):
        n_labeled = 0
        for node in c2i[cluster]:
            if node in nx_graph.nodes():
                nx_graph.nodes[node]["labeled"] = True
                n_labeled += 1
                if n_labeled >= top_n:
                    break

    return nx_graph
