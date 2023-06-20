# flake8: noqa
"""
Key Concepts Thematic Map
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.report.conceptual_structure.key_concepts_thematic_map(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/key_concepts_thematic_map.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/key_concepts_thematic_map.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                              | CL_01                          | CL_02                          |
|---:|:-----------------------------------|:-------------------------------|:-------------------------------|
|  0 | REGULATORY_TECHNOLOGY 20:274       | FINANCIAL_INSTITUTIONS 15:194  | REGTECH 28:329                 |
|  1 | REGULATORY_COMPLIANCE 15:232       | FINTECH 12:249                 | FINANCIAL_CRISIS 07:058        |
|  2 | FINANCIAL_REGULATION 12:395        | ARTIFICIAL_INTELLIGENCE 08:036 | COMPLIANCE 07:030              |
|  3 | FINANCIAL_SERVICES 06:195          | FINANCIAL_SECTOR 07:169        | GLOBAL_FINANCIAL_CRISIS 06:177 |
|  4 | FINANCIAL_TECHNOLOGY 06:173        | FINANCE 07:017                 | INFORMATION_TECHNOLOGY 06:177  |
|  5 | FINANCIAL_SERVICES_INDUSTRY 05:315 | ANTI_MONEY_LAUNDERING 05:024   |                                |
|  6 | FINANCIAL_SYSTEM 05:189            | RISK_MANAGEMENT 05:019         |                                |
|  7 | REGULATION 05:164                  |                                |                                |



>>> print(nnet.network_metrics__table_.head().to_markdown())
|                               |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329                |       19 |     0.0211353 |        1    |  0.060222  |           28 |       112 |
| REGULATORY_TECHNOLOGY 20:274  |       19 |     0.0211353 |        1    |  0.060222  |           20 |        86 |
| FINANCIAL_INSTITUTIONS 15:194 |       19 |     0.0211353 |        1    |  0.060222  |           15 |        59 |
| REGULATORY_COMPLIANCE 15:232  |       18 |     0.0144705 |        0.95 |  0.0572486 |           15 |        72 |
| FINTECH 12:249                |       18 |     0.0196211 |        0.95 |  0.0574544 |           12 |        63 |


>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network for a \\
research paper. Summarize the text below, delimited by triple backticks, in at \\
most 30 words, identifiying any notable patterns, trends, or outliers in the data.
<BLANKLINE>
Table:
```
|                                    |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329                     |       19 |   0.0211353   |    1        |  0.060222  |           28 |       112 |
| REGULATORY_TECHNOLOGY 20:274       |       19 |   0.0211353   |    1        |  0.060222  |           20 |        86 |
| FINANCIAL_INSTITUTIONS 15:194      |       19 |   0.0211353   |    1        |  0.060222  |           15 |        59 |
| REGULATORY_COMPLIANCE 15:232       |       18 |   0.0144705   |    0.95     |  0.0572486 |           15 |        72 |
| FINTECH 12:249                     |       18 |   0.0196211   |    0.95     |  0.0574544 |           12 |        63 |
| FINANCE 07:017                     |       18 |   0.0168468   |    0.95     |  0.0573489 |            7 |        40 |
| FINANCIAL_REGULATION 12:395        |       17 |   0.0124933   |    0.904762 |  0.0544522 |           12 |        55 |
| INFORMATION_TECHNOLOGY 06:177      |       16 |   0.0126151   |    0.863636 |  0.05174   |            6 |        34 |
| REGULATION 05:164                  |       16 |   0.0123386   |    0.863636 |  0.0517701 |            5 |        30 |
| ARTIFICIAL_INTELLIGENCE 08:036     |       15 |   0.010003    |    0.826087 |  0.0489387 |            8 |        31 |
| FINANCIAL_SERVICES_INDUSTRY 05:315 |       15 |   0.00629741  |    0.826087 |  0.0487545 |            5 |        30 |
| FINANCIAL_SYSTEM 05:189            |       15 |   0.00813977  |    0.826087 |  0.0488675 |            5 |        30 |
| RISK_MANAGEMENT 05:019             |       15 |   0.010836    |    0.826087 |  0.0490093 |            5 |        29 |
| FINANCIAL_CRISIS 07:058            |       14 |   0.00731131  |    0.791667 |  0.0460915 |            7 |        29 |
| FINANCIAL_SERVICES 06:195          |       14 |   0.00436413  |    0.791667 |  0.0458819 |            6 |        34 |
| GLOBAL_FINANCIAL_CRISIS 06:177     |       14 |   0.00567977  |    0.791667 |  0.046011  |            6 |        30 |
| FINANCIAL_SECTOR 07:169            |       12 |   0.00175787  |    0.730769 |  0.0402848 |            7 |        24 |
| COMPLIANCE 07:030                  |       12 |   0.00262542  |    0.730769 |  0.0403626 |            7 |        29 |
| FINANCIAL_TECHNOLOGY 06:173        |       12 |   0.000783208 |    0.730769 |  0.0402461 |            6 |        32 |
| ANTI_MONEY_LAUNDERING 05:024       |       10 |   0.000937172 |    0.678571 |  0.0348718 |            5 |        17 |
```
<BLANKLINE>


>>> file_name = "sphinx/_static/key_concepts_thematic_map__degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/key_concepts_thematic_map__degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                           Name  Degree
0     0   REGULATORY_TECHNOLOGY 20:274      19
1     1  FINANCIAL_INSTITUTIONS 15:194      19
2     2                 REGTECH 28:329      19
3     3   REGULATORY_COMPLIANCE 15:232      18
4     4                 FINTECH 12:249      18




>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a networkx \\
graph of a co-ocurrence matrix. Analyze the table below, delimited by triple  \\
backticks, identifying any notable patterns, trends, or outliers in the data, and  \\
discuss their implications in the network. 
<BLANKLINE>
Table:
```
|    |   Node | Name                               |   Degree |
|---:|-------:|:-----------------------------------|---------:|
|  0 |      0 | REGULATORY_TECHNOLOGY 20:274       |       19 |
|  1 |      1 | FINANCIAL_INSTITUTIONS 15:194      |       19 |
|  2 |      2 | REGTECH 28:329                     |       19 |
|  3 |      3 | REGULATORY_COMPLIANCE 15:232       |       18 |
|  4 |      4 | FINTECH 12:249                     |       18 |
|  5 |      5 | FINANCE 07:017                     |       18 |
|  6 |      6 | FINANCIAL_REGULATION 12:395        |       17 |
|  7 |      7 | INFORMATION_TECHNOLOGY 06:177      |       16 |
|  8 |      8 | REGULATION 05:164                  |       16 |
|  9 |      9 | ARTIFICIAL_INTELLIGENCE 08:036     |       15 |
| 10 |     10 | FINANCIAL_SERVICES_INDUSTRY 05:315 |       15 |
| 11 |     11 | FINANCIAL_SYSTEM 05:189            |       15 |
| 12 |     12 | RISK_MANAGEMENT 05:019             |       15 |
| 13 |     13 | FINANCIAL_CRISIS 07:058            |       14 |
| 14 |     14 | FINANCIAL_SERVICES 06:195          |       14 |
| 15 |     15 | GLOBAL_FINANCIAL_CRISIS 06:177     |       14 |
| 16 |     16 | FINANCIAL_SECTOR 07:169            |       12 |
| 17 |     17 | COMPLIANCE 07:030                  |       12 |
| 18 |     18 | FINANCIAL_TECHNOLOGY 06:173        |       12 |
| 19 |     19 | ANTI_MONEY_LAUNDERING 05:024       |       10 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""

# from ...classes import CoWordsNetwork
# from ...vantagepoint.analyze import (
#     co_occurrence_matrix,
#     matrix_normalization,
#     network_clustering,
#     network_communities,
#     network_degree_plot,
#     network_metrics,
#     network_viewer,
# )

FIELD = "key_concepts"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def key_concepts_thematic_map(
    algorithm="louvain",
    network_viewer_dict=None,
    network_degree_plot_dict=None,
    # Items params:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Co-word network from key_concepts."""

    if network_degree_plot_dict is None:
        network_degree_plot_dict = {}

    if network_viewer_dict is None:
        network_viewer_dict = {}

    coc_matrix = co_occurrence_matrix(
        columns=FIELD,
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    norm_coc_matrix = matrix_normalization(
        coc_matrix, index_name="association"
    )

    graph = network_clustering(norm_coc_matrix, algorithm=algorithm)

    degree_plot = network_degree_plot(graph=graph, **network_degree_plot_dict)

    metrics = network_metrics(graph=graph)

    network = CoWordsNetwork()
    network.plot_ = network_viewer(graph=graph, **network_viewer_dict)
    network.graph_ = graph
    network.communities_ = network_communities(graph=graph)

    network.network_metrics__table_ = metrics.table_
    network.network_metrics__prompt_ = metrics.prompt_

    network.degree_plot__plot_ = degree_plot.plot_
    network.degree_plot__table_ = degree_plot.table_
    network.degree_plot__prompt_ = degree_plot.prompt_

    return network
