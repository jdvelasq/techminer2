# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _most_relevant_countries_table:

Most Relevant Countries Table
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p
>>> print(tm2p.most_relevant_countries_table(
...    top_n=20,
...    root_dir=root_dir,
... ).to_markdown())
| countries            |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:---------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| United Kingdom       |          1 |         1 |     7 |             6 |                   1 |                199 |                34 |                           28.43 |                           4.86 |                   0   |                     0.5 |                   0.0714286 |                     2018 |     6 |                       33.17 |         4 |         3 |      0.67 |
| Australia            |          2 |         2 |     7 |             7 |                   0 |                199 |                15 |                           28.43 |                           2.14 |                  -1   |                     0   |                   0         |                     2017 |     7 |                       28.43 |         4 |         3 |      0.57 |
| United States        |          3 |         4 |     6 |             4 |                   2 |                 59 |                11 |                            9.83 |                           1.83 |                   0.5 |                     1   |                   0.166667  |                     2016 |     8 |                        7.38 |         3 |         2 |      0.38 |
| Ireland              |          4 |         5 |     5 |             4 |                   1 |                 55 |                22 |                           11    |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                        9.17 |         3 |         2 |      0.5  |
| China                |          5 |         9 |     5 |             1 |                   4 |                 27 |                 5 |                            5.4  |                           1    |                   0.5 |                     2   |                   0.4       |                     2017 |     7 |                        3.86 |         3 |         2 |      0.43 |
| Italy                |          6 |        16 |     5 |             3 |                   2 |                  5 |                 2 |                            1    |                           0.4  |                   0   |                     1   |                   0.2       |                     2019 |     5 |                        1    |         1 |         1 |      0.2  |
| Germany              |          7 |         6 |     4 |             3 |                   1 |                 51 |                17 |                           12.75 |                           4.25 |                   0   |                     0.5 |                   0.125     |                     2018 |     6 |                        8.5  |         3 |         2 |      0.5  |
| Switzerland          |          8 |         7 |     4 |             3 |                   1 |                 45 |                13 |                           11.25 |                           3.25 |                   0.5 |                     0.5 |                   0.125     |                     2017 |     7 |                        6.43 |         2 |         2 |      0.29 |
| Bahrain              |          9 |        11 |     4 |             3 |                   1 |                 19 |                 5 |                            4.75 |                           1.25 |                  -1   |                     0.5 |                   0.125     |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Hong Kong            |         10 |         3 |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                   0         |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Luxembourg           |         11 |         8 |     2 |             2 |                   0 |                 34 |                 8 |                           17    |                           4    |                   0   |                     0   |                   0         |                     2020 |     4 |                        8.5  |         2 |         2 |      0.5  |
| United Arab Emirates |         12 |        12 |     2 |             2 |                   0 |                 13 |                 7 |                            6.5  |                           3.5  |                   0   |                     0   |                   0         |                     2020 |     4 |                        3.25 |         2 |         1 |      0.5  |
| Spain                |         13 |        17 |     2 |             1 |                   1 |                  4 |                 0 |                            2    |                           0    |                  -0.5 |                     0.5 |                   0.25      |                     2021 |     3 |                        1.33 |         1 |         1 |      0.33 |
| Indonesia            |         14 |        23 |     2 |             0 |                   2 |                  0 |                 0 |                            0    |                           0    |                   0   |                     1   |                   0.5       |                     2022 |     2 |                        0    |         0 |         0 |      0    |
| Greece               |         15 |        10 |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                   0         |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| Japan                |         16 |        13 |     1 |             0 |                   1 |                 13 |                 1 |                           13    |                           1    |                   0   |                     0.5 |                   0.5       |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| Jordan               |         17 |        14 |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                   0   |                     0   |                   0         |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| South Africa         |         18 |        15 |     1 |             1 |                   0 |                 11 |                 4 |                           11    |                           4    |                  -0.5 |                     0   |                   0         |                     2021 |     3 |                        3.67 |         1 |         1 |      0.33 |
| Ukraine              |         19 |        18 |     1 |             1 |                   0 |                  4 |                 0 |                            4    |                           0    |                   0   |                     0   |                   0         |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| Malaysia             |         20 |        19 |     1 |             1 |                   0 |                  3 |                 0 |                            3    |                           0    |                   0   |                     0   |                   0         |                     2019 |     5 |                        0.6  |         1 |         1 |      0.2  |
| India                |         21 |        20 |     1 |             1 |                   0 |                  1 |                 1 |                            1    |                           1    |                   0   |                     0   |                   0         |                     2020 |     4 |                        0.25 |         1 |         1 |      0.25 |



"""
from .list_items_table import list_items_table

MARKER_COLOR = "#8da4b4"
MARKER_LINE_COLOR = "#556f81"
FIELD = "countries"
METRIC = "OCCGC"


def most_relevant_countries_table(
    #
    # ITEM FILTERS:
    top_n=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """Creates a rank chart."""

    return list_items_table(
        #
        # ITEMS PARAMS:
        field=FIELD,
        metric=METRIC,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=(None, None),
        gc_range=(None, None),
        custom_items=None,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
