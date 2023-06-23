# flake8: noqa
"""
MDS 2D Map 
===============================================================================

Plots the MDS (with 2 components) of the normalized co-occurrence matrix.



>>> import techminer2plus
>>> cooc_matrix = techminer2plus.analyze.matrix.co_occurrence_matrix(
...     columns='author_keywords',
...     col_top_n=30,
...     root_dir="data/regtech/",
... )
>>> file_name = "sphinx/_static/analyze/map/mds_2d_map.html"
>>> chart = techminer2plus.analyze.map.mds_2d_map(cooc_matrix)
>>> chart.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../_static//analyze/map/mds_2d_map.html" height="800px" width="100%" frameBorder="0"></iframe>


>>> chart.table_.head()
                                 Dim_01     Dim_02
author_keywords                                   
REGTECH 28:329               -17.158842 -23.166553
FINTECH 12:249                -4.770553 -13.727826
REGULATORY_TECHNOLOGY 07:037  -6.482699   2.450538
COMPLIANCE 07:030              2.580874  -7.547167
REGULATION 05:164             -3.354086  -3.505347




# pylint: disable=line-too-long
"""
import pandas as pd
from sklearn.manifold import MDS

from ...classes import ManifoldMap
from ...manifold_2d_map import manifold_2d_map
from ..matrix.matrix_normalization import matrix_normalization


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
    matrix = cooc_matrix.matrix_
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
    frame.index.name = cooc_matrix.rows_

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

    manifold_map = ManifoldMap()
    manifold_map.plot_ = fig
    manifold_map.table_ = frame
    manifold_map.method_ = "MDS"

    return manifold_map
