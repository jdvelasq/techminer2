# flake8: noqa
"""Most Global Cited Authors
===============================================================================




>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/most_global_cited_authors.html"

>>> import techminer2plus
>>> r = techminer2plus.examples.authors.most_global_cited_authors(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/most_global_cited_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
authors
Arner DW             185
Buckley RP           185
Barberis JN          161
Anagnostopoulos I    153
Butler T              41
Name: global_citations, dtype: int64


>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'global_citations' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors           |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Arner DW          |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                        0    |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Buckley RP        |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                        0    |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Barberis JN       |     2 |             2 |                   0 |                161 |                 3 |                           80.5  |                           1.5  |                   0   |                     0   |                        0    |                     2017 |     7 |                       23    |         2 |         2 |      0.29 |
| Anagnostopoulos I |     1 |             1 |                   0 |                153 |                17 |                          153    |                          17    |                   0   |                     0   |                        0    |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| Butler T          |     2 |             2 |                   0 |                 41 |                19 |                           20.5  |                           9.5  |                   0   |                     0   |                        0    |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| OBrien L          |     1 |             1 |                   0 |                 33 |                14 |                           33    |                          14    |                   0   |                     0   |                        0    |                     2019 |     5 |                        6.6  |         1 |         1 |      0.2  |
| Baxter LG         |     1 |             1 |                   0 |                 30 |                 0 |                           30    |                           0    |                   0   |                     0   |                        0    |                     2016 |     8 |                        3.75 |         1 |         1 |      0.12 |
| Weber RH          |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                        0    |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Zetzsche DA       |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                        0    |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Breymann W        |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                        0    |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Gross FJ          |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                        0    |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Kavassalis P      |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                        0    |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Saxton K          |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                        0    |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Stieber H         |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                        0    |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Hamdan A          |     2 |             2 |                   0 |                 18 |                 5 |                            9    |                           2.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| Turki M           |     2 |             2 |                   0 |                 18 |                 5 |                            9    |                           2.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| Lin W             |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Singh C           |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Brennan R         |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Crane M           |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""
from ...analyze import list_items
from ...report import ranking_chart


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def most_global_cited_authors(
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
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database options:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most global cited authors.

    Args:
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
        title = "Most Global Cited Authors"

    item_list = list_items(
        field="authors",
        metric="global_citations",
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
