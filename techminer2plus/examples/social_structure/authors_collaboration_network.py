# flake8: noqa
"""
Authors Collaboration Network
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.examples.social_structure.authors_collaboration_network(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/examples/authors_collaboration_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/examples/authors_collaboration_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00             | CL_01          | CL_02           | CL_03          | CL_04         | CL_05              |
|---:|:------------------|:---------------|:----------------|:---------------|:--------------|:-------------------|
|  0 | Arner DW 3:185    | Hamdan A 2:018 | Brennan R 2:014 | Butler T 2:041 | Lin W 2:017   | Grassi L 2:002     |
|  1 | Buckley RP 3:185  | Turki M 2:018  | Crane M 2:014   | OBrien L 1:033 | Singh C 2:017 | Lanfranchi D 2:002 |
|  2 | Barberis JN 2:161 | Sarea A 2:012  | Ryan P 2:014    |                |               |                    |
|  3 | Weber RH 1:024    |                |                 |                |               |                    |
|  4 | Zetzsche DA 1:024 |                |                 |                |               |                    |


>>> print(nnet.network_metrics__table_.head().to_markdown())
|                   |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| Arner DW 3:185    |        4 |    0.00833333 |    0.25     |  0.072188  |            3 |         7 |
| Buckley RP 3:185  |        4 |    0.00833333 |    0.25     |  0.072188  |            3 |         7 |
| Weber RH 1:024    |        3 |    0          |    0.2      |  0.0551198 |            1 |         3 |
| Zetzsche DA 1:024 |        3 |    0          |    0.2      |  0.0551198 |            1 |         3 |
| Barberis JN 2:161 |        2 |    0          |    0.166667 |  0.039502  |            2 |         4 |


>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network for a \\
research paper. Summarize the text below, delimited by triple backticks, in at \\
most 30 words, identifiying any notable patterns, trends, or outliers in the data.
<BLANKLINE>
Table:
```
|                    |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| Arner DW 3:185     |        4 |    0.00833333 |    0.25     |  0.072188  |            3 |         7 |
| Buckley RP 3:185   |        4 |    0.00833333 |    0.25     |  0.072188  |            3 |         7 |
| Weber RH 1:024     |        3 |    0          |    0.2      |  0.0551198 |            1 |         3 |
| Zetzsche DA 1:024  |        3 |    0          |    0.2      |  0.0551198 |            1 |         3 |
| Barberis JN 2:161  |        2 |    0          |    0.166667 |  0.039502  |            2 |         4 |
| Hamdan A 2:018     |        2 |    0          |    0.125    |  0.0588235 |            2 |         3 |
| Turki M 2:018      |        2 |    0          |    0.125    |  0.0588235 |            2 |         3 |
| Brennan R 2:014    |        2 |    0          |    0.125    |  0.0588235 |            2 |         4 |
| Crane M 2:014      |        2 |    0          |    0.125    |  0.0588235 |            2 |         4 |
| Ryan P 2:014       |        2 |    0          |    0.125    |  0.0588235 |            2 |         4 |
| Sarea A 2:012      |        2 |    0          |    0.125    |  0.0588235 |            2 |         2 |
| Butler T 2:041     |        1 |    0          |    0.0625   |  0.0588235 |            2 |         1 |
| Lin W 2:017        |        1 |    0          |    0.0625   |  0.0588235 |            2 |         2 |
| Singh C 2:017      |        1 |    0          |    0.0625   |  0.0588235 |            2 |         2 |
| Grassi L 2:002     |        1 |    0          |    0.0625   |  0.0588235 |            2 |         2 |
| Lanfranchi D 2:002 |        1 |    0          |    0.0625   |  0.0588235 |            2 |         2 |
| OBrien L 1:033     |        1 |    0          |    0.0625   |  0.0588235 |            1 |         1 |
```
<BLANKLINE>



>>> file_name = "sphinx/_static/examples/authors_collaboration_network_degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/examples/authors_collaboration_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node               Name  Degree
0     0   Buckley RP 3:185       4
1     1     Arner DW 3:185       4
2     2     Weber RH 1:024       3
3     3  Zetzsche DA 1:024       3
4     4  Barberis JN 2:161       2


>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a networkx \\
graph of a co-ocurrence matrix. Analyze the table below, delimited by triple  \\
backticks, identifying any notable patterns, trends, or outliers in the data, and  \\
discuss their implications in the network. 
<BLANKLINE>
Table:
```
|    |   Node | Name               |   Degree |
|---:|-------:|:-------------------|---------:|
|  0 |      0 | Buckley RP 3:185   |        4 |
|  1 |      1 | Arner DW 3:185     |        4 |
|  2 |      2 | Weber RH 1:024     |        3 |
|  3 |      3 | Zetzsche DA 1:024  |        3 |
|  4 |      4 | Barberis JN 2:161  |        2 |
|  5 |      5 | Turki M 2:018      |        2 |
|  6 |      6 | Sarea A 2:012      |        2 |
|  7 |      7 | Hamdan A 2:018     |        2 |
|  8 |      8 | Crane M 2:014      |        2 |
|  9 |      9 | Ryan P 2:014       |        2 |
| 10 |     10 | Brennan R 2:014    |        2 |
| 11 |     11 | OBrien L 1:033     |        1 |
| 12 |     12 | Singh C 2:017      |        1 |
| 13 |     13 | Lin W 2:017        |        1 |
| 14 |     14 | Lanfranchi D 2:002 |        1 |
| 15 |     15 | Grassi L 2:002     |        1 |
| 16 |     16 | Butler T 2:041     |        1 |
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

FIELD = "authors"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def authors_collaboration_network(
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
    """Co-authorship network"""

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
