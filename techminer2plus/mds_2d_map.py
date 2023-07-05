# flake8: noqa
# pylint: disable=line-too-long
"""
.. _mds_2d_map:

MDS 2D Map 
===============================================================================

Plots the MDS (with 2 components) of the normalized co-occurrence matrix.


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"

* Object oriented interface

>>> fig = (
...     tm2p.records(root_dir=root_dir)
...     .co_occurrence_matrix(
...         columns='author_keywords',
...         col_top_n=20,
...     )
...     .mds_2d_map()
... )

.. raw:: html

    <iframe src="../../_static/mds_2d_map.html" height="800px" width="100%" frameBorder="0"></iframe>

    
* Functional interface

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... )
>>> fig = tm2p.mds_2d_map(cooc_matrix)

* Results:

>>> fig.write_html("sphinx/_static/mds_2d_map.html")

.. raw:: html

    <iframe src="../../_static/mds_2d_map.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import pandas as pd
from sklearn.manifold import MDS

from .manifold_2d_map import manifold_2d_map
from .matrix_normalization import matrix_normalization


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def mds_2d_map(
    cooc_matrix,
    association_index=None,
    #
    # MDS params:
    metric=True,
    n_init=4,
    max_iter=300,
    eps=0.001,
    n_jobs=None,
    random_state=0,
    dissimilarity="euclidean",
    #
    # Plot params:
    node_color="#8da4b4",
    node_size_min=12,
    node_size_max=50,
    textfont_size_min=8,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
):
    """MDS 2D map."""

    cooc_matrix = matrix_normalization(cooc_matrix, association_index)
    matrix = cooc_matrix.df_
    estimator = MDS(
        n_components=2,
        metric=metric,
        n_init=n_init,
        max_iter=max_iter,
        eps=eps,
        n_jobs=n_jobs,
        random_state=random_state,
        dissimilarity=dissimilarity,
    )

    transformed_matrix = estimator.fit_transform(matrix)
    columns = ["Dim_01", "Dim_02"]

    frame = pd.DataFrame(
        transformed_matrix,
        index=matrix.index,
        columns=columns,
    )
    frame.index.name = cooc_matrix.rows

    node_occ = [
        int(text.split(" ")[-1].split(":")[0])
        for text in matrix.index.to_list()
    ]

    fig = manifold_2d_map(
        node_x=frame.Dim_01,
        node_y=frame.Dim_02,
        node_text=frame.index.to_list(),
        node_occ=node_occ,
        node_color=node_color,
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )

    return fig
