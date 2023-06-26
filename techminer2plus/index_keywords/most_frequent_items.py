# flake8: noqa
"""
Most Frequent Items
===============================================================================




>>> FILE_NAME = "sphinx/_static/use_cases/index_keywords/most_frequent_items.html"
>>> import techminer2plus
>>> items = techminer2plus.use_cases.index_keywords.most_frequent_items(
...     top_n=20,
...     root_dir="data/regtech/",
... )
>>> items.ranking_chart_.write_html(FILE_NAME)

.. raw:: html

    <iframe src="../../_static/use_cases/index_keywords/most_frequent_items.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> items.items_list_.head()
                        rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
index_keywords                                  ...                           
REGULATORY_COMPLIANCE          1        1    9  ...      3.0      2.0     0.43
FINANCIAL_INSTITUTIONS         2       23    6  ...      2.0      1.0     0.50
FINANCE                        3        2    5  ...      2.0      1.0     0.29
REGTECH                        4        3    5  ...      2.0      1.0     0.29
ANTI_MONEY_LAUNDERING          5       22    3  ...      2.0      1.0     0.50
<BLANKLINE>
[5 rows x 18 columns]

>>> print(items.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'index_keywords' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| index_keywords                  |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:--------------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGULATORY_COMPLIANCE           |          1 |         1 |     9 |             6 |                   3 |                 34 |                11 |                            3.78 |                           1.22 |                   0   |                     1.5 |                    0.166667 |                     2017 |     7 |                        4.86 |         3 |         2 |      0.43 |
| FINANCIAL_INSTITUTIONS          |          2 |        23 |     6 |             4 |                   2 |                  9 |                 3 |                            1.5  |                           0.5  |                  -0.5 |                     1   |                    0.166667 |                     2020 |     4 |                        2.25 |         2 |         1 |      0.5  |
| FINANCE                         |          3 |         2 |     5 |             3 |                   2 |                 16 |                 5 |                            3.2  |                           1    |                  -0.5 |                     1   |                    0.2      |                     2017 |     7 |                        2.29 |         2 |         1 |      0.29 |
| REGTECH                         |          4 |         3 |     5 |             3 |                   2 |                 15 |                 5 |                            3    |                           1    |                   0   |                     1   |                    0.2      |                     2017 |     7 |                        2.14 |         2 |         1 |      0.29 |
| ANTI_MONEY_LAUNDERING           |          5 |        22 |     3 |             3 |                   0 |                 10 |                 1 |                            3.33 |                           0.33 |                  -1   |                     0   |                    0        |                     2020 |     4 |                        2.5  |         2 |         1 |      0.5  |
| FINTECH                         |          6 |        25 |     3 |             3 |                   0 |                  8 |                 2 |                            2.67 |                           0.67 |                   0   |                     0   |                    0        |                     2019 |     5 |                        1.6  |         2 |         1 |      0.4  |
| INFORMATION_SYSTEMS             |          7 |         4 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| INFORMATION_USE                 |          8 |         5 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| SOFTWARE_SOLUTION               |          9 |         6 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| SANDBOXES                       |         10 |         7 |     2 |             2 |                   0 |                 12 |                 3 |                            6    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2017 |     7 |                        1.71 |         1 |         1 |      0.14 |
| FINANCIAL_REGULATION            |         11 |        15 |     2 |             1 |                   1 |                 11 |                 3 |                            5.5  |                           1.5  |                   0   |                     0.5 |                    0.25     |                     2017 |     7 |                        1.57 |         1 |         1 |      0.14 |
| FINANCIAL_SERVICES_INDUSTRY     |         12 |        16 |     2 |             1 |                   1 |                 11 |                 3 |                            5.5  |                           1.5  |                   0   |                     0.5 |                    0.25     |                     2017 |     7 |                        1.57 |         1 |         1 |      0.14 |
| LAUNDERING                      |         13 |        24 |     2 |             2 |                   0 |                  9 |                 1 |                            4.5  |                           0.5  |                  -1   |                     0   |                    0        |                     2021 |     3 |                        3    |         2 |         1 |      0.67 |
| BANKING                         |         14 |        26 |     2 |             2 |                   0 |                  8 |                 1 |                            4    |                           0.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        2    |         1 |         1 |      0.25 |
| FINANCIAL_CRISIS                |         15 |        27 |     2 |             1 |                   1 |                  7 |                 1 |                            3.5  |                           0.5  |                   0   |                     0.5 |                    0.25     |                     2021 |     3 |                        2.33 |         1 |         1 |      0.33 |
| RISK_MANAGEMENT                 |         16 |        36 |     2 |             2 |                   0 |                  5 |                 0 |                            2.5  |                           0    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| COMMERCE                        |         17 |        37 |     2 |             2 |                   0 |                  4 |                 2 |                            2    |                           1    |                   0   |                     0   |                    0        |                     2019 |     5 |                        0.8  |         1 |         1 |      0.2  |
| CLASSIFICATION (OF_INFORMATION) |         18 |        54 |     2 |             1 |                   1 |                  3 |                 1 |                            1.5  |                           0.5  |                  -0.5 |                     0.5 |                    0.25     |                     2021 |     3 |                        1    |         1 |         1 |      0.33 |
| ARTIFICIAL_INTELLIGENCE         |         19 |        65 |     2 |             1 |                   1 |                  2 |                 0 |                            1    |                           0    |                  -0.5 |                     0.5 |                    0.25     |                     2021 |     3 |                        0.67 |         1 |         1 |      0.33 |
| BLOCKCHAIN                      |         20 |        66 |     2 |             2 |                   0 |                  2 |                 0 |                            1    |                           0    |                  -0.5 |                     0   |                    0        |                     2017 |     7 |                        0.29 |         1 |         1 |      0.14 |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""
# from ... import list_items
# from ...graphing_lib import ranking_chart

FIELD = "index_keywords"
METRIC = "OCC"
TITLE = "Most Frequent Index Keywords"


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
