# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.co_authorship.associations.countries.co_occurrence_matrix:

Co-occurrence Matrix
===============================================================================


>>> from techminer2.co_authorship.associations.countries import co_occurrence_matrix
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
countries             United Kingdom 7:199  ...  Hong Kong 3:185
countries                                   ...                 
United Kingdom 7:199                     7  ...                0
Australia 7:199                          0  ...                3
United States 6:059                      1  ...                0
Ireland 5:055                            1  ...                0
China 5:027                              1  ...                1
<BLANKLINE>
[5 rows x 10 columns]


>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...


>>> matrix.list_cells_.head()
                    row                column  matrix_value
0  United Kingdom 7:199  United Kingdom 7:199             7
1  United Kingdom 7:199       Australia 7:199             0
2  United Kingdom 7:199   United States 6:059             1
3  United Kingdom 7:199         Ireland 5:055             1
4  United Kingdom 7:199           China 5:027             1

>>> print(matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the 'countries' \\
and 'None' fields in a bibliographic dataset. Identify any notable \\
patterns, trends, or outliers in the data, and discuss their implications \\
for the research field. Be sure to provide a concise summary of your \\
findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries            |   United Kingdom 7:199 |   Australia 7:199 |   United States 6:059 |   Ireland 5:055 |   China 5:027 |   Italy 5:005 |   Germany 4:051 |   Switzerland 4:045 |   Bahrain 4:019 |   Hong Kong 3:185 |
|:---------------------|-----------------------:|------------------:|----------------------:|----------------:|--------------:|--------------:|----------------:|--------------------:|----------------:|------------------:|
| United Kingdom 7:199 |                      7 |                 0 |                     1 |               1 |             1 |             0 |               1 |                   1 |               0 |                 0 |
| Australia 7:199      |                      0 |                 7 |                     0 |               0 |             1 |             0 |               1 |                   1 |               0 |                 3 |
| United States 6:059  |                      1 |                 0 |                     6 |               0 |             0 |             1 |               1 |                   2 |               0 |                 0 |
| Ireland 5:055        |                      1 |                 0 |                     0 |               5 |             0 |             0 |               0 |                   0 |               0 |                 0 |
| China 5:027          |                      1 |                 1 |                     0 |               0 |             5 |             0 |               0 |                   0 |               0 |                 1 |
| Italy 5:005          |                      0 |                 0 |                     1 |               0 |             0 |             5 |               0 |                   1 |               0 |                 0 |
| Germany 4:051        |                      1 |                 1 |                     1 |               0 |             0 |             0 |               4 |                   2 |               0 |                 1 |
| Switzerland 4:045    |                      1 |                 1 |                     2 |               0 |             0 |             1 |               2 |                   4 |               0 |                 1 |
| Bahrain 4:019        |                      0 |                 0 |                     0 |               0 |             0 |             0 |               0 |                   0 |               4 |                 0 |
| Hong Kong 3:185      |                      0 |                 3 |                     0 |               0 |             1 |             0 |               1 |                   1 |               0 |                 3 |
```
<BLANKLINE>

"""
from ....co_occurrence_matrix import co_occurrence_matrix as __co_occurrence_matrix

ROWS_AND_COLUMNS = "countries"


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
