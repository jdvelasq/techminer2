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
>>> graph = vantagepoint.analyze.cluster_column(
...    normalized_co_occ_matrix,
...    community_clustering='louvain',
... )
>>> metrics = vantagepoint.analyze.network_metrics(graph)
>>> metrics.table_.head()
                                Degree  Betweenness  Closeness  PageRank
REGTECH 28:329                      12     0.235256   0.928571  0.126702
FINTECH 12:249                      11     0.129487   0.866667  0.114555
REGULATION 05:164                    9     0.070299   0.764706  0.094636
COMPLIANCE 07:030                    8     0.013034   0.684211  0.083308
ARTIFICIAL_INTELLIGENCE 04:023       7     0.047436   0.684211  0.077037



>>> print(metrics.prompt_)
Analyze the table below, which provides the degree centrality, betweeness centrality, closeness centrality, and pagerank of nodes in a networkx graph of a co-ocurrence matrix. Identify any notable patterns, trends, or outliers in the data, and discuss their implications in the network.
<BLANKLINE>
|                                        |   Degree |   Betweenness |   Closeness |   PageRank |
|:---------------------------------------|---------:|--------------:|------------:|-----------:|
| REGTECH 28:329                         |       12 |    0.235256   |    0.928571 |  0.126702  |
| FINTECH 12:249                         |       11 |    0.129487   |    0.866667 |  0.114555  |
| REGULATION 05:164                      |        9 |    0.0702991  |    0.764706 |  0.0946356 |
| COMPLIANCE 07:030                      |        8 |    0.0130342  |    0.684211 |  0.0833083 |
| ARTIFICIAL_INTELLIGENCE 04:023         |        7 |    0.0474359  |    0.684211 |  0.0770373 |
| RISK_MANAGEMENT 03:014                 |        7 |    0.00470085 |    0.65     |  0.0737394 |
| REGULATORY_TECHNOLOGY 03:007           |        7 |    0.00470085 |    0.65     |  0.0737394 |
| SUPTECH 03:004                         |        6 |    0          |    0.619048 |  0.0642384 |
| INNOVATION 03:012                      |        5 |    0.0987179  |    0.619048 |  0.0622221 |
| BLOCKCHAIN 03:005                      |        5 |    0.00213675 |    0.590909 |  0.0556851 |
| FINANCIAL_SERVICES 04:168              |        4 |    0.00320513 |    0.565217 |  0.0479574 |
| FINANCIAL_REGULATION 04:035            |        4 |    0.00576923 |    0.590909 |  0.0493095 |
| ANTI-MONEY_LAUNDERING 03:021           |        3 |    0.0455128  |    0.565217 |  0.0433084 |
| REGULATORY_TECHNOLOGY (REGTECH) 04:030 |        2 |    0.00641026 |    0.433333 |  0.0335623 |
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
