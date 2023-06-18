# flake8: noqa
"""
Most Frequent Topics
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__title_nlp_phrases_most_frequent_topics.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.title_nlp_phrases.most_frequent_topics(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__title_nlp_phrases_most_frequent_topics.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
title_nlp_phrases
REGULATORY_TECHNOLOGY      3
ARTIFICIAL_INTELLIGENCE    3
FINANCIAL_REGULATION       2
FINANCIAL_CRIME            2
EUROPEAN_UNION             1
Name: OCC, dtype: int64



>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of the \\
'title_nlp_phrases' field in a scientific bibliography database. Summarize the table below, \\
sorted by the 'OCC' metric, and delimited by triple backticks, identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| title_nlp_phrases                    |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:-------------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGULATORY_TECHNOLOGY                |     3 |             3 |                   0 |                 20 |                 8 |                            6.67 |                           2.67 |                  -1   |                     0   |                    0        |                     2020 |     4 |                        5    |         2 |         2 |      0.5  |
| ARTIFICIAL_INTELLIGENCE              |     3 |             2 |                   1 |                 17 |                 3 |                            5.67 |                           1    |                  -0.5 |                     0.5 |                    0.166667 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| FINANCIAL_REGULATION                 |     2 |             2 |                   0 |                180 |                 0 |                           90    |                           0    |                   0   |                     0   |                    0        |                     2016 |     8 |                       22.5  |         2 |         2 |      0.25 |
| FINANCIAL_CRIME                      |     2 |             2 |                   0 |                 12 |                 3 |                            6    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3    |         2 |         1 |      0.5  |
| EUROPEAN_UNION                       |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| FINANCIAL_RISK                       |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                    0        |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| EFFECTIVE_SOLUTIONS                  |     1 |             1 |                   0 |                 14 |                 3 |                           14    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        3.5  |         1 |         1 |      0.25 |
| FINANCIAL_DEVELOPMENT                |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| BANK_TREASURY                        |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| DIGITAL_TRANSFORMATION               |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| REGULATORY_TECHNOLOGY_REGTECH        |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                   0   |                     0   |                    0        |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| FINANCIAL_SYSTEM                     |     1 |             1 |                   0 |                 11 |                 3 |                           11    |                           3    |                   0   |                     0   |                    0        |                     2017 |     7 |                        1.57 |         1 |         1 |      0.14 |
| AML_COMPLIANCE                       |     1 |             1 |                   0 |                 10 |                 3 |                           10    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        2.5  |         1 |         1 |      0.25 |
| REGTECH_SOLUTIONS                    |     1 |             1 |                   0 |                 10 |                 3 |                           10    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        2.5  |         1 |         1 |      0.25 |
| MODERN_INFORMATION_TECHNOLOGY        |     1 |             1 |                   0 |                  5 |                 3 |                            5    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| REGULATORY_AFFAIRS                   |     1 |             1 |                   0 |                  5 |                 3 |                            5    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| SMART_REGULATION                     |     1 |             1 |                   0 |                  4 |                 3 |                            4    |                           3    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| FINANCIAL_STABILITY                  |     1 |             1 |                   0 |                  4 |                 0 |                            4    |                           0    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| TRADITIONAL_FINANCIAL_INTERMEDIATION |     1 |             1 |                   0 |                  4 |                 0 |                            4    |                           0    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| CHARITABLE_ORGANISATIONS             |     1 |             0 |                   1 |                  3 |                 1 |                            3    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
# from ...vantagepoint.analyze import list_items
# from ...vantagepoint.charts import ranking_chart

FIELD = "title_nlp_phrases"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def most_frequent_topics(
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    metric_label=None,
    field_label=None,
    title=None,
    # Item filters:
    top_n=20,
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
    """Plots the number of documents by country using the specified plot.

    Args:
        textfont_size (int, optional): Font size. Defaults to 10.
        marker_size (int, optional): Marker size. Defaults to 6.
        line_color (str, optional): Line color. Defaults to "black".
        line_width (int, optional): Line width. Defaults to 1.
        yshift (int, optional): Y shift. Defaults to 4.
        metric_label (str): metric label.
        field_label (str): field label.
        title (str): plot title.

        top_n (int): number of items to be plotted.
        occ_range (tuple): range of occurrences.
        gc_range (tuple): range of global citations.
        custom_items (list): list of items to be plotted.

        root_dir (str): path to the database directory.
        database (str): name of the database.
        year_filter (tuple): range of years.
        cited_by_filter (tuple): range of citations.
        **filters (dict, optional): Filters to be applied to the database. Defaults to {}.

    Returns:
        BasicChart: A basic chart object.

    # pylint: disable=line-too-long
    """

    item_list = list_items(
        field=FIELD,
        metric="OCC",
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return ranking_chart(
        obj=item_list,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )
