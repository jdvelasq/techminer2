# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.co_authorship.associations.authors.co_occurrence_matrix:

Co-occurrence Matrix
===============================================================================


>>> from techminer2.co_authorship.associations.authors import co_occurrence_matrix
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
authors            Arner DW 3:185  ...  Crane M 2:014
authors                            ...               
Arner DW 3:185                  3  ...              0
Buckley RP 3:185                3  ...              0
Barberis JN 2:161               2  ...              0
Butler T 2:041                  0  ...              0
Hamdan A 2:018                  0  ...              0
<BLANKLINE>
[5 rows x 10 columns]

>>> matrix.heat_map_ # doctest: +ELLIPSIS
<pandas.io.formats.style.Styler object ...


>>> matrix.list_cells_.head()
              row             column  matrix_value
0  Arner DW 3:185     Arner DW 3:185             3
1  Arner DW 3:185   Buckley RP 3:185             3
2  Arner DW 3:185  Barberis JN 2:161             2
3  Arner DW 3:185     Butler T 2:041             0
4  Arner DW 3:185     Hamdan A 2:018             0


>>> print(matrix.prompt_)
Your task is to generate a short paragraph for a research paper analyzing \\
the co-occurrence between the values of different columns in a \\
bibliographic dataset. Analyze the table below, and delimited by triple \\
backticks, which contains values of co-occurrence (OCC) for the 'authors' \\
and 'None' fields in a bibliographic dataset. Identify any notable \\
patterns, trends, or outliers in the data, and discuss their implications \\
for the research field. Be sure to provide a concise summary of your \\
findings in no more than 150 words.
<BLANKLINE>
Table:
```
| authors           |   Arner DW 3:185 |   Buckley RP 3:185 |   Barberis JN 2:161 |   Butler T 2:041 |   Hamdan A 2:018 |   Turki M 2:018 |   Lin W 2:017 |   Singh C 2:017 |   Brennan R 2:014 |   Crane M 2:014 |
|:------------------|-----------------:|-------------------:|--------------------:|-----------------:|-----------------:|----------------:|--------------:|----------------:|------------------:|----------------:|
| Arner DW 3:185    |                3 |                  3 |                   2 |                0 |                0 |               0 |             0 |               0 |                 0 |               0 |
| Buckley RP 3:185  |                3 |                  3 |                   2 |                0 |                0 |               0 |             0 |               0 |                 0 |               0 |
| Barberis JN 2:161 |                2 |                  2 |                   2 |                0 |                0 |               0 |             0 |               0 |                 0 |               0 |
| Butler T 2:041    |                0 |                  0 |                   0 |                2 |                0 |               0 |             0 |               0 |                 0 |               0 |
| Hamdan A 2:018    |                0 |                  0 |                   0 |                0 |                2 |               2 |             0 |               0 |                 0 |               0 |
| Turki M 2:018     |                0 |                  0 |                   0 |                0 |                2 |               2 |             0 |               0 |                 0 |               0 |
| Lin W 2:017       |                0 |                  0 |                   0 |                0 |                0 |               0 |             2 |               2 |                 0 |               0 |
| Singh C 2:017     |                0 |                  0 |                   0 |                0 |                0 |               0 |             2 |               2 |                 0 |               0 |
| Brennan R 2:014   |                0 |                  0 |                   0 |                0 |                0 |               0 |             0 |               0 |                 2 |               2 |
| Crane M 2:014     |                0 |                  0 |                   0 |                0 |                0 |               0 |             0 |               0 |                 2 |               2 |
```
<BLANKLINE>


"""
from ....co_occurrence_matrix import co_occurrence_matrix as __co_occurrence_matrix

ROWS_AND_COLUMNS = "authors"


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
