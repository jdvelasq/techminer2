import networkx as nx  # type: ignore
import pandas as pd  # type: ignore

BETWEENNESS_CENTRALITY = "BETWEENNESS_CENTRALITY"
CLOSENESS_CENTRALITY = "CLOSENESS_CENTRALITY"
CLUSTERING = "CLUSTERING"
CORE_NUMBER = "CORE_NUMBER"
DEGREE_CENTRALITY = "DEGREE_CENTRALITY"
EIGENVECTOR_CENTRALITY = "EIGENVECTOR_CENTRALITY"
PAGERANK = "PAGERANK"
STRENGTH = "STRENGTH"


def compute_node_metrics(
    nx_graph,
):
    """Compute network statistics."""

    def compute_node_degree(nx_graph):
        """Computes the degree of each node in a networkx graph."""

        for node in nx_graph.nodes():
            nx_graph.nodes[node]["labeled"] = True

        return nx_graph

    nx_graph = compute_node_degree(nx_graph)

    nodes = list(nx_graph.nodes())
    occ_gc = [node.split(" ")[-1] for node in nodes]

    data_frame = pd.DataFrame(
        {
            DEGREE_CENTRALITY: nx.degree_centrality(nx_graph),
            BETWEENNESS_CENTRALITY: nx.betweenness_centrality(nx_graph),
            CLOSENESS_CENTRALITY: nx.closeness_centrality(nx_graph),
            PAGERANK: nx.pagerank(nx_graph),
            EIGENVECTOR_CENTRALITY: nx.eigenvector_centrality(nx_graph),
            CLUSTERING: nx.clustering(nx_graph),
            CORE_NUMBER: nx.core_number(nx_graph),
            STRENGTH: dict(nx_graph.degree(weight="weight")),
            "_occ_gc_": occ_gc,
            "_name_": nodes,
        },
        index=nodes,
    )

    data_frame = data_frame.sort_values(
        by=[STRENGTH, "_occ_gc_", "_name_"],
        ascending=[False, False, True],
    )
    data_frame = data_frame.drop(columns=["_name_", "_occ_gc_"])

    return data_frame
