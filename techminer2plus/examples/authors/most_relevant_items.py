# flake8: noqa
"""
Most Relevant Authors
===============================================================================


>>> ROOT_DIR = "data/regtech/"
>>> FIELD = "authors"

>>> import techminer2plus
>>> items = techminer2plus.analyze.most_relevant_items(
...     field=FIELD,
...     root_dir=ROOT_DIR,
...     top_n=10,
... )
>>> items.table_
                   rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
authors                                    ...                           
Arner DW                  1        1    3  ...      3.0      3.0     0.43
Buckley RP                2        2    3  ...      3.0      3.0     0.43
Barberis JN               3        3    2  ...      2.0      2.0     0.29
Butler T                  4        5    2  ...      2.0      2.0     0.33
Hamdan A                  5       15    2  ...      2.0      2.0     0.50
Turki M                   6       16    2  ...      2.0      2.0     0.50
Lin W                     7       17    2  ...      2.0      1.0     0.50
Singh C                   8       18    2  ...      2.0      1.0     0.50
Brennan R                 9       19    2  ...      2.0      1.0     0.50
Crane M                  10       20    2  ...      2.0      1.0     0.50
Anagnostopoulos I        16        4    1  ...      1.0      1.0     0.17
OBrien L                 17        6    1  ...      1.0      1.0     0.20
Baxter LG                18        7    1  ...      1.0      1.0     0.12
Weber RH                 19        8    1  ...      1.0      1.0     0.25
Zetzsche DA              20        9    1  ...      1.0      1.0     0.25
Breymann W               21       10    1  ...      1.0      1.0     0.17
<BLANKLINE>
[16 rows x 18 columns]


>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'authors' field in a scientific bibliography database. Summarize the \\
table below, delimited by triple backticks, which contains the union of top \\
10 items by occurences and top 10 by global citations. Identify any notable \\
patterns, trends, or outliers in the data, and discuss their implications \\
for the research field. Be sure to provide a concise summary of your \\
findings in no more than 150 words.
<BLANKLINE>
Table:
```
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
| Anagnostopoulos I |         16 |         4 |     1 |             1 |                   0 |                153 |                17 |                          153    |                          17    |                   0   |                     0   |                        0    |                     2018 |     6 |                       25.5  |         1 |         1 |      0.17 |
| OBrien L          |         17 |         6 |     1 |             1 |                   0 |                 33 |                14 |                           33    |                          14    |                   0   |                     0   |                        0    |                     2019 |     5 |                        6.6  |         1 |         1 |      0.2  |
| Baxter LG         |         18 |         7 |     1 |             1 |                   0 |                 30 |                 0 |                           30    |                           0    |                   0   |                     0   |                        0    |                     2016 |     8 |                        3.75 |         1 |         1 |      0.12 |
| Weber RH          |         19 |         8 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                        0    |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Zetzsche DA       |         20 |         9 |     1 |             1 |                   0 |                 24 |                 5 |                           24    |                           5    |                   0   |                     0   |                        0    |                     2020 |     4 |                        6    |         1 |         1 |      0.25 |
| Breymann W        |         21 |        10 |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                        0    |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
```
<BLANKLINE>




# pylint: disable=line-too-long
"""
