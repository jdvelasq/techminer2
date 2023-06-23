# flake8: noqa
"""
Network Metrics
===============================================================================

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> cooc_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=root_dir,
... )
>>> graph = techminer2plus.analyze.network.cluster_network(
...    cooc_matrix,
...    algorithm_or_estimator='louvain',
... )
>>> metrics = techminer2plus.analyze.network.network_metrics(graph)
>>> metrics.table_.head()
                              Degree  Betweenness  ...  Centrality  Density
REGTECH 28:329                    12     0.195960  ...        28.0     41.0
FINTECH 12:249                    11     0.120202  ...        12.0     29.0
REGULATORY_TECHNOLOGY 07:037       9     0.059848  ...         7.0     12.0
REGULATION 05:164                  9     0.055303  ...         5.0     16.0
COMPLIANCE 07:030                  8     0.015404  ...         7.0     15.0
<BLANKLINE>
[5 rows x 6 columns]


>>> print(metrics.prompt_)
Your task is to generate a short analysis of the indicators of a network \\
for a research paper. Summarize the text below, delimited by triple \\
backticks, in at most 30 words, identifiying any notable patterns, trends, \\
or outliers in the data.
<BLANKLINE>
Table:
```
|                                |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329                 |       12 |    0.19596    |    1        |  0.128111  |           28 |        41 |
| FINTECH 12:249                 |       11 |    0.120202   |    0.923077 |  0.117019  |           12 |        29 |
| REGULATORY_TECHNOLOGY 07:037   |        9 |    0.0598485  |    0.8      |  0.0970981 |            7 |        12 |
| REGULATION 05:164              |        9 |    0.055303   |    0.8      |  0.0967905 |            5 |        16 |
| COMPLIANCE 07:030              |        8 |    0.015404   |    0.75     |  0.085818  |            7 |        15 |
| ARTIFICIAL_INTELLIGENCE 04:023 |        7 |    0.0287879  |    0.705882 |  0.0780476 |            4 |         8 |
| RISK_MANAGEMENT 03:014         |        7 |    0.00555556 |    0.705882 |  0.0759564 |            3 |        11 |
| SUPTECH 03:004                 |        6 |    0          |    0.666667 |  0.0663087 |            3 |         9 |
| INNOVATION 03:012              |        5 |    0.00883838 |    0.631579 |  0.0586198 |            3 |         5 |
| BLOCKCHAIN 03:005              |        5 |    0.00252525 |    0.631579 |  0.0573923 |            3 |         6 |
| FINANCIAL_SERVICES 04:168      |        4 |    0.00378788 |    0.6      |  0.0494494 |            4 |         8 |
| FINANCIAL_REGULATION 04:035    |        4 |    0.00378788 |    0.6      |  0.0501285 |            4 |         6 |
| ANTI_MONEY_LAUNDERING 05:034   |        3 |    0          |    0.571429 |  0.0392607 |            5 |         4 |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""

from ...classes import NetworkMetrics
from ...network import nx_compute_node_degree, nx_compute_node_statistics
from ...prompts import format_prompt_for_tables


def network_metrics(
    graph,
):
    """Compute network metrics a co-occurrence matrix."""

    def generate_chatgpt_prompt(table):
        """Generates a chatgpt prompt."""

        main_text = (
            "Your task is to generate a short analysis of the indicators of a network for a "
            "research paper. Summarize the text below, delimited by triple backticks, in at "
            "most 30 words, identifiying any notable patterns, trends, or outliers in the data."
        )

        return format_prompt_for_tables(main_text, table.to_markdown())

    #
    #
    # Main:
    #
    #

    graph = nx_compute_node_degree(graph)
    table = nx_compute_node_statistics(graph)

    obj = NetworkMetrics()

    obj.table_ = table
    obj.prompt_ = generate_chatgpt_prompt(table)

    return obj
