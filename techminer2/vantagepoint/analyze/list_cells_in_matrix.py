"""
List Cells in Matrix
===============================================================================

Creates a list that has a row for each cell in the original matrix. The list is
sorted by the value of the cell. The columns of the original matrix correspond
to the 'column' column of the list, and the rows of the original matrix
correspond to the 'row' column of the list. The value of the cell is stored in
the 'value' column of the list.


>>> directory = "data/regtech/"

>>> from techminer2 import vantagepoint
>>> matrix = vantagepoint.analyze.auto_corr_matrix(
...     criterion='authors',
...     topics_length=10,
...     directory=directory,
... )

>>> matrix_list = vantagepoint.analyze.list_cells_in_matrix(matrix)
>>> matrix_list.matrix_.head()
                row            column  CORR
0    Arner DW 3:185    Arner DW 3:185   1.0
1    Arner DW 3:185  Buckley RP 3:185   1.0
2   Brennan R 2:014   Brennan R 2:014   1.0
3  Buckley RP 3:185    Arner DW 3:185   1.0
4  Buckley RP 3:185  Buckley RP 3:185   1.0

>>> print(matrix_list.prompt_)
Analyze the table below which contains the auto-correlation values for the authors. High correlation values indicate that the topics tends to appear together in the same document and forms a group. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
|    | row             | column           |   CORR |
|---:|:----------------|:-----------------|-------:|
|  1 | Arner DW 3:185  | Buckley RP 3:185 |  1     |
| 10 | Lin W 2:017     | Singh C 2:017    |  1     |
| 14 | Brennan R 2:014 | Crane M 2:014    |  1     |
| 16 | Hamdan A 2:018  | Sarea A 2:012    |  0.417 |
<BLANKLINE>
<BLANKLINE>

"""
from dataclasses import dataclass

from ... import chatgpt


@dataclass(init=False)
class _MatrixListResult:
    matrix_list_: None
    prompt_: None
    metric_: None
    criterion_for_columns_: None
    criterion_for_rows_: None


def list_cells_in_matrix(obj):
    """List the cells in a matrix."""

    results = _MatrixListResult()
    results.matrix_list_ = _transform_matrix_to_matrix_list(obj)
    results.criterion_for_columns_ = obj.criterion_for_columns_
    results.criterion_for_rows_ = obj.criterion_for_rows_
    results.metric_ = obj.metric_
    results.prompt_ = chatgpt.generate_prompt_for_list_cells_in_matrix(results)

    return results


def _transform_matrix_to_matrix_list(obj):
    matrix = obj.matrix_
    value_name = obj.metric_

    matrix = matrix.melt(
        value_name=value_name, var_name="column", ignore_index=False
    )
    matrix = matrix.reset_index()
    matrix = matrix.rename(columns={"index": "row"})
    matrix = matrix.sort_values(
        by=[value_name, "row", "column"], ascending=[False, True, True]
    )
    matrix = matrix[matrix[value_name] > 0.0]
    matrix = matrix.reset_index(drop=True)
    return matrix
