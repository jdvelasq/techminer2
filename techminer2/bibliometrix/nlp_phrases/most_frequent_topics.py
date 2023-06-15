# flake8: noqa
"""
Most Frequent Topics
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__nlp_phrases_most_frequent_topics.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.nlp_phrases.most_frequent_topics(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/bibliometrix__nlp_phrases_most_frequent_topics.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
nlp_phrases
REGULATORY_TECHNOLOGY     18
FINANCIAL_INSTITUTIONS    15
FINANCIAL_REGULATION       7
REGULATORY_COMPLIANCE      7
FINANCIAL_SECTOR           7
Name: OCC, dtype: int64


>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of the \\
'nlp_phrases' field in a scientific bibliography database. Summarize the table below, \\
sorted by the 'OCC' metric, and delimited by triple backticks, identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| nlp_phrases                  |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:-----------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGULATORY_TECHNOLOGY        |    18 |            13 |                   5 |                273 |                42 |                           15.17 |                           2.33 |                  -1.5 |                     2.5 |                   0.138889  |                     2017 |     7 |                       39    |         7 |         3 |      1    |
| FINANCIAL_INSTITUTIONS       |    15 |            11 |                   4 |                194 |                30 |                           12.93 |                           2    |                  -1.5 |                     2   |                   0.133333  |                     2018 |     6 |                       32.33 |         4 |         3 |      0.67 |
| FINANCIAL_REGULATION         |     7 |             6 |                   1 |                360 |                22 |                           51.43 |                           3.14 |                  -1   |                     0.5 |                   0.0714286 |                     2016 |     8 |                       45    |         5 |         3 |      0.62 |
| REGULATORY_COMPLIANCE        |     7 |             6 |                   1 |                198 |                40 |                           28.29 |                           5.71 |                  -0.5 |                     0.5 |                   0.0714286 |                     2018 |     6 |                       33    |         3 |         2 |      0.5  |
| FINANCIAL_SECTOR             |     7 |             5 |                   2 |                169 |                 5 |                           24.14 |                           0.71 |                  -1.5 |                     1   |                   0.142857  |                     2017 |     7 |                       24.14 |         3 |         2 |      0.43 |
| ARTIFICIAL_INTELLIGENCE      |     7 |             4 |                   3 |                 33 |                 9 |                            4.71 |                           1.29 |                  -0.5 |                     1.5 |                   0.214286  |                     2020 |     4 |                        8.25 |         3 |         2 |      0.75 |
| GLOBAL_FINANCIAL_CRISIS      |     6 |             3 |                   3 |                177 |                 5 |                           29.5  |                           0.83 |                   0.5 |                     1.5 |                   0.25      |                     2017 |     7 |                       25.29 |         3 |         2 |      0.43 |
| FINANCIAL_CRISIS             |     6 |             6 |                   0 |                 58 |                11 |                            9.67 |                           1.83 |                  -1   |                     0   |                   0         |                     2016 |     8 |                        7.25 |         4 |         2 |      0.5  |
| FINANCIAL_SERVICES_INDUSTRY  |     5 |             3 |                   2 |                315 |                21 |                           63    |                           4.2  |                   0   |                     1   |                   0.2       |                     2017 |     7 |                       45    |         3 |         3 |      0.43 |
| FINANCIAL_SYSTEM             |     5 |             4 |                   1 |                189 |                28 |                           37.8  |                           5.6  |                   0   |                     0.5 |                   0.1       |                     2017 |     7 |                       27    |         3 |         3 |      0.43 |
| INFORMATION_TECHNOLOGY       |     5 |             4 |                   1 |                177 |                10 |                           35.4  |                           2    |                  -0.5 |                     0.5 |                   0.1       |                     2017 |     7 |                       25.29 |         4 |         3 |      0.57 |
| FINANCIAL_TECHNOLOGY         |     5 |             4 |                   1 |                173 |                25 |                           34.6  |                           5    |                  -0.5 |                     0.5 |                   0.1       |                     2017 |     7 |                       24.71 |         3 |         2 |      0.43 |
| REGTECH_SOLUTIONS            |     5 |             4 |                   1 |                 18 |                 4 |                            3.6  |                           0.8  |                   0   |                     0.5 |                   0.1       |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| FINANCIAL_MARKETS            |     4 |             2 |                   2 |                151 |                 0 |                           37.75 |                           0    |                  -0.5 |                     1   |                   0.25      |                     2017 |     7 |                       21.57 |         1 |         1 |      0.14 |
| REGTECH_APPROACH             |     4 |             2 |                   2 |                 37 |                12 |                            9.25 |                           3    |                   0   |                     1   |                   0.25      |                     2018 |     6 |                        6.17 |         3 |         2 |      0.5  |
| RISK_MANAGEMENT              |     4 |             3 |                   1 |                 15 |                 8 |                            3.75 |                           2    |                   0   |                     0.5 |                   0.125     |                     2018 |     6 |                        2.5  |         2 |         2 |      0.33 |
| NEW_TECHNOLOGIES             |     4 |             3 |                   1 |                 12 |                 1 |                            3    |                           0.25 |                  -1   |                     0.5 |                   0.125     |                     2019 |     5 |                        2.4  |         2 |         1 |      0.4  |
| MACHINE_LEARNING             |     4 |             1 |                   3 |                  7 |                 4 |                            1.75 |                           1    |                  -0.5 |                     1.5 |                   0.375     |                     2021 |     3 |                        2.33 |         2 |         1 |      0.67 |
| DIGITAL_INNOVATION           |     3 |             2 |                   1 |                164 |                21 |                           54.67 |                           7    |                  -0.5 |                     0.5 |                   0.166667  |                     2018 |     6 |                       27.33 |         2 |         2 |      0.33 |
| SYSTEMATIC_LITERATURE_REVIEW |     3 |             1 |                   2 |                  4 |                 0 |                            1.33 |                           0    |                   0   |                     1   |                   0.333333  |                     2019 |     5 |                        0.8  |         1 |         1 |      0.2  |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_items
from ...vantagepoint.report import ranking_chart

FIELD = "nlp_phrases"


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
