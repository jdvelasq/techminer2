# flake8: noqa
"""
Most Frequent Title NLP Phrases
===============================================================================

See :ref:`report.ranking_chart`.



>>> FILE_NAME = "sphinx/_static/use_cases/title_nlp_phrases/most_frequent_items.html"
>>> import techminer2plus
>>> items = techminer2plus.use_cases.title_nlp_phrases.most_frequent_items(
...     top_n=20,
...     root_dir="data/regtech/",
... )
>>> items.ranking_chart_.write_html(FILE_NAME)

.. raw:: html

    <iframe src="../../_static/use_cases/title_nlp_phrases/most_frequent_items.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> items.items_list_.head()
                         rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
title_nlp_phrases                                ...                           
REGULATORY_TECHNOLOGY           1        4    3  ...      2.0      2.0     0.50
ARTIFICIAL_INTELLIGENCE         2        5    3  ...      2.0      1.0     0.50
FINANCIAL_REGULATION            3        1    2  ...      2.0      2.0     0.25
FINANCIAL_CRIME                 4        8    2  ...      2.0      1.0     0.50
EUROPEAN_UNION                  5        2    1  ...      1.0      1.0     0.25
<BLANKLINE>
[5 rows x 18 columns]


>>> print(items.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'title_nlp_phrases' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| title_nlp_phrases                    |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:-------------------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGULATORY_TECHNOLOGY                |          1 |         4 |     3 |             3 |                   0 |                 20 |                 8 |                            6.67 |                           2.67 |                  -1   |                     0   |                    0        |                     2020 |     4 |                        5    |         2 |         2 |      0.5  |
| ARTIFICIAL_INTELLIGENCE              |          2 |         5 |     3 |             2 |                   1 |                 17 |                 3 |                            5.67 |                           1    |                  -0.5 |                     0.5 |                    0.166667 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| FINANCIAL_REGULATION                 |          3 |         1 |     2 |             2 |                   0 |                180 |                 0 |                           90    |                           0    |                   0   |                     0   |                    0        |                     2016 |     8 |                       22.5  |         2 |         2 |      0.25 |
| FINANCIAL_CRIME                      |          4 |         8 |     2 |             2 |                   0 |                 12 |                 3 |                            6    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3    |         2 |         1 |      0.5  |
| EUROPEAN_UNION                       |          5 |         2 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| FINANCIAL_RISK                       |          6 |         3 |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                    0        |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| EFFECTIVE_SOLUTIONS                  |          7 |         6 |     1 |             1 |                   0 |                 14 |                 3 |                           14    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        3.5  |         1 |         1 |      0.25 |
| FINANCIAL_DEVELOPMENT                |          8 |         7 |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| BANK_TREASURY                        |          9 |         9 |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| DIGITAL_TRANSFORMATION               |         10 |        10 |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| REGULATORY_TECHNOLOGY_REGTECH        |         11 |        11 |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                   0   |                     0   |                    0        |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| FINANCIAL_SYSTEM                     |         12 |        12 |     1 |             1 |                   0 |                 11 |                 3 |                           11    |                           3    |                   0   |                     0   |                    0        |                     2017 |     7 |                        1.57 |         1 |         1 |      0.14 |
| AML_COMPLIANCE                       |         13 |        13 |     1 |             1 |                   0 |                 10 |                 3 |                           10    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        2.5  |         1 |         1 |      0.25 |
| REGTECH_SOLUTIONS                    |         14 |        14 |     1 |             1 |                   0 |                 10 |                 3 |                           10    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        2.5  |         1 |         1 |      0.25 |
| MODERN_INFORMATION_TECHNOLOGY        |         15 |        15 |     1 |             1 |                   0 |                  5 |                 3 |                            5    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| REGULATORY_AFFAIRS                   |         16 |        16 |     1 |             1 |                   0 |                  5 |                 3 |                            5    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| SMART_REGULATION                     |         17 |        17 |     1 |             1 |                   0 |                  4 |                 3 |                            4    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| FINANCIAL_STABILITY                  |         18 |        18 |     1 |             1 |                   0 |                  4 |                 0 |                            4    |                           0    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| TRADITIONAL_FINANCIAL_INTERMEDIATION |         19 |        19 |     1 |             1 |                   0 |                  4 |                 0 |                            4    |                           0    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| CHARITABLE_ORGANISATIONS             |         20 |        20 |     1 |             0 |                   1 |                  3 |                 1 |                            3    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
```
<BLANKLINE>

# pylint: disable=line-too-long
"""
from ... import list_items
from ...graphing_lib import ranking_chart

FIELD = "title_nlp_phrases"
METRIC = "OCC"
TITLE = "Most Frequent Title NLP Phrases"


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
