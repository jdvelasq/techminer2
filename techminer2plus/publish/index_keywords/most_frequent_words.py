# flake8: noqa
"""
Most Frequent Words
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/index_keywords/most_frequent_words.html"

>>> import techminer2plus
>>> r = techminer2plus.publish.index_keywords.most_frequent_words(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/examples/index_keywords/most_frequent_words.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()
index_keywords
REGULATORY_COMPLIANCE     9
FINANCIAL_INSTITUTIONS    6
FINANCE                   5
REGTECH                   5
ANTI_MONEY_LAUNDERING     3
Name: OCC, dtype: int64




>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'index_keywords' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| index_keywords                  |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:--------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| REGULATORY_COMPLIANCE           |     9 |             6 |                   3 |                 34 |                11 |                            3.78 |                           1.22 |                   0   |                     1.5 |                    0.166667 |                     2017 |     7 |                        4.86 |         3 |         2 |      0.43 |
| FINANCIAL_INSTITUTIONS          |     6 |             4 |                   2 |                  9 |                 3 |                            1.5  |                           0.5  |                  -0.5 |                     1   |                    0.166667 |                     2020 |     4 |                        2.25 |         2 |         1 |      0.5  |
| FINANCE                         |     5 |             3 |                   2 |                 16 |                 5 |                            3.2  |                           1    |                  -0.5 |                     1   |                    0.2      |                     2017 |     7 |                        2.29 |         2 |         1 |      0.29 |
| REGTECH                         |     5 |             3 |                   2 |                 15 |                 5 |                            3    |                           1    |                   0   |                     1   |                    0.2      |                     2017 |     7 |                        2.14 |         2 |         1 |      0.29 |
| ANTI_MONEY_LAUNDERING           |     3 |             3 |                   0 |                 10 |                 1 |                            3.33 |                           0.33 |                  -1   |                     0   |                    0        |                     2020 |     4 |                        2.5  |         2 |         1 |      0.5  |
| FINTECH                         |     3 |             3 |                   0 |                  8 |                 2 |                            2.67 |                           0.67 |                   0   |                     0   |                    0        |                     2019 |     5 |                        1.6  |         2 |         1 |      0.4  |
| INFORMATION_SYSTEMS             |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| INFORMATION_USE                 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| SOFTWARE_SOLUTION               |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| SANDBOXES                       |     2 |             2 |                   0 |                 12 |                 3 |                            6    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2017 |     7 |                        1.71 |         1 |         1 |      0.14 |
| FINANCIAL_REGULATION            |     2 |             1 |                   1 |                 11 |                 3 |                            5.5  |                           1.5  |                   0   |                     0.5 |                    0.25     |                     2017 |     7 |                        1.57 |         1 |         1 |      0.14 |
| FINANCIAL_SERVICES_INDUSTRY     |     2 |             1 |                   1 |                 11 |                 3 |                            5.5  |                           1.5  |                   0   |                     0.5 |                    0.25     |                     2017 |     7 |                        1.57 |         1 |         1 |      0.14 |
| LAUNDERING                      |     2 |             2 |                   0 |                  9 |                 1 |                            4.5  |                           0.5  |                  -1   |                     0   |                    0        |                     2021 |     3 |                        3    |         2 |         1 |      0.67 |
| BANKING                         |     2 |             2 |                   0 |                  8 |                 1 |                            4    |                           0.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        2    |         1 |         1 |      0.25 |
| FINANCIAL_CRISIS                |     2 |             1 |                   1 |                  7 |                 1 |                            3.5  |                           0.5  |                   0   |                     0.5 |                    0.25     |                     2021 |     3 |                        2.33 |         1 |         1 |      0.33 |
| RISK_MANAGEMENT                 |     2 |             2 |                   0 |                  5 |                 0 |                            2.5  |                           0    |                   0   |                     0   |                    0        |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| COMMERCE                        |     2 |             2 |                   0 |                  4 |                 2 |                            2    |                           1    |                   0   |                     0   |                    0        |                     2019 |     5 |                        0.8  |         1 |         1 |      0.2  |
| CLASSIFICATION (OF_INFORMATION) |     2 |             1 |                   1 |                  3 |                 1 |                            1.5  |                           0.5  |                  -0.5 |                     0.5 |                    0.25     |                     2021 |     3 |                        1    |         1 |         1 |      0.33 |
| ARTIFICIAL_INTELLIGENCE         |     2 |             1 |                   1 |                  2 |                 0 |                            1    |                           0    |                  -0.5 |                     0.5 |                    0.25     |                     2021 |     3 |                        0.67 |         1 |         1 |      0.33 |
| BLOCKCHAIN                      |     2 |             2 |                   0 |                  2 |                 0 |                            1    |                           0    |                  -0.5 |                     0   |                    0        |                     2017 |     7 |                        0.29 |         1 |         1 |      0.14 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...analyze import list_items
from ...report import ranking_chart

FIELD = "index_keywords"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def most_frequent_words(
    root_dir="./",
    database="main",
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
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the number of documents by country using the specified plot.

    Args:
        field (str): field name. Options {'author_keywords', 'index_keywords', 'abstract_words', 'title_words'}
        root_dir (str): path to the database directory.
        database (str): name of the database.
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
