# flake8: noqa
"""
G-Index
===============================================================================



>>> FILE_NAME = "sphinx/_static/use_cases/sources/g_index.html"
>>> import techminer2plus
>>> items = techminer2plus.use_cases.sources.g_index(
...     top_n=20,
...     root_dir="data/regtech/",
... )
>>> items.ranking_chart_.write_html(FILE_NAME)

.. raw:: html

    <iframe src="../../_static/use_cases/sources/g_index.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> items.items_list_.head()
                               rank_occ  rank_gc  ...  g_index  m_index
source_abbr                                       ...                  
J BANK REGUL                          1        3  ...      2.0     0.50
J ECON BUS                            7        1  ...      1.0     0.17
NORTHWEST J INTL LAW BUS              8        2  ...      1.0     0.14
PALGRAVE STUD DIGIT BUS ENABL         9        4  ...      1.0     0.20
DUKE LAW J                           10        5  ...      1.0     0.12
<BLANKLINE>
[5 rows x 18 columns]

>>> print(items.chatbot_prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'g_index' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| source_abbr                   |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:------------------------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| J BANK REGUL                  |          1 |         3 |     2 |             2 |                   0 |                 35 |                 9 |                            17.5 |                            4.5 |                  -0.5 |                     0   |                        0    |                     2020 |     4 |                        8.75 |         2 |         2 |      0.5  |
| J ECON BUS                    |          7 |         1 |     1 |             1 |                   0 |                153 |                17 |                           153   |                           17   |                   0   |                     0   |                        0    |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| NORTHWEST J INTL LAW BUS      |          8 |         2 |     1 |             1 |                   0 |                150 |                 0 |                           150   |                            0   |                   0   |                     0   |                        0    |                     2017 |     7 |                       21.43 |         1 |         1 |      0.14 |
| PALGRAVE STUD DIGIT BUS ENABL |          9 |         4 |     1 |             1 |                   0 |                 33 |                14 |                            33   |                           14   |                   0   |                     0   |                        0    |                     2019 |     5 |                        6.6  |         1 |         1 |      0.2  |
| DUKE LAW J                    |         10 |         5 |     1 |             1 |                   0 |                 30 |                 0 |                            30   |                            0   |                   0   |                     0   |                        0    |                     2016 |     8 |                        3.75 |         1 |         1 |      0.12 |
| J RISK FINANC                 |         11 |         6 |     1 |             1 |                   0 |                 21 |                 8 |                            21   |                            8   |                   0   |                     0   |                        0    |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
| J MONEY LAUND CONTROL         |         12 |         7 |     1 |             1 |                   0 |                 14 |                 3 |                            14   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        3.5  |         1 |         1 |      0.25 |
| J FINANC CRIME                |          2 |         8 |     2 |             1 |                   1 |                 13 |                 4 |                             6.5 |                            2   |                   0   |                     0.5 |                        0.25 |                     2020 |     4 |                        3.25 |         2 |         1 |      0.5  |
| FINANCIAL INNOV               |         13 |         9 |     1 |             0 |                   1 |                 13 |                 1 |                            13   |                            1   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        6.5  |         1 |         1 |      0.5  |
| ICEIS - PROC INT CONF ENTERP  |         14 |        10 |     1 |             1 |                   0 |                 12 |                 3 |                            12   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        3    |         1 |         1 |      0.25 |
| HANDBBLOCKCHAIN, DIGIT FINANC |         16 |        12 |     1 |             1 |                   0 |                 11 |                 3 |                            11   |                            3   |                   0   |                     0   |                        0    |                     2017 |     7 |                        1.57 |         1 |         1 |      0.14 |
| HELIYON                       |         15 |        11 |     1 |             1 |                   0 |                 11 |                 4 |                            11   |                            4   |                   0   |                     0   |                        0    |                     2020 |     4 |                        2.75 |         1 |         1 |      0.25 |
| J RISK MANG FINANCIAL INST    |         17 |        13 |     1 |             1 |                   0 |                  8 |                 5 |                             8   |                            5   |                   0   |                     0   |                        0    |                     2018 |     6 |                        1.33 |         1 |         1 |      0.17 |
| ADV INTELL SYS COMPUT         |         18 |        14 |     1 |             1 |                   0 |                  7 |                 1 |                             7   |                            1   |                  -0.5 |                     0   |                        0    |                     2021 |     3 |                        2.33 |         1 |         1 |      0.33 |
| ADELAIDE LAW REV              |         20 |        16 |     1 |             1 |                   0 |                  5 |                 1 |                             5   |                            1   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| INTELL SYST ACCOUNT FINANCE M |         19 |        15 |     1 |             1 |                   0 |                  5 |                 3 |                             5   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1.25 |         1 |         1 |      0.25 |
| J FINANCIAL DATA SCI          |         21 |        17 |     1 |             1 |                   0 |                  5 |                 1 |                             5   |                            1   |                   0   |                     0   |                        0    |                     2019 |     5 |                        1    |         1 |         1 |      0.2  |
| LECTURE NOTES DATA ENG COMMUN |         23 |        19 |     1 |             1 |                   0 |                  4 |                 0 |                             4   |                            0   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| UNIV NEW SOUTH WALES LAW J    |         22 |        18 |     1 |             1 |                   0 |                  4 |                 3 |                             4   |                            3   |                   0   |                     0   |                        0    |                     2020 |     4 |                        1    |         1 |         1 |      0.25 |
| EUR J RISK REGUL              |         27 |        23 |     1 |             0 |                   1 |                  3 |                 0 |                             3   |                            0   |                   0   |                     0.5 |                        0.5  |                     2022 |     2 |                        1.5  |         1 |         1 |      0.5  |
```
<BLANKLINE>






# pylint: disable=line-too-long
"""
from ... import list_items
from ...graphing_lib import ranking_chart

FIELD = "source_abbr"
METRIC = "g_index"
TITLE = "Sources' G-Index"


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def g_index(
    #
    # Plot options:
    textfont_size=10,
    marker_size=7,
    line_color="black",
    line_width=1.5,
    yshift=4,
    metric_label=None,
    field_label=None,
    title=None,
    #
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # Database params:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Most Relevant Source Items."""

    if title is None:
        title = TITLE

    itemslist = list_items(
        field=FIELD,
        metric=METRIC,
        #
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # Database filters:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    return ranking_chart(
        itemslist=itemslist,
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_color=line_color,
        line_width=line_width,
        yshift=yshift,
    )
