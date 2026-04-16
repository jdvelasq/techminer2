import networkx as nx  # type: ignore
import pandas as pd  # type: ignore


def set_edge_width_from_pandas_adjacency(
    nx_graph: nx.Graph,
    adjacency_matrix: pd.DataFrame,
) -> nx.Graph:

    for u, v in nx_graph.edges():
        width = adjacency_matrix.loc[u, v]
        nx_graph.edges[u, v]["width"] = width

    return nx_graph
