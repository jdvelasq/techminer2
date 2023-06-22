# flake8: noqa
"""
Most Relevant Countries
===============================================================================


>>> ROOT_DIR = "data/regtech/"
>>> FIELD = "countries"

>>> import techminer2plus
>>> items = techminer2plus.analyze.most_relevant_items(
...     field=FIELD,
...     root_dir=ROOT_DIR,
...     top_n=10,
... )
>>> items.table_
                rank_occ  rank_gc  OCC  ...  h_index  g_index  m_index
countries                               ...                           
United Kingdom         1        1    7  ...      4.0      3.0     0.67
Australia              2        2    7  ...      4.0      3.0     0.57
United States          3        4    6  ...      3.0      2.0     0.38
Ireland                4        5    5  ...      3.0      2.0     0.50
China                  5        9    5  ...      3.0      2.0     0.43
Italy                  6       16    5  ...      1.0      1.0     0.20
Germany                7        6    4  ...      3.0      2.0     0.50
Switzerland            8        7    4  ...      2.0      2.0     0.29
Bahrain                9       11    4  ...      2.0      2.0     0.50
Hong Kong             10        3    3  ...      3.0      3.0     0.43
Luxembourg            11        8    2  ...      2.0      2.0     0.50
Greece                15       10    1  ...      1.0      1.0     0.17
<BLANKLINE>
[12 rows x 18 columns]

>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize the \\
table below, delimited by triple backticks, which contains the union of top \\
10 items by occurences and top 10 by global citations. Identify any notable \\
patterns, trends, or outliers in the data, and discuss their implications \\
for the research field. Be sure to provide a concise summary of your \\
findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries      |   rank_occ |   rank_gc |   OCC |   Before 2022 |   Between 2022-2023 |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |   first_publication_year |   age |   global_citations_per_year |   h_index |   g_index |   m_index |
|:---------------|-----------:|----------:|------:|--------------:|--------------------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|----------------------:|------------------------:|----------------------------:|-------------------------:|------:|----------------------------:|----------:|----------:|----------:|
| United Kingdom |          1 |         1 |     7 |             6 |                   1 |                199 |                34 |                           28.43 |                           4.86 |                   0   |                     0.5 |                   0.0714286 |                     2018 |     6 |                       33.17 |         4 |         3 |      0.67 |
| Australia      |          2 |         2 |     7 |             7 |                   0 |                199 |                15 |                           28.43 |                           2.14 |                  -1   |                     0   |                   0         |                     2017 |     7 |                       28.43 |         4 |         3 |      0.57 |
| United States  |          3 |         4 |     6 |             4 |                   2 |                 59 |                11 |                            9.83 |                           1.83 |                   0.5 |                     1   |                   0.166667  |                     2016 |     8 |                        7.38 |         3 |         2 |      0.38 |
| Ireland        |          4 |         5 |     5 |             4 |                   1 |                 55 |                22 |                           11    |                           4.4  |                  -0.5 |                     0.5 |                   0.1       |                     2018 |     6 |                        9.17 |         3 |         2 |      0.5  |
| China          |          5 |         9 |     5 |             1 |                   4 |                 27 |                 5 |                            5.4  |                           1    |                   0.5 |                     2   |                   0.4       |                     2017 |     7 |                        3.86 |         3 |         2 |      0.43 |
| Italy          |          6 |        16 |     5 |             3 |                   2 |                  5 |                 2 |                            1    |                           0.4  |                   0   |                     1   |                   0.2       |                     2019 |     5 |                        1    |         1 |         1 |      0.2  |
| Germany        |          7 |         6 |     4 |             3 |                   1 |                 51 |                17 |                           12.75 |                           4.25 |                   0   |                     0.5 |                   0.125     |                     2018 |     6 |                        8.5  |         3 |         2 |      0.5  |
| Switzerland    |          8 |         7 |     4 |             3 |                   1 |                 45 |                13 |                           11.25 |                           3.25 |                   0.5 |                     0.5 |                   0.125     |                     2017 |     7 |                        6.43 |         2 |         2 |      0.29 |
| Bahrain        |          9 |        11 |     4 |             3 |                   1 |                 19 |                 5 |                            4.75 |                           1.25 |                  -1   |                     0.5 |                   0.125     |                     2020 |     4 |                        4.75 |         2 |         2 |      0.5  |
| Hong Kong      |         10 |         3 |     3 |             3 |                   0 |                185 |                 8 |                           61.67 |                           2.67 |                   0   |                     0   |                   0         |                     2017 |     7 |                       26.43 |         3 |         3 |      0.43 |
| Luxembourg     |         11 |         8 |     2 |             2 |                   0 |                 34 |                 8 |                           17    |                           4    |                   0   |                     0   |                   0         |                     2020 |     4 |                        8.5  |         2 |         2 |      0.5  |
| Greece         |         15 |        10 |     1 |             1 |                   0 |                 21 |                 8 |                           21    |                           8    |                   0   |                     0   |                   0         |                     2018 |     6 |                        3.5  |         1 |         1 |      0.17 |
```
<BLANKLINE>



# pylint: disable=line-too-long
"""
