# flake8: noqa
"""
Most Frequent Topics
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__key_concepts_most_frequent_topics.html"

>>> import techminer2plus
>>> r = techminer2plus.report.key_concepts.most_frequent_topics(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__key_concepts_most_frequent_topics.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
key_concepts
REGTECH                   28
REGULATORY_TECHNOLOGY     20
REGULATORY_COMPLIANCE     15
FINANCIAL_INSTITUTIONS    15
FINANCIAL_REGULATION      12
Name: OCC, dtype: int64


>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of the \\
'key_concepts' field in a scientific bibliography database. Summarize the table below, \\
sorted by the 'OCC' metric, and delimited by triple backticks, identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| key_concepts                |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:----------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                     |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| REGULATORY_TECHNOLOGY       |    20 |            14 |                   6 |                274 |                43 |                           13.7  |                           2.15 |                  -1.5 |                     3   |                   0.15      |                     2017 |     7 |                       39.14 |         7 |         3 |      1    |
| REGULATORY_COMPLIANCE       |    15 |            12 |                   3 |                232 |                51 |                           15.47 |                           3.4  |                  -0.5 |                     1.5 |                   0.1       |                     2017 |     7 |                       33.14 |         5 |         3 |      0.71 |
| FINANCIAL_INSTITUTIONS      |    15 |            11 |                   4 |                194 |                30 |                           12.93 |                           2    |                  -1.5 |                     2   |                   0.133333  |                     2018 |     6 |                       32.33 |         4 |         3 |      0.67 |
| FINANCIAL_REGULATION        |    12 |             8 |                   4 |                395 |                30 |                           32.92 |                           2.5  |                  -1   |                     2   |                   0.166667  |                     2016 |     8 |                       49.38 |         7 |         4 |      0.88 |
| FINTECH                     |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| ARTIFICIAL_INTELLIGENCE     |     8 |             5 |                   3 |                 36 |                 9 |                            4.5  |                           1.12 |                  -0.5 |                     1.5 |                   0.1875    |                     2019 |     5 |                        7.2  |         3 |         2 |      0.6  |
| FINANCIAL_SECTOR            |     7 |             5 |                   2 |                169 |                 5 |                           24.14 |                           0.71 |                  -1.5 |                     1   |                   0.142857  |                     2017 |     7 |                       24.14 |         3 |         2 |      0.43 |
| FINANCIAL_CRISIS            |     7 |             6 |                   1 |                 58 |                11 |                            8.29 |                           1.57 |                  -0.5 |                     0.5 |                   0.0714286 |                     2016 |     8 |                        7.25 |         4 |         2 |      0.5  |
| COMPLIANCE                  |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| FINANCE                     |     7 |             4 |                   3 |                 17 |                 5 |                            2.43 |                           0.71 |                  -0.5 |                     1.5 |                   0.214286  |                     2017 |     7 |                        2.43 |         2 |         1 |      0.29 |
| FINANCIAL_SERVICES          |     6 |             5 |                   1 |                195 |                28 |                           32.5  |                           4.67 |                  -0.5 |                     0.5 |                   0.0833333 |                     2017 |     7 |                       27.86 |         4 |         3 |      0.57 |
| INFORMATION_TECHNOLOGY      |     6 |             4 |                   2 |                177 |                10 |                           29.5  |                           1.67 |                   0   |                     1   |                   0.166667  |                     2017 |     7 |                       25.29 |         4 |         3 |      0.57 |
| GLOBAL_FINANCIAL_CRISIS     |     6 |             3 |                   3 |                177 |                 5 |                           29.5  |                           0.83 |                   0.5 |                     1.5 |                   0.25      |                     2017 |     7 |                       25.29 |         3 |         2 |      0.43 |
| FINANCIAL_TECHNOLOGY        |     6 |             5 |                   1 |                173 |                25 |                           28.83 |                           4.17 |                  -0.5 |                     0.5 |                   0.0833333 |                     2017 |     7 |                       24.71 |         3 |         2 |      0.43 |
| FINANCIAL_SERVICES_INDUSTRY |     5 |             3 |                   2 |                315 |                21 |                           63    |                           4.2  |                   0   |                     1   |                   0.2       |                     2017 |     7 |                       45    |         3 |         3 |      0.43 |
| FINANCIAL_SYSTEM            |     5 |             4 |                   1 |                189 |                28 |                           37.8  |                           5.6  |                   0   |                     0.5 |                   0.1       |                     2017 |     7 |                       27    |         3 |         3 |      0.43 |
| REGULATION                  |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| ANTI_MONEY_LAUNDERING       |     5 |             5 |                   0 |                 24 |                 4 |                            4.8  |                           0.8  |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        6    |         2 |         2 |      0.5  |
| RISK_MANAGEMENT             |     5 |             4 |                   1 |                 19 |                 8 |                            3.8  |                           1.6  |                   0   |                     0.5 |                   0.1       |                     2018 |     6 |                        3.17 |         3 |         2 |      0.5  |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
# from ...vantagepoint.analyze import list_items
# from ...vantagepoint.charts import ranking_chart

FIELD = "key_concepts"


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
