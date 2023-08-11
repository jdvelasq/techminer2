# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.co_occurrence.associations.keywords.co_occurrence_matrix:

Co-occurrence Matrix
===============================================================================


>>> from techminer2.co_occurrence.associations.keywords import co_occurrence_matrix
>>> matrix = co_occurrence_matrix(
...     #
...     # ITEM PARAMS:
...     top_n=10,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> matrix.df_.head()
keywords                      REGTECH 28:329  ...  REGULATION 05:164
keywords                                      ...                   
REGTECH 28:329                            28  ...                  4
FINTECH 12:249                            12  ...                  4
REGULATORY_COMPLIANCE 09:034               9  ...                  0
REGULATORY_TECHNOLOGY 08:037               3  ...                  1
COMPLIANCE 07:030                          7  ...                  1
<BLANKLINE>
[5 rows x 10 columns]


>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...


>>> matrix.list_cells_.head()
              row                        column  matrix_value
0  REGTECH 28:329                REGTECH 28:329            28
1  REGTECH 28:329                FINTECH 12:249            12
2  REGTECH 28:329  REGULATORY_COMPLIANCE 09:034             9
3  REGTECH 28:329  REGULATORY_TECHNOLOGY 08:037             3
4  REGTECH 28:329             COMPLIANCE 07:030             7


>>> print(matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the 'keywords' \\
and 'None' fields in a bibliographic dataset. Identify any notable \\
patterns, trends, or outliers in the data, and discuss their implications \\
for the research field. Be sure to provide a concise summary of your \\
findings in no more than 150 words.
<BLANKLINE>
Table:
```
| keywords                       |   REGTECH 28:329 |   FINTECH 12:249 |   REGULATORY_COMPLIANCE 09:034 |   REGULATORY_TECHNOLOGY 08:037 |   COMPLIANCE 07:030 |   FINANCE 07:017 |   ANTI_MONEY_LAUNDERING 06:035 |   ARTIFICIAL_INTELLIGENCE 06:025 |   FINANCIAL_INSTITUTIONS 06:009 |   REGULATION 05:164 |
|:-------------------------------|-----------------:|-----------------:|-------------------------------:|-------------------------------:|--------------------:|-----------------:|-------------------------------:|---------------------------------:|--------------------------------:|--------------------:|
| REGTECH 28:329                 |               28 |               12 |                              9 |                              3 |                   7 |                5 |                              2 |                                3 |                               4 |                   4 |
| FINTECH 12:249                 |               12 |               12 |                              2 |                              1 |                   2 |                2 |                              1 |                                1 |                               2 |                   4 |
| REGULATORY_COMPLIANCE 09:034   |                9 |                2 |                              9 |                              1 |                   4 |                4 |                              0 |                                1 |                               3 |                   0 |
| REGULATORY_TECHNOLOGY 08:037   |                3 |                1 |                              1 |                              8 |                   2 |                0 |                              2 |                                1 |                               0 |                   1 |
| COMPLIANCE 07:030              |                7 |                2 |                              4 |                              2 |                   7 |                0 |                              0 |                                1 |                               1 |                   1 |
| FINANCE 07:017                 |                5 |                2 |                              4 |                              0 |                   0 |                7 |                              2 |                                2 |                               3 |                   1 |
| ANTI_MONEY_LAUNDERING 06:035   |                2 |                1 |                              0 |                              2 |                   0 |                2 |                              6 |                                2 |                               2 |                   1 |
| ARTIFICIAL_INTELLIGENCE 06:025 |                3 |                1 |                              1 |                              1 |                   1 |                2 |                              2 |                                6 |                               1 |                   0 |
| FINANCIAL_INSTITUTIONS 06:009  |                4 |                2 |                              3 |                              0 |                   1 |                3 |                              2 |                                1 |                               6 |                   1 |
| REGULATION 05:164              |                4 |                4 |                              0 |                              1 |                   1 |                1 |                              1 |                                0 |                               1 |                   5 |
```
<BLANKLINE>

"""
from ....co_occurrence_matrix import co_occurrence_matrix as __co_occurrence_matrix

ROWS_AND_COLUMNS = "keywords"


def co_occurrence_matrix(
    #
    # ITEM PARAMS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """
    :meta private:
    """

    return __co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=ROWS_AND_COLUMNS,
        rows=None,
        #
        # COLUMN PARAMS:
        col_top_n=top_n,
        col_occ_range=occ_range,
        col_gc_range=gc_range,
        col_custom_items=custom_items,
        #
        # ROW PARAMS:
        row_top_n=None,
        row_occ_range=(None, None),
        row_gc_range=(None, None),
        row_custom_items=None,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
