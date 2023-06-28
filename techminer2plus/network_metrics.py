# flake8: noqa
"""
Network Metrics
===============================================================================

>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> graph = techminer2plus.network_clustering(
...    cooc_matrix,
...    algorithm_or_estimator='louvain',
... )
>>> metrics = techminer2plus.network_metrics(graph)
>>> metrics.table_.head()
                              Degree  Betweenness  ...  Centrality  Density
REGTECH 28:329                    19     0.461111  ...        28.0     55.0
FINTECH 12:249                    13     0.088791  ...        12.0     32.0
COMPLIANCE 07:030                 10     0.046881  ...         7.0     19.0
REGULATION 05:164                 10     0.031579  ...         5.0     17.0
REGULATORY_TECHNOLOGY 07:037       9     0.023099  ...         7.0     12.0
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
| REGTECH 28:329                 |       19 |    0.461111   |    1        |  0.136626  |           28 |        55 |
| FINTECH 12:249                 |       13 |    0.0887914  |    0.76     |  0.0913549 |           12 |        32 |
| COMPLIANCE 07:030              |       10 |    0.0468811  |    0.678571 |  0.0722431 |            7 |        19 |
| REGULATION 05:164              |       10 |    0.0315789  |    0.678571 |  0.0707314 |            5 |        17 |
| REGULATORY_TECHNOLOGY 07:037   |        9 |    0.0230994  |    0.655172 |  0.0635479 |            7 |        12 |
| ARTIFICIAL_INTELLIGENCE 04:023 |        9 |    0.0384016  |    0.655172 |  0.0655643 |            4 |        10 |
| RISK_MANAGEMENT 03:014         |        8 |    0.00847953 |    0.633333 |  0.0568575 |            3 |        12 |
| BLOCKCHAIN 03:005              |        6 |    0.0126706  |    0.59375  |  0.046516  |            3 |         7 |
| SUPTECH 03:004                 |        6 |    0          |    0.59375  |  0.0437808 |            3 |         9 |
| ANTI_MONEY_LAUNDERING 05:034   |        5 |    0.00389864 |    0.575758 |  0.0401809 |            5 |         6 |
| FINANCIAL_REGULATION 04:035    |        5 |    0.00536062 |    0.575758 |  0.0405341 |            4 |         7 |
| INNOVATION 03:012              |        5 |    0.00341131 |    0.575758 |  0.0384896 |            3 |         5 |
| FINANCIAL_SERVICES 04:168      |        4 |    0.00146199 |    0.558824 |  0.0324878 |            4 |         8 |
| SEMANTIC_TECHNOLOGIES 02:041   |        4 |    0          |    0.558824 |  0.0316384 |            2 |         6 |
| CHARITYTECH 02:017             |        4 |    0          |    0.558824 |  0.0338227 |            2 |         6 |
| ENGLISH_LAW 02:017             |        4 |    0          |    0.558824 |  0.0338227 |            2 |         6 |
| DATA_PROTECTION 02:027         |        3 |    0          |    0.542857 |  0.0264758 |            2 |         4 |
| ACCOUNTABILITY 02:014          |        3 |    0          |    0.542857 |  0.0275621 |            2 |         6 |
| DATA_PROTECTION_OFFICER 02:014 |        3 |    0          |    0.542857 |  0.0275621 |            2 |         6 |
| SMART_CONTRACTS 02:022         |        2 |    0          |    0.527778 |  0.020202  |            2 |         3 |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""

from .chatbot_prompts import format_chatbot_prompt_for_df
from .classes import NetworkMetrics
from .network_lib import nx_compute_node_degree, nx_compute_node_statistics


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

        return format_chatbot_prompt_for_df(main_text, table.to_markdown())

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
