# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements


#
# Compute network metrics
#

import networkx as nx  # type: ignore
import pandas as pd  # type: ignore


def internal__compute_network_metrics(
    #
    # NETWORKX GRAPH:
    nx_graph,
):
    """Compute network statistics."""

    def compute_node_degree(nx_graph):
        """Computes the degree of each node in a networkx graph."""

        for node, adjacencies in nx_graph.adjacency():
            nx_graph.nodes[node]["degree"] = len(adjacencies)

        return nx_graph

    nx_graph = compute_node_degree(nx_graph)

    nodes = list(nx_graph.nodes())
    degree = [nx_graph.nodes[node]["degree"] for node in nodes]

    # occ_gc = [node.split(" ")[-1] for node in nodes]
    # occ = [int(text.split(":")[0]) for text in occ_gc]
    # gc = [int(text.split(":")[-1]) for text in occ_gc]
    betweenness = nx.betweenness_centrality(nx_graph)
    closeness = nx.closeness_centrality(nx_graph)
    pagerank = nx.pagerank(nx_graph)

    #
    # Callon centrality - density map
    ## callon_matrix = nx_graph_to_co_occ_matrix(graph).astype(float)
    ## callon_centrality = callon_matrix.values.diagonal()
    ## callon_density = callon_matrix.sum() - callon_centrality
    ## strategic_diagram["callon_centrality"] *= 10
    ## strategic_diagram["callon_density"] *= 100

    data_frame = pd.DataFrame(
        {
            "Degree": degree,
            "Betweenness": betweenness,
            "Closeness": closeness,
            "PageRank": pagerank,
            ## "Centrality": callon_centrality,
            ## "Density": callon_density,
            ## "_occ_": occ,
            ## "_gc_": gc,
            "_name_": nodes,
        },
        index=nodes,
    )

    ## data_frame = data_frame.sort_values(
    ##     by=["Degree", "_occ_", "_gc_", "_name_"],
    ##     ascending=[False, False, False, True],
    ## )
    ## data_frame = data_frame.drop(columns=["_occ_", "_gc_", "_name_"])

    data_frame = data_frame.sort_values(
        by=["Degree", "_name_"],
        ascending=[False, True],
    )
    data_frame = data_frame.drop(columns=["_name_"])

    return data_frame
