"""
2D-TSNE map --- ChatGPT
===============================================================================

Plots the TSNE of the normalized co-occurrence matrix. The plot is based on the
TSNE technique used in T-LAB's comparative analysis.

**Algorithm**

1. Computes the normalized co-occurrence matrix.

2. Apply TSNE to the co-occurrence matrix with `n_components=20`.

3. Plot the decomposed matrix.


>>> # working directory
>>> root_dir = "data/regtech/"
>>> # computes the co-occurrence matrix
>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...     criterion='author_keywords',
...     topics_length=50,
...     root_dir=root_dir,
... )
>>> # normalizes the co-occurrence matrix
>>> norm_co_occ_matrix = vantagepoint.analyze.association_index(
...     co_occ_matrix, "mutualinfo"
... )
>>> # computes the tsne
>>> from techminer2 import tlab
>>> tsne = tlab.word_associations.tsne_map(norm_co_occ_matrix)
>>> file_name = "sphinx/_static/tlab__word_associations__tsne_map.html"
>>> tsne.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/tlab__word_associations__tsne_map.html"
    height="800px" width="100%" frameBorder="0"></iframe>


>>> tsne.table_.head()
                                  Dim_00      Dim_01
row                                                 
regtech 28:329                656.460144 -160.212708
fintech 12:249                338.662903 -546.714478
regulatory technology 07:037 -146.625397  564.891052
compliance 07:030             558.554077   31.211735
regulation 05:164             -48.133255 -595.929932

"""


import pandas as pd
from sklearn.manifold import TSNE

from ...classes import ManifoldMap, NormCocMatrix
from ...scatter_plot import scatter_plot

MAX_DIMENSIONS = 2


def tsne_map(
    obj,
    # TSNE parameters
    perplexity=30.0,
    early_exaggeration=12.0,
    learning_rate="auto",
    n_iter=1000,
    n_iter_without_progress=300,
    min_grad_norm=1e-07,
    metric="euclidean",
    metric_params=None,
    init="pca",
    random_state=0,
    method="barnes_hut",
    angle=0.5,
    n_jobs=None,
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

    if not isinstance(obj, NormCocMatrix):
        raise ValueError("Invalid obj type. Must be a NormCocMatrix instance.")

    node_occ = extract_occ(obj.matrix_.columns.tolist())
    matrix = obj.matrix_.copy()

    decomposed_matrix = TSNE(
        n_components=MAX_DIMENSIONS,
        perplexity=perplexity,
        early_exaggeration=early_exaggeration,
        learning_rate=learning_rate,
        n_iter=n_iter,
        n_iter_without_progress=n_iter_without_progress,
        min_grad_norm=min_grad_norm,
        metric=metric,
        metric_params=metric_params,
        init=init,
        random_state=random_state,
        method=method,
        angle=angle,
        n_jobs=n_jobs,
    ).fit_transform(matrix)

    table = pd.DataFrame(
        decomposed_matrix,
        columns=[f"Dim_{dim:02d}" for dim in range(MAX_DIMENSIONS)],
        index=matrix.index,
    )

    fig = scatter_plot(
        node_x=decomposed_matrix[:, 0],
        node_y=decomposed_matrix[:, 1],
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
