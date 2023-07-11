# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _most_relevant_sources_table:

Most Relevant Sources Table
===============================================================================

>>> root_dir = "data/regtech/"
>>> import techminer2 as tm2
>>> print(tm2p.most_relevant_sources_table(
...    top_n=20,
...    root_dir=root_dir,
... ).to_markdown())
| source_abbr                   |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| J BANK REGUL                  |          1 |         3 |     2 |             2 |                   0 |                 35 |                 9 |                            17.5 |                            4.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        8.75 |         2 |         2 |      0.5  |
| J FINANC CRIME                |          2 |         8 |     2 |             1 |                   1 |                 13 |                 4 |                             6.5 |                            2   |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        3.25 |         2 |         1 |      0.5  |
| FOSTER INNOVCOMPET WITH FINTE |          3 |        28 |     2 |             2 |                   0 |                  1 |                 1 |                             0.5 |                            0.5 |                   0   |                     0   |                        0    |                     2020 |     4 |                        0.25 |         1 |         1 |      0.25 |
| STUD COMPUT INTELL            |          4 |        29 |     2 |             2 |                   0 |                  1 |                 1 |                             0.5 |                            0.5 |                  -1   |                     0   |                        0    |                     2021 |     3 |                        0.33 |         1 |         1 |      0.33 |
| INT CONF INF TECHNOL SYST INN |          5 |        36 |     2 |             0 |                   2 |                  0 |                 0 |                             0   |                            0   |                   0   |                     1   |                        0.5  |                     2022 |     2 |                        0    |         0 |         0 |      0    |
| ROUTLEDGE HANDBFINANCIAL TECH |          6 |        37 |     2 |             2 |                   0 |                  0 |                 0 |                             0   |                            0   |                  -1   |                     0   |                        0    |                     2021 |     3 |                        0    |         0 |         0 |      0    |
| J ECON BUS                    |          7 |         1 |     1 |             1 |                   0 |                153 |                17 |                           153   |                           17   |                   0   |                     0   |                        0    |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| NORTHWEST J INTL LAW BUS      |          8 |         2 |     1 |             1 |                   0 |                150 |                 0 |                           150   |                            0   |                   0   |                     0   |                        0    |                     2017 |     7 |                       21.43 |         1 |         1 |      0.14 |
| PALGRAVE STUD DIGIT BUS ENABL |          9 |         4 |     1 |             1 |                   0 |                 33 |                14 |                            33   |                           14   |                   0   |                     0   |                        0    |                     2019 |     5 |                        6.6  |         1 |         1 |      0.2  |
| DUKE LAW J                    |         10 |         5 |     1 |             1 |                   0 |                 30 |                 0 |                            30   |                            0   |                   0   |                     0   |                        0    |                     2016 |     8 |                        3.75 |         1 |         1 |      0.12 |
| J RISK FINANC                 |         11 |         6 |     1 |             1 |                   0 |                 21 |                 8 |                            21   |                            8   |                   0   |                     0   |                        0    |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| J MONEY LAUND CONTROL         |         12 |         7 |     1 |             1 |                   0 |                 14 |                 3 |                            14   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        3.5  |         1 |         1 |      0.25 |
| FINANCIAL INNOV               |         13 |         9 |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| ICEIS - PROC INT CONF ENTERP  |         14 |        10 |     1 |             1 |                   0 |                 12 |                 3 |                            12   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| HELIYON                       |         15 |        11 |     1 |             1 |                   0 |                 11 |                 4 |                            11   |                            4   |                   0   |                     0   |                        0    |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| HANDBBLOCKCHAIN, DIGIT FINANC |         16 |        12 |     1 |             1 |                   0 |                 11 |                 3 |                            11   |                            3   |                   0   |                     0   |                        0    |                     2017 |     7 |                        1.57 |         1 |         1 |      0.14 |
| J RISK MANG FINANCIAL INST    |         17 |        13 |     1 |             1 |                   0 |                  8 |                 5 |                             8   |                            5   |                   0   |                     0   |                        0    |                     2018 |     6 |                        1.33 |         1 |         1 |      0.17 |
| ADV INTELL SYS COMPUT         |         18 |        14 |     1 |             1 |                   0 |                  7 |                 1 |                             7   |                            1   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        2.33 |         1 |         1 |      0.33 |
| INTELL SYST ACCOUNT FINANCE M |         19 |        15 |     1 |             1 |                   0 |                  5 |                 3 |                             5   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| ADELAIDE LAW REV              |         20 |        16 |     1 |             1 |                   0 |                  5 |                 1 |                             5   |                            1   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| J FINANCIAL DATA SCI          |         21 |        17 |     1 |             1 |                   0 |                  5 |                 1 |                             5   |                            1   |                   0   |                     0   |                        0    |                     2019 |     5 |                        1    |         1 |         1 |      0.2  |
| UNIV NEW SOUTH WALES LAW J    |         22 |        18 |     1 |             1 |                   0 |                  4 |                 3 |                             4   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| LECTURE NOTES DATA ENG COMMUN |         23 |        19 |     1 |             1 |                   0 |                  4 |                 0 |                             4   |                            0   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| J ANTITRUST ENFORC            |         24 |        20 |     1 |             1 |                   0 |                  3 |                 3 |                             3   |                            3   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        1    |         1 |         1 |      0.33 |


"""
from ...vantagepoint.discover.list_items_table import list_items_table

MARKER_COLOR = "#8da4b4"
MARKER_LINE_COLOR = "#556f81"
FIELD = "source_abbr"
METRIC = "OCCGC"


def most_relevant_sources_table(
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
