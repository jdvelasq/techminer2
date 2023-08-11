# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.co_occurrence.associations.abstract_nlp_phrases.co_occurrence_matrix:

Co-occurrence Matrix
===============================================================================


>>> from techminer2.co_occurrence.associations.abstract_nlp_phrases import co_occurrence_matrix
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
abstract_nlp_phrases            REGULATORY_TECHNOLOGY 17:266  ...  INFORMATION_TECHNOLOGY 05:177
abstract_nlp_phrases                                          ...                               
REGULATORY_TECHNOLOGY 17:266                              17  ...                              5
FINANCIAL_INSTITUTIONS 15:194                              5  ...                              1
REGULATORY_COMPLIANCE 07:198                               4  ...                              0
FINANCIAL_SECTOR 07:169                                    4  ...                              2
ARTIFICIAL_INTELLIGENCE 07:033                             3  ...                              1
<BLANKLINE>
[5 rows x 10 columns]


>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...


>>> matrix.list_cells_.head()
                            row                          column  matrix_value
0  REGULATORY_TECHNOLOGY 17:266    REGULATORY_TECHNOLOGY 17:266            17
1  REGULATORY_TECHNOLOGY 17:266   FINANCIAL_INSTITUTIONS 15:194             5
2  REGULATORY_TECHNOLOGY 17:266    REGULATORY_COMPLIANCE 07:198             4
3  REGULATORY_TECHNOLOGY 17:266         FINANCIAL_SECTOR 07:169             4
4  REGULATORY_TECHNOLOGY 17:266  ARTIFICIAL_INTELLIGENCE 07:033             3

>>> print(matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the \\
'abstract_nlp_phrases' and 'None' fields in a bibliographic dataset. \\
Identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| abstract_nlp_phrases               |   REGULATORY_TECHNOLOGY 17:266 |   FINANCIAL_INSTITUTIONS 15:194 |   REGULATORY_COMPLIANCE 07:198 |   FINANCIAL_SECTOR 07:169 |   ARTIFICIAL_INTELLIGENCE 07:033 |   FINANCIAL_REGULATION 06:330 |   GLOBAL_FINANCIAL_CRISIS 06:177 |   FINANCIAL_CRISIS 06:058 |   FINANCIAL_SERVICES_INDUSTRY 05:315 |   INFORMATION_TECHNOLOGY 05:177 |
|:-----------------------------------|-------------------------------:|--------------------------------:|-------------------------------:|--------------------------:|---------------------------------:|------------------------------:|---------------------------------:|--------------------------:|-------------------------------------:|--------------------------------:|
| REGULATORY_TECHNOLOGY 17:266       |                             17 |                               5 |                              4 |                         4 |                                3 |                             3 |                                3 |                         2 |                                    4 |                               5 |
| FINANCIAL_INSTITUTIONS 15:194      |                              5 |                              15 |                              3 |                         2 |                                3 |                             4 |                                2 |                         3 |                                    1 |                               1 |
| REGULATORY_COMPLIANCE 07:198       |                              4 |                               3 |                              7 |                         1 |                                1 |                             1 |                                0 |                         2 |                                    2 |                               0 |
| FINANCIAL_SECTOR 07:169            |                              4 |                               2 |                              1 |                         7 |                                2 |                             3 |                                1 |                         0 |                                    2 |                               2 |
| ARTIFICIAL_INTELLIGENCE 07:033     |                              3 |                               3 |                              1 |                         2 |                                7 |                             0 |                                0 |                         0 |                                    1 |                               1 |
| FINANCIAL_REGULATION 06:330        |                              3 |                               4 |                              1 |                         3 |                                0 |                             6 |                                2 |                         1 |                                    2 |                               2 |
| GLOBAL_FINANCIAL_CRISIS 06:177     |                              3 |                               2 |                              0 |                         1 |                                0 |                             2 |                                6 |                         0 |                                    1 |                               2 |
| FINANCIAL_CRISIS 06:058            |                              2 |                               3 |                              2 |                         0 |                                0 |                             1 |                                0 |                         6 |                                    0 |                               1 |
| FINANCIAL_SERVICES_INDUSTRY 05:315 |                              4 |                               1 |                              2 |                         2 |                                1 |                             2 |                                1 |                         0 |                                    5 |                               2 |
| INFORMATION_TECHNOLOGY 05:177      |                              5 |                               1 |                              0 |                         2 |                                1 |                             2 |                                2 |                         1 |                                    2 |                               5 |
```
<BLANKLINE>


"""
from ....co_occurrence_matrix import co_occurrence_matrix as __co_occurrence_matrix

ROWS_AND_COLUMNS = "abstract_nlp_phrases"


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
