# flake8: noqa
"""
Organization M-Index
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/report/organizations/organization_m_index.html"

>>> import techminer2plus
>>> r = techminer2plus.report.organizations.organization_m_index(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/report/organizations/organization_m_index.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> print(r.table_.head().to_markdown())
| organizations               |   m_index |
|:----------------------------|----------:|
| Ahlia Univ (BHR)            |       0.5 |
| Coventry Univ (GBR)         |       0.5 |
| Univ of Westminster (GBR)   |       0.5 |
| Dublin City Univ (IRL)      |       0.5 |
| Hebei Univ of Technol (CHN) |       0.5 |



>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'organizations' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'm_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| organizations                                 |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:----------------------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Ahlia Univ (BHR)                              |     3 |             2 |                   1 |                 19 |                 5 |                            6.33 |                           1.67 |                  -0.5 |                     0.5 |                    0.166667 |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Coventry Univ (GBR)                           |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                    0.25     |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Univ of Westminster (GBR)                     |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                    0.25     |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Dublin City Univ (IRL)                        |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Hebei Univ of Technol (CHN)                   |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Jiangsu Univ (CHN)                            |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Shanghai Univ (CHN)                           |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Tokai Univ (JPN)                              |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Tongji Univ (CHN)                             |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| 3PB, London, United Kingdom (GBR)             |     1 |             0 |                   1 |                  3 |                 1 |                            3    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
| Univ de Almeria (ESP)                         |     1 |             0 |                   1 |                  3 |                 0 |                            3    |                           0    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
| Univ of Chinese Acad of Social Sciences (CHN) |     1 |             0 |                   1 |                  3 |                 1 |                            3    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
| Goethe Univ Frankfurt (DEU)                   |     1 |             0 |                   1 |                  1 |                 1 |                            1    |                           1    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| Univ Coll of Bahrain (BHR)                    |     1 |             0 |                   1 |                  1 |                 0 |                            1    |                           0    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| Univ of Bahrain (BHR)                         |     1 |             0 |                   1 |                  1 |                 0 |                            1    |                           0    |                   0   |                     0.5 |                    0.5      |                     2022 |     2 |                        0.5  |         1 |         1 |      0.5  |
| Univ of Hong Kong (HKG)                       |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                    0        |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Univ Coll Cork (IRL)                          |     3 |             2 |                   1 |                 41 |                19 |                           13.67 |                           6.33 |                   0   |                     0.5 |                    0.166667 |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| Univ of Johannesburg (ZAF)                    |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| Conventional Wholesale B (BHR)                |     1 |             1 |                   0 |                  7 |                 1 |                            7    |                           1    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        2.33 |         1 |         1 |      0.33 |
| Sch of Taxation and Bus Law (AUS)             |     1 |             1 |                   0 |                  3 |                 3 |                            3    |                           3    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        1    |         1 |         1 |      0.33 |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
from ...analyze import list_items
from ...visualize import ranking_chart


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def organization_m_index(
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
    # Database filters:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Plots the selected impact measure by organizations.


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
        title = "Organization Impact by M-Index"

    item_list = list_items(
        field="organizations",
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
