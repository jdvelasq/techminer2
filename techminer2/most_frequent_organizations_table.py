# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _most_frequent_organizations_table:

Most Frequent Organizations Table
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p
>>> print(tm2p.most_frequent_organizations_table(
...    top_n=10,
...    root_dir=root_dir,
... ).to_markdown())
| organizations                                                      |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:-------------------------------------------------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| Univ of Hong Kong (HKG)                                            |          1 |         1 |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                    0        |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Univ Coll Cork (IRL)                                               |          2 |         5 |     3 |             2 |                   1 |                 41 |                19 |                           13.67 |                           6.33 |                   0   |                     0.5 |                    0.166667 |                     2018 |     6 |                        6.83 |         2 |         2 |      0.33 |
| Ahlia Univ (BHR)                                                   |          3 |        16 |     3 |             2 |                   1 |                 19 |                 5 |                            6.33 |                           1.67 |                  -0.5 |                     0.5 |                    0.166667 |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Coventry Univ (GBR)                                                |          4 |        17 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                    0.25     |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Univ of Westminster (GBR)                                          |          5 |        18 |     2 |             1 |                   1 |                 17 |                 4 |                            8.5  |                           2    |                   0   |                     0.5 |                    0.25     |                     2020 |     4 |                        4.25 |         2 |         1 |      0.5  |
| Dublin City Univ (IRL)                                             |          6 |        19 |     2 |             2 |                   0 |                 14 |                 3 |                            7    |                           1.5  |                  -0.5 |                     0   |                    0        |                     2020 |     4 |                        3.5  |         2 |         1 |      0.5  |
| Politec di Milano (ITA)                                            |          7 |        50 |     2 |             1 |                   1 |                  2 |                 0 |                            1    |                           0    |                   0   |                     0.5 |                    0.25     |                     2020 |     4 |                        0.5  |         1 |         1 |      0.25 |
| Kingston Bus Sch (GBR)                                             |          8 |         2 |     1 |             1 |                   0 |                153 |                17 |                          153    |                          17    |                   0   |                     0   |                    0        |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| FinTech HK, Hong Kong (HKG)                                        |          9 |         3 |     1 |             1 |                   0 |                150 |                 0 |                          150    |                           0    |                   0   |                     0   |                    0        |                     2017 |     7 |                       21.43 |         1 |         1 |      0.14 |
| ctr for Law, Markets & Regulation, UNSW Australia, Australia (AUS) |         10 |         4 |     1 |             1 |                   0 |                150 |                 0 |                          150    |                           0    |                   0   |                     0   |                    0        |                     2017 |     7 |                       21.43 |         1 |         1 |      0.14 |
| Duke Univ Sch of Law (USA)                                         |         11 |         6 |     1 |             1 |                   0 |                 30 |                 0 |                           30    |                           0    |                   0   |                     0   |                    0        |                     2016 |     8 |                        3.75 |         1 |         1 |      0.12 |
| Heinrich-Heine-Univ (DEU)                                          |         12 |         7 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| UNSW Sydney, Kensington, Australia (AUS)                           |         13 |         8 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Univ of Luxembourg (LUX)                                           |         14 |         9 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Univ of Zurich (CHE)                                               |         15 |        10 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                    0        |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |


"""
from .list_items_table import list_items_table

MARKER_COLOR = "#8da4b4"
MARKER_LINE_COLOR = "#556f81"
FIELD = "organizations"
METRIC = "OCCGC"


def most_frequent_organizations_table(
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
