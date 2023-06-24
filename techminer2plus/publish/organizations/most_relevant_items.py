# flake8: noqa
"""
Most Relevant Organizations
===============================================================================


>>> ROOT_DIR = "data/regtech/"
>>> FIELD = "organizations"

>>> import techminer2plus
>>> items = techminer2plus.analyze.most_relevant_items(
...     field=FIELD,
...     root_dir=ROOT_DIR,
...     top_n=10,
... )
>>> items.table_
                                                    rank_occ  ...  m_index
organizations                                                 ...         
Univ of Hong Kong (HKG)                                    1  ...     0.43
Univ Coll Cork (IRL)                                       2  ...     0.33
Ahlia Univ (BHR)                                           3  ...     0.50
Coventry Univ (GBR)                                        4  ...     0.50
Univ of Westminster (GBR)                                  5  ...     0.50
Dublin City Univ (IRL)                                     6  ...     0.50
Politec di Milano (ITA)                                    7  ...     0.25
Kingston Bus Sch (GBR)                                     8  ...     0.17
FinTech HK, Hong Kong (HKG)                                9  ...     0.14
ctr for Law, Markets & Regulation, UNSW Austral...        10  ...     0.14
Duke Univ Sch of Law (USA)                                11  ...     0.12
Heinrich-Heine-Univ (DEU)                                 12  ...     0.25
UNSW Sydney, Kensington, Australia (AUS)                  13  ...     0.25
Univ of Luxembourg (LUX)                                  14  ...     0.25
Univ of Zurich (CHE)                                      15  ...     0.25
<BLANKLINE>
[15 rows x 18 columns]

>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'organizations' field in a scientific bibliography database. Summarize \\
the table below, delimited by triple backticks, which contains the union of \\
top 10 items by occurences and top 10 by global citations. Identify any \\
notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
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
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
