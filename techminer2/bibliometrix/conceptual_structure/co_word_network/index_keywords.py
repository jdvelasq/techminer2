# flake8: noqa
"""
Index Keywords
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.publish.conceptual_structure.co_word_network.index_keywords(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm_or_estimator="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )
--INFO-- The file 'data/regtech/reports/reports/co_word_network/index_keywords/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/index_keywords/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/index_keywords/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/index_keywords/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/index_keywords/CL_01_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/index_keywords/CL_02_prompt.txt' was created.


>>> file_name = "sphinx/_static/examples/conceptual_structure/co_word_network/index_keywords.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/examples/conceptual_structure/co_word_network/index_keywords.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                                | CL_01                            | CL_02                      |
|---:|:-------------------------------------|:---------------------------------|:---------------------------|
|  0 | FINANCIAL_INSTITUTIONS 6:09          | FINANCE 5:16                     | REGULATORY_COMPLIANCE 9:34 |
|  1 | ANTI_MONEY_LAUNDERING 3:10           | REGTECH 5:15                     | INFORMATION_SYSTEMS 2:14   |
|  2 | FINTECH 3:08                         | SANDBOXES 2:12                   | INFORMATION_USE 2:14       |
|  3 | LAUNDERING 2:09                      | FINANCIAL_REGULATION 2:11        | SOFTWARE_SOLUTION 2:14     |
|  4 | BANKING 2:08                         | FINANCIAL_SERVICES_INDUSTRY 2:11 |                            |
|  5 | FINANCIAL_CRISIS 2:07                | BLOCKCHAIN 2:02                  |                            |
|  6 | RISK_MANAGEMENT 2:05                 |                                  |                            |
|  7 | COMMERCE 2:04                        |                                  |                            |
|  8 | CLASSIFICATION (OF_INFORMATION) 2:03 |                                  |                            |
|  9 | ARTIFICIAL_INTELLIGENCE 2:02         |                                  |                            |

>>> print(nnet.network_metrics__table_.head().to_markdown())
|                             |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:----------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGULATORY_COMPLIANCE 9:34  |       14 |     0.364822  |    0.791667 |  0.0990793 |            9 |        28 |
| FINANCIAL_INSTITUTIONS 6:09 |       12 |     0.0844128 |    0.730769 |  0.0773944 |            6 |        18 |
| FINANCE 5:16                |       12 |     0.0938949 |    0.730769 |  0.0781129 |            5 |        22 |
| REGTECH 5:15                |       10 |     0.0915639 |    0.678571 |  0.0686701 |            5 |        18 |
| ANTI_MONEY_LAUNDERING 3:10  |       10 |     0.0374605 |    0.59375  |  0.0658976 |            3 |        13 |


>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network \\
for a research paper. Summarize the text below, delimited by triple \\
backticks, in at most 30 words, identifiying any notable patterns, trends, \\
or outliers in the data.
<BLANKLINE>
Table:
```
|                                      |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGULATORY_COMPLIANCE 9:34           |       14 |    0.364822   |    0.791667 |  0.0990793 |            9 |        28 |
| FINANCIAL_INSTITUTIONS 6:09          |       12 |    0.0844128  |    0.730769 |  0.0773944 |            6 |        18 |
| FINANCE 5:16                         |       12 |    0.0938949  |    0.730769 |  0.0781129 |            5 |        22 |
| REGTECH 5:15                         |       10 |    0.0915639  |    0.678571 |  0.0686701 |            5 |        18 |
| ANTI_MONEY_LAUNDERING 3:10           |       10 |    0.0374605  |    0.59375  |  0.0658976 |            3 |        13 |
| FINTECH 3:08                         |        8 |    0.0213188  |    0.633333 |  0.0534336 |            3 |        12 |
| COMMERCE 2:04                        |        8 |    0.0213188  |    0.633333 |  0.0534336 |            2 |         9 |
| ARTIFICIAL_INTELLIGENCE 2:02         |        8 |    0.0369273  |    0.633333 |  0.0540262 |            2 |         9 |
| LAUNDERING 2:09                      |        7 |    0.0144585  |    0.542857 |  0.0483494 |            2 |         8 |
| BANKING 2:08                         |        7 |    0.0121832  |    0.513514 |  0.0482885 |            2 |         8 |
| SANDBOXES 2:12                       |        6 |    0.02846    |    0.575758 |  0.0454863 |            2 |         6 |
| FINANCIAL_REGULATION 2:11            |        6 |    0.00339329 |    0.59375  |  0.0429245 |            2 |         9 |
| FINANCIAL_SERVICES_INDUSTRY 2:11     |        6 |    0.00263158 |    0.575758 |  0.0431506 |            2 |         9 |
| RISK_MANAGEMENT 2:05                 |        6 |    0.00878176 |    0.575758 |  0.0418169 |            2 |         8 |
| CLASSIFICATION (OF_INFORMATION) 2:03 |        5 |    0          |    0.513514 |  0.0357273 |            2 |         5 |
| FINANCIAL_CRISIS 2:07                |        4 |    0.0146297  |    0.542857 |  0.0308513 |            2 |         4 |
| INFORMATION_SYSTEMS 2:14             |        3 |    0          |    0.475    |  0.0311922 |            2 |         6 |
| INFORMATION_USE 2:14                 |        3 |    0          |    0.475    |  0.0311922 |            2 |         6 |
| SOFTWARE_SOLUTION 2:14               |        3 |    0          |    0.475    |  0.0311922 |            2 |         6 |
| BLOCKCHAIN 2:02                      |        2 |    0          |    0.422222 |  0.0197808 |            2 |         2 |
```
<BLANKLINE>



>>> file_name = "sphinx/_static/examples/conceptual_structure/co_word_network/index_keywords_degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/examples/conceptual_structure/co_word_network/index_keywords_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                         Name  Degree
0     0   REGULATORY_COMPLIANCE 9:34      14
1     1  FINANCIAL_INSTITUTIONS 6:09      12
2     2                 FINANCE 5:16      12
3     3                 REGTECH 5:15      10
4     4   ANTI_MONEY_LAUNDERING 3:10      10


>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                 |   Degree |
|---:|-------:|:-------------------------------------|---------:|
|  0 |      0 | REGULATORY_COMPLIANCE 9:34           |       14 |
|  1 |      1 | FINANCIAL_INSTITUTIONS 6:09          |       12 |
|  2 |      2 | FINANCE 5:16                         |       12 |
|  3 |      3 | REGTECH 5:15                         |       10 |
|  4 |      4 | ANTI_MONEY_LAUNDERING 3:10           |       10 |
|  5 |      5 | FINTECH 3:08                         |        8 |
|  6 |      6 | COMMERCE 2:04                        |        8 |
|  7 |      7 | ARTIFICIAL_INTELLIGENCE 2:02         |        8 |
|  8 |      8 | LAUNDERING 2:09                      |        7 |
|  9 |      9 | BANKING 2:08                         |        7 |
| 10 |     10 | SANDBOXES 2:12                       |        6 |
| 11 |     11 | FINANCIAL_REGULATION 2:11            |        6 |
| 12 |     12 | FINANCIAL_SERVICES_INDUSTRY 2:11     |        6 |
| 13 |     13 | RISK_MANAGEMENT 2:05                 |        6 |
| 14 |     14 | CLASSIFICATION (OF_INFORMATION) 2:03 |        5 |
| 15 |     15 | FINANCIAL_CRISIS 2:07                |        4 |
| 16 |     16 | INFORMATION_SYSTEMS 2:14             |        3 |
| 17 |     17 | INFORMATION_USE 2:14                 |        3 |
| 18 |     18 | SOFTWARE_SOLUTION 2:14               |        3 |
| 19 |     19 | BLOCKCHAIN 2:02                      |        2 |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""
# from ...co_word_network import co_word_network

FIELD = "index_keywords"
REPORT_DIR = "reports/co_word_network/index_keywords/"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def index_keywords(
    concordances_top_n=10,
    #
    # 'co_word_matrix' params:
    normalization="association",
    algorithm_or_estimator="louvain",
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

    return co_word_network(
        #
        # 'co_occurrence_matrix' params:
        field=FIELD,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # 'cluster_field' params:
        normalization=normalization,
        algorithm_or_estimator=algorithm_or_estimator,
        #
        # report:
        report_dir=REPORT_DIR,
        concordances_top_n=concordances_top_n,
        #
        # Results params:
        network_viewer_dict=network_viewer_dict,
        network_degree_plot_dict=network_degree_plot_dict,
        #
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
