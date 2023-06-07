# flake8: noqa
"""
Co-occurrence Matrix
===============================================================================

A co-occurrence matrix is a square matrix that contains the co-occurrence 
between all pairs of terms in a corpus. The co-occurrence between two terms
is the number of documents in which the two terms appear together. The
co-occurrence matrix is a useful tool for identifying the most relevant
terms associated with a given term.

It can be obtained directly using functions in the **VantagePoint** module as
is explained in the following example.





>>> root_dir = "data/regtech/"
>>> # Create a co-occurrence matrix
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=root_dir,
... )
>>> co_occ_matrix.matrix_
column                                  REGTECH 28:329  ...  SUPTECH 03:004
row                                                     ...                
REGTECH 28:329                                      28  ...               3
FINTECH 12:249                                      12  ...               2
COMPLIANCE 07:030                                    7  ...               1
REGULATION 05:164                                    4  ...               1
FINANCIAL_SERVICES 04:168                            3  ...               0
FINANCIAL_REGULATION 04:035                          2  ...               0
REGULATORY_TECHNOLOGY (REGTECH) 04:030               0  ...               0
ARTIFICIAL_INTELLIGENCE 04:023                       2  ...               0
ANTI-MONEY_LAUNDERING 03:021                         1  ...               0
RISK_MANAGEMENT 03:014                               2  ...               1
INNOVATION 03:012                                    1  ...               0
REGULATORY_TECHNOLOGY 03:007                         2  ...               1
BLOCKCHAIN 03:005                                    2  ...               0
SUPTECH 03:004                                       3  ...               3
<BLANKLINE>
[14 rows x 14 columns]



* Optional: ChatGPT prompt.

>>> print(co_occ_matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing the co-occurrence between the items of the same column in a bibliographic dataset.
<BLANKLINE>
Analyze the table below which contains values of co-occurrence (OCC) for the 'author_keywords' field in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                                    |   REGTECH 28:329 |   FINTECH 12:249 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   REGULATORY_TECHNOLOGY (REGTECH) 04:030 |   ARTIFICIAL_INTELLIGENCE 04:023 |   ANTI-MONEY_LAUNDERING 03:021 |   RISK_MANAGEMENT 03:014 |   INNOVATION 03:012 |   REGULATORY_TECHNOLOGY 03:007 |   BLOCKCHAIN 03:005 |   SUPTECH 03:004 |
|:---------------------------------------|-----------------:|-----------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|-----------------------------------------:|---------------------------------:|-------------------------------:|-------------------------:|--------------------:|-------------------------------:|--------------------:|-----------------:|
| REGTECH 28:329                         |               28 |               12 |                   7 |                   4 |                           3 |                             2 |                                        0 |                                2 |                              1 |                        2 |                   1 |                              2 |                   2 |                3 |
| FINTECH 12:249                         |               12 |               12 |                   2 |                   4 |                           2 |                             1 |                                        0 |                                1 |                              0 |                        2 |                   1 |                              1 |                   1 |                2 |
| COMPLIANCE 07:030                      |                7 |                2 |                   7 |                   1 |                           0 |                             0 |                                        0 |                                1 |                              0 |                        1 |                   0 |                              1 |                   1 |                1 |
| REGULATION 05:164                      |                4 |                4 |                   1 |                   5 |                           1 |                             0 |                                        0 |                                0 |                              0 |                        2 |                   1 |                              1 |                   1 |                1 |
| FINANCIAL_SERVICES 04:168              |                3 |                2 |                   0 |                   1 |                           4 |                             2 |                                        0 |                                0 |                              0 |                        0 |                   0 |                              0 |                   0 |                0 |
| FINANCIAL_REGULATION 04:035            |                2 |                1 |                   0 |                   0 |                           2 |                             4 |                                        0 |                                0 |                              0 |                        0 |                   1 |                              0 |                   0 |                0 |
| REGULATORY_TECHNOLOGY (REGTECH) 04:030 |                0 |                0 |                   0 |                   0 |                           0 |                             0 |                                        4 |                                0 |                              1 |                        0 |                   1 |                              0 |                   0 |                0 |
| ARTIFICIAL_INTELLIGENCE 04:023         |                2 |                1 |                   1 |                   0 |                           0 |                             0 |                                        0 |                                4 |                              1 |                        1 |                   0 |                              1 |                   1 |                0 |
| ANTI-MONEY_LAUNDERING 03:021           |                1 |                0 |                   0 |                   0 |                           0 |                             0 |                                        1 |                                1 |                              3 |                        0 |                   0 |                              0 |                   0 |                0 |
| RISK_MANAGEMENT 03:014                 |                2 |                2 |                   1 |                   2 |                           0 |                             0 |                                        0 |                                1 |                              0 |                        3 |                   0 |                              2 |                   0 |                1 |
| INNOVATION 03:012                      |                1 |                1 |                   0 |                   1 |                           0 |                             1 |                                        1 |                                0 |                              0 |                        0 |                   3 |                              0 |                   0 |                0 |
| REGULATORY_TECHNOLOGY 03:007           |                2 |                1 |                   1 |                   1 |                           0 |                             0 |                                        0 |                                1 |                              0 |                        2 |                   0 |                              3 |                   0 |                1 |
| BLOCKCHAIN 03:005                      |                2 |                1 |                   1 |                   1 |                           0 |                             0 |                                        0 |                                1 |                              0 |                        0 |                   0 |                              0 |                   3 |                0 |
| SUPTECH 03:004                         |                3 |                2 |                   1 |                   1 |                           0 |                             0 |                                        0 |                                0 |                              0 |                        1 |                   0 |                              1 |                   0 |                3 |
<BLANKLINE>
<BLANKLINE>


# pylint: disable=line-too-long
"""
