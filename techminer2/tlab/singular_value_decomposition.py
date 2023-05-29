"""
Singular Value Decomposition
===============================================================================

Plots the SVD of the co-occurrence matrix normalized with the **mutualinfo**
measure.

The plot is based on the SVD technique used in T-LAB's comparative analysis.

**Algorithm**

1. Computes the co-occurrence matrix normalized with the **nutualinfo**
    association index.

2. Apply SVD to the co-occurrence matrix with `n_components=20`.

3. Plot the decomposed matrix.


>>> # working directory
>>> root_dir = "data/regtech/"
>>> # computes the co-occurrence matrix
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...     criterion='author_keywords',
...     topics_length=20,
...     root_dir=root_dir,
... )
>>> # computes the SVD
>>> from techminer2 import tlab
>>> svd = tlab.singular_value_decomposition(
...     co_occ_matrix,
...     dim_x=0,
...     dim_y=1,
... )
>>> file_name = "sphinx/_static/tlab__singular_value_decomposition.html"
>>> svd.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static/tlab__singular_value_decomposition.html"
    height="800px" width="100%" frameBorder="0"></iframe>


>>> svd.table_.head()
                                 Dim_00    Dim_01  ...    Dim_17        Dim_18
row                                                ...                        
regtech 28:329                32.386508 -2.623531  ...  0.017208 -1.110223e-16
fintech 12:249                17.171575  5.275711  ... -0.005000 -1.103810e-16
regulatory technology 07:037   3.500129  1.437108  ... -0.055078  8.428475e-16
compliance 07:030              8.945366 -4.175846  ... -0.027151 -3.330669e-16
regulation 05:164              6.700788  3.488011  ... -0.152399  9.285094e-16
<BLANKLINE>
[5 rows x 19 columns]


"""


import pandas as pd
from sklearn.decomposition import TruncatedSVD

from ..classes import CocMatrix, ManifoldMap
from ..matrix_normalization import matrix_normalization
from ..scatter_plot import scatter_plot


def singular_value_decomposition(
    obj,
    dim_x=0,
    dim_y=1,
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

    if isinstance(obj, CocMatrix):
        obj = matrix_normalization(
            obj,
            normalization="mutualinfo",
        )
    else:
        ValueError(
            "Invalid obj type. Must be a CocMatrix/TfidfMatrix instance."
        )

    node_occ = extract_occ(obj.matrix_.columns.tolist())
    matrix = obj.matrix_.copy()

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
