# flake8: noqa
"""
Country Scientific Production
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_scientific_production.html"


>>> from techminer2 import bibliometrix
>>> chart = bibliometrix.countries.country_scientific_production(
...     root_dir=root_dir
... )
>>> chart.plot_.write_html(file_name)
 
.. raw:: html

    <iframe src="../../../_static/bibliometrix__country_scientific_production.html" height="410px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head()
countries
United Kingdom    7
Australia         7
United States     6
Ireland           5
China             5
Name: OCC, dtype: int64


>>> print(chart.prompt_)
Your task is to generate an analysis about the bibliometric indicators of the \\
'countries' field in a scientific bibliography database. Summarize the table below, \\
sorted by the 'OCC' metric, and delimited by triple backticks, identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries            |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:---------------------|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| United Kingdom       |     7 |             6 |                   1 |                199 |                34 |                           28.43 |                           4.86 |                   0   |                     0.5 |                   0.0714286 |                     2018 |     6 |                       33.17 |         4 |         3 |      0.67 |
| Australia            |     7 |             7 |                   0 |                199 |                15 |                           28.43 |                           2.14 |                  -1   |                     0   |                   0         |                     2017 |     7 |                       28.43 |         4 |         3 |      0.57 |
| United States        |     6 |             4 |                   2 |                 59 |                11 |                            9.83 |                           1.83 |                   0.5 |                     1   |                   0.166667  |                     2016 |     8 |                        7.38 |         3 |         2 |      0.38 |
| Ireland              |     5 |             4 |                   1 |                 55 |                22 |                           11    |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                        9.17 |         3 |         2 |      0.5  |
| China                |     5 |             1 |                   4 |                 27 |                 5 |                            5.4  |                           1    |                   0.5 |                     2   |                   0.4       |                     2017 |     7 |                        3.86 |         3 |         2 |      0.43 |
| Italy                |     5 |             3 |                   2 |                  5 |                 2 |                            1    |                           0.4  |                   0   |                     1   |                   0.2       |                     2019 |     5 |                        1    |         1 |         1 |      0.2  |
| Germany              |     4 |             3 |                   1 |                 51 |                17 |                           12.75 |                           4.25 |                   0   |                     0.5 |                   0.125     |                     2018 |     6 |                        8.5  |         3 |         2 |      0.5  |
| Switzerland          |     4 |             3 |                   1 |                 45 |                13 |                           11.25 |                           3.25 |                   0.5 |                     0.5 |                   0.125     |                     2017 |     7 |                        6.43 |         2 |         2 |      0.29 |
| Bahrain              |     4 |             3 |                   1 |                 19 |                 5 |                            4.75 |                           1.25 |                  -1   |                     0.5 |                   0.125     |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Hong Kong            |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                   0         |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Luxembourg           |     2 |             2 |                   0 |                 34 |                 8 |                           17    |                           4    |                   0   |                     0   |                   0         |                     2020 |     4 |                        8.5  |         2 |         2 |      0.5  |
| United Arab Emirates |     2 |             2 |                   0 |                 13 |                 7 |                            6.5  |                           3.5  |                   0   |                     0   |                   0         |                     2020 |     4 |                        3.25 |         2 |         1 |      0.5  |
| Spain                |     2 |             1 |                   1 |                  4 |                 0 |                            2    |                           0    |                  -0.5 |                     0.5 |                   0.25      |                     2021 |     3 |                        1.33 |         1 |         1 |      0.33 |
| Indonesia            |     2 |             0 |                   2 |                  0 |                 0 |                            0    |                           0    |                   0   |                     1   |                   0.5       |                     2022 |     2 |                        0    |         0 |         0 |      0    |
| Greece               |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                   0         |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Japan                |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                   0.5       |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Jordan               |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                   0   |                     0   |                   0         |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| South Africa         |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                   0         |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| Ukraine              |     1 |             1 |                   0 |                  4 |                 0 |                            4    |                           0    |                   0   |                     0   |                   0         |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| Malaysia             |     1 |             1 |                   0 |                  3 |                 0 |                            3    |                           0    |                   0   |                     0   |                   0         |                     2019 |     5 |                        0.6  |         1 |         1 |      0.2  |
| India                |     1 |             1 |                   0 |                  1 |                 1 |                            1    |                           1    |                   0   |                     0   |                   0         |                     2020 |     4 |                        0.25 |         1 |         1 |      0.25 |
| Palestine            |     1 |             1 |                   0 |                  1 |                 1 |                            1    |                           1    |                  -0.5 |                     0   |                   0         |                     2021 |     3 |                        0.33 |         1 |         1 |      0.33 |
| Taiwan               |     1 |             1 |                   0 |                  1 |                 0 |                            1    |                           0    |                   0   |                     0   |                   0         |                     2017 |     7 |                        0.14 |         1 |         1 |      0.14 |
| Belgium              |     1 |             1 |                   0 |                  0 |                 0 |                            0    |                           0    |                  -0.5 |                     0   |                   0         |                     2021 |     3 |                        0    |         0 |         0 |      0    |
| France               |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0   |                     0.5 |                   0.5       |                     2022 |     2 |                        0    |         0 |         0 |      0    |
| Netherlands          |     1 |             0 |                   1 |                  0 |                 0 |                            0    |                           0    |                   0   |                     0.5 |                   0.5       |                     2022 |     2 |                        0    |         0 |         0 |      0    |
| Poland               |     1 |             1 |                   0 |                  0 |                 0 |                            0    |                           0    |                   0   |                     0   |                   0         |                     2020 |     4 |                        0    |         0 |         0 |      0    |
| Romania              |     1 |             1 |                   0 |                  0 |                 0 |                            0    |                           0    |                   0   |                     0   |                   0         |                     2020 |     4 |                        0    |         0 |         0 |      0    |
| Singapore            |     1 |             1 |                   0 |                  0 |                 0 |                            0    |                           0    |                  -0.5 |                     0   |                   0         |                     2021 |     3 |                        0    |         0 |         0 |      0    |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_items
from ...vantagepoint.report import world_map


# pylint: disable=too-many-arguments
def country_scientific_production(
    root_dir="./",
    # Chart options:
    colormap="Blues",
    title=None,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    database="main",
    metric="OCC",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Worldmap plot

    Args:


    Returns:
        BasicChart: A basic chart object.
    """

    obj = list_items(
        field="countries",
        metric=metric,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database params:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if title is None:
        title = "Country scientific production"

    return world_map(
        obj,
        title=title,
        colormap=colormap,
    )
