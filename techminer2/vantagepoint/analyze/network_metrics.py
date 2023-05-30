# flake8: noqa
"""
Network metrics
===============================================================================

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> file_name = "sphinx/_static/vantagepoint__network_degree_plot.html"
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_occ_min=3,
...    root_dir=root_dir,
... )
>>> normalized_co_occ_matrix = vantagepoint.analyze.association_index(
...     co_occ_matrix, "association"
... )
>>> graph = vantagepoint.analyze.cluster_criterion(
...    normalized_co_occ_matrix,
...    community_clustering='louvain',
... )
>>> metrics = vantagepoint.analyze.network_metrics(graph)
>>> metrics.table_.head()
                              Degree  Betweenness  Closeness  PageRank
regulatory technology 07:037       9     0.059848   0.800000  0.097098
compliance 07:030                  8     0.015404   0.750000  0.085818
financial regulation 04:035        4     0.003788   0.600000  0.050128
blockchain 03:005                  5     0.002525   0.631579  0.057392
regulation 05:164                  9     0.055303   0.800000  0.096790



>>> print(obj.prompt_)



# noqa: E501


"""

from ... import network_utils
from ...classes import NetworkStatistics


def network_metrics(
    graph,
):
    """Compute network metrics a co-occurrence matrix."""

    def generate_chatgpt_prompt(table):
        """Generates a chatgpt prompt."""

        prompt = (
            "Analyze the table below, which provides the degree centrality, "
            "betweeness centrality, closeness centrality, and pagerank of "
            "nodes in a networkx graph of a co-ocurrence matrix. Identify "
            "any notable patterns, trends, or outliers in the data, and "
            "discuss their implications in the network."
            f"\n\n{table.to_markdown()}\n\n"
        )

        return prompt

    #
    #
    # Main:
    #
    #
    graph = network_utils.compute_node_degree(graph)
    table = network_utils.compute_newtork_statistics(graph)

    obj = NetworkStatistics()

    obj.table_ = table
    obj.prompt_ = generate_chatgpt_prompt(table)

    return obj
