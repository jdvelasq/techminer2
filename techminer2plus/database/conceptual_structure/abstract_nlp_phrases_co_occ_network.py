# flake8: noqa
"""
Abstract NLP Phrases Co-occurrence Network
===============================================================================


>>> root_dir = "data/regtech/"

>>> from techminer2 import bibliometrix
>>> nnet = bibliometrix.conceptual_structure.abstract_nlp_phrases_co_occ_network(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/abstract_nlp_phrases_co_occ_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/abstract_nlp_phrases_co_occ_network.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                              | CL_01                          |
|---:|:-----------------------------------|:-------------------------------|
|  0 | REGULATORY_TECHNOLOGY 17:266       | FINANCIAL_INSTITUTIONS 15:194  |
|  1 | FINANCIAL_SECTOR 07:169            | REGULATORY_COMPLIANCE 07:198   |
|  2 | FINANCIAL_REGULATION 06:330        | ARTIFICIAL_INTELLIGENCE 07:033 |
|  3 | GLOBAL_FINANCIAL_CRISIS 06:177     | FINANCIAL_CRISIS 06:058        |
|  4 | FINANCIAL_SERVICES_INDUSTRY 05:315 | REGTECH_SOLUTIONS 05:018       |
|  5 | INFORMATION_TECHNOLOGY 05:177      | FINANCIAL_SYSTEM 04:178        |
|  6 | FINANCIAL_TECHNOLOGY 05:173        | RISK_MANAGEMENT 04:015         |
|  7 | MACHINE_LEARNING 04:007            | NEW_TECHNOLOGIES 04:012        |
|  8 | DIGITAL_INNOVATION 03:164          | COMPLIANCE_COSTS 03:002        |
|  9 | FINANCIAL_MARKETS 03:151           |                                |
| 10 | REGTECH_APPROACH 03:034            |                                |



>>> print(nnet.network_metrics__table_.head().to_markdown())
|                                    |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGULATORY_TECHNOLOGY 17:266       |       19 |     0.108535  |    1        |  0.0813975 |           17 |        52 |
| FINANCIAL_INSTITUTIONS 15:194      |       17 |     0.0548083 |    0.904762 |  0.0722123 |           15 |        36 |
| REGULATORY_COMPLIANCE 07:198       |       14 |     0.0278868 |    0.791667 |  0.0603404 |            7 |        24 |
| FINANCIAL_SERVICES_INDUSTRY 05:315 |       14 |     0.0480692 |    0.791667 |  0.0618488 |            5 |        23 |
| ARTIFICIAL_INTELLIGENCE 07:033     |       13 |     0.0322983 |    0.76     |  0.0568675 |            7 |        20 |


>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network for a \\
research paper. Summarize the text below, delimited by triple backticks, in at \\
most 30 words, identifiying any notable patterns, trends, or outliers in the data.
<BLANKLINE>
Table:
```
|                                    |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGULATORY_TECHNOLOGY 17:266       |       19 |    0.108535   |    1        |  0.0813975 |           17 |        52 |
| FINANCIAL_INSTITUTIONS 15:194      |       17 |    0.0548083  |    0.904762 |  0.0722123 |           15 |        36 |
| REGULATORY_COMPLIANCE 07:198       |       14 |    0.0278868  |    0.791667 |  0.0603404 |            7 |        24 |
| FINANCIAL_SERVICES_INDUSTRY 05:315 |       14 |    0.0480692  |    0.791667 |  0.0618488 |            5 |        23 |
| ARTIFICIAL_INTELLIGENCE 07:033     |       13 |    0.0322983  |    0.76     |  0.0568675 |            7 |        20 |
| FINANCIAL_SYSTEM 04:178            |       13 |    0.0438736  |    0.76     |  0.0581972 |            4 |        15 |
| FINANCIAL_SECTOR 07:169            |       12 |    0.0154924  |    0.730769 |  0.052701  |            7 |        21 |
| FINANCIAL_REGULATION 06:330        |       12 |    0.0170032  |    0.730769 |  0.0526937 |            6 |        23 |
| INFORMATION_TECHNOLOGY 05:177      |       12 |    0.0179871  |    0.730769 |  0.0527186 |            5 |        20 |
| DIGITAL_INNOVATION 03:164          |       12 |    0.0121531  |    0.730769 |  0.0524775 |            3 |        16 |
| FINANCIAL_CRISIS 06:058            |       11 |    0.0147243  |    0.703704 |  0.0490495 |            6 |        17 |
| RISK_MANAGEMENT 04:015             |       11 |    0.0131788  |    0.703704 |  0.0488797 |            4 |        17 |
| FINANCIAL_TECHNOLOGY 05:173        |       10 |    0.0107421  |    0.678571 |  0.0452118 |            5 |        14 |
| REGTECH_SOLUTIONS 05:018           |       10 |    0.0126195  |    0.678571 |  0.0454906 |            5 |        14 |
| FINANCIAL_MARKETS 03:151           |        9 |    0.00936369 |    0.655172 |  0.0414746 |            3 |        10 |
| COMPLIANCE_COSTS 03:002            |        9 |    0.00629351 |    0.655172 |  0.0412899 |            3 |        13 |
| GLOBAL_FINANCIAL_CRISIS 06:177     |        8 |    0.005718   |    0.633333 |  0.0374905 |            6 |        13 |
| MACHINE_LEARNING 04:007            |        8 |    0.00146199 |    0.633333 |  0.037182  |            4 |        11 |
| NEW_TECHNOLOGIES 04:012            |        7 |    0.00393112 |    0.612903 |  0.0337752 |            4 |         8 |
| REGTECH_APPROACH 03:034            |        3 |    0          |    0.542857 |  0.0187017 |            3 |         3 |
```
<BLANKLINE>

>>> file_name = "sphinx/_static/abstract_nlp_phrases_co_occ_network__degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/abstract_nlp_phrases_co_occ_network__degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                                Name  Degree
0     0        REGULATORY_TECHNOLOGY 17:266      19
1     1       FINANCIAL_INSTITUTIONS 15:194      17
2     2        REGULATORY_COMPLIANCE 07:198      14
3     3  FINANCIAL_SERVICES_INDUSTRY 05:315      14
4     4      ARTIFICIAL_INTELLIGENCE 07:033      13

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
|  0 |      0 | REGULATORY_TECHNOLOGY 17:266       |       19 |
|  1 |      1 | FINANCIAL_INSTITUTIONS 15:194      |       17 |
|  2 |      2 | REGULATORY_COMPLIANCE 07:198       |       14 |
|  3 |      3 | FINANCIAL_SERVICES_INDUSTRY 05:315 |       14 |
|  4 |      4 | ARTIFICIAL_INTELLIGENCE 07:033     |       13 |
|  5 |      5 | FINANCIAL_SYSTEM 04:178            |       13 |
|  6 |      6 | FINANCIAL_SECTOR 07:169            |       12 |
|  7 |      7 | FINANCIAL_REGULATION 06:330        |       12 |
|  8 |      8 | INFORMATION_TECHNOLOGY 05:177      |       12 |
|  9 |      9 | DIGITAL_INNOVATION 03:164          |       12 |
| 10 |     10 | FINANCIAL_CRISIS 06:058            |       11 |
| 11 |     11 | RISK_MANAGEMENT 04:015             |       11 |
| 12 |     12 | FINANCIAL_TECHNOLOGY 05:173        |       10 |
| 13 |     13 | REGTECH_SOLUTIONS 05:018           |       10 |
| 14 |     14 | FINANCIAL_MARKETS 03:151           |        9 |
| 15 |     15 | COMPLIANCE_COSTS 03:002            |        9 |
| 16 |     16 | GLOBAL_FINANCIAL_CRISIS 06:177     |        8 |
| 17 |     17 | MACHINE_LEARNING 04:007            |        8 |
| 18 |     18 | NEW_TECHNOLOGIES 04:012            |        7 |
| 19 |     19 | REGTECH_APPROACH 03:034            |        3 |
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

FIELD = "abstract_nlp_phrases"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def abstract_nlp_phrases_co_occ_network(
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
    """Co-word network from abstract_nlp_phrases."""

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
