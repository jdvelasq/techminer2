# flake8: noqa
"""
Author M-Index
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__author_m_index.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.author_m_index(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__author_m_index.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
| authors   |   m_index |
|:----------|----------:|
| Hamdan A  |       0.5 |
| Turki M   |       0.5 |
| Lin W     |       0.5 |
| Singh C   |       0.5 |
| Brennan R |       0.5 |



>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of the \\
'authors' field in a scientific bibliography database. Summarize the table below, \\
sorted by the 'm_index' metric, and delimited by triple backticks, identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors             |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:--------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Hamdan A            |     2 |             2 |                   0 |                 18 |                 5 |                             9   |                            2.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |       0.5 |
| Turki M             |     2 |             2 |                   0 |                 18 |                 5 |                             9   |                            2.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |       0.5 |
| Lin W               |     2 |             1 |                   1 |                 17 |                 4 |                             8.5 |                            2   |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |       0.5 |
| Singh C             |     2 |             1 |                   1 |                 17 |                 4 |                             8.5 |                            2   |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |       0.5 |
| Brennan R           |     2 |             2 |                   0 |                 14 |                 3 |                             7   |                            1.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |       0.5 |
| Crane M             |     2 |             2 |                   0 |                 14 |                 3 |                             7   |                            1.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |       0.5 |
| Ryan P              |     2 |             2 |                   0 |                 14 |                 3 |                             7   |                            1.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |       0.5 |
| Gong X              |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Muganyi T           |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Sun H-P             |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Taghizadeh-Hesary F |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Yan L               |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Yin Y               |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |       0.5 |
| Cruz Rambaud S      |     1 |             0 |                   1 |                  3 |                 0 |                             3   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |       0.5 |
| Exposito Gazquez A  |     1 |             0 |                   1 |                  3 |                 0 |                             3   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |       0.5 |
| Ye Z                |     1 |             0 |                   1 |                  3 |                 1 |                             3   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |       0.5 |
| Zhao L              |     1 |             0 |                   1 |                  3 |                 1 |                             3   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |       0.5 |
| Abdullah Y          |     1 |             0 |                   1 |                  1 |                 0 |                             1   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        0.5  |         1 |         1 |       0.5 |
| Rabbani MR          |     1 |             0 |                   1 |                  1 |                 0 |                             1   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        0.5  |         1 |         1 |       0.5 |
| Shahnawaz S         |     1 |             0 |                   1 |                  1 |                 0 |                             1   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        0.5  |         1 |         1 |       0.5 |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_items
from ...vantagepoint.report import ranking_chart


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def author_m_index(
    metric="h_index",
    root_dir="./",
    database="main",
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
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the selected impact measure by author.

    Args:
        metric (str, optional): Impact metric. Defaults to "h_index".
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

    if title is None:
        title = f"Author Impact by {metric.replace('_', ' ').title()}"

    item_list = list_items(
        field="authors",
        metric="m_index",
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
