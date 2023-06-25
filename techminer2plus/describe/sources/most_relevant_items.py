# flake8: noqa
"""
Most Relevant Sources
===============================================================================


>>> ROOT_DIR = "data/regtech/"
>>> FIELD = "source_abbr"

>>> import techminer2plus
>>> items = techminer2plus.analyze.most_relevant_items(
...     field=FIELD,
...     root_dir=ROOT_DIR,
...     top_n=10,
... )
>>> items.table_
                               rank_occ  rank_gc  ...  g_index  m_index
source_abbr                                       ...                  
J BANK REGUL                          1        3  ...      2.0     0.50
J FINANC CRIME                        2        8  ...      1.0     0.50
FOSTER INNOVCOMPET WITH FINTE         3       28  ...      1.0     0.25
STUD COMPUT INTELL                    4       29  ...      1.0     0.33
INT CONF INF TECHNOL SYST INN         5       36  ...      0.0     0.00
ROUTLEDGE HANDBFINANCIAL TECH         6       37  ...      0.0     0.00
J ECON BUS                            7        1  ...      1.0     0.17
NORTHWEST J INTL LAW BUS              8        2  ...      1.0     0.14
PALGRAVE STUD DIGIT BUS ENABL         9        4  ...      1.0     0.20
DUKE LAW J                           10        5  ...      1.0     0.12
J RISK FINANC                        11        6  ...      1.0     0.17
J MONEY LAUND CONTROL                12        7  ...      1.0     0.25
FINANCIAL INNOV                      13        9  ...      1.0     0.50
ICEIS - PROC INT CONF ENTERP         14       10  ...      1.0     0.25
<BLANKLINE>
[14 rows x 18 columns]

>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, delimited by triple backticks, which contains the union of \\
top 10 items by occurences and top 10 by global citations. Identify any \\
notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
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
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
