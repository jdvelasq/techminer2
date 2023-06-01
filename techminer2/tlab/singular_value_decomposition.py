# flake8: noqa
"""
Singular Value Decomposition --- ChatGPT
===============================================================================

Plots the SVD of the normalized co-occurrence matrix. The plot is based on the 
SVD technique used in T-LAB's comparative analysis.



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
>>> # computes the SVD
>>> from techminer2 import tlab
>>> svd = tlab.singular_value_decomposition(
...     norm_co_occ_matrix,
...     dim_x=0,
...     dim_y=1,
... )
>>> file_name = "sphinx/_static/tlab__singular_value_decomposition.html"
>>> svd.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/tlab__singular_value_decomposition.html"
    height="800px" width="100%" frameBorder="0"></iframe>


>>> svd.table_.head()
                                 Dim_00     Dim_01  ...    Dim_17    Dim_18
row                                                 ...                    
regtech 28:329                12.972062  10.391976  ...  0.012216  0.001943
fintech 12:249                10.874094  -7.841626  ...  0.005265  0.000956
regulatory technology 07:037   3.073117  -0.538119  ...  0.011494 -0.001101
compliance 07:030              6.628352  -3.686916  ...  0.019177 -0.001415
regulation 05:164              5.894711  -0.250128  ... -0.060850  0.002620
<BLANKLINE>
[5 rows x 19 columns]

# pylint: disable=line-too-long
"""


import pandas as pd
from sklearn.decomposition import TruncatedSVD

from ..classes import ManifoldMap, NormCocMatrix, TFMatrix
from ..scatter_plot import scatter_plot
from ..vantagepoint.analyze.association_index import association_index


def singular_value_decomposition(
    obj,
    dim_x=0,
    dim_y=1,
    # Technique parameters
    is_2d=False,
    # SVD parameters
    algorithm="randomized",
    n_iter=5,
    n_oversamples=10,
    power_iteration_normalizer="auto",
    random_state=0,
    tol=0.0,
    # Map parameters
    node_size_min=12,
    node_size_max=50,
    textfont_size_min=8,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
):
    """Singular value decompositoin map."""

    def extract_occ(axis_values):
        "Extracts occurrence values from axis values."
        occ = [x.split(" ")[-1] for x in axis_values]
        occ = [x.split(":")[1] for x in occ]
        occ = [int(x) for x in occ]
        return occ

    #
    # Main:
    #
    if not isinstance(obj, (NormCocMatrix, TFMatrix)):
        raise ValueError(
            "Invalid obj type. Must be a NormCocMatrix/TFMatrix instance."
        )

    if isinstance(obj, TFMatrix) and obj.scheme_ != "binary":
        raise ValueError("TFMatrix must be binary.")

    node_occ = extract_occ(obj.matrix_.columns.tolist())
    matrix = obj.matrix_.copy()
    if isinstance(obj, TFMatrix):
        matrix = matrix.transpose()

    if is_2d:
        max_dimensions = 2
    else:
        max_dimensions = min(20, len(matrix.columns) - 1)

    decomposed_matrix = TruncatedSVD(
        n_components=max_dimensions,
        algorithm=algorithm,
        n_oversamples=n_oversamples,
        power_iteration_normalizer=power_iteration_normalizer,
        n_iter=n_iter,
        random_state=random_state,
        tol=tol,
    ).fit_transform(matrix)

    table = pd.DataFrame(
        decomposed_matrix,
        columns=[f"Dim_{dim:02d}" for dim in range(max_dimensions)],
        index=matrix.index,
    )

    fig = scatter_plot(
        node_x=decomposed_matrix[:, dim_x],
        node_y=decomposed_matrix[:, dim_y],
        node_text=obj.matrix_.index,
        node_occ=node_occ,
        node_color=None,
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )

    manifoldmap = ManifoldMap()
    manifoldmap.plot_ = fig
    manifoldmap.table_ = table
    manifoldmap.prompt_ = "TODO"

    return manifoldmap
