# flake8: noqa
"""
Countries Collaboration Network
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.report.social_structure.countries_collaboration_network(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )


>>> file_name = "sphinx/_static/report/countries_collaboration_network_plot.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/report/countries_collaboration_network_plot.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                | CL_01            | CL_02                      |
|---:|:---------------------|:-----------------|:---------------------------|
|  0 | United Kingdom 7:199 | Australia 7:199  | Bahrain 4:019              |
|  1 | United States 6:059  | China 5:027      | United Arab Emirates 2:013 |
|  2 | Ireland 5:055        | Germany 4:051    | Jordan 1:011               |
|  3 | Italy 5:005          | Hong Kong 3:185  |                            |
|  4 | Switzerland 4:045    | Luxembourg 2:034 |                            |
|  5 | Greece 1:021         | Japan 1:013      |                            |

>>> print(nnet.network_metrics__table_.head().to_markdown())
|                      |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:---------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| Switzerland 4:045    |        8 |     0.130037  |    0.57619  |  0.113234  |            4 |        10 |
| Germany 4:051        |        7 |     0.0586081 |    0.540179 |  0.0985296 |            4 |         8 |
| United Kingdom 7:199 |        6 |     0.179487  |    0.540179 |  0.0940787 |            7 |         6 |
| Australia 7:199      |        5 |     0.0311355 |    0.480159 |  0.0738883 |            7 |         7 |
| United States 6:059  |        5 |     0.0274725 |    0.480159 |  0.0748553 |            6 |         6 |

>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network for a \\
research paper. Summarize the text below, delimited by triple backticks, in at \\
most 30 words, identifiying any notable patterns, trends, or outliers in the data.
<BLANKLINE>
Table:
```
|                            |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:---------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| Switzerland 4:045          |        8 |     0.130037  |    0.57619  |  0.113234  |            4 |        10 |
| Germany 4:051              |        7 |     0.0586081 |    0.540179 |  0.0985296 |            4 |         8 |
| United Kingdom 7:199       |        6 |     0.179487  |    0.540179 |  0.0940787 |            7 |         6 |
| Australia 7:199            |        5 |     0.0311355 |    0.480159 |  0.0738883 |            7 |         7 |
| United States 6:059        |        5 |     0.0274725 |    0.480159 |  0.0748553 |            6 |         6 |
| Hong Kong 3:185            |        5 |     0.0311355 |    0.480159 |  0.0738883 |            3 |         7 |
| China 5:027                |        4 |     0.124542  |    0.454887 |  0.0695053 |            5 |         4 |
| Luxembourg 2:034           |        4 |     0         |    0.432143 |  0.0591177 |            2 |         4 |
| Greece 1:021               |        4 |     0         |    0.454887 |  0.0600487 |            1 |         4 |
| Italy 5:005                |        2 |     0         |    0.360119 |  0.0347564 |            5 |         2 |
| Bahrain 4:019              |        2 |     0         |    0.142857 |  0.0666667 |            4 |         2 |
| United Arab Emirates 2:013 |        2 |     0         |    0.142857 |  0.0666667 |            2 |         2 |
| Jordan 1:011               |        2 |     0         |    0.142857 |  0.0666667 |            1 |         2 |
| Ireland 5:055              |        1 |     0         |    0.332418 |  0.0233281 |            5 |         1 |
| Japan 1:013                |        1 |     0         |    0.29803  |  0.0247694 |            1 |         1 |
```
<BLANKLINE>



>>> file_name = "sphinx/_static/report/countries_collaboration_network_degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../_static/report/countries_collaboration_network_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                  Name  Degree
0     0     Switzerland 4:045       8
1     1         Germany 4:051       7
2     2  United Kingdom 7:199       6
3     3   United States 6:059       5
4     4       Hong Kong 3:185       5


>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a networkx \\
graph of a co-ocurrence matrix. Analyze the table below, delimited by triple  \\
backticks, identifying any notable patterns, trends, or outliers in the data, and  \\
discuss their implications in the network. 
<BLANKLINE>
Table:
```
|    |   Node | Name                       |   Degree |
|---:|-------:|:---------------------------|---------:|
|  0 |      0 | Switzerland 4:045          |        8 |
|  1 |      1 | Germany 4:051              |        7 |
|  2 |      2 | United Kingdom 7:199       |        6 |
|  3 |      3 | United States 6:059        |        5 |
|  4 |      4 | Hong Kong 3:185            |        5 |
|  5 |      5 | Australia 7:199            |        5 |
|  6 |      6 | China 5:027                |        4 |
|  7 |      7 | Greece 1:021               |        4 |
|  8 |      8 | Luxembourg 2:034           |        4 |
|  9 |      9 | Italy 5:005                |        2 |
| 10 |     10 | United Arab Emirates 2:013 |        2 |
| 11 |     11 | Jordan 1:011               |        2 |
| 12 |     12 | Bahrain 4:019              |        2 |
| 13 |     13 | Ireland 5:055              |        1 |
| 14 |     14 | Japan 1:013                |        1 |
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

FIELD = "countries"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def countries_collaboration_network(
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
    """Countries collaboration network"""

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
