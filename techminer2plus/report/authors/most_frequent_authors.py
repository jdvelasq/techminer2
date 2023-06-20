# flake8: noqa
"""
Most Frequent Authors
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_authors.html"

>>> import techminer2plus
>>> r = techminer2plus.report.authors.most_frequent_authors(
...     root_dir=root_dir,
...     top_n=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_frequent_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
authors
Arner DW       3
Buckley RP     3
Barberis JN    2
Butler T       2
Hamdan A       2
Name: OCC, dtype: int64


>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of the \\
'authors' field in a scientific bibliography database. Summarize the table below, \\
sorted by the 'OCC' metric, and delimited by triple backticks, identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors           |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Arner DW          |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                        0    |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Buckley RP        |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                        0    |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Barberis JN       |     2 |             2 |                   0 |                161 |                 3 |                           80.5  |                           1.5  |                   0   |                     0   |                        0    |                     2017 |     7 |                       23    |         2 |         2 |      0.29 |
| Butler T          |     2 |             2 |                   0 |                 41 |                19 |                           20.5  |                           9.5  |                   0   |                     0   |                        0    |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| Hamdan A          |     2 |             2 |                   0 |                 18 |                 5 |                            9    |                           2.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| Turki M           |     2 |             2 |                   0 |                 18 |                 5 |                            9    |                           2.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| Lin W             |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Singh C           |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Brennan R         |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Crane M           |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Ryan P            |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Sarea A           |     2 |             1 |                   1 |                 12 |                 4 |                            6    |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| Grassi L          |     2 |             1 |                   1 |                  2 |                 0 |                            1    |                           0    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        0.5  |         1 |         1 |      0.25 |
| Lanfranchi D      |     2 |             1 |                   1 |                  2 |                 0 |                            1    |                           0    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        0.5  |         1 |         1 |      0.25 |
| Arman AA          |     2 |             0 |                   2 |                  0 |                 0 |                            0    |                           0    |                   0   |                     1   |                        0.5  |                     2022 |     2 |                        0    |         0 |         0 |      0    |
| Anagnostopoulos I |     1 |             1 |                   0 |                153 |                17 |                          153    |                          17    |                   0   |                     0   |                        0    |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| OBrien L          |     1 |             1 |                   0 |                 33 |                14 |                           33    |                          14    |                   0   |                     0   |                        0    |                     2019 |     5 |                        6.6  |         1 |         1 |      0.2  |
| Baxter LG         |     1 |             1 |                   0 |                 30 |                 0 |                           30    |                           0    |                   0   |                     0   |                        0    |                     2016 |     8 |                        3.75 |         1 |         1 |      0.12 |
| Weber RH          |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                        0    |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Zetzsche DA       |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                        0    |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
```
<BLANKLINE>






# pylint: disable=line-too-long
"""
# from ...vantagepoint.analyze import list_items
# from ...vantagepoint.charts import ranking_chart


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def most_frequent_authors(
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
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the number of documents by author.

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

    item_list = list_items(
        field="authors",
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
