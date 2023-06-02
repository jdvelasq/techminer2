# flake8: noqa
"""
Network metrics
===============================================================================

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> file_name = "sphinx/_static/vantagepoint__network_degree_plot.html"
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
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
regtech 28:329                    12     0.195960   1.000000  0.128111
fintech 12:249                    11     0.120202   0.923077  0.117019
regulatory technology 07:037       9     0.059848   0.800000  0.097098
regulation 05:164                  9     0.055303   0.800000  0.096790
compliance 07:030                  8     0.015404   0.750000  0.085818



>>> print(metrics.prompt_)
Analyze the table below, which provides the degree centrality, betweeness centrality, closeness centrality, and pagerank of nodes in a networkx graph of a co-ocurrence matrix. Identify any notable patterns, trends, or outliers in the data, and discuss their implications in the network.
<BLANKLINE>
|                                |   Degree |   Betweenness |   Closeness |   PageRank |
|:-------------------------------|---------:|--------------:|------------:|-----------:|
| regtech 28:329                 |       12 |    0.19596    |    1        |  0.128111  |
| fintech 12:249                 |       11 |    0.120202   |    0.923077 |  0.117019  |
| regulatory technology 07:037   |        9 |    0.0598485  |    0.8      |  0.0970981 |
| regulation 05:164              |        9 |    0.055303   |    0.8      |  0.0967905 |
| compliance 07:030              |        8 |    0.015404   |    0.75     |  0.085818  |
| artificial intelligence 04:023 |        7 |    0.0287879  |    0.705882 |  0.0780476 |
| risk management 03:014         |        7 |    0.00555556 |    0.705882 |  0.0759564 |
| suptech 03:004                 |        6 |    0          |    0.666667 |  0.0663087 |
| innovation 03:012              |        5 |    0.00883838 |    0.631579 |  0.0586198 |
| blockchain 03:005              |        5 |    0.00252525 |    0.631579 |  0.0573923 |
| financial services 04:168      |        4 |    0.00378788 |    0.6      |  0.0494494 |
| financial regulation 04:035    |        4 |    0.00378788 |    0.6      |  0.0501285 |
| anti-money laundering 03:021   |        3 |    0          |    0.571429 |  0.0392607 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""

from ...classes import NetworkStatistics
from ...network_utils import compute_newtork_statistics, compute_node_degree


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
    graph = compute_node_degree(graph)
    table = compute_newtork_statistics(graph)

    obj = NetworkStatistics()

    obj.table_ = table
    obj.prompt_ = generate_chatgpt_prompt(table)

    return obj
