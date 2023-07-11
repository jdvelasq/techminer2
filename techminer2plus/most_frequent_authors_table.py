# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _most_frequent_authors_table:

Most Frequent Authors Table
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p
>>> print(tm2p.most_frequent_authors_table(
...    top_n=20,
...    root_dir=root_dir,
... ).to_markdown())
| authors           |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Arner DW          |          1 |         1 |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                        0    |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Buckley RP        |          2 |         2 |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                        0    |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Barberis JN       |          3 |         3 |     2 |             2 |                   0 |                161 |                 3 |                           80.5  |                           1.5  |                   0   |                     0   |                        0    |                     2017 |     7 |                       23    |         2 |         2 |      0.29 |
| Butler T          |          4 |         5 |     2 |             2 |                   0 |                 41 |                19 |                           20.5  |                           9.5  |                   0   |                     0   |                        0    |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| Hamdan A          |          5 |        15 |     2 |             2 |                   0 |                 18 |                 5 |                            9    |                           2.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| Turki M           |          6 |        16 |     2 |             2 |                   0 |                 18 |                 5 |                            9    |                           2.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        4.5  |         2 |         2 |      0.5  |
| Lin W             |          7 |        17 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Singh C           |          8 |        18 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Brennan R         |          9 |        19 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Crane M           |         10 |        20 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Ryan P            |         11 |        21 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Sarea A           |         12 |        28 |     2 |             1 |                   1 |                 12 |                 4 |                            6    |                           2    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| Grassi L          |         13 |        60 |     2 |             1 |                   1 |                  2 |                 0 |                            1    |                           0    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        0.5  |         1 |         1 |      0.25 |
| Lanfranchi D      |         14 |        61 |     2 |             1 |                   1 |                  2 |                 0 |                            1    |                           0    |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        0.5  |         1 |         1 |      0.25 |
| Arman AA          |         15 |        77 |     2 |             0 |                   2 |                  0 |                 0 |                            0    |                           0    |                   0   |                     1   |                        0.5  |                     2022 |     2 |                        0    |         0 |         0 |      0    |
| Anagnostopoulos I |         16 |         4 |     1 |             1 |                   0 |                153 |                17 |                          153    |                          17    |                   0   |                     0   |                        0    |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| OBrien L          |         17 |         6 |     1 |             1 |                   0 |                 33 |                14 |                           33    |                          14    |                   0   |                     0   |                        0    |                     2019 |     5 |                        6.6  |         1 |         1 |      0.2  |
| Baxter LG         |         18 |         7 |     1 |             1 |                   0 |                 30 |                 0 |                           30    |                           0    |                   0   |                     0   |                        0    |                     2016 |     8 |                        3.75 |         1 |         1 |      0.12 |
| Weber RH          |         19 |         8 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                        0    |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Zetzsche DA       |         20 |         9 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                        0    |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |



"""
from .list_items_table import list_items_table

MARKER_COLOR = "#8da4b4"
MARKER_LINE_COLOR = "#556f81"
FIELD = "authors"
METRIC = "OCC"


def most_frequent_authors_table(
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
