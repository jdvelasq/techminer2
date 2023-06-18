# flake8: noqa
"""
Keywords Co-occurrence Network
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.conceptual_structure.keywords_co_occ_network(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/keywords_co_occ_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/keywords_co_occ_network.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                        | CL_01                          | CL_02                                  |
|---:|:-----------------------------|:-------------------------------|:---------------------------------------|
|  0 | FINTECH 12:249               | REGTECH 28:329                 | REGULATION 05:164                      |
|  1 | REGULATORY_COMPLIANCE 09:034 | COMPLIANCE 07:030              | ANTI_MONEY_LAUNDERING 05:024           |
|  2 | FINANCE 07:017               | ARTIFICIAL_INTELLIGENCE 06:025 | REGULATORY_TECHNOLOGY (REGTECH) 04:030 |
|  3 | FINANCIAL_REGULATION 05:035  | REGULATORY_TECHNOLOGY 05:008   | INNOVATION 03:012                      |
|  4 | RISK_MANAGEMENT 05:019       | BLOCKCHAIN 03:005              |                                        |
|  5 | FINANCIAL_INSTITUTION 05:007 | SMART_CONTRACTS 02:022         |                                        |
|  6 | FINANCIAL_SERVICES 04:168    | CHARITYTECH 02:017             |                                        |
|  7 | SUPTECH 03:004               |                                |                                        |
|  8 | DATA_PROTECTION 02:027       |                                |                                        |


>>> print(nnet.network_metrics__table_.head().to_markdown())
|                        |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329         |       18 |     0.218361  |    0.95     |  0.0943363 |           28 |        71 |
| FINTECH 12:249         |       16 |     0.0809338 |    0.863636 |  0.081157  |           12 |        39 |
| RISK_MANAGEMENT 05:019 |       13 |     0.0215005 |    0.76     |  0.0654412 |            5 |        23 |
| FINANCE 07:017         |       12 |     0.016539  |    0.730769 |  0.0609392 |            7 |        26 |
| REGULATION 05:164      |       12 |     0.0277082 |    0.730769 |  0.0616375 |            5 |        20 |


>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network for a \\
research paper. Summarize the text below, delimited by triple backticks, in at \\
most 30 words, identifiying any notable patterns, trends, or outliers in the data.
<BLANKLINE>
Table:
```
|                                        |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:---------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329                         |       18 |    0.218361   |    0.95     |  0.0943363 |           28 |        71 |
| FINTECH 12:249                         |       16 |    0.0809338  |    0.863636 |  0.081157  |           12 |        39 |
| RISK_MANAGEMENT 05:019                 |       13 |    0.0215005  |    0.76     |  0.0654412 |            5 |        23 |
| FINANCE 07:017                         |       12 |    0.016539   |    0.730769 |  0.0609392 |            7 |        26 |
| REGULATION 05:164                      |       12 |    0.0277082  |    0.730769 |  0.0616375 |            5 |        20 |
| FINANCIAL_INSTITUTION 05:007           |       12 |    0.0153555  |    0.730769 |  0.0607975 |            5 |        20 |
| REGULATORY_COMPLIANCE 09:034           |       11 |    0.013267   |    0.703704 |  0.0563238 |            9 |        30 |
| COMPLIANCE 07:030                      |       10 |    0.0110995  |    0.678571 |  0.0524041 |            7 |        21 |
| ARTIFICIAL_INTELLIGENCE 06:025         |       10 |    0.0297341  |    0.678571 |  0.0541883 |            6 |        14 |
| ANTI_MONEY_LAUNDERING 05:024           |       10 |    0.0472918  |    0.678571 |  0.0548235 |            5 |        13 |
| SUPTECH 03:004                         |       10 |    0.00724961 |    0.678571 |  0.0515413 |            3 |        13 |
| FINANCIAL_REGULATION 05:035            |        9 |    0.0162327  |    0.655172 |  0.0486602 |            5 |        15 |
| REGULATORY_TECHNOLOGY 05:008           |        9 |    0.0381625  |    0.655172 |  0.0487621 |            5 |        13 |
| INNOVATION 03:012                      |        9 |    0.030421   |    0.655172 |  0.0488465 |            3 |         9 |
| FINANCIAL_SERVICES 04:168              |        8 |    0.00221619 |    0.612903 |  0.0424815 |            4 |        14 |
| BLOCKCHAIN 03:005                      |        6 |    0.0124269  |    0.575758 |  0.0370024 |            3 |         7 |
| REGULATORY_TECHNOLOGY (REGTECH) 04:030 |        3 |    0.00214425 |    0.487179 |  0.0213786 |            4 |         3 |
| DATA_PROTECTION 02:027                 |        3 |    0          |    0.527778 |  0.0208615 |            2 |         4 |
| CHARITYTECH 02:017                     |        3 |    0          |    0.542857 |  0.0212208 |            2 |         4 |
| SMART_CONTRACTS 02:022                 |        2 |    0          |    0.513514 |  0.0171967 |            2 |         3 |
```
<BLANKLINE>



>>> file_name = "sphinx/_static/keywords_co_occ_network__degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/keywords_co_occ_network__degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                    Name  Degree
0     0          REGTECH 28:329      18
1     1          FINTECH 12:249      16
2     2  RISK_MANAGEMENT 05:019      13
3     3          FINANCE 07:017      12
4     4       REGULATION 05:164      12


>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a networkx \\
graph of a co-ocurrence matrix. Analyze the table below, delimited by triple  \\
backticks, identifying any notable patterns, trends, or outliers in the data, and  \\
discuss their implications in the network. 
<BLANKLINE>
Table:
```
|    |   Node | Name                                   |   Degree |
|---:|-------:|:---------------------------------------|---------:|
|  0 |      0 | REGTECH 28:329                         |       18 |
|  1 |      1 | FINTECH 12:249                         |       16 |
|  2 |      2 | RISK_MANAGEMENT 05:019                 |       13 |
|  3 |      3 | FINANCE 07:017                         |       12 |
|  4 |      4 | REGULATION 05:164                      |       12 |
|  5 |      5 | FINANCIAL_INSTITUTION 05:007           |       12 |
|  6 |      6 | REGULATORY_COMPLIANCE 09:034           |       11 |
|  7 |      7 | COMPLIANCE 07:030                      |       10 |
|  8 |      8 | ARTIFICIAL_INTELLIGENCE 06:025         |       10 |
|  9 |      9 | ANTI_MONEY_LAUNDERING 05:024           |       10 |
| 10 |     10 | SUPTECH 03:004                         |       10 |
| 11 |     11 | FINANCIAL_REGULATION 05:035            |        9 |
| 12 |     12 | REGULATORY_TECHNOLOGY 05:008           |        9 |
| 13 |     13 | INNOVATION 03:012                      |        9 |
| 14 |     14 | FINANCIAL_SERVICES 04:168              |        8 |
| 15 |     15 | BLOCKCHAIN 03:005                      |        6 |
| 16 |     16 | DATA_PROTECTION 02:027                 |        3 |
| 17 |     17 | CHARITYTECH 02:017                     |        3 |
| 18 |     18 | REGULATORY_TECHNOLOGY (REGTECH) 04:030 |        3 |
| 19 |     19 | SMART_CONTRACTS 02:022                 |        2 |
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

FIELD = "keywords"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def keywords_co_occ_network(
    normalization="association",
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
    """Co-word network from keywords."""

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
        coc_matrix, index_name=normalization
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
