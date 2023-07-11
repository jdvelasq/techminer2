# flake8: noqa
# pylint: disable=line-too-long
"""
MDS Factor Matrix
===============================================================================

Factor matrix obtained by appliying MDS to the co-occurrence matrix. 

**Algorithm:**

1. Computes the co-occurrence matrix of the specified field.

2. Normalize the co-occurrence matrix.

3. Applies MDS to the co-occurrence matrix.

4. Returns the factor matrix.



>>> import techminer2plus
>>> cooc_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )

>>> mds_factor_matrix = techminer2plus.analyze.matrix.mds_factor_matrix(
...     cooc_matrix,
... )
>>> mds_factor_matrix.table_.round(3)



"""
import pandas as pd
from sklearn.manifold import MDS

# from ...classes import MdsFactorMatrix
# from .matrix_normalization import matrix_normalization


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def mds_factor_matrix(
    #
    # Specific params:
    cooc_matrix,
    estimator=None,
    association_index=None,
):
    """Creates a MDS factor matrix from the co-occurrence matrix.


    # pylint: disable=line-too-long
    """
    cooc_matrix = matrix_normalization(cooc_matrix, association_index)
    matrix = cooc_matrix.matrix_

    if estimator is None:
        estimator = MDS()

    estimator.fit(matrix)

    transformed_matrix = estimator.transform(matrix)
    columns = [f"DIM_{i:>02d}" for i in range(transformed_matrix.shape[1])]

    matrix = pd.DataFrame(
        transformed_matrix,
        index=matrix.index,
        columns=columns,
    )
    matrix.index.name = cooc_matrix.rows_

    factor_matrix = MdsFactorMatrix()
    factor_matrix.table_ = matrix
    factor_matrix.field_ = cooc_matrix.columns_
    factor_matrix.prompt_ = "TODO"

    return factor_matrix


# def multidimensional_scaling(
#     obj,
#     dim_x=0,
#     dim_y=1,
#     # Technique parameters
#     is_2d=False,
#     # MDS parameters
#     metric=True,
#     n_init=4,
#     max_iter=300,
#     eps=0.001,
#     n_jobs=None,
#     random_state=0,
#     dissimilarity="euclidean",
#     # Map parameters
#     node_size_min=12,
#     node_size_max=50,
#     textfont_size_min=8,
#     textfont_size_max=20,
#     xaxes_range=None,
#     yaxes_range=None,
# ):
#     """MDS map of a co-occurrence network."""

# def extract_occ(axis_values):
#     "Extracts occurrence values from axis values."
#     occ = [x.split(" ")[-1] for x in axis_values]
#     occ = [x.split(":")[1] for x in occ]
#     occ = [int(x) for x in occ]
#     return occ

# #
# # Main:
# #
# if not isinstance(obj, (NormCocMatrix, TFMatrix)):
#     raise ValueError(
#         "Invalid obj type. Must be a NormCocMatrix/TFMatrix instance."
#     )

# if isinstance(obj, TFMatrix) and obj.scheme_ != "binary":
#     raise ValueError("TFMatrix must be binary.")

# node_occ = extract_occ(obj.matrix_.columns.tolist())
# matrix = obj.matrix_.copy()
# if isinstance(obj, TFMatrix):
#     matrix = matrix.transpose()

# if is_2d:
#     max_dimensions = 2
# else:
#     max_dimensions = min(20, len(matrix.columns) - 1)

# decomposed_matrix = MDS(
#     n_components=max_dimensions,
#     metric=metric,
#     n_init=n_init,
#     max_iter=max_iter,
#     eps=eps,
#     n_jobs=n_jobs,
#     random_state=random_state,
#     dissimilarity=dissimilarity,
# ).fit_transform(obj.matrix_)

# table = pd.DataFrame(
#     decomposed_matrix,
#     columns=[f"Dim_{dim:02d}" for dim in range(max_dimensions)],
#     index=obj.matrix_.index,
# )

# fig = scatter_plot(
#     node_x=decomposed_matrix[:, dim_x],
#     node_y=decomposed_matrix[:, dim_y],
#     node_text=obj.matrix_.index,
#     node_occ=node_occ,
#     node_color=None,
#     node_size_min=node_size_min,
#     node_size_max=node_size_max,
#     textfont_size_min=textfont_size_min,
#     textfont_size_max=textfont_size_max,
#     xaxes_range=xaxes_range,
#     yaxes_range=yaxes_range,
# )

# manifoldmap = ManifoldMap()
# manifoldmap.plot_ = fig
# manifoldmap.table_ = table
# manifoldmap.prompt_ = "TODO"

# return manifoldmap
