# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Co-occurrence Matrix
===============================================================================


>>> from techminer2.co_occurrence.associations.title_nlp_phrases import co_occurrence_matrix
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
title_nlp_phrases              REGULATORY_TECHNOLOGY 3:020  ...  DIGITAL_TRANSFORMATION 1:011
title_nlp_phrases                                           ...                              
REGULATORY_TECHNOLOGY 3:020                              3  ...                             1
ARTIFICIAL_INTELLIGENCE 3:017                            0  ...                             0
FINANCIAL_REGULATION 2:180                               0  ...                             0
FINANCIAL_CRIME 2:012                                    0  ...                             0
EUROPEAN_UNION 1:024                                     0  ...                             0
<BLANKLINE>
[5 rows x 10 columns]


>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...


>>> matrix.list_cells_.head()
                           row                         column  matrix_value
0  REGULATORY_TECHNOLOGY 3:020    REGULATORY_TECHNOLOGY 3:020             3
1  REGULATORY_TECHNOLOGY 3:020  ARTIFICIAL_INTELLIGENCE 3:017             0
2  REGULATORY_TECHNOLOGY 3:020     FINANCIAL_REGULATION 2:180             0
3  REGULATORY_TECHNOLOGY 3:020          FINANCIAL_CRIME 2:012             0
4  REGULATORY_TECHNOLOGY 3:020           EUROPEAN_UNION 1:024             0

>>> print(matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the \\
'title_nlp_phrases' and 'None' fields in a bibliographic dataset. Identify \\
any notable patterns, trends, or outliers in the data, and discuss their \\
implications for the research field. Be sure to provide a concise summary \\
of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| title_nlp_phrases             |   REGULATORY_TECHNOLOGY 3:020 |   ARTIFICIAL_INTELLIGENCE 3:017 |   FINANCIAL_REGULATION 2:180 |   FINANCIAL_CRIME 2:012 |   EUROPEAN_UNION 1:024 |   FINANCIAL_RISK 1:021 |   EFFECTIVE_SOLUTIONS 1:014 |   FINANCIAL_DEVELOPMENT 1:013 |   BANK_TREASURY 1:011 |   DIGITAL_TRANSFORMATION 1:011 |
|:------------------------------|------------------------------:|--------------------------------:|-----------------------------:|------------------------:|-----------------------:|-----------------------:|----------------------------:|------------------------------:|----------------------:|-------------------------------:|
| REGULATORY_TECHNOLOGY 3:020   |                             3 |                               0 |                            0 |                       0 |                      0 |                      0 |                           0 |                             0 |                     1 |                              1 |
| ARTIFICIAL_INTELLIGENCE 3:017 |                             0 |                               3 |                            0 |                       1 |                      0 |                      0 |                           1 |                             0 |                     0 |                              0 |
| FINANCIAL_REGULATION 2:180    |                             0 |                               0 |                            2 |                       0 |                      0 |                      0 |                           0 |                             0 |                     0 |                              0 |
| FINANCIAL_CRIME 2:012         |                             0 |                               1 |                            0 |                       2 |                      0 |                      0 |                           0 |                             0 |                     0 |                              0 |
| EUROPEAN_UNION 1:024          |                             0 |                               0 |                            0 |                       0 |                      1 |                      0 |                           0 |                             0 |                     0 |                              0 |
| FINANCIAL_RISK 1:021          |                             0 |                               0 |                            0 |                       0 |                      0 |                      1 |                           0 |                             0 |                     0 |                              0 |
| EFFECTIVE_SOLUTIONS 1:014     |                             0 |                               1 |                            0 |                       0 |                      0 |                      0 |                           1 |                             0 |                     0 |                              0 |
| FINANCIAL_DEVELOPMENT 1:013   |                             0 |                               0 |                            0 |                       0 |                      0 |                      0 |                           0 |                             1 |                     0 |                              0 |
| BANK_TREASURY 1:011           |                             1 |                               0 |                            0 |                       0 |                      0 |                      0 |                           0 |                             0 |                     1 |                              1 |
| DIGITAL_TRANSFORMATION 1:011  |                             1 |                               0 |                            0 |                       0 |                      0 |                      0 |                           0 |                             0 |                     1 |                              1 |
```
<BLANKLINE>

"""
from ....co_occurrence_matrix import co_occurrence_matrix as __co_occurrence_matrix

ROWS_AND_COLUMNS = "title_nlp_phrases"


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