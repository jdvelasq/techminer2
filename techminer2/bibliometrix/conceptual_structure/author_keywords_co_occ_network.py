# flake8: noqa
"""
Author Keywords Co-occurrence Network
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.conceptual_structure.author_keywords_co_occ_network(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/author_keywords_co_occ_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/author_keywords_co_occ_network.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                       | CL_01                                  | CL_02                          | CL_03                        |
|---:|:----------------------------|:---------------------------------------|:-------------------------------|:-----------------------------|
|  0 | REGTECH 28:329              | REGULATORY_TECHNOLOGY (REGTECH) 04:030 | COMPLIANCE 07:030              | REGULATION 05:164            |
|  1 | FINTECH 12:249              | ANTI_MONEY_LAUNDERING 04:023           | ACCOUNTABILITY 02:014          | RISK_MANAGEMENT 03:014       |
|  2 | FINANCIAL_SERVICES 04:168   | ARTIFICIAL_INTELLIGENCE 04:023         | DATA_PROTECTION_OFFICER 02:014 | REGULATORY_TECHNOLOGY 03:007 |
|  3 | FINANCIAL_REGULATION 04:035 | CHARITYTECH 02:017                     | GDPR 02:014                    | SUPTECH 03:004               |
|  4 | INNOVATION 03:012           | ENGLISH_LAW 02:017                     |                                |                              |
|  5 | BLOCKCHAIN 03:005           |                                        |                                |                              |
|  6 | DATA_PROTECTION 02:027      |                                        |                                |                              |

>>> print(nnet.network_metrics__table_.head().to_markdown())
|                                |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329                 |       18 |     0.441618  |    0.95     |  0.131035  |           28 |        53 |
| FINTECH 12:249                 |       12 |     0.0848928 |    0.730769 |  0.08664   |           12 |        30 |
| COMPLIANCE 07:030              |       11 |     0.0673489 |    0.678571 |  0.0796284 |            7 |        21 |
| REGULATION 05:164              |        9 |     0.0320663 |    0.655172 |  0.0655075 |            5 |        16 |
| ARTIFICIAL_INTELLIGENCE 04:023 |        9 |     0.0508772 |    0.655172 |  0.067371  |            4 |        10 |

>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network for a \\
research paper. Summarize the text below, delimited by triple backticks, in at \\
most 30 words, identifiying any notable patterns, trends, or outliers in the data.
<BLANKLINE>
Table:
```
|                                        |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:---------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329                         |       18 |   0.441618    |    0.95     |  0.131035  |           28 |        53 |
| FINTECH 12:249                         |       12 |   0.0848928   |    0.730769 |  0.08664   |           12 |        30 |
| COMPLIANCE 07:030                      |       11 |   0.0673489   |    0.678571 |  0.0796284 |            7 |        21 |
| REGULATION 05:164                      |        9 |   0.0320663   |    0.655172 |  0.0655075 |            5 |        16 |
| ARTIFICIAL_INTELLIGENCE 04:023         |        9 |   0.0508772   |    0.655172 |  0.067371  |            4 |        10 |
| RISK_MANAGEMENT 03:014                 |        7 |   0.00214425  |    0.59375  |  0.0510375 |            3 |        11 |
| REGULATORY_TECHNOLOGY 03:007           |        7 |   0.00214425  |    0.59375  |  0.0510375 |            3 |         9 |
| SUPTECH 03:004                         |        6 |   0           |    0.575758 |  0.0445594 |            3 |         9 |
| FINANCIAL_REGULATION 04:035            |        5 |   0.0079922   |    0.575758 |  0.0417243 |            4 |         7 |
| ANTI_MONEY_LAUNDERING 04:023           |        5 |   0.0426901   |    0.575758 |  0.0444215 |            4 |         5 |
| INNOVATION 03:012                      |        5 |   0.0581871   |    0.575758 |  0.0425786 |            3 |         5 |
| BLOCKCHAIN 03:005                      |        5 |   0.000974659 |    0.558824 |  0.0385276 |            3 |         6 |
| FINANCIAL_SERVICES 04:168              |        4 |   0.00146199  |    0.542857 |  0.0331049 |            4 |         8 |
| CHARITYTECH 02:017                     |        4 |   0           |    0.558824 |  0.035051  |            2 |         6 |
| ENGLISH_LAW 02:017                     |        4 |   0           |    0.558824 |  0.035051  |            2 |         6 |
| ACCOUNTABILITY 02:014                  |        4 |   0           |    0.542857 |  0.0345056 |            2 |         8 |
| DATA_PROTECTION_OFFICER 02:014         |        4 |   0           |    0.542857 |  0.0345056 |            2 |         8 |
| GDPR 02:014                            |        4 |   0           |    0.542857 |  0.0345056 |            2 |         8 |
| DATA_PROTECTION 02:027                 |        3 |   0           |    0.527778 |  0.0269181 |            2 |         4 |
| REGULATORY_TECHNOLOGY (REGTECH) 04:030 |        2 |   0.00292398  |    0.413043 |  0.0222899 |            4 |         2 |
```
<BLANKLINE>



>>> file_name = "sphinx/_static/author_keywords_co_occ_network__degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/author_keywords_co_occ_network__degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                            Name  Degree
0     0                  REGTECH 28:329      18
1     1                  FINTECH 12:249      12
2     2               COMPLIANCE 07:030      11
3     3               REGULATION 05:164       9
4     4  ARTIFICIAL_INTELLIGENCE 04:023       9

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
|  1 |      1 | FINTECH 12:249                         |       12 |
|  2 |      2 | COMPLIANCE 07:030                      |       11 |
|  3 |      3 | REGULATION 05:164                      |        9 |
|  4 |      4 | ARTIFICIAL_INTELLIGENCE 04:023         |        9 |
|  5 |      5 | RISK_MANAGEMENT 03:014                 |        7 |
|  6 |      6 | REGULATORY_TECHNOLOGY 03:007           |        7 |
|  7 |      7 | SUPTECH 03:004                         |        6 |
|  8 |      8 | FINANCIAL_REGULATION 04:035            |        5 |
|  9 |      9 | ANTI_MONEY_LAUNDERING 04:023           |        5 |
| 10 |     10 | INNOVATION 03:012                      |        5 |
| 11 |     11 | BLOCKCHAIN 03:005                      |        5 |
| 12 |     12 | FINANCIAL_SERVICES 04:168              |        4 |
| 13 |     13 | CHARITYTECH 02:017                     |        4 |
| 14 |     14 | ENGLISH_LAW 02:017                     |        4 |
| 15 |     15 | ACCOUNTABILITY 02:014                  |        4 |
| 16 |     16 | DATA_PROTECTION_OFFICER 02:014         |        4 |
| 17 |     17 | GDPR 02:014                            |        4 |
| 18 |     18 | DATA_PROTECTION 02:027                 |        3 |
| 19 |     19 | REGULATORY_TECHNOLOGY (REGTECH) 04:030 |        2 |
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

FIELD = "author_keywords"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def author_keywords_co_occ_network(
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
    """Co-word network from author_keywords."""

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
