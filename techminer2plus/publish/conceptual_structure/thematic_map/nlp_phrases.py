# flake8: noqa
"""
NLP Phrases
===============================================================================


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> nnet = techminer2plus.publish.conceptual_structure.thematic_map.nlp_phrases(
...     top_n=20,
...     root_dir=root_dir,
...     algorithm_or_estimator="louvain",
...     network_viewer_dict={'nx_k': 0.2, 'nx_iterations': 10},
... )
--INFO-- The file 'data/regtech/reports/reports/thematic_map/nlp_phrases/CL_00_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/nlp_phrases/CL_02_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/nlp_phrases/CL_01_abstracts_report.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/nlp_phrases/CL_00_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/nlp_phrases/CL_02_prompt.txt' was created.
--INFO-- The file 'data/regtech/reports/reports/thematic_map/nlp_phrases/CL_01_prompt.txt' was created.

>>> file_name = "sphinx/_static/examples/conceptual_structure/thematic_map/nlp_phrases.html"
>>> nnet.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/examples/conceptual_structure/thematic_map/nlp_phrases.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> print(nnet.communities_.to_markdown())
|    | CL_00                         | CL_01                               | CL_02                          |
|---:|:------------------------------|:------------------------------------|:-------------------------------|
|  0 | REGULATORY_TECHNOLOGY 18:273  | REGULATORY_COMPLIANCE 07:198        | FINANCIAL_REGULATION 07:360    |
|  1 | FINANCIAL_INSTITUTIONS 15:194 | FINANCIAL_SECTOR 07:169             | GLOBAL_FINANCIAL_CRISIS 06:177 |
|  2 | FINANCIAL_CRISIS 06:058       | ARTIFICIAL_INTELLIGENCE 07:033      | INFORMATION_TECHNOLOGY 05:177  |
|  3 | FINANCIAL_SYSTEM 05:189       | FINANCIAL_SERVICES_INDUSTRY 05:315  | FINANCIAL_MARKETS 04:151       |
|  4 | FINANCIAL_TECHNOLOGY 05:173   | MACHINE_LEARNING 04:007             |                                |
|  5 | REGTECH_SOLUTIONS 05:018      | DIGITAL_INNOVATION 03:164           |                                |
|  6 | REGTECH 04:037                | SYSTEMATIC_LITERATURE_REVIEW 03:004 |                                |
|  7 | RISK_MANAGEMENT 04:015        |                                     |                                |
|  8 | NEW_TECHNOLOGIES 04:012       |                                     |                                |



>>> print(nnet.network_metrics__table_.head().to_markdown())
|                                    |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:-----------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGULATORY_TECHNOLOGY 18:273       |       19 |     0.0891629 |    1        |  0.0770293 |           18 |        55 |
| FINANCIAL_INSTITUTIONS 15:194      |       17 |     0.0477585 |    0.904762 |  0.0689321 |           15 |        36 |
| FINANCIAL_SERVICES_INDUSTRY 05:315 |       15 |     0.0432704 |    0.826087 |  0.0619345 |            5 |        25 |
| REGULATORY_COMPLIANCE 07:198       |       14 |     0.0240369 |    0.791667 |  0.0576665 |            7 |        24 |
| FINANCIAL_REGULATION 07:360        |       13 |     0.0190246 |    0.76     |  0.0539831 |            7 |        25 |

>>> print(nnet.network_metrics__prompt_)
Your task is to generate a short analysis of the indicators of a network \\
for a research paper. Summarize the text below, delimited by triple \\
backticks, in at most 30 words, identifiying any notable patterns, trends, \\
or outliers in the data.
<BLANKLINE>
Table:
```
|                                     |   Degree |   Betweenness |   Closeness |   PageRank |   Centrality |   Density |
|:------------------------------------|---------:|--------------:|------------:|-----------:|-------------:|----------:|
| REGULATORY_TECHNOLOGY 18:273        |       19 |   0.0891629   |    1        |  0.0770293 |           18 |        55 |
| FINANCIAL_INSTITUTIONS 15:194       |       17 |   0.0477585   |    0.904762 |  0.0689321 |           15 |        36 |
| FINANCIAL_SERVICES_INDUSTRY 05:315  |       15 |   0.0432704   |    0.826087 |  0.0619345 |            5 |        25 |
| REGULATORY_COMPLIANCE 07:198        |       14 |   0.0240369   |    0.791667 |  0.0576665 |            7 |        24 |
| FINANCIAL_REGULATION 07:360         |       13 |   0.0190246   |    0.76     |  0.0539831 |            7 |        25 |
| FINANCIAL_SECTOR 07:169             |       13 |   0.0141537   |    0.76     |  0.0538999 |            7 |        23 |
| ARTIFICIAL_INTELLIGENCE 07:033      |       13 |   0.028393    |    0.76     |  0.054324  |            7 |        21 |
| FINANCIAL_SYSTEM 05:189             |       13 |   0.0298897   |    0.76     |  0.0550593 |            5 |        19 |
| INFORMATION_TECHNOLOGY 05:177       |       13 |   0.0210387   |    0.76     |  0.0540849 |            5 |        21 |
| DIGITAL_INNOVATION 03:164           |       13 |   0.0143904   |    0.76     |  0.0537843 |            3 |        17 |
| SYSTEMATIC_LITERATURE_REVIEW 03:004 |       12 |   0.0122018   |    0.730769 |  0.0503233 |            3 |        14 |
| FINANCIAL_TECHNOLOGY 05:173         |       11 |   0.0184305   |    0.703704 |  0.0475937 |            5 |        16 |
| RISK_MANAGEMENT 04:015              |       11 |   0.0142372   |    0.703704 |  0.0468748 |            4 |        16 |
| FINANCIAL_CRISIS 06:058             |       10 |   0.00954491  |    0.678571 |  0.0434172 |            6 |        18 |
| GLOBAL_FINANCIAL_CRISIS 06:177      |        9 |   0.00743061  |    0.655172 |  0.0395703 |            6 |        14 |
| REGTECH_SOLUTIONS 05:018            |        9 |   0.00968625  |    0.655172 |  0.0400333 |            5 |        13 |
| FINANCIAL_MARKETS 04:151            |        9 |   0.00410053  |    0.655172 |  0.0395214 |            4 |        11 |
| MACHINE_LEARNING 04:007             |        9 |   0.00229741  |    0.655172 |  0.0392385 |            4 |        12 |
| NEW_TECHNOLOGIES 04:012             |        8 |   0.0110299   |    0.633333 |  0.0370583 |            4 |        10 |
| REGTECH 04:037                      |        5 |   0.000974659 |    0.575758 |  0.0256712 |            4 |         6 |
```
<BLANKLINE>

>>> file_name = "sphinx/_static/examples/conceptual_structure/thematic_map/nlp_phrases_degree_plot.html"
>>> nnet.degree_plot__plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../../../_static/examples/conceptual_structure/thematic_map/nlp_phrases__degree_plot.html" height="600px" width="100%" frameBorder="0"></iframe>


    
>>> print(nnet.degree_plot__table_.head())
   Node                                Name  Degree
0     0        REGULATORY_TECHNOLOGY 18:273      19
1     1       FINANCIAL_INSTITUTIONS 15:194      17
2     2  FINANCIAL_SERVICES_INDUSTRY 05:315      15
3     3        REGULATORY_COMPLIANCE 07:198      14
4     4         FINANCIAL_REGULATION 07:360      13


>>> print(nnet.degree_plot__prompt_)
Your task is to generate an analysis about the degree of the nodes in a \\
networkx graph of a co-ocurrence matrix. Analyze the table below, delimited \\
by triple backticks, identifying any notable patterns, trends, or outliers \\
in the data, and discuss their implications in the network.
<BLANKLINE>
Table:
```
|    |   Node | Name                                |   Degree |
|---:|-------:|:------------------------------------|---------:|
|  0 |      0 | REGULATORY_TECHNOLOGY 18:273        |       19 |
|  1 |      1 | FINANCIAL_INSTITUTIONS 15:194       |       17 |
|  2 |      2 | FINANCIAL_SERVICES_INDUSTRY 05:315  |       15 |
|  3 |      3 | REGULATORY_COMPLIANCE 07:198        |       14 |
|  4 |      4 | FINANCIAL_REGULATION 07:360         |       13 |
|  5 |      5 | FINANCIAL_SECTOR 07:169             |       13 |
|  6 |      6 | ARTIFICIAL_INTELLIGENCE 07:033      |       13 |
|  7 |      7 | FINANCIAL_SYSTEM 05:189             |       13 |
|  8 |      8 | INFORMATION_TECHNOLOGY 05:177       |       13 |
|  9 |      9 | DIGITAL_INNOVATION 03:164           |       13 |
| 10 |     10 | SYSTEMATIC_LITERATURE_REVIEW 03:004 |       12 |
| 11 |     11 | FINANCIAL_TECHNOLOGY 05:173         |       11 |
| 12 |     12 | RISK_MANAGEMENT 04:015              |       11 |
| 13 |     13 | FINANCIAL_CRISIS 06:058             |       10 |
| 14 |     14 | GLOBAL_FINANCIAL_CRISIS 06:177      |        9 |
| 15 |     15 | REGTECH_SOLUTIONS 05:018            |        9 |
| 16 |     16 | FINANCIAL_MARKETS 04:151            |        9 |
| 17 |     17 | MACHINE_LEARNING 04:007             |        9 |
| 18 |     18 | NEW_TECHNOLOGIES 04:012             |        8 |
| 19 |     19 | REGTECH 04:037                      |        5 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...co_word_network import co_word_network

FIELD = "nlp_phrases"
REPORT_DIR = "reports/thematic_map/nlp_phrases/"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def nlp_phrases(
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
