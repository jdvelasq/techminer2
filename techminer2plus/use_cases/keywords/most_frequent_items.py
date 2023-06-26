# flake8: noqa
"""
Most Frequent Items
===============================================================================





>>> FILE_NAME = "sphinx/_static/use_cases/keywords/most_frequent_items.html"
>>> import techminer2plus
>>> items = techminer2plus.use_cases.keywords.most_frequent_items(
...     top_n=20,
...     root_dir="data/regtech/",
... )
>>> items.ranking_chart_.write_html(FILE_NAME)

.. raw:: html

    <iframe src="../../_static/use_cases/keywords/most_frequent_items.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> items.items_list_.head()
                       rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
keywords                                       ...                           
REGTECH                       1        1   28  ...      9.0      4.0     1.29
FINTECH                       2        2   12  ...      5.0      3.0     0.83
REGULATORY_COMPLIANCE         3       11    9  ...      3.0      2.0     0.43
REGULATORY_TECHNOLOGY         4        8    8  ...      4.0      2.0     1.00
COMPLIANCE                    5       13    7  ...      3.0      2.0     0.60
<BLANKLINE>
[5 rows x 18 columns]

>>> print(items.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'keywords' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| keywords                |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                 |          1 |         1 |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| FINTECH                 |          2 |         2 |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| REGULATORY_COMPLIANCE   |          3 |        11 |     9 |             6 |                   3 |                 34 |                11 |                            3.78 |                           1.22 |                   0   |                     1.5 |                   0.166667  |                     2017 |     7 |                        4.86 |         3 |         2 |      0.43 |
| REGULATORY_TECHNOLOGY   |          4 |         8 |     8 |             5 |                   3 |                 37 |                14 |                            4.62 |                           1.75 |                  -1   |                     1.5 |                   0.1875    |                     2020 |     4 |                        9.25 |         4 |         2 |      1    |
| COMPLIANCE              |          5 |        13 |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| FINANCE                 |          6 |        25 |     7 |             4 |                   3 |                 17 |                 5 |                            2.43 |                           0.71 |                  -0.5 |                     1.5 |                   0.214286  |                     2017 |     7 |                        2.43 |         2 |         1 |      0.29 |
| ANTI_MONEY_LAUNDERING   |          7 |         9 |     6 |             6 |                   0 |                 35 |                 8 |                            5.83 |                           1.33 |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        8.75 |         3 |         2 |      0.75 |
| ARTIFICIAL_INTELLIGENCE |          8 |        15 |     6 |             4 |                   2 |                 25 |                 6 |                            4.17 |                           1    |                  -0.5 |                     1   |                   0.166667  |                     2019 |     5 |                        5    |         3 |         2 |      0.6  |
| FINANCIAL_INSTITUTIONS  |          9 |        65 |     6 |             4 |                   2 |                  9 |                 3 |                            1.5  |                           0.5  |                  -0.5 |                     1   |                   0.166667  |                     2020 |     4 |                        2.25 |         2 |         1 |      0.5  |
| REGULATION              |         10 |         4 |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| FINANCIAL_REGULATION    |         11 |        10 |     5 |             2 |                   3 |                 35 |                 8 |                            7    |                           1.6  |                   0   |                     1.5 |                   0.3       |                     2017 |     7 |                        5    |         2 |         2 |      0.29 |
| RISK_MANAGEMENT         |         12 |        24 |     5 |             4 |                   1 |                 19 |                 8 |                            3.8  |                           1.6  |                   0   |                     0.5 |                   0.1       |                     2018 |     6 |                        3.17 |         3 |         2 |      0.5  |
| FINANCIAL_SERVICES      |         13 |         3 |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                   0.125     |                     2017 |     7 |                       24    |         3 |         2 |      0.43 |
| SMART_CONTRACTS         |         14 |        21 |     3 |             3 |                   0 |                 23 |                 8 |                            7.67 |                           2.67 |                  -0.5 |                     0   |                   0         |                     2017 |     7 |                        3.29 |         1 |         1 |      0.14 |
| INNOVATION              |         15 |        38 |     3 |             2 |                   1 |                 12 |                 4 |                            4    |                           1.33 |                  -0.5 |                     0.5 |                   0.166667  |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| BLOCKCHAIN              |         16 |        87 |     3 |             3 |                   0 |                  5 |                 0 |                            1.67 |                           0    |                  -0.5 |                     0   |                   0         |                     2017 |     7 |                        0.71 |         1 |         1 |      0.14 |
| SUPTECH                 |         17 |        88 |     3 |             1 |                   2 |                  4 |                 2 |                            1.33 |                           0.67 |                   0   |                     1   |                   0.333333  |                     2019 |     5 |                        0.8  |         1 |         1 |      0.2  |
| SEMANTIC_TECHNOLOGIES   |         18 |         7 |     2 |             2 |                   0 |                 41 |                19 |                           20.5  |                           9.5  |                   0   |                     0   |                   0         |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| DATA_PROTECTION         |         19 |        14 |     2 |             1 |                   1 |                 27 |                 5 |                           13.5  |                           2.5  |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        6.75 |         2 |         1 |      0.5  |
| CHARITYTECH             |         20 |        26 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ... import list_items
from ...graphing_lib import ranking_chart

FIELD = "keywords"
METRIC = "OCC"
TITLE = "Most Frequent Keywords"


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
