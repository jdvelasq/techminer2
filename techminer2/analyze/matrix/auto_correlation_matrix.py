# flake8: noqa
"""
Auto-correlation Matrix
===============================================================================

Returns an auto-correlation matrix.


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> corr_matrix = techminer2plus.system.analyze.auto_correlation_matrix(
...     rows_and_columns='authors',
...     occ_range=(2, None),
...     root_dir=root_dir,
... )
>>> corr_matrix.matrix_



>>> print(corr_matrix.prompt_)

# pylint: disable=line-too-long
"""

# from ..classes import CorrMatrix
# from ..prompts import format_prompt_for_tables
# from .compute_corr_matrix import compute_corr_matrix
# from .tf_matrix import tf_matrix


# # pylint: disable=too-many-arguments
# # pylint: disable=too-many-locals
# def auto_correlation_matrix(
#     rows_and_columns,
#     method="pearson",
#     # Item filters:
#     top_n=None,
#     occ_range=None,
#     gc_range=None,
#     custom_items=None,
#     # Database params:
#     root_dir="./",
#     database="main",
#     year_filter=None,
#     cited_by_filter=None,
#     **filters,
# ):
#     """Returns an auto-correlation."""

#     def generate_prompt(obj):
#         prompt = (
#             "Your task is to generate a short paragraph of a research paper "
#             "analyzing the auto-correlation values between the items of the "
#             f"column '{obj.rows_and_columns_}' of a bibliographic dataset.\n\n"
#             "Analyze the table below which contains the auto-correlation "
#             f"values for the '{obj.rows_and_columns_}'. High correlation values "
#             "indicate that the items tends to appear together in the same "
#             "document and forms a group. Identify any notable patterns, "
#             "trends, or outliers in the data, and discuss their implications "
#             "for the research field. Be sure to provide a concise summary of "
#             "your findings, in at most 50 words."
#             f"\n\n{obj.matrix_.round(3).to_markdown()}\n\n"
#         )
#         return prompt

#     #
#     # Main:
#     #
#     data_matrix = tf_matrix(
#         field=rows_and_columns,
#         # Item filters:
#         top_n=top_n,
#         occ_range=occ_range,
#         gc_range=gc_range,
#         custom_items=custom_items,
#         # Database params:
#         root_dir=root_dir,
#         database=database,
#         year_filter=year_filter,
#         cited_by_filter=cited_by_filter,
#         **filters,
#     )

#     corr_matrix = CorrMatrix()
#     corr_matrix.rows_and_columns_ = rows_and_columns
#     corr_matrix.cross_with_ = None
#     corr_matrix.method_ = method
#     corr_matrix.metric_ = "CORR"
#     corr_matrix.matrix_ = compute_corr_matrix(
#         method=method, data_matrix=data_matrix
#     )
#     corr_matrix.prompt_ = generate_prompt(corr_matrix)

#     return corr_matrix
