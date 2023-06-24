# flake8: noqa
"""
Title NLP Phrases Co-occurrence Network
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.publish.conceptual_structure.title_nlp_phrases_co_occ_network(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/title_nlp_phrases_co_occ_network.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/title_nlp_phrases_co_occ_network.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                        | CL_01                   | CL_02                         | CL_03                               | CL_04                                      |
|---:|:-----------------------------|:------------------------|:------------------------------|:------------------------------------|:-------------------------------------------|
|  0 | REGULATORY_TECHNOLOGY 3:020  | FINANCIAL_CRIME 2:012   | ARTIFICIAL_INTELLIGENCE 3:017 | MODERN_INFORMATION_TECHNOLOGY 1:005 | FINANCIAL_STABILITY 1:004                  |
|  1 | BANK_TREASURY 1:011          | AML_COMPLIANCE 1:010    | EFFECTIVE_SOLUTIONS 1:014     | REGULATORY_AFFAIRS 1:005            | TRADITIONAL_FINANCIAL_INTERMEDIATION 1:004 |
|  2 | DIGITAL_TRANSFORMATION 1:011 | REGTECH_SOLUTIONS 1:010 |                               |                                     |                                            |



>>> print(nnet.network_metrics__table_.head().to_markdown())
|                               |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| FINANCIAL_CRIME 2:012         |        3 |     0.0727273 |    0.290909 |  0.118086  |            2 |         3 |
| REGULATORY_TECHNOLOGY 3:020   |        2 |     0         |    0.181818 |  0.0833333 |            3 |         2 |
| ARTIFICIAL_INTELLIGENCE 3:017 |        2 |     0.0545455 |    0.242424 |  0.0885814 |            3 |         2 |
| BANK_TREASURY 1:011           |        2 |     0         |    0.181818 |  0.0833333 |            1 |         2 |
| DIGITAL_TRANSFORMATION 1:011  |        2 |     0         |    0.181818 |  0.0833333 |            1 |         2 |



>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network for a \\
research paper. Summarize the text below, delimited by triple backticks, in at \\
most 30 words, identifiying any notable patterns, trends, or outliers in the data.
<BLANKLINE>
Table:
```
|                                            |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-------------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| FINANCIAL_CRIME 2:012                      |        3 |     0.0727273 |   0.290909  |  0.118086  |            2 |         3 |
| REGULATORY_TECHNOLOGY 3:020                |        2 |     0         |   0.181818  |  0.0833333 |            3 |         2 |
| ARTIFICIAL_INTELLIGENCE 3:017              |        2 |     0.0545455 |   0.242424  |  0.0885814 |            3 |         2 |
| BANK_TREASURY 1:011                        |        2 |     0         |   0.181818  |  0.0833333 |            1 |         2 |
| DIGITAL_TRANSFORMATION 1:011               |        2 |     0         |   0.181818  |  0.0833333 |            1 |         2 |
| AML_COMPLIANCE 1:010                       |        2 |     0         |   0.207792  |  0.0799254 |            1 |         2 |
| REGTECH_SOLUTIONS 1:010                    |        2 |     0         |   0.207792  |  0.0799254 |            1 |         2 |
| EFFECTIVE_SOLUTIONS 1:014                  |        1 |     0         |   0.161616  |  0.0501486 |            1 |         1 |
| MODERN_INFORMATION_TECHNOLOGY 1:005        |        1 |     0         |   0.0909091 |  0.0833333 |            1 |         1 |
| REGULATORY_AFFAIRS 1:005                   |        1 |     0         |   0.0909091 |  0.0833333 |            1 |         1 |
| FINANCIAL_STABILITY 1:004                  |        1 |     0         |   0.0909091 |  0.0833333 |            1 |         1 |
| TRADITIONAL_FINANCIAL_INTERMEDIATION 1:004 |        1 |     0         |   0.0909091 |  0.0833333 |            1 |         1 |
```
<BLANKLINE>


>>> file_name = "sphinx/_static/title_nlp_phrases_co_occ_network__degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/title_nlp_phrases_co_occ_network__degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                           Name  Degree
0     0          FINANCIAL_CRIME 2:012       3
1     1            BANK_TREASURY 1:011       2
2     2   DIGITAL_TRANSFORMATION 1:011       2
3     3  ARTIFICIAL_INTELLIGENCE 3:017       2
4     4           AML_COMPLIANCE 1:010       2


>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a networkx \\
graph of a co-ocurrence matrix. Analyze the table below, delimited by triple  \\
backticks, identifying any notable patterns, trends, or outliers in the data, and  \\
discuss their implications in the network. 
<BLANKLINE>
Table:
```
|    |   Node | Name                                       |   Degree |
|---:|-------:|:-------------------------------------------|---------:|
|  0 |      0 | FINANCIAL_CRIME 2:012                      |        3 |
|  1 |      1 | BANK_TREASURY 1:011                        |        2 |
|  2 |      2 | DIGITAL_TRANSFORMATION 1:011               |        2 |
|  3 |      3 | ARTIFICIAL_INTELLIGENCE 3:017              |        2 |
|  4 |      4 | AML_COMPLIANCE 1:010                       |        2 |
|  5 |      5 | REGTECH_SOLUTIONS 1:010                    |        2 |
|  6 |      6 | REGULATORY_TECHNOLOGY 3:020                |        2 |
|  7 |      7 | EFFECTIVE_SOLUTIONS 1:014                  |        1 |
|  8 |      8 | REGULATORY_AFFAIRS 1:005                   |        1 |
|  9 |      9 | MODERN_INFORMATION_TECHNOLOGY 1:005        |        1 |
| 10 |     10 | TRADITIONAL_FINANCIAL_INTERMEDIATION 1:004 |        1 |
| 11 |     11 | FINANCIAL_STABILITY 1:004                  |        1 |
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

FIELD = "title_nlp_phrases"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def title_nlp_phrases_thematic_map(
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
    """Co-word network from title_nlp_phrases."""

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
