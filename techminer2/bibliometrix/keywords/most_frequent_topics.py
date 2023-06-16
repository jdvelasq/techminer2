# flake8: noqa
"""
Most Frequent Topics
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__keywords_most_frequent_topics.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.keywords.most_frequent_topics(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__keywords_most_frequent_topics.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
keywords
REGTECH                  28
FINTECH                  12
REGULATORY_COMPLIANCE     9
COMPLIANCE                7
FINANCE                   7
Name: OCC, dtype: int64


>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of the \\
'keywords' field in a scientific bibliography database. Summarize the table below, \\
sorted by the 'OCC' metric, and delimited by triple backticks, identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| keywords                        |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:--------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGTECH                         |    28 |            20 |                   8 |                329 |                74 |                           11.75 |                           2.64 |                  -0.5 |                     4   |                   0.142857  |                     2017 |     7 |                       47    |         9 |         4 |      1.29 |
| FINTECH                         |    12 |            10 |                   2 |                249 |                49 |                           20.75 |                           4.08 |                  -0.5 |                     1   |                   0.0833333 |                     2018 |     6 |                       41.5  |         5 |         3 |      0.83 |
| REGULATORY_COMPLIANCE           |     9 |             6 |                   3 |                 34 |                11 |                            3.78 |                           1.22 |                   0   |                     1.5 |                   0.166667  |                     2017 |     7 |                        4.86 |         3 |         2 |      0.43 |
| COMPLIANCE                      |     7 |             5 |                   2 |                 30 |                 9 |                            4.29 |                           1.29 |                   0   |                     1   |                   0.142857  |                     2019 |     5 |                        6    |         3 |         2 |      0.6  |
| FINANCE                         |     7 |             4 |                   3 |                 17 |                 5 |                            2.43 |                           0.71 |                  -0.5 |                     1.5 |                   0.214286  |                     2017 |     7 |                        2.43 |         2 |         1 |      0.29 |
| ARTIFICIAL_INTELLIGENCE         |     6 |             4 |                   2 |                 25 |                 6 |                            4.17 |                           1    |                  -0.5 |                     1   |                   0.166667  |                     2019 |     5 |                        5    |         3 |         2 |      0.6  |
| REGULATION                      |     5 |             4 |                   1 |                164 |                22 |                           32.8  |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| FINANCIAL_REGULATION            |     5 |             2 |                   3 |                 35 |                 8 |                            7    |                           1.6  |                   0   |                     1.5 |                   0.3       |                     2017 |     7 |                        5    |         2 |         2 |      0.29 |
| ANTI_MONEY_LAUNDERING           |     5 |             5 |                   0 |                 24 |                 4 |                            4.8  |                           0.8  |                  -1.5 |                     0   |                   0         |                     2020 |     4 |                        6    |         2 |         2 |      0.5  |
| RISK_MANAGEMENT                 |     5 |             4 |                   1 |                 19 |                 8 |                            3.8  |                           1.6  |                   0   |                     0.5 |                   0.1       |                     2018 |     6 |                        3.17 |         3 |         2 |      0.5  |
| REGULATORY_TECHNOLOGY           |     5 |             2 |                   3 |                  8 |                 5 |                            1.6  |                           1    |                   0   |                     1.5 |                   0.3       |                     2020 |     4 |                        2    |         1 |         1 |      0.25 |
| FINANCIAL_INSTITUTION           |     5 |             3 |                   2 |                  7 |                 3 |                            1.4  |                           0.6  |                   0   |                     1   |                   0.2       |                     2020 |     4 |                        1.75 |         2 |         1 |      0.5  |
| FINANCIAL_SERVICES              |     4 |             3 |                   1 |                168 |                20 |                           42    |                           5    |                   0   |                     0.5 |                   0.125     |                     2017 |     7 |                       24    |         3 |         2 |      0.43 |
| REGULATORY_TECHNOLOGY (REGTECH) |     4 |             3 |                   1 |                 30 |                10 |                            7.5  |                           2.5  |                  -1   |                     0.5 |                   0.125     |                     2020 |     4 |                        7.5  |         3 |         2 |      0.75 |
| INNOVATION                      |     3 |             2 |                   1 |                 12 |                 4 |                            4    |                           1.33 |                  -0.5 |                     0.5 |                   0.166667  |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| BLOCKCHAIN                      |     3 |             3 |                   0 |                  5 |                 0 |                            1.67 |                           0    |                  -0.5 |                     0   |                   0         |                     2017 |     7 |                        0.71 |         1 |         1 |      0.14 |
| SUPTECH                         |     3 |             1 |                   2 |                  4 |                 2 |                            1.33 |                           0.67 |                   0   |                     1   |                   0.333333  |                     2019 |     5 |                        0.8  |         1 |         1 |      0.2  |
| DATA_PROTECTION                 |     2 |             1 |                   1 |                 27 |                 5 |                           13.5  |                           2.5  |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        6.75 |         2 |         1 |      0.5  |
| SMART_CONTRACTS                 |     2 |             2 |                   0 |                 22 |                 8 |                           11    |                           4    |                   0   |                     0   |                   0         |                     2017 |     7 |                        3.14 |         1 |         1 |      0.14 |
| CHARITYTECH                     |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                   0.25      |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_items
from ...vantagepoint.report import ranking_chart

FIELD = "keywords"


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
