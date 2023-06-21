# flake8: noqa
"""
Keywords
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.report.conceptual_structure.thematic_map.keywords(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm_or_estimator="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )
--INFO-- The file 'data/regtech/reports/reports/thematic_map/keywords/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/keywords/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/keywords/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/keywords/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/keywords/CL_01_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/keywords/CL_02_prompt.txt' was created.


>>> file_name = "sphinx/_static/report/conceptual_structure/thematic_map/keywords.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/report/conceptual_structure/thematic_map/keywords.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                         | CL_01                          | CL_02                        |
|---:|:------------------------------|:-------------------------------|:-----------------------------|
|  0 | FINTECH 12:249                | REGULATORY_TECHNOLOGY 08:037   | REGTECH 28:329               |
|  1 | REGULATORY_COMPLIANCE 09:034  | ANTI_MONEY_LAUNDERING 06:035   | COMPLIANCE 07:030            |
|  2 | FINANCE 07:017                | ARTIFICIAL_INTELLIGENCE 06:025 | REGULATION 05:164            |
|  3 | FINANCIAL_INSTITUTIONS 06:009 | RISK_MANAGEMENT 05:019         | SMART_CONTRACTS 03:023       |
|  4 | FINANCIAL_REGULATION 05:035   | INNOVATION 03:012              | BLOCKCHAIN 03:005            |
|  5 | FINANCIAL_SERVICES 04:168     | CHARITYTECH 02:017             | SEMANTIC_TECHNOLOGIES 02:041 |
|  6 | SUPTECH 03:004                |                                |                              |
|  7 | DATA_PROTECTION 02:027        |                                |                              |


>>> print(nnet.network_metrics__table_.head().to_markdown())
|                               |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGTECH 28:329                |       19 |     0.203655  |    1        |  0.0943323 |           28 |        73 |
| FINTECH 12:249                |       17 |     0.0935185 |    0.904762 |  0.0827304 |           12 |        41 |
| REGULATION 05:164             |       14 |     0.0656804 |    0.791667 |  0.0698668 |            5 |        22 |
| RISK_MANAGEMENT 05:019        |       14 |     0.0311334 |    0.791667 |  0.0676816 |            5 |        24 |
| FINANCIAL_INSTITUTIONS 06:009 |       13 |     0.0182099 |    0.76     |  0.0627387 |            6 |        23 |


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
| REGTECH 28:329                 |       19 |    0.203655   |    1        |  0.0943323 |           28 |        73 |
| FINTECH 12:249                 |       17 |    0.0935185  |    0.904762 |  0.0827304 |           12 |        41 |
| REGULATION 05:164              |       14 |    0.0656804  |    0.791667 |  0.0698668 |            5 |        22 |
| RISK_MANAGEMENT 05:019         |       14 |    0.0311334  |    0.791667 |  0.0676816 |            5 |        24 |
| FINANCIAL_INSTITUTIONS 06:009  |       13 |    0.0182099  |    0.76     |  0.0627387 |            6 |        23 |
| FINANCE 07:017                 |       12 |    0.0135246  |    0.730769 |  0.0584387 |            7 |        27 |
| REGULATORY_COMPLIANCE 09:034   |       11 |    0.0107862  |    0.703704 |  0.0540245 |            9 |        30 |
| ARTIFICIAL_INTELLIGENCE 06:025 |       11 |    0.0300497  |    0.703704 |  0.0558942 |            6 |        15 |
| REGULATORY_TECHNOLOGY 08:037   |       10 |    0.0079133  |    0.678571 |  0.0498094 |            8 |        15 |
| COMPLIANCE 07:030              |       10 |    0.00904808 |    0.678571 |  0.0501494 |            7 |        21 |
| ANTI_MONEY_LAUNDERING 06:035   |       10 |    0.0183143  |    0.678571 |  0.0510692 |            6 |        15 |
| SUPTECH 03:004                 |       10 |    0.00652093 |    0.678571 |  0.0495484 |            3 |        13 |
| FINANCIAL_REGULATION 05:035    |        9 |    0.0148287  |    0.655172 |  0.0468864 |            5 |        15 |
| INNOVATION 03:012              |        9 |    0.00514017 |    0.655172 |  0.045452  |            3 |         9 |
| FINANCIAL_SERVICES 04:168      |        8 |    0.00221619 |    0.633333 |  0.0410519 |            4 |        14 |
| BLOCKCHAIN 03:005              |        6 |    0.00747238 |    0.59375  |  0.0345913 |            3 |         8 |
| SEMANTIC_TECHNOLOGIES 02:041   |        4 |    0          |    0.558824 |  0.0242076 |            2 |         6 |
| SMART_CONTRACTS 03:023         |        3 |    0          |    0.542857 |  0.0208624 |            3 |         5 |
| DATA_PROTECTION 02:027         |        3 |    0          |    0.542857 |  0.0202846 |            2 |         4 |
| CHARITYTECH 02:017             |        3 |    0          |    0.542857 |  0.0203801 |            2 |         4 |
```
<BLANKLINE>


>>> file_name = "sphinx/_static/report/conceptual_structure/thematic_map/keywords_degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/report/conceptual_structure/thematic_map/keywords_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                           Name  Degree
0     0                 REGTECH 28:329      19
1     1                 FINTECH 12:249      17
2     2              REGULATION 05:164      14
3     3         RISK_MANAGEMENT 05:019      14
4     4  FINANCIAL_INSTITUTIONS 06:009      13


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
|  1 |      1 | FINTECH 12:249                 |       17 |
|  2 |      2 | REGULATION 05:164              |       14 |
|  3 |      3 | RISK_MANAGEMENT 05:019         |       14 |
|  4 |      4 | FINANCIAL_INSTITUTIONS 06:009  |       13 |
|  5 |      5 | FINANCE 07:017                 |       12 |
|  6 |      6 | REGULATORY_COMPLIANCE 09:034   |       11 |
|  7 |      7 | ARTIFICIAL_INTELLIGENCE 06:025 |       11 |
|  8 |      8 | REGULATORY_TECHNOLOGY 08:037   |       10 |
|  9 |      9 | COMPLIANCE 07:030              |       10 |
| 10 |     10 | ANTI_MONEY_LAUNDERING 06:035   |       10 |
| 11 |     11 | SUPTECH 03:004                 |       10 |
| 12 |     12 | FINANCIAL_REGULATION 05:035    |        9 |
| 13 |     13 | INNOVATION 03:012              |        9 |
| 14 |     14 | FINANCIAL_SERVICES 04:168      |        8 |
| 15 |     15 | BLOCKCHAIN 03:005              |        6 |
| 16 |     16 | SEMANTIC_TECHNOLOGIES 02:041   |        4 |
| 17 |     17 | SMART_CONTRACTS 03:023         |        3 |
| 18 |     18 | DATA_PROTECTION 02:027         |        3 |
| 19 |     19 | CHARITYTECH 02:017             |        3 |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ...co_word_network import co_word_network

FIELD = "keywords"
REPORT_DIR = "reports/thematic_map/keywords/"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def keywords(
    concordances_top_n=10,
    #
    # 'co_word_matrix' params:
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
        normalization="association",
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
