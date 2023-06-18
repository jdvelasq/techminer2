# flake8: noqa
"""
Matrix Subset (*) --- ChatGPT
===============================================================================



Example: Matrix subset for a occurrence matrix.
-------------------------------------------------------------------------------


>>> root_dir = "data/regtech/"

>>> import techminer2plus
>>> co_occ_matrix = techminer2plus.system.analyze.co_occ_matrix(
...    columns='author_keywords',
...    rows='authors',
...    col_top_n=10,
...    row_top_n=10,
...    root_dir=root_dir,
... )
>>> matrix_subset = techminer2plus.system.analyze.matrix_subset(
...    co_occ_matrix,
...    custom_items=['REGTECH', 'FINTECH'],
... )
>>> matrix_subset.matrix_
column             REGTECH 28:329  FINTECH 12:249
row                                              
Arner DW 3:185                  2               1
Buckley RP 3:185                2               1
Barberis JN 2:161               1               0
Butler T/1 2:041                2               2
Lin W 2:017                     2               0
Singh C 2:017                   2               0
Brennan R 2:014                 2               0
Crane M 2:014                   2               0



>>> matrix_subset.custom_items_
['REGTECH 28:329', 'FINTECH 12:249']


>>> print(matrix_subset.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the ['REGTECH', 'FINTECH'] and 'authors' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row               |   REGTECH 28:329 |   FINTECH 12:249 |
|:------------------|-----------------:|-----------------:|
| Arner DW 3:185    |                2 |                1 |
| Buckley RP 3:185  |                2 |                1 |
| Barberis JN 2:161 |                1 |                0 |
| Butler T/1 2:041  |                2 |                2 |
| Lin W 2:017       |                2 |                0 |
| Singh C 2:017     |                2 |                0 |
| Brennan R 2:014   |                2 |                0 |
| Crane M 2:014     |                2 |                0 |
<BLANKLINE>
<BLANKLINE>





Example: Matrix subset for a co-occurrence matrix.
-------------------------------------------------------------------------------


>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...    columns='author_keywords',
...    col_occ_range=(3, None),
...    root_dir=root_dir,
... )
>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    custom_items=['REGTECH', 'FINTECH', "COMPLIANCE", 'REGULATION', 
...        'FINANCIAL_SERVICES'],
... )
>>> matrix_subset.matrix_
column                          REGTECH 28:329  ...  FINANCIAL_SERVICES 04:168
row                                             ...                           
FINANCIAL_REGULATION 04:035                  2  ...                          2
ARTIFICIAL_INTELLIGENCE 04:023               2  ...                          0
ANTI_MONEY_LAUNDERING 04:023                 1  ...                          0
RISK_MANAGEMENT 03:014                       2  ...                          0
INNOVATION 03:012                            1  ...                          0
REGULATORY_TECHNOLOGY 03:007                 2  ...                          0
BLOCKCHAIN 03:005                            2  ...                          0
SUPTECH 03:004                               3  ...                          0
<BLANKLINE>
[8 rows x 5 columns]


>>> matrix_subset.custom_items_
['REGTECH 28:329', 'FINTECH 12:249', 'COMPLIANCE 07:030', 'REGULATION 05:164', 'FINANCIAL_SERVICES 04:168']




>>> print(matrix_subset.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the ['REGTECH', 'FINTECH', 'COMPLIANCE', 'REGULATION', 'FINANCIAL_SERVICES'] and 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   REGTECH 28:329 |   FINTECH 12:249 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   FINANCIAL_SERVICES 04:168 |
|:-------------------------------|-----------------:|-----------------:|--------------------:|--------------------:|----------------------------:|
| FINANCIAL_REGULATION 04:035    |                2 |                1 |                   0 |                   0 |                           2 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |                1 |                   1 |                   0 |                           0 |
| ANTI_MONEY_LAUNDERING 04:023   |                1 |                0 |                   0 |                   0 |                           0 |
| RISK_MANAGEMENT 03:014         |                2 |                2 |                   1 |                   2 |                           0 |
| INNOVATION 03:012              |                1 |                1 |                   0 |                   1 |                           0 |
| REGULATORY_TECHNOLOGY 03:007   |                2 |                1 |                   1 |                   1 |                           0 |
| BLOCKCHAIN 03:005              |                2 |                1 |                   1 |                   1 |                           0 |
| SUPTECH 03:004                 |                3 |                2 |                   1 |                   1 |                           0 |
<BLANKLINE>
<BLANKLINE>






Example: Matrix subset for an ego matrix.
-------------------------------------------------------------------------------


>>> matrix_subset = vantagepoint.analyze.matrix_subset(
...    co_occ_matrix,
...    custom_items=['REGTECH', 'FINTECH', "COMPLIANCE", 'REGULATION',
...        'FINANCIAL_SERVICES'],
...    is_ego_matrix=True,
... )
>>> matrix_subset.matrix_
column                          REGTECH 28:329  ...  SUPTECH 03:004
row                                             ...                
REGTECH 28:329                              28  ...               3
FINTECH 12:249                              12  ...               2
COMPLIANCE 07:030                            7  ...               1
REGULATION 05:164                            4  ...               1
FINANCIAL_SERVICES 04:168                    3  ...               0
FINANCIAL_REGULATION 04:035                  2  ...               0
ARTIFICIAL_INTELLIGENCE 04:023               2  ...               0
ANTI_MONEY_LAUNDERING 04:023                 1  ...               0
RISK_MANAGEMENT 03:014                       2  ...               1
INNOVATION 03:012                            1  ...               0
REGULATORY_TECHNOLOGY 03:007                 2  ...               1
BLOCKCHAIN 03:005                            2  ...               0
SUPTECH 03:004                               3  ...               3
<BLANKLINE>
[13 rows x 13 columns]



>>> matrix_subset.custom_items_
['REGTECH 28:329', 'FINTECH 12:249', 'COMPLIANCE 07:030', 'REGULATION 05:164', 'FINANCIAL_SERVICES 04:168']




>>> print(matrix_subset.prompt_)
Analyze the table below which contains values of co-occurrence (OCC) for the 'author_keywords' fields in a bibliographic dataset. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| row                            |   REGTECH 28:329 |   FINTECH 12:249 |   COMPLIANCE 07:030 |   REGULATION 05:164 |   FINANCIAL_SERVICES 04:168 |   FINANCIAL_REGULATION 04:035 |   ARTIFICIAL_INTELLIGENCE 04:023 |   ANTI_MONEY_LAUNDERING 04:023 |   RISK_MANAGEMENT 03:014 |   INNOVATION 03:012 |   REGULATORY_TECHNOLOGY 03:007 |   BLOCKCHAIN 03:005 |   SUPTECH 03:004 |
|:-------------------------------|-----------------:|-----------------:|--------------------:|--------------------:|----------------------------:|------------------------------:|---------------------------------:|-------------------------------:|-------------------------:|--------------------:|-------------------------------:|--------------------:|-----------------:|
| REGTECH 28:329                 |               28 |               12 |                   7 |                   4 |                           3 |                             2 |                                2 |                              1 |                        2 |                   1 |                              2 |                   2 |                3 |
| FINTECH 12:249                 |               12 |               12 |                   2 |                   4 |                           2 |                             1 |                                1 |                              0 |                        2 |                   1 |                              1 |                   1 |                2 |
| COMPLIANCE 07:030              |                7 |                2 |                   7 |                   1 |                           0 |                             0 |                                1 |                              0 |                        1 |                   0 |                              1 |                   1 |                1 |
| REGULATION 05:164              |                4 |                4 |                   1 |                   5 |                           1 |                             0 |                                0 |                              0 |                        2 |                   1 |                              1 |                   1 |                1 |
| FINANCIAL_SERVICES 04:168      |                3 |                2 |                   0 |                   1 |                           4 |                             2 |                                0 |                              0 |                        0 |                   0 |                              0 |                   0 |                0 |
| FINANCIAL_REGULATION 04:035    |                2 |                1 |                   0 |                   0 |                           2 |                             4 |                                0 |                              0 |                        0 |                   1 |                              0 |                   0 |                0 |
| ARTIFICIAL_INTELLIGENCE 04:023 |                2 |                1 |                   1 |                   0 |                           0 |                             0 |                                4 |                              1 |                        1 |                   0 |                              1 |                   1 |                0 |
| ANTI_MONEY_LAUNDERING 04:023   |                1 |                0 |                   0 |                   0 |                           0 |                             0 |                                1 |                              4 |                        0 |                   0 |                              0 |                   0 |                0 |
| RISK_MANAGEMENT 03:014         |                2 |                2 |                   1 |                   2 |                           0 |                             0 |                                1 |                              0 |                        3 |                   0 |                              2 |                   0 |                1 |
| INNOVATION 03:012              |                1 |                1 |                   0 |                   1 |                           0 |                             1 |                                0 |                              0 |                        0 |                   3 |                              0 |                   0 |                0 |
| REGULATORY_TECHNOLOGY 03:007   |                2 |                1 |                   1 |                   1 |                           0 |                             0 |                                1 |                              0 |                        2 |                   0 |                              3 |                   0 |                1 |
| BLOCKCHAIN 03:005              |                2 |                1 |                   1 |                   1 |                           0 |                             0 |                                1 |                              0 |                        0 |                   0 |                              0 |                   3 |                0 |
| SUPTECH 03:004                 |                3 |                2 |                   1 |                   1 |                           0 |                             0 |                                0 |                              0 |                        1 |                   0 |                              1 |                   0 |                3 |
<BLANKLINE>
<BLANKLINE>




# pylint: disable=line-too-long
"""
# from ..classes import MatrixSubset


# def matrix_subset(
#     obj,
#     custom_items,
#     is_ego_matrix=False,
# ):
#     """Extracts a subset of columns and associated rows from a matrix.

#     Args:
#         obj (Matrix): A co-occurrnce matrix object.
#         custom_items (list): A list of items to extract.
#         is_ego_matrix (bool): Whether the matrix is an ego matrix.

#     Returns:
#         MatrixSubset: A MatrixSubset object.

#     """

#     def extract_custom_item_positions(candidate_items, custom_items):
#         """Obtains the positions of topics in a list."""

#         item_positions = []
#         candidate_items = [col.split(" ")[:-1] for col in candidate_items]
#         candidate_items = [" ".join(col) for col in candidate_items]
#         for item in custom_items:
#             if item in candidate_items:
#                 item_positions.append(candidate_items.index(item))
#         item_positions = sorted(item_positions)

#         return item_positions

#     def generate_default_prompt(matrix, topics, other_criterion):
#         """Generates a ChatGPT prompt for a occurrence matrix."""

#         return (
#             "Analyze the table below which contains values of co-occurrence "
#             f"(OCC) for the {repr(topics)} and '{other_criterion}' fields "
#             "in a bibliographic dataset. Identify any notable patterns, "
#             "trends, or outliers in the data, and discuss their implications "
#             "for the research field. Be sure to provide a concise summary of "
#             "your findings in no more than 150 words."
#             f"\n\n{matrix.to_markdown()}\n\n"
#         )

#     def generate_prompt_for_ego_matrix(matrix, columns):
#         """Generates a ChatGPT prompt for a occurrence matrix."""

#         return (
#             "Analyze the table below which contains values of co-occurrence "
#             f"(OCC) for the '{columns}' fields "
#             "in a bibliographic dataset. Identify any notable patterns, "
#             "trends, or outliers in the data, and discuss their implications "
#             "for the research field. Be sure to provide a concise summary of "
#             "your findings in no more than 150 words."
#             f"\n\n{matrix.to_markdown()}\n\n"
#         )

#     def matrix_subset_for_non_ego_matrix(obj, custom_items):
#         """Non-ego matrix subset."""

#         if isinstance(custom_items, str):
#             custom_items = [custom_items]

#         matrix = obj.matrix_.copy()

#         item_positions = extract_custom_item_positions(
#             candidate_items=matrix.columns.tolist(), custom_items=custom_items
#         )
#         selected_items_ = matrix.columns[item_positions].tolist()

#         matrix = matrix.iloc[:, item_positions]
#         matrix = matrix.loc[matrix.sum(axis=1) > 0, :]

#         matrix = matrix.drop(
#             labels=matrix.columns.tolist(), axis=0, errors="ignore"
#         )

#         prompt = generate_default_prompt(matrix, custom_items, obj.rows_)

#         matrix_subset_ = MatrixSubset()
#         matrix_subset_.columns_ = obj.columns_
#         matrix_subset_.rows_ = obj.rows_
#         matrix_subset_.matrix_ = matrix
#         matrix_subset_.metric_ = obj.metric_
#         matrix_subset_.is_ego_matrix_ = is_ego_matrix
#         matrix_subset_.prompt_ = prompt
#         matrix_subset_.custom_items_ = selected_items_

#         return matrix_subset_

#     def matrix_subset_for_ego_matrix(obj, custom_items):
#         """Ego matrix subset."""

#         if isinstance(custom_items, str):
#             custom_items = [custom_items]

#         matrix = obj.matrix_.copy()

#         item_positions = extract_custom_item_positions(
#             candidate_items=matrix.columns.tolist(), custom_items=custom_items
#         )
#         selected_items_ = matrix.columns[item_positions].tolist()

#         matrix = matrix.iloc[:, item_positions]
#         matrix = matrix.loc[matrix.sum(axis=1) > 0, :]

#         candidates = matrix.index.tolist()
#         candidates = [col.split(" ")[:-1] for col in candidates]
#         candidates = [" ".join(col) for col in candidates]

#         matrix = obj.matrix_.copy()

#         item_positions = extract_custom_item_positions(
#             candidate_items=matrix.columns.tolist(), custom_items=candidates
#         )

#         matrix = matrix.iloc[:, item_positions]
#         matrix = matrix.iloc[item_positions, :]

#         prompt = generate_prompt_for_ego_matrix(matrix, obj.columns_)

#         matrix_subset_ = MatrixSubset()
#         matrix_subset_.columns_ = obj.columns_
#         matrix_subset_.rows_ = obj.rows_
#         matrix_subset_.matrix_ = matrix
#         matrix_subset_.metric_ = obj.metric_
#         matrix_subset_.is_ego_matrix_ = is_ego_matrix
#         matrix_subset_.prompt_ = prompt
#         matrix_subset_.custom_items_ = selected_items_

#         return matrix_subset_

#     #
#     # Main code:
#     #
#     if is_ego_matrix:
#         return matrix_subset_for_ego_matrix(obj, custom_items)

#     return matrix_subset_for_non_ego_matrix(obj, custom_items)
