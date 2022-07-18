"""Network interface."""


from .vp.analyze.matrix.co_occ_matrix_list import co_occ_matrix_list
from .co_occ_network import co_occ_network
from .network_communities import network_communities
from .network_community_detection import network_community_detection
from .network_degree_plot import network_degree_plot
from .tm2.indicators.network_indicators import network_indicators
from .tm2.plots.network_plot import network_plot


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

    matrix_list = co_occ_matrix_list(
        column=column,
        row=None,
        top_n=top_n,
        directory=directory,
        database=database,
    )

    graph = co_occ_network(matrix_list)
    graph = network_community_detection(graph, method=method)

    result = Result(
        communities=network_communities(graph),
        indicators=network_indicators(graph),
        plot=network_plot(
            graph,
            nx_k=nx_k,
            nx_iteratons=nx_iteratons,
            delta=delta,
        ),
        degree_plot=network_degree_plot(graph),
    )

    return result
