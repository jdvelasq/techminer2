# flake8: noqa
# pylint: disable=line-too-long
"""
List Cells In Matrix
===============================================================================

Creates a list that has a row for each cell in the original matrix. The list is
sorted by the value of the cell. The columns of the original matrix correspond
to the 'column' column of the list, and the rows of the original matrix
correspond to the 'row' column of the list. The value of the cell is stored in
the 'value' column of the list.

* Preparation

>>> root_dir = "data/regtech/"
>>> import techminer2plus as tm2p

* Object oriented interface

>>> (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=10,
...     )
...     .list_cells_in_matrix()
... ).head()
              row                        column  matrix_value
0  REGTECH 28:329                REGTECH 28:329            28
1  REGTECH 28:329                FINTECH 12:249            12
2  REGTECH 28:329  REGULATORY_TECHNOLOGY 07:037             2
3  REGTECH 28:329             COMPLIANCE 07:030             7
4  REGTECH 28:329             REGULATION 05:164             4

>>> (
...     tm2p.records(root_dir=root_dir)
...     .auto_correlation_matrix(
...         rows_and_columns='authors',
...         top_n=10,
...     )
...     .list_cells_in_matrix()
... ).head()
              row             column  matrix_value
0  Arner DW 3:185     Arner DW 3:185        1.0000
1  Arner DW 3:185   Buckley RP 3:185        1.0000
2  Arner DW 3:185  Barberis JN 2:161        0.7698
3  Arner DW 3:185     Butler T 2:041        0.0000
4  Arner DW 3:185     Hamdan A 2:018        0.0000


>>> (
...     tm2p.records(root_dir=root_dir)
...     .cross_correlation_matrix(
...         rows_and_columns='authors',
...         cross_with='countries',
...         top_n=10,
...     )
...     .list_cells_in_matrix()
... ).head()
              row             column  matrix_value
0  Arner DW 3:185     Arner DW 3:185      1.000000
1  Arner DW 3:185   Buckley RP 3:185      1.000000
2  Arner DW 3:185  Barberis JN 2:161      0.907242
3  Arner DW 3:185     Butler T 2:041      0.000000
4  Arner DW 3:185     Hamdan A 2:018      0.000000

* Functional interface


>>> matrix = tm2p.co_occurrence_matrix(
...     columns='author_keywords',
...     col_top_n=10,
...     root_dir=root_dir,
... )
>>> tm2p.list_cells_in_matrix(matrix).head()
              row                        column  matrix_value
0  REGTECH 28:329                REGTECH 28:329            28
1  REGTECH 28:329                FINTECH 12:249            12
2  REGTECH 28:329  REGULATORY_TECHNOLOGY 07:037             2
3  REGTECH 28:329             COMPLIANCE 07:030             7
4  REGTECH 28:329             REGULATION 05:164             4

>>> matrix = tm2p.auto_correlation_matrix(
...     rows_and_columns='authors',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> tm2p.list_cells_in_matrix(matrix).head()
              row             column  matrix_value
0  Arner DW 3:185     Arner DW 3:185        1.0000
1  Arner DW 3:185   Buckley RP 3:185        1.0000
2  Arner DW 3:185  Barberis JN 2:161        0.7698
3  Arner DW 3:185     Butler T 2:041        0.0000
4  Arner DW 3:185     Hamdan A 2:018        0.0000



>>> matrix = tm2p.cross_correlation_matrix(
...     rows_and_columns='authors', 
...     cross_with='countries',
...     top_n=10,
...     root_dir=root_dir,
... )
>>> tm2p.list_cells_in_matrix(matrix).head()
              row             column  matrix_value
0  Arner DW 3:185     Arner DW 3:185      1.000000
1  Arner DW 3:185   Buckley RP 3:185      1.000000
2  Arner DW 3:185  Barberis JN 2:161      0.907242
3  Arner DW 3:185     Butler T 2:041      0.000000
4  Arner DW 3:185     Hamdan A 2:018      0.000000
    

"""


def list_cells_in_matrix(obj):
    """List the cells in a matrix."""

    #
    #
    # MAIN CODE:
    #
    #

    matrix = obj.df_
    matrix = matrix.melt(
        value_name="matrix_value",
        var_name="row",
        ignore_index=False,
    )
    matrix["column"] = matrix.index.to_list()
    matrix = matrix.reset_index(drop=True)
    matrix = matrix[["row", "column", "matrix_value"]]

    return matrix
