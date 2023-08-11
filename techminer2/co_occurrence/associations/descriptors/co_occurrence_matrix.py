# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.co_occurrence.associations.descriptors.co_occurrence_matrix:

Co-occurrence Matrix
===============================================================================


>>> from techminer2.co_occurrence.associations.descriptors import co_occurrence_matrix
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
descriptors                    REGTECH 29:330  ...  COMPLIANCE 07:030
descriptors                                    ...                   
REGTECH 29:330                             29  ...                  7
REGULATORY_TECHNOLOGY 20:274               14  ...                  3
FINANCIAL_INSTITUTIONS 16:198               9  ...                  3
REGULATORY_COMPLIANCE 15:232               14  ...                  4
FINANCIAL_REGULATION 12:395                 6  ...                  1
<BLANKLINE>
[5 rows x 10 columns]


>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...


>>> matrix.list_cells_.head()
              row                         column  matrix_value
0  REGTECH 29:330                 REGTECH 29:330            29
1  REGTECH 29:330   REGULATORY_TECHNOLOGY 20:274            14
2  REGTECH 29:330  FINANCIAL_INSTITUTIONS 16:198             9
3  REGTECH 29:330   REGULATORY_COMPLIANCE 15:232            14
4  REGTECH 29:330    FINANCIAL_REGULATION 12:395             6

>>> print(matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the \\
'descriptors' and 'None' fields in a bibliographic dataset. Identify any \\
notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| descriptors                    |   REGTECH 29:330 |   REGULATORY_TECHNOLOGY 20:274 |   FINANCIAL_INSTITUTIONS 16:198 |   REGULATORY_COMPLIANCE 15:232 |   FINANCIAL_REGULATION 12:395 |   FINTECH 12:249 |   ARTIFICIAL_INTELLIGENCE 08:036 |   FINANCIAL_SECTOR 07:169 |   FINANCIAL_CRISIS 07:058 |   COMPLIANCE 07:030 |
|:-------------------------------|-----------------:|-------------------------------:|--------------------------------:|-------------------------------:|------------------------------:|-----------------:|---------------------------------:|--------------------------:|--------------------------:|--------------------:|
| REGTECH 29:330                 |               29 |                             14 |                               9 |                             14 |                             6 |               12 |                                5 |                         3 |                         3 |                   7 |
| REGULATORY_TECHNOLOGY 20:274   |               14 |                             20 |                               5 |                              8 |                             6 |                6 |                                3 |                         5 |                         4 |                   3 |
| FINANCIAL_INSTITUTIONS 16:198  |                9 |                              5 |                              16 |                              6 |                             5 |                6 |                                4 |                         2 |                         3 |                   3 |
| REGULATORY_COMPLIANCE 15:232   |               14 |                              8 |                               6 |                             15 |                             3 |                6 |                                1 |                         1 |                         3 |                   4 |
| FINANCIAL_REGULATION 12:395    |                6 |                              6 |                               5 |                              3 |                            12 |                4 |                                1 |                         3 |                         2 |                   1 |
| FINTECH 12:249                 |               12 |                              6 |                               6 |                              6 |                             4 |               12 |                                2 |                         1 |                         2 |                   2 |
| ARTIFICIAL_INTELLIGENCE 08:036 |                5 |                              3 |                               4 |                              1 |                             1 |                2 |                                8 |                         2 |                         0 |                   3 |
| FINANCIAL_SECTOR 07:169        |                3 |                              5 |                               2 |                              1 |                             3 |                1 |                                2 |                         7 |                         0 |                   0 |
| FINANCIAL_CRISIS 07:058        |                3 |                              4 |                               3 |                              3 |                             2 |                2 |                                0 |                         0 |                         7 |                   1 |
| COMPLIANCE 07:030              |                7 |                              3 |                               3 |                              4 |                             1 |                2 |                                3 |                         0 |                         1 |                   7 |
```
<BLANKLINE>


"""
from ....co_occurrence_matrix import co_occurrence_matrix as __co_occurrence_matrix

ROWS_AND_COLUMNS = "descriptors"


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
