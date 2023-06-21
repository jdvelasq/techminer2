# flake8: noqa
"""
Author Keywords
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.report.conceptual_structure.co_word_network.author_keywords(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm_or_estimator="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )
--INFO-- The file 'data/regtech/reports/reports/co_word_network/author_keywords/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/author_keywords/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/author_keywords/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/author_keywords/CL_03_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/author_keywords/CL_01_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/author_keywords/CL_02_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/author_keywords/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/co_word_network/author_keywords/CL_03_prompt.txt' was created.

>>> file_name = "sphinx/_static/report/conceptual_structure/co_word_network/author_keywords.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/report/conceptual_structure/co_word_network/author_keywords.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                          | CL_01                       | CL_02                        | CL_03                          |
|---:|:-------------------------------|:----------------------------|:-----------------------------|:-------------------------------|
|  0 | REGTECH 28:329                 | FINTECH 12:249              | REGULATORY_TECHNOLOGY 07:037 | ANTI_MONEY_LAUNDERING 05:034   |
|  1 | COMPLIANCE 07:030              | FINANCIAL_SERVICES 04:168   | REGULATION 05:164            | ARTIFICIAL_INTELLIGENCE 04:023 |
|  2 | BLOCKCHAIN 03:005              | FINANCIAL_REGULATION 04:035 | RISK_MANAGEMENT 03:014       | CHARITYTECH 02:017             |
|  3 | SMART_CONTRACTS 02:022         | INNOVATION 03:012           | SUPTECH 03:004               | ENGLISH_LAW 02:017             |
|  4 | ACCOUNTABILITY 02:014          | DATA_PROTECTION 02:027      | SEMANTIC_TECHNOLOGIES 02:041 |                                |
|  5 | DATA_PROTECTION_OFFICER 02:014 |                             |                              |                                |


>>> print(nnet.network_metrics__table_.head().to_markdown())
|                              |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329               |       19 |     0.461111  |    1        |  0.136626  |           28 |        55 |
| FINTECH 12:249               |       13 |     0.0887914 |    0.76     |  0.0913549 |           12 |        32 |
| COMPLIANCE 07:030            |       10 |     0.0468811 |    0.678571 |  0.0722431 |            7 |        19 |
| REGULATION 05:164            |       10 |     0.0315789 |    0.678571 |  0.0707314 |            5 |        17 |
| REGULATORY_TECHNOLOGY 07:037 |        9 |     0.0230994 |    0.655172 |  0.0635479 |            7 |        12 |


>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network \\
for a research paper. Summarize the text below, delimited by triple \\
backticks, in at most 30 words, identifiying any notable patterns, trends, \\
or outliers in the data.
<BLANKLINE>
Table:
```
|                                |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329                 |       19 |    0.461111   |    1        |  0.136626  |           28 |        55 |
| FINTECH 12:249                 |       13 |    0.0887914  |    0.76     |  0.0913549 |           12 |        32 |
| COMPLIANCE 07:030              |       10 |    0.0468811  |    0.678571 |  0.0722431 |            7 |        19 |
| REGULATION 05:164              |       10 |    0.0315789  |    0.678571 |  0.0707314 |            5 |        17 |
| REGULATORY_TECHNOLOGY 07:037   |        9 |    0.0230994  |    0.655172 |  0.0635479 |            7 |        12 |
| ARTIFICIAL_INTELLIGENCE 04:023 |        9 |    0.0384016  |    0.655172 |  0.0655643 |            4 |        10 |
| RISK_MANAGEMENT 03:014         |        8 |    0.00847953 |    0.633333 |  0.0568575 |            3 |        12 |
| BLOCKCHAIN 03:005              |        6 |    0.0126706  |    0.59375  |  0.046516  |            3 |         7 |
| SUPTECH 03:004                 |        6 |    0          |    0.59375  |  0.0437808 |            3 |         9 |
| ANTI_MONEY_LAUNDERING 05:034   |        5 |    0.00389864 |    0.575758 |  0.0401809 |            5 |         6 |
| FINANCIAL_REGULATION 04:035    |        5 |    0.00536062 |    0.575758 |  0.0405341 |            4 |         7 |
| INNOVATION 03:012              |        5 |    0.00341131 |    0.575758 |  0.0384896 |            3 |         5 |
| FINANCIAL_SERVICES 04:168      |        4 |    0.00146199 |    0.558824 |  0.0324878 |            4 |         8 |
| SEMANTIC_TECHNOLOGIES 02:041   |        4 |    0          |    0.558824 |  0.0316384 |            2 |         6 |
| CHARITYTECH 02:017             |        4 |    0          |    0.558824 |  0.0338227 |            2 |         6 |
| ENGLISH_LAW 02:017             |        4 |    0          |    0.558824 |  0.0338227 |            2 |         6 |
| DATA_PROTECTION 02:027         |        3 |    0          |    0.542857 |  0.0264758 |            2 |         4 |
| ACCOUNTABILITY 02:014          |        3 |    0          |    0.542857 |  0.0275621 |            2 |         6 |
| DATA_PROTECTION_OFFICER 02:014 |        3 |    0          |    0.542857 |  0.0275621 |            2 |         6 |
| SMART_CONTRACTS 02:022         |        2 |    0          |    0.527778 |  0.020202  |            2 |         3 |
```
<BLANKLINE>



>>> file_name = "sphinx/_static/author_keywords_co_occ_network__degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/author_keywords_co_occ_network__degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                          Name  Degree
0     0                REGTECH 28:329      19
1     1                FINTECH 12:249      13
2     2             COMPLIANCE 07:030      10
3     3             REGULATION 05:164      10
4     4  REGULATORY_TECHNOLOGY 07:037       9

>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                           |   Degree |
|---:|-------:|:-------------------------------|---------:|
|  0 |      0 | REGTECH 28:329                 |       19 |
|  1 |      1 | FINTECH 12:249                 |       13 |
|  2 |      2 | COMPLIANCE 07:030              |       10 |
|  3 |      3 | REGULATION 05:164              |       10 |
|  4 |      4 | REGULATORY_TECHNOLOGY 07:037   |        9 |
|  5 |      5 | ARTIFICIAL_INTELLIGENCE 04:023 |        9 |
|  6 |      6 | RISK_MANAGEMENT 03:014         |        8 |
|  7 |      7 | BLOCKCHAIN 03:005              |        6 |
|  8 |      8 | SUPTECH 03:004                 |        6 |
|  9 |      9 | ANTI_MONEY_LAUNDERING 05:034   |        5 |
| 10 |     10 | FINANCIAL_REGULATION 04:035    |        5 |
| 11 |     11 | INNOVATION 03:012              |        5 |
| 12 |     12 | FINANCIAL_SERVICES 04:168      |        4 |
| 13 |     13 | SEMANTIC_TECHNOLOGIES 02:041   |        4 |
| 14 |     14 | CHARITYTECH 02:017             |        4 |
| 15 |     15 | ENGLISH_LAW 02:017             |        4 |
| 16 |     16 | DATA_PROTECTION 02:027         |        3 |
| 17 |     17 | ACCOUNTABILITY 02:014          |        3 |
| 18 |     18 | DATA_PROTECTION_OFFICER 02:014 |        3 |
| 19 |     19 | SMART_CONTRACTS 02:022         |        2 |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""
from ...co_word_network import co_word_network

FIELD = "author_keywords"
REPORT_DIR = "reports/co_word_network/author_keywords/"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def author_keywords(
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
