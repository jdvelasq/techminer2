# flake8: noqa
# pylint: disable=line-too-long
"""
Most Frequent Sources
==============================================================================




>>> import techminer2 as tm2 # doctsest: +ELIPSIS
Note: ...
Note: ...
Note: ...

>>> root_dir = "data/regtech/"

>>> most_frequent_sources = (
...     tm2p.records(root_dir=root_dir)
...     .list_items(
...         field='source_abbr',
...         top_n=10,
...     )
... )
>>> most_frequent_sources
ListItems(field='source_abbr', metric='OCC', top_n=10, occ_range=(None, None),
    gc_range=(None, None), custom_items=['J BANK REGUL', 'J FINANC CRIME',
    'FOSTER INNOVCOMPET WITH FINTE', 'STUD COMPUT INTELL', 'INT CONF INF TECHNOL
    SYST INN', 'ROUTLEDGE HANDBFINANCIAL TECH', 'J ECON BUS', 'NORTHWEST J INTL
    LAW BUS', 'PALGRAVE STUD DIGIT BUS ENABL', 'DUKE LAW J'])

        
>>> most_frequent_sources.df_.head()
                               rank_occ  rank_gc  ...  g_index  m_index
source_abbr                                       ...                  
J BANK REGUL                          1        3  ...      2.0     0.50
J FINANC CRIME                        2        8  ...      1.0     0.50
FOSTER INNOVCOMPET WITH FINTE         3       28  ...      1.0     0.25
STUD COMPUT INTELL                    4       29  ...      1.0     0.33
INT CONF INF TECHNOL SYST INN         5       36  ...      0.0     0.00
<BLANKLINE>
[5 rows x 18 columns]

>>> print(most_frequent_sources.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'source_abbr' field in a scientific bibliography database. Summarize \\
the table below, sorted by the 'OCC' metric, and delimited by triple \\
backticks, identify any notable patterns, trends, or outliers in the data, \\
and discuss their implications for the research field. Be sure to provide a \\
concise summary of your findings in no more than 150 words.
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
```
<BLANKLINE>


>>> most_frequent_sources.ranking_chart(
...     title="Most Frequent Sources",
... ).write_html("sphinx/_static/most_frequent_sources.html")

.. raw:: html


    <iframe src="../../_static/most_frequent_sources.html" height="600px" width="100%" frameBorder="0"></iframe>



"""
