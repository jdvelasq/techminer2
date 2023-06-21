# flake8: noqa
"""
Organizations Collaboration Network
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.examples.social_structure.organizations_collaboration_network(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/examples/organizations_collaboration_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/examples/organizations_collaboration_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                                                                    | CL_01                                                              | CL_02                           |
|---:|:-------------------------------------------------------------------------|:-------------------------------------------------------------------|:--------------------------------|
|  0 | Univ of Hong Kong (HKG) 3:185                                            | European Central B (DEU) 1:021                                     | Coventry Univ (GBR) 2:017       |
|  1 | FinTech HK, Hong Kong (HKG) 1:150                                        | Harvard Univ Weatherhead ctr for International Affairs (USA) 1:021 | Univ of Westminster (GBR) 2:017 |
|  2 | ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150 | KS Strategic, London, United Kingdom (GBR) 1:021                   |                                 |
|  3 | Heinrich-Heine-Univ (DEU) 1:024                                          | Panepistemio Aigaiou, Chios, Greece (GRC) 1:021                    |                                 |
|  4 | UNSW Sydney, Kensington, Australia (AUS) 1:024                           | Sch of Eng (CHE) 1:021                                             |                                 |
|  5 | Univ of Luxembourg (LUX) 1:024                                           |                                                                    |                                 |
|  6 | Univ of Zurich (CHE) 1:024                                               |                                                                    |                                 |

>>> print(nnet.network_metrics__table_.head().to_markdown())
|                                                |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| Univ of Hong Kong (HKG) 3:185                  |        6 |      0.102564 |    0.461538 |  0.112734  |            3 |         6 |
| Heinrich-Heine-Univ (DEU) 1:024                |        4 |      0        |    0.346154 |  0.0736114 |            1 |         4 |
| UNSW Sydney, Kensington, Australia (AUS) 1:024 |        4 |      0        |    0.346154 |  0.0736114 |            1 |         4 |
| Univ of Luxembourg (LUX) 1:024                 |        4 |      0        |    0.346154 |  0.0736114 |            1 |         4 |
| Univ of Zurich (CHE) 1:024                     |        4 |      0        |    0.346154 |  0.0736114 |            1 |         4 |


>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network for a \\
research paper. Summarize the text below, delimited by triple backticks, in at \\
most 30 words, identifiying any notable patterns, trends, or outliers in the data.
<BLANKLINE>
Table:
```
|                                                                          |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-------------------------------------------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| Univ of Hong Kong (HKG) 3:185                                            |        6 |      0.102564 |   0.461538  |  0.112734  |            3 |         6 |
| Heinrich-Heine-Univ (DEU) 1:024                                          |        4 |      0        |   0.346154  |  0.0736114 |            1 |         4 |
| UNSW Sydney, Kensington, Australia (AUS) 1:024                           |        4 |      0        |   0.346154  |  0.0736114 |            1 |         4 |
| Univ of Luxembourg (LUX) 1:024                                           |        4 |      0        |   0.346154  |  0.0736114 |            1 |         4 |
| Univ of Zurich (CHE) 1:024                                               |        4 |      0        |   0.346154  |  0.0736114 |            1 |         4 |
| European Central B (DEU) 1:021                                           |        4 |      0        |   0.307692  |  0.0714286 |            1 |         4 |
| Harvard Univ Weatherhead ctr for International Affairs (USA) 1:021       |        4 |      0        |   0.307692  |  0.0714286 |            1 |         4 |
| KS Strategic, London, United Kingdom (GBR) 1:021                         |        4 |      0        |   0.307692  |  0.0714286 |            1 |         4 |
| Panepistemio Aigaiou, Chios, Greece (GRC) 1:021                          |        4 |      0        |   0.307692  |  0.0714286 |            1 |         4 |
| Sch of Eng (CHE) 1:021                                                   |        4 |      0        |   0.307692  |  0.0714286 |            1 |         4 |
| FinTech HK, Hong Kong (HKG) 1:150                                        |        2 |      0        |   0.276923  |  0.0464104 |            1 |         2 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150 |        2 |      0        |   0.276923  |  0.0464104 |            1 |         2 |
| Coventry Univ (GBR) 2:017                                                |        1 |      0        |   0.0769231 |  0.0714286 |            2 |         2 |
| Univ of Westminster (GBR) 2:017                                          |        1 |      0        |   0.0769231 |  0.0714286 |            2 |         2 |
```
<BLANKLINE>


>>> file_name = "sphinx/_static/examples/organizations_collaboration_network_degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/examples/organizations_collaboration_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                                            Name  Degree
0     0                   Univ of Hong Kong (HKG) 3:185       6
1     1                 Heinrich-Heine-Univ (DEU) 1:024       4
2     2  UNSW Sydney, Kensington, Australia (AUS) 1:024       4
3     3                  Univ of Luxembourg (LUX) 1:024       4
4     4                      Univ of Zurich (CHE) 1:024       4



>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a networkx \\
graph of a co-ocurrence matrix. Analyze the table below, delimited by triple  \\
backticks, identifying any notable patterns, trends, or outliers in the data, and  \\
discuss their implications in the network. 
<BLANKLINE>
Table:
```
|    |   Node | Name                                                                     |   Degree |
|---:|-------:|:-------------------------------------------------------------------------|---------:|
|  0 |      0 | Univ of Hong Kong (HKG) 3:185                                            |        6 |
|  1 |      1 | Heinrich-Heine-Univ (DEU) 1:024                                          |        4 |
|  2 |      2 | UNSW Sydney, Kensington, Australia (AUS) 1:024                           |        4 |
|  3 |      3 | Univ of Luxembourg (LUX) 1:024                                           |        4 |
|  4 |      4 | Univ of Zurich (CHE) 1:024                                               |        4 |
|  5 |      5 | Harvard Univ Weatherhead ctr for International Affairs (USA) 1:021       |        4 |
|  6 |      6 | KS Strategic, London, United Kingdom (GBR) 1:021                         |        4 |
|  7 |      7 | Panepistemio Aigaiou, Chios, Greece (GRC) 1:021                          |        4 |
|  8 |      8 | Sch of Eng (CHE) 1:021                                                   |        4 |
|  9 |      9 | European Central B (DEU) 1:021                                           |        4 |
| 10 |     10 | FinTech HK, Hong Kong (HKG) 1:150                                        |        2 |
| 11 |     11 | ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) 1:150 |        2 |
| 12 |     12 | Univ of Westminster (GBR) 2:017                                          |        1 |
| 13 |     13 | Coventry Univ (GBR) 2:017                                                |        1 |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""

# from ...classes import CollaborationNetwork
# from ...vantagepoint.analyze import (
#     co_occurrence_matrix,
#     matrix_normalization,
#     network_clustering,
#     network_communities,
#     network_degree_plot,
#     network_metrics,
#     network_viewer,
# )

FIELD = "organizations"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def organizations_collaboration_network(
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
    """Organizations collaboration network"""

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

    network = CollaborationNetwork()
    network.plot_ = network_viewer(graph=graph, **network_viewer_dict)
    network.graph_ = graph
    network.communities_ = network_communities(graph=graph)

    network.network_metrics__table_ = metrics.table_
    network.network_metrics__prompt_ = metrics.prompt_

    network.degree_plot__plot_ = degree_plot.plot_
    network.degree_plot__table_ = degree_plot.table_
    network.degree_plot__prompt_ = degree_plot.prompt_

    return network
