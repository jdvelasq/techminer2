# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _mds_2d_map:

Co-occurrence MDS 2D Map
===============================================================================

Plots the MDS (with 2 components) of the normalized co-occurrence matrix.


* Preparation

>>> import techminer2plus as tm2p
>>> root_dir = "data/regtech/"
>>> tm2p.co_occurrence_mds_2d_map(
...    columns='author_keywords',
...    col_top_n=20,
...    root_dir=root_dir,
... ).write_html("sphinx/_static/co_occurrence_mds_2d_map.html")

.. raw:: html

    <iframe src="../../../../_static/co_occurrence_mds_2d_map.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import pandas as pd
from sklearn.manifold import MDS

from .co_occurrence_matrix import co_occurrence_matrix
from .manifold_2d_map import manifold_2d_map
from .matrix_normalization import matrix_normalization


def co_occurrence_mds_2d_map(
    #
    # FUNCTION PARAMS:
    columns,
    rows=None,
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
    #
    # COLUMN PARAMS:
    col_top_n=None,
    col_occ_range=(None, None),
    col_gc_range=(None, None),
    col_custom_items=None,
    #
    # ROW PARAMS:
    row_top_n=None,
    row_occ_range=(None, None),
    row_gc_range=(None, None),
    row_custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """MDS 2D map."""

    cooc_matrix = co_occurrence_matrix(
        #
        # FUNCTION PARAMS:
        columns=columns,
        rows=rows,
        #
        # COLUMN PARAMS:
        col_top_n=col_top_n,
        col_occ_range=col_occ_range,
        col_gc_range=col_gc_range,
        col_custom_items=col_custom_items,
        #
        # ROW PARAMS:
        row_top_n=row_top_n,
        row_occ_range=row_occ_range,
        row_gc_range=row_gc_range,
        row_custom_items=row_custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    matrix = matrix_normalization(cooc_matrix, association_index)
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
    frame.index.name = cooc_matrix.index.name

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
