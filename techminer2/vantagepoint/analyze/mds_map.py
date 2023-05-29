"""
MDS Map (*) --- ChatGPT
===============================================================================

Plots the MDS of the co-occurrence matrix.

Examples
-------------------------------------------------------------------------------

>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__mds_map_0.html"

>>> from techminer2 import vantagepoint
>>> co_occ_matrix = vantagepoint.analyze.co_occ_matrix(
...     criterion='author_keywords',
...     topic_min_occ=2,
...     topics_length=20,
...     root_dir=root_dir,
... )
>>> chart = vantagepoint.analyze.mds_map(co_occ_matrix)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint__mds_map_0.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head()
                                 Dim_00    Dim_01
row                                              
regtech 28:329               -25.929804 -8.921119
fintech 12:249               -13.222318  2.094028
regulatory technology 07:037   2.927744 -6.204613
compliance 07:030             -3.750517 -5.291312
regulation 05:164             -3.462766  1.053675



"""
import pandas as pd
from sklearn.manifold import MDS

from ...classes import ManifoldMap
from ...scatter_plot import scatter_plot

N_COMPONENTS = 2


def mds_map(
    obj,
    # MDS parameters
    metric=True,
    n_init=4,
    max_iter=300,
    eps=0.001,
    n_jobs=None,
    random_state=0,
    dissimilarity="euclidean",
    # Map parameters
    node_size_min=30,
    node_size_max=70,
    textfont_size_min=10,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
):
    """Creates and clustering a co-occurrence network."""

    def extract_occ(axis_values):
        "Extracts occurrence values from axis values."
        occ = [x.split(" ")[-1] for x in axis_values]
        occ = [x.split(":")[1] for x in occ]
        occ = [int(x) for x in occ]
        return occ

    #
    # Main:
    #

    node_occ = extract_occ(obj.matrix_.columns.tolist())

    embedding = MDS(
        n_components=N_COMPONENTS,
        metric=metric,
        n_init=n_init,
        max_iter=max_iter,
        eps=eps,
        n_jobs=n_jobs,
        random_state=random_state,
        dissimilarity=dissimilarity,
    )

    matrix_transformed = embedding.fit_transform(obj.matrix_)

    table = pd.DataFrame(
        matrix_transformed,
        columns=[f"Dim_{dim:02d}" for dim in range(N_COMPONENTS)],
        index=obj.matrix_.index,
    )

    fig = scatter_plot(
        node_x=matrix_transformed[:, 0],
        node_y=matrix_transformed[:, 1],
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
