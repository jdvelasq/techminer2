# flake8: noqa
"""
Multidimensional Scaling (*) --- ChatGPT
===============================================================================

Plots the MDS of the co-occurrence matrix.



>>> root_dir = "data/regtech/"
>>> # ------------------------- Algorithm -------------------------
>>> # computes the co-occurrence matrix
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...     columns='author_keywords',
...     col_top_n=20,
...     root_dir=root_dir,
... )
>>> # normalizes the co-occurrence matrix
>>> norm_co_occ_matrix = vantagepoint.analyze.association_index(
...     co_occ_matrix, "association"
... )
>>> # computes the MDS
>>> from techminer2 import tlab
>>> mds = tlab.multidimensional_scaling(
...     norm_co_occ_matrix,
...     dim_x=0,
...     dim_y=1,
... )
>>> file_name = "sphinx/_static/tlab__multidimensional_scaling.html"
>>> mds.plot_.write_html(file_name)


.. raw:: html

    <iframe src="../../../../_static/tlab__multidimensional_scaling.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> mds.table_.head()
                             Dim_00    Dim_01  ...    Dim_17    Dim_18
row                                            ...                    
REGTECH 28:329             3.999987 -1.366373  ... -0.941161  2.964623
FINTECH 12:249             3.034797 -3.617296  ... -2.236131 -1.769722
COMPLIANCE 07:030          0.048056 -0.987758  ... -2.036287 -1.261271
REGULATION 05:164          0.672382 -0.361991  ...  0.349183  0.048651
FINANCIAL_SERVICES 04:168  0.040366 -0.356867  ...  0.333825  0.426246
<BLANKLINE>
[5 rows x 19 columns]

# pylint: disable=line-too-long
"""
# import pandas as pd
# from sklearn.manifold import MDS

# from ...classes import ManifoldMap, NormCocMatrix, TFMatrix
# from ...scatter_plot import scatter_plot


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

#     decomposed_matrix = MDS(
#         n_components=max_dimensions,
#         metric=metric,
#         n_init=n_init,
#         max_iter=max_iter,
#         eps=eps,
#         n_jobs=n_jobs,
#         random_state=random_state,
#         dissimilarity=dissimilarity,
#     ).fit_transform(obj.matrix_)

#     table = pd.DataFrame(
#         decomposed_matrix,
#         columns=[f"Dim_{dim:02d}" for dim in range(max_dimensions)],
#         index=obj.matrix_.index,
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