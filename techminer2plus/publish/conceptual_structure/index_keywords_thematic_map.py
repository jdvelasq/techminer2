# flake8: noqa
"""
Index Keywords Thematic Map
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.publish.conceptual_structure.index_keywords_thematic_map(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/index_keywords_thematic_map.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/index_keywords_thematic_map.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                                | CL_01                      | CL_02                        | CL_03                              |
|---:|:-------------------------------------|:---------------------------|:-----------------------------|:-----------------------------------|
|  0 | FINANCE 5:16                         | FINANCIAL_INSTITUTION 5:07 | REGULATORY_COMPLIANCE 9:34   | REGTECH 5:15                       |
|  1 | ANTI_MONEY_LAUNDERING 3:10           | FINTECH 3:08               | INFORMATION_SYSTEMS 2:14     | FINANCIAL_REGULATION 2:11          |
|  2 | LAUNDERING 2:09                      | BANKING 2:08               | INFORMATION_USE 2:14         | FINANCIAL_SERVICES_INDUSTRIES 2:11 |
|  3 | FINANCIAL_CRISIS 2:07                | RISK_MANAGEMENT 2:05       | SOFTWARE_SOLUTION 2:14       | BLOCKCHAIN 2:02                    |
|  4 | CLASSIFICATION (OF_INFORMATION) 2:03 | COMMERCE 2:04              | REGULATORY_REQUIREMENTS 2:02 |                                    |
|  5 | ARTIFICIAL_INTELLIGENCE 2:02         |                            |                              |                                    |


>>> print(nnet.network_metrics__table_.head().to_markdown())
|                            |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:---------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGULATORY_COMPLIANCE 9:34 |       14 |     0.284186  |    0.791667 |  0.096056  |            9 |        29 |
| FINANCE 5:16               |       12 |     0.119037  |    0.730769 |  0.0805649 |            5 |        21 |
| REGTECH 5:15               |       10 |     0.126827  |    0.678571 |  0.0729142 |            5 |        18 |
| FINANCIAL_INSTITUTION 5:07 |       10 |     0.0539543 |    0.678571 |  0.0671159 |            5 |        14 |
| ANTI_MONEY_LAUNDERING 3:10 |       10 |     0.0542398 |    0.59375  |  0.0683607 |            3 |        12 |


>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network for a \\
research paper. Summarize the text below, delimited by triple backticks, in at \\
most 30 words, identifiying any notable patterns, trends, or outliers in the data.
<BLANKLINE>
Table:
```
|                                      |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGULATORY_COMPLIANCE 9:34           |       14 |    0.284186   |    0.791667 |  0.096056  |            9 |        29 |
| FINANCE 5:16                         |       12 |    0.119037   |    0.730769 |  0.0805649 |            5 |        21 |
| REGTECH 5:15                         |       10 |    0.126827   |    0.678571 |  0.0729142 |            5 |        18 |
| FINANCIAL_INSTITUTION 5:07           |       10 |    0.0539543  |    0.678571 |  0.0671159 |            5 |        14 |
| ANTI_MONEY_LAUNDERING 3:10           |       10 |    0.0542398  |    0.59375  |  0.0683607 |            3 |        12 |
| FINTECH 3:08                         |        8 |    0.0194758  |    0.633333 |  0.0545966 |            3 |        12 |
| COMMERCE 2:04                        |        8 |    0.0194758  |    0.633333 |  0.0545966 |            2 |         9 |
| REGULATORY_REQUIREMENTS 2:02         |        8 |    0.0609162  |    0.633333 |  0.0588268 |            2 |         9 |
| BANKING 2:08                         |        7 |    0.0165692  |    0.527778 |  0.0496328 |            2 |         8 |
| ARTIFICIAL_INTELLIGENCE 2:02         |        7 |    0.04143    |    0.612903 |  0.0504194 |            2 |         8 |
| FINANCIAL_REGULATION 2:11            |        6 |    0.00328947 |    0.59375  |  0.0435721 |            2 |         9 |
| LAUNDERING 2:09                      |        6 |    0.0145712  |    0.527778 |  0.044538  |            2 |         7 |
| RISK_MANAGEMENT 2:05                 |        6 |    0.0072438  |    0.575758 |  0.0424758 |            2 |         8 |
| FINANCIAL_SERVICES_INDUSTRIES 2:11   |        5 |    0.00146199 |    0.558824 |  0.0375315 |            2 |         8 |
| INFORMATION_SYSTEMS 2:14             |        4 |    0          |    0.487179 |  0.0340578 |            2 |         7 |
| INFORMATION_USE 2:14                 |        4 |    0          |    0.487179 |  0.0340578 |            2 |         7 |
| SOFTWARE_SOLUTION 2:14               |        4 |    0          |    0.487179 |  0.0340578 |            2 |         7 |
| FINANCIAL_CRISIS 2:07                |        4 |    0.0135791  |    0.542857 |  0.0314787 |            2 |         4 |
| CLASSIFICATION (OF_INFORMATION) 2:03 |        4 |    0          |    0.5      |  0.0314489 |            2 |         4 |
| BLOCKCHAIN 2:02                      |        1 |    0          |    0.413043 |  0.0136977 |            2 |         1 |
```
<BLANKLINE>




>>> file_name = "sphinx/_static/index_keywords_thematic_map__degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/index_keywords_thematic_map__degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                        Name  Degree
0     0  REGULATORY_COMPLIANCE 9:34      14
1     1                FINANCE 5:16      12
2     2                REGTECH 5:15      10
3     3  FINANCIAL_INSTITUTION 5:07      10
4     4  ANTI_MONEY_LAUNDERING 3:10      10



>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a networkx \\
graph of a co-ocurrence matrix. Analyze the table below, delimited by triple  \\
backticks, identifying any notable patterns, trends, or outliers in the data, and  \\
discuss their implications in the network. 
<BLANKLINE>
Table:
```
|    |   Node | Name                                 |   Degree |
|---:|-------:|:-------------------------------------|---------:|
|  0 |      0 | REGULATORY_COMPLIANCE 9:34           |       14 |
|  1 |      1 | FINANCE 5:16                         |       12 |
|  2 |      2 | REGTECH 5:15                         |       10 |
|  3 |      3 | FINANCIAL_INSTITUTION 5:07           |       10 |
|  4 |      4 | ANTI_MONEY_LAUNDERING 3:10           |       10 |
|  5 |      5 | FINTECH 3:08                         |        8 |
|  6 |      6 | COMMERCE 2:04                        |        8 |
|  7 |      7 | REGULATORY_REQUIREMENTS 2:02         |        8 |
|  8 |      8 | ARTIFICIAL_INTELLIGENCE 2:02         |        7 |
|  9 |      9 | BANKING 2:08                         |        7 |
| 10 |     10 | FINANCIAL_REGULATION 2:11            |        6 |
| 11 |     11 | RISK_MANAGEMENT 2:05                 |        6 |
| 12 |     12 | LAUNDERING 2:09                      |        6 |
| 13 |     13 | FINANCIAL_SERVICES_INDUSTRIES 2:11   |        5 |
| 14 |     14 | INFORMATION_SYSTEMS 2:14             |        4 |
| 15 |     15 | INFORMATION_USE 2:14                 |        4 |
| 16 |     16 | SOFTWARE_SOLUTION 2:14               |        4 |
| 17 |     17 | FINANCIAL_CRISIS 2:07                |        4 |
| 18 |     18 | CLASSIFICATION (OF_INFORMATION) 2:03 |        4 |
| 19 |     19 | BLOCKCHAIN 2:02                      |        1 |
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

FIELD = "index_keywords"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def index_keywords_thematic_map(
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
    """Co-word network from index_keywords."""

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
