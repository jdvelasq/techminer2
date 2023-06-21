# flake8: noqa
"""
Most Local Cited Institutions
===============================================================================



>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/examples/organizations/most_local_cited_organizations.html"

>>> import techminer2plus
>>> r = techminer2plus.examples.organizations.most_local_cited_organizations(
...     top_n=20,
...     root_dir=root_dir,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/examples/organizations/most_local_cited_organizations.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
organizations
Univ Coll Cork (IRL)                                            19
Kingston Bus Sch (GBR)                                          17
Univ of Hong Kong (HKG)                                          8
European Central B (DEU)                                         8
Harvard Univ Weatherhead ctr for International Affairs (USA)     8
Name: local_citations, dtype: int64




>>> print(r.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'organizations' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'local_citations' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| organizations                                                             |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:--------------------------------------------------------------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Univ Coll Cork (IRL)                                                      |     3 |             2 |                   1 |                 41 |                19 |                           13.67 |                           6.33 |                   0   |                     0.5 |                    0.166667 |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| Kingston Bus Sch (GBR)                                                    |     1 |             1 |                   0 |                153 |                17 |                          153    |                          17    |                   0   |                     0   |                    0        |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| Univ of Hong Kong (HKG)                                                   |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                    0        |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| European Central B (DEU)                                                  |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                    0        |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Harvard Univ Weatherhead ctr for International Affairs (USA)              |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                    0        |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| KS Strategic, London, United Kingdom (GBR)                                |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                    0        |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Panepistemio Aigaiou, Chios, Greece (GRC)                                 |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                    0        |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Sch of Eng (CHE)                                                          |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                    0        |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Heinrich-Heine-Univ (DEU)                                                 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| UNSW Sydney, Kensington, Australia (AUS)                                  |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Univ of Luxembourg (LUX)                                                  |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Univ of Zurich (CHE)                                                      |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Ahlia Univ (BHR)                                                          |     3 |             2 |                   1 |                 19 |                 5 |                            6.33 |                           1.67 |                  -0.5 |                     0.5 |                    0.166667 |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Deloitte LLP, 1 Little New Street, London, EC4A 3TR, United Kingdom (GBR) |     1 |             1 |                   0 |                  8 |                 5 |                            8    |                           5    |                   0   |                     0   |                    0        |                     2018 |     6 |                        1.33 |         1 |         1 |      0.17 |
| Coventry Univ (GBR)                                                       |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                    0.25     |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Univ of Westminster (GBR)                                                 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                    0.25     |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Mutah Univ (JOR)                                                          |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                   0   |                     0   |                    0        |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| Univ of Johannesburg (ZAF)                                                |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                    0        |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| Zayed Univ (ARE)                                                          |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                   0   |                     0   |                    0        |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| Dublin City Univ (IRL)                                                    |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""
from ...analyze import list_items
from ...visualize import ranking_chart


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def most_local_cited_organizations(
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
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most local cited organizations.

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
        field="organizations",
        metric="local_citations",
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
