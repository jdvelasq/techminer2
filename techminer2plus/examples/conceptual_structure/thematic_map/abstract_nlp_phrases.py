# flake8: noqa
"""
Abstract NLP Phrases
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.examples.conceptual_structure.thematic_map.abstract_nlp_phrases(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm_or_estimator="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )
--INFO-- The file 'data/regtech/reports/reports/thematic_map/abstract_nlp_phrases/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/abstract_nlp_phrases/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/abstract_nlp_phrases/CL_01_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/abstract_nlp_phrases/CL_00_prompt.txt' was created.

>>> file_name = "sphinx/_static/examples/conceptual_structure/thematic_map/abstract_nlp_phrases.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/examples/conceptual_structure/thematic_map/abstract_nlp_phrases.html" height="600px" width="100%" frameBorder="0"></iframe>

    
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
| 10 | REGTECH 03:034                     |                                |


>>> print(nnet.network_metrics__table_.head().to_markdown())
|                                    |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGULATORY_TECHNOLOGY 17:266       |       19 |     0.108535  |    1        |  0.0813975 |           17 |        52 |
| FINANCIAL_INSTITUTIONS 15:194      |       17 |     0.0548083 |    0.904762 |  0.0722123 |           15 |        36 |
| REGULATORY_COMPLIANCE 07:198       |       14 |     0.0278868 |    0.791667 |  0.0603404 |            7 |        24 |
| FINANCIAL_SERVICES_INDUSTRY 05:315 |       14 |     0.0480692 |    0.791667 |  0.0618488 |            5 |        23 |
| ARTIFICIAL_INTELLIGENCE 07:033     |       13 |     0.0322983 |    0.76     |  0.0568675 |            7 |        20 |


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
| REGTECH 03:034                     |        3 |    0          |    0.542857 |  0.0187017 |            3 |         3 |
```
<BLANKLINE>



>>> file_name = "sphinx/_static/examples/conceptual_structure/thematic_map/abstract_nlp_phrases_degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/conceptual_structure/thematic_map/abstract_nlp_phrases_degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                                Name  Degree
0     0        REGULATORY_TECHNOLOGY 17:266      19
1     1       FINANCIAL_INSTITUTIONS 15:194      17
2     2        REGULATORY_COMPLIANCE 07:198      14
3     3  FINANCIAL_SERVICES_INDUSTRY 05:315      14
4     4      ARTIFICIAL_INTELLIGENCE 07:033      13

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
| 19 |     19 | REGTECH 03:034                     |        3 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...co_word_network import co_word_network

FIELD = "abstract_nlp_phrases"
REPORT_DIR = "reports/thematic_map/abstract_nlp_phrases/"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def abstract_nlp_phrases(
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
