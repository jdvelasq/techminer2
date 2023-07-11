# flake8: noqa
"""
Descriptors
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.publish.conceptual_structure.co_word_network.descriptors(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm_or_estimator="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )
--INFO-- The file 'data/regtech/reports/reports/co_word_network/descriptors/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/descriptors/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/descriptors/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/descriptors/CL_01_prompt.txt' was created.


>>> file_name = "sphinx/_static/examples/conceptual_structure/co_word_network/descriptors.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/examples/conceptual_structure/co_word_network/descriptors.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                          | CL_01                              |
|---:|:-------------------------------|:-----------------------------------|
|  0 | REGTECH 29:330                 | REGULATORY_COMPLIANCE 15:232       |
|  1 | REGULATORY_TECHNOLOGY 20:274   | FINANCIAL_REGULATION 12:395        |
|  2 | FINANCIAL_INSTITUTIONS 16:198  | FINANCIAL_SECTOR 07:169            |
|  3 | FINTECH 12:249                 | FINANCE 07:017                     |
|  4 | ARTIFICIAL_INTELLIGENCE 08:036 | FINANCIAL_SERVICES 06:195          |
|  5 | FINANCIAL_CRISIS 07:058        | GLOBAL_FINANCIAL_CRISIS 06:177     |
|  6 | COMPLIANCE 07:030              | INFORMATION_TECHNOLOGY 06:177      |
|  7 | ANTI_MONEY_LAUNDERING 06:035   | FINANCIAL_TECHNOLOGY 06:173        |
|  8 | REGULATION 05:164              | FINANCIAL_SERVICES_INDUSTRY 05:315 |
|  9 | RISK_MANAGEMENT 05:019         | FINANCIAL_SYSTEM 05:189            |



>>> print(nnet.network_metrics__table_.head().to_markdown())
|                               |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 29:330                |       19 |     0.0211353 |        1    |  0.060222  |           29 |       115 |
| REGULATORY_TECHNOLOGY 20:274  |       19 |     0.0211353 |        1    |  0.060222  |           20 |        88 |
| FINANCIAL_INSTITUTIONS 16:198 |       19 |     0.0211353 |        1    |  0.060222  |           16 |        64 |
| REGULATORY_COMPLIANCE 15:232  |       18 |     0.0144705 |        0.95 |  0.0572486 |           15 |        73 |
| FINTECH 12:249                |       18 |     0.0196211 |        0.95 |  0.0574544 |           12 |        64 |



>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network \\
for a research paper. Summarize the text below, delimited by triple \\
backticks, in at most 30 words, identifiying any notable patterns, trends, \\
or outliers in the data.
<BLANKLINE>
Table:
```
|                                    |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 29:330                     |       19 |   0.0211353   |    1        |  0.060222  |           29 |       115 |
| REGULATORY_TECHNOLOGY 20:274       |       19 |   0.0211353   |    1        |  0.060222  |           20 |        88 |
| FINANCIAL_INSTITUTIONS 16:198      |       19 |   0.0211353   |    1        |  0.060222  |           16 |        64 |
| REGULATORY_COMPLIANCE 15:232       |       18 |   0.0144705   |    0.95     |  0.0572486 |           15 |        73 |
| FINTECH 12:249                     |       18 |   0.0196211   |    0.95     |  0.0574544 |           12 |        64 |
| FINANCE 07:017                     |       18 |   0.0168468   |    0.95     |  0.0573489 |            7 |        40 |
| FINANCIAL_REGULATION 12:395        |       17 |   0.0124933   |    0.904762 |  0.0544522 |           12 |        55 |
| INFORMATION_TECHNOLOGY 06:177      |       16 |   0.0126151   |    0.863636 |  0.05174   |            6 |        34 |
| REGULATION 05:164                  |       16 |   0.0123386   |    0.863636 |  0.0517701 |            5 |        30 |
| ARTIFICIAL_INTELLIGENCE 08:036     |       15 |   0.010003    |    0.826087 |  0.0489387 |            8 |        31 |
| FINANCIAL_SERVICES_INDUSTRY 05:315 |       15 |   0.00629741  |    0.826087 |  0.0487545 |            5 |        31 |
| FINANCIAL_SYSTEM 05:189            |       15 |   0.00813977  |    0.826087 |  0.0488675 |            5 |        30 |
| RISK_MANAGEMENT 05:019             |       15 |   0.010836    |    0.826087 |  0.0490093 |            5 |        30 |
| FINANCIAL_CRISIS 07:058            |       14 |   0.00731131  |    0.791667 |  0.0460915 |            7 |        29 |
| FINANCIAL_SERVICES 06:195          |       14 |   0.00436413  |    0.791667 |  0.0458819 |            6 |        35 |
| GLOBAL_FINANCIAL_CRISIS 06:177     |       14 |   0.00567977  |    0.791667 |  0.046011  |            6 |        30 |
| FINANCIAL_SECTOR 07:169            |       12 |   0.00175787  |    0.730769 |  0.0402848 |            7 |        24 |
| COMPLIANCE 07:030                  |       12 |   0.00262542  |    0.730769 |  0.0403626 |            7 |        29 |
| FINANCIAL_TECHNOLOGY 06:173        |       12 |   0.000783208 |    0.730769 |  0.0402461 |            6 |        32 |
| ANTI_MONEY_LAUNDERING 06:035       |       10 |   0.000937172 |    0.678571 |  0.0348718 |            6 |        18 |
```
<BLANKLINE>



>>> file_name = "sphinx/_static/examples/conceptual_structure/co_word_network/descriptors_degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/examples/co_word_network/descriptors_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                           Name  Degree
0     0   REGULATORY_TECHNOLOGY 20:274      19
1     1  FINANCIAL_INSTITUTIONS 16:198      19
2     2                 REGTECH 29:330      19
3     3   REGULATORY_COMPLIANCE 15:232      18
4     4                 FINTECH 12:249      18



>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                               |   Degree |
|---:|-------:|:-----------------------------------|---------:|
|  0 |      0 | REGULATORY_TECHNOLOGY 20:274       |       19 |
|  1 |      1 | FINANCIAL_INSTITUTIONS 16:198      |       19 |
|  2 |      2 | REGTECH 29:330                     |       19 |
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
| 19 |     19 | ANTI_MONEY_LAUNDERING 06:035       |       10 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
# from ...co_word_network import co_word_network

FIELD = "descriptors"
REPORT_DIR = "reports/co_word_network/descriptors/"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def descriptors(
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
