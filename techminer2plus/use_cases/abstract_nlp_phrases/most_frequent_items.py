# flake8: noqa
"""
Most Frequent Items
===============================================================================


>>> FILE_NAME = "sphinx/_static/use_cases/abstract_nlp_phrases/most_frequent_items.html"
>>> import techminer2plus
>>> items = techminer2plus.use_cases.abstract_nlp_phrases.most_frequent_items(
...     top_n=20,
...     root_dir="data/regtech/",
... )
>>> items.ranking_chart_.write_html(FILE_NAME)

.. raw:: html

    <iframe src="../../_static/use_cases/abstract_nlp_phrases/most_frequent_items.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> items.items_list_.head()
                         rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
abstract_nlp_phrases                             ...                           
REGULATORY_TECHNOLOGY           1        3   17  ...      7.0      3.0     1.00
FINANCIAL_INSTITUTIONS          2        5   15  ...      4.0      3.0     0.67
REGULATORY_COMPLIANCE           3        4    7  ...      3.0      2.0     0.50
FINANCIAL_SECTOR                4       10    7  ...      3.0      2.0     0.43
ARTIFICIAL_INTELLIGENCE         5       30    7  ...      3.0      2.0     0.75
<BLANKLINE>
[5 rows x 18 columns]

>>> print(items.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'abstract_nlp_phrases' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| abstract_nlp_phrases        |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:----------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGULATORY_TECHNOLOGY       |          1 |         3 |    17 |            12 |                   5 |                266 |                41 |                           15.65 |                           2.41 |                  -1   |                     2.5 |                   0.147059  |                     2017 |     7 |                       38    |         7 |         3 |      1    |
| FINANCIAL_INSTITUTIONS      |          2 |         5 |    15 |            11 |                   4 |                194 |                30 |                           12.93 |                           2    |                  -1.5 |                     2   |                   0.133333  |                     2018 |     6 |                       32.33 |         4 |         3 |      0.67 |
| REGULATORY_COMPLIANCE       |          3 |         4 |     7 |             6 |                   1 |                198 |                40 |                           28.29 |                           5.71 |                  -0.5 |                     0.5 |                   0.0714286 |                     2018 |     6 |                       33    |         3 |         2 |      0.5  |
| FINANCIAL_SECTOR            |          4 |        10 |     7 |             5 |                   2 |                169 |                 5 |                           24.14 |                           0.71 |                  -1.5 |                     1   |                   0.142857  |                     2017 |     7 |                       24.14 |         3 |         2 |      0.43 |
| ARTIFICIAL_INTELLIGENCE     |          5 |        30 |     7 |             4 |                   3 |                 33 |                 9 |                            4.71 |                           1.29 |                  -0.5 |                     1.5 |                   0.214286  |                     2020 |     4 |                        8.25 |         3 |         2 |      0.75 |
| FINANCIAL_REGULATION        |          6 |         1 |     6 |             5 |                   1 |                330 |                22 |                           55    |                           3.67 |                  -1   |                     0.5 |                   0.0833333 |                     2017 |     7 |                       47.14 |         4 |         3 |      0.57 |
| GLOBAL_FINANCIAL_CRISIS     |          7 |         8 |     6 |             3 |                   3 |                177 |                 5 |                           29.5  |                           0.83 |                   0.5 |                     1.5 |                   0.25      |                     2017 |     7 |                       25.29 |         3 |         2 |      0.43 |
| FINANCIAL_CRISIS            |          8 |        28 |     6 |             6 |                   0 |                 58 |                11 |                            9.67 |                           1.83 |                  -1   |                     0   |                   0         |                     2016 |     8 |                        7.25 |         4 |         2 |      0.5  |
| FINANCIAL_SERVICES_INDUSTRY |          9 |         2 |     5 |             3 |                   2 |                315 |                21 |                           63    |                           4.2  |                   0   |                     1   |                   0.2       |                     2017 |     7 |                       45    |         3 |         3 |      0.43 |
| INFORMATION_TECHNOLOGY      |         10 |         7 |     5 |             4 |                   1 |                177 |                10 |                           35.4  |                           2    |                  -0.5 |                     0.5 |                   0.1       |                     2017 |     7 |                       25.29 |         4 |         3 |      0.57 |
| FINANCIAL_TECHNOLOGY        |         11 |         9 |     5 |             4 |                   1 |                173 |                25 |                           34.6  |                           5    |                  -0.5 |                     0.5 |                   0.1       |                     2017 |     7 |                       24.71 |         3 |         2 |      0.43 |
| REGTECH_SOLUTIONS           |         12 |        39 |     5 |             4 |                   1 |                 18 |                 4 |                            3.6  |                           0.8  |                   0   |                     0.5 |                   0.1       |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| FINANCIAL_SYSTEM            |         13 |         6 |     4 |             3 |                   1 |                178 |                25 |                           44.5  |                           6.25 |                   0   |                     0.5 |                   0.125     |                     2018 |     6 |                       29.67 |         3 |         2 |      0.5  |
| RISK_MANAGEMENT             |         14 |        40 |     4 |             3 |                   1 |                 15 |                 8 |                            3.75 |                           2    |                   0   |                     0.5 |                   0.125     |                     2018 |     6 |                        2.5  |         2 |         2 |      0.33 |
| NEW_TECHNOLOGIES            |         15 |        47 |     4 |             3 |                   1 |                 12 |                 1 |                            3    |                           0.25 |                  -1   |                     0.5 |                   0.125     |                     2019 |     5 |                        2.4  |         2 |         1 |      0.4  |
| MACHINE_LEARNING            |         16 |        57 |     4 |             1 |                   3 |                  7 |                 4 |                            1.75 |                           1    |                  -0.5 |                     1.5 |                   0.375     |                     2021 |     3 |                        2.33 |         2 |         1 |      0.67 |
| DIGITAL_INNOVATION          |         17 |        11 |     3 |             2 |                   1 |                164 |                21 |                           54.67 |                           7    |                  -0.5 |                     0.5 |                   0.166667  |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| FINANCIAL_MARKETS           |         18 |        25 |     3 |             1 |                   2 |                151 |                 0 |                           50.33 |                           0    |                   0   |                     1   |                   0.333333  |                     2017 |     7 |                       21.57 |         1 |         1 |      0.14 |
| REGTECH                     |         19 |        29 |     3 |             2 |                   1 |                 34 |                12 |                           11.33 |                           4    |                   0   |                     0.5 |                   0.166667  |                     2018 |     6 |                        5.67 |         2 |         2 |      0.33 |
| COMPLIANCE_COSTS            |         20 |        92 |     3 |             2 |                   1 |                  2 |                 0 |                            0.67 |                           0    |                   0   |                     0.5 |                   0.166667  |                     2020 |     4 |                        0.5  |         1 |         1 |      0.25 |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ... import list_items
from ...graphing_lib import ranking_chart

FIELD = "abstract_nlp_phrases"
METRIC = "OCC"
TITLE = "Most Frequent Abstract NLP Phrases"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def most_frequent_items(
    #
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    metric_label=None,
    field_label=None,
    title=None,
    #
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most Relevant Source Items."""

    if title is None:
        title = TITLE

    itemslist = list_items(
        field=FIELD,
        metric=METRIC,
        #
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # Database filters:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return ranking_chart(
        itemslist=itemslist,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )
