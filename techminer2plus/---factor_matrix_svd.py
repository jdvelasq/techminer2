# flake8: noqa
# pylint: disable=line-too-long
"""
.. _svd_factor_matrix:

SVD Factor Matrix
===============================================================================

Factor matrix obtained by appliying SVD to the co-occurrence matrix. 

**Algorithm:**

1. Computes the co-occurrence matrix of the specified field.

2. Optionally, normalize the co-occurrence matrix.

3. Applies SVD to the co-occurrence matrix.

4. Returns the factor matrix.


>>> import techminer2plus
>>> cooc_matrix = techminer2plus.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )

>>> factor_matrix = techminer2plus.factor_matrix_svd(
...     cooc_matrix,
... )
>>> factor_matrix
FactorMatrixSVD(field='author_keywords', shape=(20, 2))

>>> factor_matrix.df_.round(3)
                                DIM_00  DIM_01
author_keywords                               
REGTECH 28:329                  32.386  -2.485
FINTECH 12:249                  17.168   5.393
REGULATORY_TECHNOLOGY 07:037     3.545   0.616
COMPLIANCE 07:030                8.944  -4.299
REGULATION 05:164                6.700   3.392
ANTI_MONEY_LAUNDERING 05:034     1.327  -1.020
FINANCIAL_SERVICES 04:168        3.996   1.500
FINANCIAL_REGULATION 04:035      2.615   0.848
ARTIFICIAL_INTELLIGENCE 04:023   2.957  -0.974
RISK_MANAGEMENT 03:014           3.757   1.615
INNOVATION 03:012                1.692   1.174
BLOCKCHAIN 03:005                2.774  -0.325
SUPTECH 03:004                   4.187   0.704
SEMANTIC_TECHNOLOGIES 02:041     2.892   1.421
DATA_PROTECTION 02:027           2.232   0.167
SMART_CONTRACTS 02:022           1.783  -0.695
CHARITYTECH 02:017               1.924  -1.240
ENGLISH_LAW 02:017               1.924  -1.240
ACCOUNTABILITY 02:014            2.303  -2.416
DATA_PROTECTION_OFFICER 02:014   2.303  -2.416



"""
import textwrap
from dataclasses import dataclass

import pandas as pd
from sklearn.decomposition import TruncatedSVD

from .matrix_normalization import matrix_normalization


@dataclass
class FactorMatrixSVD:
    """PCA factor matrix."""

    field_: str
    df_: pd.DataFrame
    prompt_: str

    def __repr__(self):
        text = "FactorMatrixSVD("
        text += f"field='{self.field_}'"
        text += f", shape={self.df_.shape}"
        text += ")"
        text = textwrap.fill(text, width=75, subsequent_indent="    ")
        return text


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def factor_matrix_svd(
    #
    # Specific params:
    cooc_matrix,
    estimator=None,
    association_index=None,
):
    """Creates a SVD factor matrix from the co-occurrence matrix.


    # pylint: disable=line-too-long
    """
    cooc_matrix = matrix_normalization(cooc_matrix, association_index)
    matrix = cooc_matrix.df_

    if estimator is None:
        estimator = TruncatedSVD()

    estimator.fit(matrix)

    transformed_matrix = estimator.transform(matrix)
    columns = [f"DIM_{i:>02d}" for i in range(transformed_matrix.shape[1])]

    matrix = pd.DataFrame(
        transformed_matrix,
        index=matrix.index,
        columns=columns,
    )
    matrix.index.name = cooc_matrix.rows_

    return FactorMatrixSVD(
        df_=matrix,
        field_=cooc_matrix.columns_,
        prompt_="TODO",
    )


# # pylint: disable=too-many-arguments
# # pylint: disable=too-many-locals
# def singular_value_decomposition(
#     obj,
#     dim_x=0,
#     dim_y=1,
#     # Technique parameters
#     is_2d=False,
#     # SVD parameters
#     algorithm="randomized",
#     n_iter=5,
#     n_oversamples=10,
#     power_iteration_normalizer="auto",
#     random_state=0,
#     tol=0.0,
#     # Map parameters
#     node_size_min=12,
#     node_size_max=50,
#     textfont_size_min=8,
#     textfont_size_max=20,
#     xaxes_range=None,
#     yaxes_range=None,
# ):
#     """Singular value decompositoin map."""

#     def extract_occ(axis_values):
#         "Extracts occurrence values from axis values."
#         occ = [x.split(" ")[-1] for x in axis_values]
#         occ = [x.split(":")[1] for x in occ]
#         occ = [int(x) for x in occ]
#         return occ

#     #
#     # Main:
#     #
#     if not isinstance(obj, (NormCocMatrix, TFMatrix)):
#         raise ValueError(
#             "Invalid obj type. Must be a NormCocMatrix/TFMatrix instance."
#         )

#     if isinstance(obj, TFMatrix) and obj.scheme_ != "binary":
#         raise ValueError("TFMatrix must be binary.")

#     node_occ = extract_occ(obj.matrix_.columns.tolist())
#     matrix = obj.matrix_.copy()
#     if isinstance(obj, TFMatrix):
#         matrix = matrix.transpose()

#     if is_2d:
#         max_dimensions = 2
#     else:
#         max_dimensions = min(20, len(matrix.columns) - 1)

#     decomposed_matrix = TruncatedSVD(
#         n_components=max_dimensions,
#         algorithm=algorithm,
#         n_oversamples=n_oversamples,
#         power_iteration_normalizer=power_iteration_normalizer,
#         n_iter=n_iter,
#         random_state=random_state,
#         tol=tol,
#     ).fit_transform(matrix)

#     table = pd.DataFrame(
#         decomposed_matrix,
#         columns=[f"Dim_{dim:02d}" for dim in range(max_dimensions)],
#         index=matrix.index,
#     )

#     fig = scatter_plot(
#         node_x=decomposed_matrix[:, dim_x],
#         node_y=decomposed_matrix[:, dim_y],
#         node_text=obj.matrix_.index,
#         node_occ=node_occ,
#         node_color=None,
#         node_size_min=node_size_min,
#         node_size_max=node_size_max,
#         textfont_size_min=textfont_size_min,
#         textfont_size_max=textfont_size_max,
#         xaxes_range=xaxes_range,
#         yaxes_range=yaxes_range,
#     )

#     manifoldmap = ManifoldMap()
#     manifoldmap.plot_ = fig
#     manifoldmap.table_ = table
#     manifoldmap.prompt_ = "TODO"

#     return manifoldmap
