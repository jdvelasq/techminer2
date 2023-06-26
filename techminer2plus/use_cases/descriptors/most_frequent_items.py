# flake8: noqa
"""
Most Frequent Items
===============================================================================



>>> FILE_NAME = "sphinx/_static/use_cases/descriptors/most_frequent_items.html"
>>> import techminer2plus
>>> items = techminer2plus.use_cases.descriptors.most_frequent_items(
...     top_n=20,
...     root_dir="data/regtech/",
... )
>>> items.ranking_chart_.write_html(FILE_NAME)

.. raw:: html

    <iframe src="../../_static/use_cases/descriptors/most_frequent_items.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> items.items_list_.head()
                        rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
descriptors                                     ...                           
REGTECH                        1        2   29  ...      9.0      4.0     1.29
REGULATORY_TECHNOLOGY          2        4   20  ...      7.0      3.0     1.00
FINANCIAL_INSTITUTIONS         3        7   16  ...      4.0      3.0     0.67
REGULATORY_COMPLIANCE          4        6   15  ...      5.0      3.0     0.71
FINANCIAL_REGULATION           5        1   12  ...      7.0      4.0     0.88
<BLANKLINE>
[5 rows x 18 columns]


>>> print(items.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'descriptors' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| descriptors                 |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:----------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                     |          1 |         2 |    29 |            20 |                   9 |                330 |                75 |                           11.38 |                           2.59 |                  -0.5 |                     4.5 |                   0.155172  |                     2017 |     7 |                       47.14 |         9 |         4 |      1.29 |
| REGULATORY_TECHNOLOGY       |          2 |         4 |    20 |            14 |                   6 |                274 |                43 |                           13.7  |                           2.15 |                  -1.5 |                     3   |                   0.15      |                     2017 |     7 |                       39.14 |         7 |         3 |      1    |
| FINANCIAL_INSTITUTIONS      |          3 |         7 |    16 |            12 |                   4 |                198 |                30 |                           12.38 |                           1.88 |                  -1.5 |                     2   |                   0.125     |                     2018 |     6 |                       33    |         4 |         3 |      0.67 |
| REGULATORY_COMPLIANCE       |          4 |         6 |    15 |            12 |                   3 |                232 |                51 |                           15.47 |                           3.4  |                  -0.5 |                     1.5 |                   0.1       |                     2017 |     7 |                       33.14 |         5 |         3 |      0.71 |
| FINANCIAL_REGULATION        |          5 |         1 |    12 |             8 |                   4 |                395 |                30 |                           32.92 |                           2.5  |                  -1   |                     2   |                   0.166667  |                     2016 |     8 |                       49.38 |         7 |         4 |      0.88 |
| FINTECH                     |          6 |         5 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| ARTIFICIAL_INTELLIGENCE     |          7 |        36 |     8 |             5 |                   3 |                 36 |                 9 |                            4.5  |                           1.12 |                  -0.5 |                     1.5 |                   0.1875    |                     2019 |     5 |                        7.2  |         3 |         2 |      0.6  |
| FINANCIAL_SECTOR            |          8 |        14 |     7 |             5 |                   2 |                169 |                 5 |                           24.14 |                           0.71 |                  -1.5 |                     1   |                   0.142857  |                     2017 |     7 |                       24.14 |         3 |         2 |      0.43 |
| FINANCIAL_CRISIS            |          9 |        34 |     7 |             6 |                   1 |                 58 |                11 |                            8.29 |                           1.57 |                  -0.5 |                     0.5 |                   0.0714286 |                     2016 |     8 |                        7.25 |         4 |         2 |      0.5  |
| COMPLIANCE                  |         10 |        39 |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| FINANCE                     |         11 |        57 |     7 |             4 |                   3 |                 17 |                 5 |                            2.43 |                           0.71 |                  -0.5 |                     1.5 |                   0.214286  |                     2017 |     7 |                        2.43 |         2 |         1 |      0.29 |
| FINANCIAL_SERVICES          |         12 |         8 |     6 |             5 |                   1 |                195 |                28 |                           32.5  |                           4.67 |                  -0.5 |                     0.5 |                   0.0833333 |                     2017 |     7 |                       27.86 |         4 |         3 |      0.57 |
| INFORMATION_TECHNOLOGY      |         13 |        11 |     6 |             4 |                   2 |                177 |                10 |                           29.5  |                           1.67 |                   0   |                     1   |                   0.166667  |                     2017 |     7 |                       25.29 |         4 |         3 |      0.57 |
| GLOBAL_FINANCIAL_CRISIS     |         14 |        12 |     6 |             3 |                   3 |                177 |                 5 |                           29.5  |                           0.83 |                   0.5 |                     1.5 |                   0.25      |                     2017 |     7 |                       25.29 |         3 |         2 |      0.43 |
| FINANCIAL_TECHNOLOGY        |         15 |        13 |     6 |             5 |                   1 |                173 |                25 |                           28.83 |                           4.17 |                  -0.5 |                     0.5 |                   0.0833333 |                     2017 |     7 |                       24.71 |         3 |         2 |      0.43 |
| ANTI_MONEY_LAUNDERING       |         16 |        37 |     6 |             6 |                   0 |                 35 |                 8 |                            5.83 |                           1.33 |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        8.75 |         3 |         2 |      0.75 |
| FINANCIAL_SERVICES_INDUSTRY |         17 |         3 |     5 |             3 |                   2 |                315 |                21 |                           63    |                           4.2  |                   0   |                     1   |                   0.2       |                     2017 |     7 |                       45    |         3 |         3 |      0.43 |
| FINANCIAL_SYSTEM            |         18 |         9 |     5 |             4 |                   1 |                189 |                28 |                           37.8  |                           5.6  |                   0   |                     0.5 |                   0.1       |                     2017 |     7 |                       27    |         3 |         3 |      0.43 |
| REGULATION                  |         19 |        16 |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| RISK_MANAGEMENT             |         20 |        55 |     5 |             4 |                   1 |                 19 |                 8 |                            3.8  |                           1.6  |                   0   |                     0.5 |                   0.1       |                     2018 |     6 |                        3.17 |         3 |         2 |      0.5  |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
from ... import list_items
from ...graphing_lib import ranking_chart

FIELD = "descriptors"
METRIC = "OCC"
TITLE = "Most Frequent Descriptors"


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
