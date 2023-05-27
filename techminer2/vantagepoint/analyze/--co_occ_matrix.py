"""
Co-occurrence Matrix
===============================================================================

Computes a co-occurrence matrix.

Examples
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> r = vantagepoint.analyze.co_occ_matrix(
...    criterion='author_keywords',
...    topic_min_occ=4,
...    root_dir=root_dir,
... )
>>> r.matrix_
column                          regtech 28:329  ...  financial services 04:168
row                                             ...                           
regtech 28:329                              28  ...                          3
fintech 12:249                              12  ...                          2
compliance 07:030                            7  ...                          0
regulatory technology 07:037                 2  ...                          0
regulation 05:164                            4  ...                          1
artificial intelligence 04:023               2  ...                          0
financial regulation 04:035                  2  ...                          2
financial services 04:168                    3  ...                          4
<BLANKLINE>
[8 rows x 8 columns]

>>> print(r.prompt_)
Analyze the table below which contains values for the metric OCC. The columns \
of the table correspond to author_keywords, and the rows correspond to \
author_keywords. Identify any notable patterns, trends, or outliers in the \
data, and discuss their implications for the research field. Be sure to \
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   regtech 28:329 |   fintech 12:249 |   compliance 07:030 |   regulatory technology 07:037 |   regulation 05:164 |   artificial intelligence 04:023 |   financial regulation 04:035 |   financial services 04:168 |
|:-------------------------------|-----------------:|-----------------:|--------------------:|-------------------------------:|--------------------:|---------------------------------:|------------------------------:|----------------------------:|
| regtech 28:329                 |               28 |               12 |                   7 |                              2 |                   4 |                                2 |                             2 |                           3 |
| fintech 12:249                 |               12 |               12 |                   2 |                              1 |                   4 |                                1 |                             1 |                           2 |
| compliance 07:030              |                7 |                2 |                   7 |                              1 |                   1 |                                1 |                             0 |                           0 |
| regulatory technology 07:037   |                2 |                1 |                   1 |                              7 |                   1 |                                1 |                             0 |                           0 |
| regulation 05:164              |                4 |                4 |                   1 |                              1 |                   5 |                                0 |                             0 |                           1 |
| artificial intelligence 04:023 |                2 |                1 |                   1 |                              1 |                   0 |                                4 |                             0 |                           0 |
| financial regulation 04:035    |                2 |                1 |                   0 |                              0 |                   0 |                                0 |                             4 |                           2 |
| financial services 04:168      |                3 |                2 |                   0 |                              0 |                   1 |                                0 |                             2 |                           4 |
<BLANKLINE>
<BLANKLINE>


"""
from .occ_matrix import occ_matrix


def co_occ_matrix(
    criterion,
    topics_length=None,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    root_dir="./",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """
    Computes a co-occurrence matrix.





    """
    return occ_matrix(
        column_criterion=criterion,
        row_criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        root_dir=root_dir,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
