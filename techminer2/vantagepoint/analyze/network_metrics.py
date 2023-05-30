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
fintech 12:249                 11     0.120202   0.923077  0.117019
regtech 28:329                 12     0.195960   1.000000  0.128111
compliance 07:030               8     0.015404   0.750000  0.085818
regulation 05:164               9     0.055303   0.800000  0.096790
financial services 04:168       4     0.003788   0.600000  0.049449


>>> print(metrics.prompt_)
Analyze the table below, which provides the degree centrality, betweeness centrality, closeness centrality, and pagerank of nodes in a networkx graph of a co-ocurrence matrix. Identify any notable patterns, trends, or outliers in the data, and discuss their implications in the network.
<BLANKLINE>
|                                |   Degree |   Betweenness |   Closeness |   PageRank |
|:-------------------------------|---------:|--------------:|------------:|-----------:|
| fintech 12:249                 |       11 |    0.120202   |    0.923077 |  0.117019  |
| regtech 28:329                 |       12 |    0.19596    |    1        |  0.128111  |
| compliance 07:030              |        8 |    0.015404   |    0.75     |  0.085818  |
| regulation 05:164              |        9 |    0.055303   |    0.8      |  0.0967905 |
| financial services 04:168      |        4 |    0.00378788 |    0.6      |  0.0494494 |
| suptech 03:004                 |        6 |    0          |    0.666667 |  0.0663087 |
| artificial intelligence 04:023 |        7 |    0.0287879  |    0.705882 |  0.0780476 |
| blockchain 03:005              |        5 |    0.00252525 |    0.631579 |  0.0573923 |
| financial regulation 04:035    |        4 |    0.00378788 |    0.6      |  0.0501285 |
| regulatory technology 07:037   |        9 |    0.0598485  |    0.8      |  0.0970981 |
| risk management 03:014         |        7 |    0.00555556 |    0.705882 |  0.0759564 |
| anti-money laundering 03:021   |        3 |    0          |    0.571429 |  0.0392607 |
| innovation 03:012              |        5 |    0.00883838 |    0.631579 |  0.0586198 |
<BLANKLINE>
<BLANKLINE>



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
