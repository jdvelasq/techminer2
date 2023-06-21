# flake8: noqa
"""
Country G-Index
===============================================================================




>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/countries/country_g_index.html"


>>> import techminer2plus
>>> r = techminer2plus.examples.countries.country_g_index(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/countries/country_g_index.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
| countries      |   g_index |
|:---------------|----------:|
| Australia      |         3 |
| United Kingdom |         3 |
| Hong Kong      |         3 |
| United States  |         2 |
| Ireland        |         2 |


>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'g_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries            |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:---------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Australia            |     7 |             7 |                   0 |                199 |                15 |                           28.43 |                           2.14 |                  -1   |                     0   |                   0         |                     2017 |     7 |                       28.43 |         4 |         3 |      0.57 |
| United Kingdom       |     7 |             6 |                   1 |                199 |                34 |                           28.43 |                           4.86 |                   0   |                     0.5 |                   0.0714286 |                     2018 |     6 |                       33.17 |         4 |         3 |      0.67 |
| Hong Kong            |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                   0         |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| United States        |     6 |             4 |                   2 |                 59 |                11 |                            9.83 |                           1.83 |                   0.5 |                     1   |                   0.166667  |                     2016 |     8 |                        7.38 |         3 |         2 |      0.38 |
| Ireland              |     5 |             4 |                   1 |                 55 |                22 |                           11    |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                        9.17 |         3 |         2 |      0.5  |
| Germany              |     4 |             3 |                   1 |                 51 |                17 |                           12.75 |                           4.25 |                   0   |                     0.5 |                   0.125     |                     2018 |     6 |                        8.5  |         3 |         2 |      0.5  |
| Switzerland          |     4 |             3 |                   1 |                 45 |                13 |                           11.25 |                           3.25 |                   0.5 |                     0.5 |                   0.125     |                     2017 |     7 |                        6.43 |         2 |         2 |      0.29 |
| Luxembourg           |     2 |             2 |                   0 |                 34 |                 8 |                           17    |                           4    |                   0   |                     0   |                   0         |                     2020 |     4 |                        8.5  |         2 |         2 |      0.5  |
| China                |     5 |             1 |                   4 |                 27 |                 5 |                            5.4  |                           1    |                   0.5 |                     2   |                   0.4       |                     2017 |     7 |                        3.86 |         3 |         2 |      0.43 |
| Bahrain              |     4 |             3 |                   1 |                 19 |                 5 |                            4.75 |                           1.25 |                  -1   |                     0.5 |                   0.125     |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Greece               |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                   0         |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| United Arab Emirates |     2 |             2 |                   0 |                 13 |                 7 |                            6.5  |                           3.5  |                   0   |                     0   |                   0         |                     2020 |     4 |                        3.25 |         2 |         1 |      0.5  |
| Japan                |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                   0.5       |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Jordan               |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                   0   |                     0   |                   0         |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| South Africa         |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                   0         |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| Italy                |     5 |             3 |                   2 |                  5 |                 2 |                            1    |                           0.4  |                   0   |                     1   |                   0.2       |                     2019 |     5 |                        1    |         1 |         1 |      0.2  |
| Spain                |     2 |             1 |                   1 |                  4 |                 0 |                            2    |                           0    |                  -0.5 |                     0.5 |                   0.25      |                     2021 |     3 |                        1.33 |         1 |         1 |      0.33 |
| Ukraine              |     1 |             1 |                   0 |                  4 |                 0 |                            4    |                           0    |                   0   |                     0   |                   0         |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| Malaysia             |     1 |             1 |                   0 |                  3 |                 0 |                            3    |                           0    |                   0   |                     0   |                   0         |                     2019 |     5 |                        0.6  |         1 |         1 |      0.2  |
| India                |     1 |             1 |                   0 |                  1 |                 1 |                            1    |                           1    |                   0   |                     0   |                   0         |                     2020 |     4 |                        0.25 |         1 |         1 |      0.25 |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
from ...analyze import list_items
from ...visualize import ranking_chart


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def country_g_index(
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    title=None,
    metric_label=None,
    field_label=None,
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
    """Plots the selected impact measure by country.


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

    if title is None:
        title = "Country Impact by G-Index"

    item_list = list_items(
        field="countries",
        metric="g_index",
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
