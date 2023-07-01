# flake8: noqa
"""
List Cells In Matrix
===============================================================================

Creates a list that has a row for each cell in the original matrix. The list is
sorted by the value of the cell. The columns of the original matrix correspond
to the 'column' column of the list, and the rows of the original matrix
correspond to the 'row' column of the list. The value of the cell is stored in
the 'value' column of the list.


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> matrix = techminer2plus.auto_correlation_matrix(
...     rows_and_columns='authors',
...     top_n=10,
...     root_dir=root_dir,
... )

>>> cells_list = techminer2plus.list_cells_in_matrix(matrix)
>>> cells_list
AutoCorrCellsList(, shape=(22, 3))

>>> cells_list.df_.head()
                 row            column    CORR
0     Arner DW 3:185    Arner DW 3:185  1.0000
1   Buckley RP 3:185    Arner DW 3:185  1.0000
2  Barberis JN 2:161    Arner DW 3:185  0.7698
3     Arner DW 3:185  Buckley RP 3:185  1.0000
4   Buckley RP 3:185  Buckley RP 3:185  1.0000




    

# pylint: disable=line-too-long
"""
import textwrap
from dataclasses import dataclass

import pandas as pd

from ..auto_correlation_matrix import AutoCorrMatrix
from ..cross_correlation_matrix import CrossCorrMatrix

# from . import CoocMatrix


@dataclass
class AutoCorrCellsList:
    """List cells from an auto-correlation matrix."""

    rows_and_columns_: str
    df_: pd.DataFrame

    def __repr__(self):
        text = "AutoCorrCellsList("
        text += f", shape={self.df_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


@dataclass
class CrossCorrCellsList(AutoCorrCellsList):
    """Cross-correlation cells list."""


@dataclass
class CoocCellsList:
    """List cells from an co-occurrence matrix."""

    rows_: str
    columns_: str
    df_: pd.DataFrame

    def __repr__(self):
        text = "CoocCellsList("
        text += f", shape={self.df_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


def list_cells_in_matrix(obj):
    """List the cells in a matrix."""

    def transform_matrix_to_matrix_list(obj):
        """Transform a matrix object to a matrix list object."""

        matrix = obj.df_
        value_name = obj.metric_

        matrix = matrix.melt(
            value_name=value_name, var_name="column", ignore_index=False
        )
        matrix = matrix.reset_index()
        matrix = matrix.rename(columns={matrix.columns[0]: "row"})
        # matrix = matrix.sort_values(
        #     by=[value_name, "row", "column"], ascending=[False, True, True]
        # )
        matrix = matrix[matrix[value_name] > 0.0]
        matrix = matrix.reset_index(drop=True)

        return matrix

    #
    #
    # Main:
    #
    #
    cells_list = transform_matrix_to_matrix_list(obj)

    if isinstance(obj, AutoCorrMatrix):
        return AutoCorrCellsList(
            df_=cells_list,
            rows_and_columns_=obj.rows_and_columns_,
        )

    if isinstance(obj, CrossCorrMatrix):
        return CrossCorrCellsList(
            df_=cells_list,
            rows_and_columns_=obj.rows_and_columns_,
        )

    if isinstance(obj, CoocMatrix):
        return CoocCellsList(
            df_=cells_list,
            columns_=obj.columns_,
            rows_=obj.rows_,
        )

    return CellsList(
        df_=cells_list,
        from_=repr(type(obj)).split(".")[-1][:-2],
        rows_=obj.rows_,
        columns_=obj.columns_,
    )
