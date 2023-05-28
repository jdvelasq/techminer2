# flake8: noqa
"""
Co-occurrence Matrix --- ChatGPT
===============================================================================

A co-occurrence matrix is a square matrix that contains the co-occurrence 
between all pairs of terms in a corpus. The co-occurrence between two terms
is the number of documents in which the two terms appear together. The
co-occurrence matrix is a useful tool for identifying the most relevant
terms associated with a given term.

It can be obtained directly using functions in the **VantagePoint** module as
is explained in the following example.


* Step 1: Import the VantagePoint module.

>>> from techminer2 import vantagepoint
>>> root_dir = "data/regtech/"


* Step 2: Create a co-occurrence matrix

>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=3,
...    root_dir=root_dir,
... )
>>> co_occ_matrix.matrix_
column                          regtech 28:329  ...  suptech 03:004
row                                             ...                
regtech 28:329                              28  ...               3
fintech 12:249                              12  ...               2
regulatory technology 07:037                 2  ...               1
compliance 07:030                            7  ...               1
regulation 05:164                            4  ...               1
financial services 04:168                    3  ...               0
financial regulation 04:035                  2  ...               0
artificial intelligence 04:023               2  ...               0
anti-money laundering 03:021                 1  ...               0
risk management 03:014                       2  ...               1
innovation 03:012                            1  ...               0
blockchain 03:005                            2  ...               0
suptech 03:004                               3  ...               3
<BLANKLINE>
[13 rows x 13 columns]


* Optional: ChatGPT prompt.

>>> print(co_occ_matrix.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the \
'author_keywords' field in a bibliographic dataset. Identify any notable \
patterns, trends, or outliers in the data, and discuss their implications for \
the research field. Be sure to provide a concise summary of your findings in \
no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |   fintech 12:249 |   regulatory technology 07:037 |   compliance 07:030 |   regulation 05:164 |   financial services 04:168 |   financial regulation 04:035 |   artificial intelligence 04:023 |   anti-money laundering 03:021 |   risk management 03:014 |   innovation 03:012 |   blockchain 03:005 |   suptech 03:004 |
|:-------------------------------|-----------------:|-----------------:|-------------------------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------------:|-------------------------:|--------------------:|--------------------:|-----------------:|
| regtech 28:329                 |               28 |               12 |                              2 |                   7 |                   4 |                           3 |                             2 |                                2 |                              1 |                        2 |                   1 |                   2 |                3 |
| fintech 12:249                 |               12 |               12 |                              1 |                   2 |                   4 |                           2 |                             1 |                                1 |                              0 |                        2 |                   1 |                   1 |                2 |
| regulatory technology 07:037   |                2 |                1 |                              7 |                   1 |                   1 |                           0 |                             0 |                                1 |                              1 |                        2 |                   1 |                   0 |                1 |
| compliance 07:030              |                7 |                2 |                              1 |                   7 |                   1 |                           0 |                             0 |                                1 |                              0 |                        1 |                   0 |                   1 |                1 |
| regulation 05:164              |                4 |                4 |                              1 |                   1 |                   5 |                           1 |                             0 |                                0 |                              0 |                        2 |                   1 |                   1 |                1 |
| financial services 04:168      |                3 |                2 |                              0 |                   0 |                   1 |                           4 |                             2 |                                0 |                              0 |                        0 |                   0 |                   0 |                0 |
| financial regulation 04:035    |                2 |                1 |                              0 |                   0 |                   0 |                           2 |                             4 |                                0 |                              0 |                        0 |                   1 |                   0 |                0 |
| artificial intelligence 04:023 |                2 |                1 |                              1 |                   1 |                   0 |                           0 |                             0 |                                4 |                              1 |                        1 |                   0 |                   1 |                0 |
| anti-money laundering 03:021   |                1 |                0 |                              1 |                   0 |                   0 |                           0 |                             0 |                                1 |                              3 |                        0 |                   0 |                   0 |                0 |
| risk management 03:014         |                2 |                2 |                              2 |                   1 |                   2 |                           0 |                             0 |                                1 |                              0 |                        3 |                   0 |                   0 |                1 |
| innovation 03:012              |                1 |                1 |                              1 |                   0 |                   1 |                           0 |                             1 |                                0 |                              0 |                        0 |                   3 |                   0 |                0 |
| blockchain 03:005              |                2 |                1 |                              0 |                   1 |                   1 |                           0 |                             0 |                                1 |                              0 |                        0 |                   0 |                   3 |                0 |
| suptech 03:004                 |                3 |                2 |                              1 |                   1 |                   1 |                           0 |                             0 |                                0 |                              0 |                        1 |                   0 |                   0 |                3 |
<BLANKLINE>
<BLANKLINE>

# pylint: disable=line-too-long
"""
