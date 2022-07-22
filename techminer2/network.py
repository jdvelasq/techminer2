"""Network interface."""


from .vantagepoint__co_occ_matrix_list import vantagepoint__co_occ_matrix_list
from ._matrix_list_2_network_graph import matrix_list_2_network_graph
from ._get_network_graph_communities import get_network_graph_communities
from ._network_community_detection import network_community_detection
from ._get_network_graph_degree_plot import get_network_graph_degree_plot
from ._get_network_graph_indicators import get_network_graph_indicators
from ._get_network_graph_plot import network_graph_plot


class Result:
    """Results"""

    def __init__(self, communities, indicators, plot, degree_plot):
        self.communities_ = communities
        self.indicators_ = indicators
        self.plot_ = plot
        self.degree_plot_ = degree_plot


def network(
    column,
    top_n=None,
    directory="./",
    database="documents",
    method="louvain",
    nx_k=0.5,
    nx_iteratons=10,
    delta=1.0,
):

    matrix_list = vantagepoint__co_occ_matrix_list(
        column=column,
        row=None,
        top_n=top_n,
        directory=directory,
        database=database,
    )

    graph = matrix_list_2_network_graph(matrix_list)
    graph = network_community_detection(graph, method=method)

    result = Result(
        communities=get_network_graph_communities(graph),
        indicators=get_network_graph_indicators(graph),
        plot=network_graph_plot(
            graph,
            nx_k=nx_k,
            nx_iteratons=nx_iteratons,
            delta=delta,
        ),
        degree_plot=get_network_graph_degree_plot(graph),
    )

    return result
