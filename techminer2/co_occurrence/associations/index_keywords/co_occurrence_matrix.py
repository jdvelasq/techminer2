# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.co_occurrence.associations.index_keywords.co_occurrence_matrix:

Co-occurrence Matrix
===============================================================================


>>> from techminer2.co_occurrence.associations.index_keywords import co_occurrence_matrix
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
index_keywords               REGULATORY_COMPLIANCE 9:34  ...  SANDBOXES 2:12
index_keywords                                           ...                
REGULATORY_COMPLIANCE 9:34                            9  ...               1
FINANCIAL_INSTITUTIONS 6:09                           3  ...               0
FINANCE 5:16                                          4  ...               1
REGTECH 5:15                                          4  ...               1
ANTI_MONEY_LAUNDERING 3:10                            0  ...               0
<BLANKLINE>
[5 rows x 10 columns]


>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...


>>> matrix.list_cells_.head()
                          row                       column  matrix_value
0  REGULATORY_COMPLIANCE 9:34   REGULATORY_COMPLIANCE 9:34             9
1  REGULATORY_COMPLIANCE 9:34  FINANCIAL_INSTITUTIONS 6:09             3
2  REGULATORY_COMPLIANCE 9:34                 FINANCE 5:16             4
3  REGULATORY_COMPLIANCE 9:34                 REGTECH 5:15             4
4  REGULATORY_COMPLIANCE 9:34   ANTI_MONEY_LAUNDERING 3:10             0

>>> print(matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the \\
'index_keywords' and 'None' fields in a bibliographic dataset. Identify any \\
notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| index_keywords              |   REGULATORY_COMPLIANCE 9:34 |   FINANCIAL_INSTITUTIONS 6:09 |   FINANCE 5:16 |   REGTECH 5:15 |   ANTI_MONEY_LAUNDERING 3:10 |   FINTECH 3:08 |   INFORMATION_SYSTEMS 2:14 |   INFORMATION_USE 2:14 |   SOFTWARE_SOLUTION 2:14 |   SANDBOXES 2:12 |
|:----------------------------|-----------------------------:|------------------------------:|---------------:|---------------:|-----------------------------:|---------------:|---------------------------:|-----------------------:|-------------------------:|-----------------:|
| REGULATORY_COMPLIANCE 9:34  |                            9 |                             3 |              4 |              4 |                            0 |              2 |                          2 |                      2 |                        2 |                1 |
| FINANCIAL_INSTITUTIONS 6:09 |                            3 |                             6 |              2 |              1 |                            2 |              2 |                          0 |                      0 |                        0 |                0 |
| FINANCE 5:16                |                            4 |                             2 |              5 |              4 |                            1 |              1 |                          0 |                      0 |                        0 |                1 |
| REGTECH 5:15                |                            4 |                             1 |              4 |              5 |                            0 |              1 |                          0 |                      0 |                        0 |                1 |
| ANTI_MONEY_LAUNDERING 3:10  |                            0 |                             2 |              1 |              0 |                            3 |              1 |                          0 |                      0 |                        0 |                0 |
| FINTECH 3:08                |                            2 |                             2 |              1 |              1 |                            1 |              3 |                          0 |                      0 |                        0 |                0 |
| INFORMATION_SYSTEMS 2:14    |                            2 |                             0 |              0 |              0 |                            0 |              0 |                          2 |                      2 |                        2 |                0 |
| INFORMATION_USE 2:14        |                            2 |                             0 |              0 |              0 |                            0 |              0 |                          2 |                      2 |                        2 |                0 |
| SOFTWARE_SOLUTION 2:14      |                            2 |                             0 |              0 |              0 |                            0 |              0 |                          2 |                      2 |                        2 |                0 |
| SANDBOXES 2:12              |                            1 |                             0 |              1 |              1 |                            0 |              0 |                          0 |                      0 |                        0 |                2 |
```
<BLANKLINE>

"""
from ...co_occurrence_matrix import co_occurrence_matrix as __co_occurrence_matrix

ROWS_AND_COLUMNS = "index_keywords"


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
