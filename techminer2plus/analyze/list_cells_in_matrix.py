# flake8: noqa
"""
List Cells in Matrix
===============================================================================

Creates a list that has a row for each cell in the original matrix. The list is
sorted by the value of the cell. The columns of the original matrix correspond
to the 'column' column of the list, and the rows of the original matrix
correspond to the 'row' column of the list. The value of the cell is stored in
the 'value' column of the list.


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> matrix = techminer2plus.system.analyze.auto_correlation_matrix(
...     rows_and_columns='authors',
...     top_n=10,
...     root_dir=root_dir,
... )

>>> matrix_list = techminer2plus.system.analyze.list_cells_in_matrix(matrix)
>>> matrix_list.cells_list_.head()
                 row             column      CORR
0     Arner DW 3:185     Arner DW 3:185  1.000000
1  Barberis JN 2:161     Arner DW 3:185  0.774597
2     Arner DW 3:185  Barberis JN 2:161  0.774597
3  Barberis JN 2:161  Barberis JN 2:161  1.000000
4     Arman AA 2:000     Arman AA 2:000  1.000000



>>> print(matrix_list.prompt_)
Analyze the table below which contains the auto-correlation values for the \\
authors. High correlation values indicate that the topics tends to appear \\
together in the same document and forms a group. Identify any notable \\
patterns, trends, or outliers in the data, and discuss their implications \\
for the research field. Be sure to provide a concise summary of your \\
findings in no more than 150 words.
<BLANKLINE>
Table:
```
|    | row            | column            |   CORR |
|---:|:---------------|:------------------|-------:|
|  2 | Arner DW 3:185 | Barberis JN 2:161 |  0.775 |
```
<BLANKLINE>


# pylint: disable=line-too-long
"""
# from ..classes import (
#     CocMatrix,
#     CorrMatrix,
#     ListCellsInMatrix,
#     MatrixSubset,
#     NormCocMatrix,
# )
# from ..prompts import format_prompt_for_tables


# def list_cells_in_matrix(obj):
#     """List the cells in a matrix."""

#     def generate_prompt(obj):
#         """Generate a ChatGPT prompt."""

#         matrix = obj.cells_list_.copy()
#         matrix = matrix[matrix.row != matrix.column]
#         matrix = matrix[matrix.row < matrix.column]

#         if obj.columns_ == obj.rows_ and obj.metric_ == "CORR":
#             return prompt_for_auto_corr_matrix(obj, matrix)

#         if obj.columns_ != obj.rows_ and obj.metric_ == "CORR":
#             return prompt_for_cross_corr_matrix(obj, matrix)

#         if obj.columns_ == obj.rows_ and obj.metric_ == "OCC":
#             return prompt_for_co_occ_matrix(obj, matrix)

#         if obj.columns_ != obj.rows_ and obj.metric_ == "OCC":
#             return prompt_for_occ_matrix(obj, matrix)

#         raise ValueError("Invalid metric")

#     def prompt_for_auto_corr_matrix(obj, matrix):
#         """Prompt for auto-correlation matrix."""

#         main_text = (
#             "Analyze the table below which contains the auto-correlation "
#             f"values for the {obj.columns_}. High correlation "
#             "values indicate that the topics tends to appear together in the "
#             "same document and forms a group. Identify any notable patterns, "
#             "trends, or outliers in the data, and discuss their implications "
#             "for the research field. Be sure to provide a concise summary of "
#             "your findings in no more than 150 words."
#         )
#         table_text = matrix.round(3).to_markdown()
#         return format_prompt_for_tables(main_text, table_text)

#     def prompt_for_cross_corr_matrix(obj, matrix):
#         """Prompt for cross-correlation matrix."""

#         main_text = (
#             "Analyze the table below which contains the cross-correlation "
#             f"values for the {obj.columns_} based on the values "
#             f"of the {obj.rows_}. High correlation values "
#             f"indicate that the topics in {obj.columns_} are "
#             f"related based on the values of the {obj.rows_}. "
#             "Identify any notable patterns, trends, or outliers in the data, "
#             "and discuss their implications for the research field. Be sure "
#             "to provide a concise summary of your findings in no more than "
#             "150 words."
#             f"\n\n{matrix.round(3).to_markdown()}\n\n"
#         )
#         table_text = matrix.round(3).to_markdown()
#         return format_prompt_for_tables(main_text, table_text)

#     def prompt_for_co_occ_matrix(obj, matrix):
#         """Prompt for co-occurrence matrix."""

#         main_text = (
#             "Analyze the table below, which contains the the co-occurrence "
#             f"values for {obj.columns_}. Identify any notable "
#             "patterns, trends, or outliers in the data, and discuss their "
#             "implications for the research field. Be sure to provide a "
#             "concise summary of your findings in no more than 150 words."
#         )

#         table_text = matrix.to_markdown()
#         return format_prompt_for_tables(main_text, table_text)

#     def prompt_for_occ_matrix(obj, matrix):
#         """Prompt for co-occurrence matrix."""

#         main_text = (
#             "Analyze the table below, which contains the the occurrence "
#             f"values for {obj.columns_} and "
#             f"{obj.rows_}. Identify any notable patterns, "
#             "trends, or outliers in the data, and discuss their implications "
#             "for the research field. Be sure to provide a concise summary of "
#             "your findings in no more than 150 words."
#         )
#         table_text = matrix.to_markdown()
#         return format_prompt_for_tables(main_text, table_text)

#     def transform_matrix_to_matrix_list(obj):
#         """Transform a matrix object to a matrix list object."""

#         matrix = obj.matrix_
#         value_name = obj.metric_

#         matrix = matrix.melt(
#             value_name=value_name, var_name="column", ignore_index=False
#         )
#         matrix = matrix.reset_index()
#         matrix = matrix.rename(columns={"index": "row"})
#         # matrix = matrix.sort_values(
#         #     by=[value_name, "row", "column"], ascending=[False, True, True]
#         # )
#         matrix = matrix[matrix[value_name] > 0.0]
#         matrix = matrix.reset_index(drop=True)

#         return matrix

#     #
#     #
#     # Main:
#     #
#     #

#     results = ListCellsInMatrix()
#     results.cells_list_ = transform_matrix_to_matrix_list(obj)

#     if isinstance(obj, CorrMatrix):
#         results.columns_ = obj.rows_and_columns_
#         results.rows_ = obj.rows_and_columns_
#     elif isinstance(
#         obj,
#         (CocMatrix, MatrixSubset, NormCocMatrix),
#     ):
#         results.columns_ = obj.columns_
#         results.rows_ = obj.rows_
#     else:
#         raise ValueError("Invalid matrix type")

#     results.metric_ = obj.metric_
#     results.prompt_ = generate_prompt(results)

#     if isinstance(obj, MatrixSubset):
#         results.is_matrix_subset_ = True
#     else:
#         results.is_matrix_subset_ = False

#     return results
