# flake8: noqa
# pylint: disable=line-too-long
"""
.. _factor_cluster_map:

Factor Cluster Map 
===============================================================================


* Preparation

>>> import techminer2 as tm2
>>> root_dir = "data/regtech/"

>>> cooc_matrix = tm2p.co_occurrence_matrix(
...     root_dir="data/regtech/",
...     columns='author_keywords',
...     col_top_n=20,
... )

>>> factor_matrix = tm2p.factor_decomposition_kernel_pca(
...     cooc_matrix,
... )

>>> factor_clusters = tm2p.factor_clustering(
...    factor_matrix,
...    n_clusters=6,
... )


>>> fig = tm2p.factor_clusters_map(factor_clusters)

* Results:

>>> fig.write_html("sphinx/_static/factor_clusters_map.html")

.. raw:: html

    <iframe src="../../_static/factor_clusters_map.html" height="600px" width="100%" frameBorder="0"></iframe>


"""
import pandas as pd
import plotly.express as px

from .tlab.manifold_2d_map import manifold_2d_map


# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
def factor_clusters_map(
    factor_clusters,
    #
    # Plot params:
    dim_x=0,
    dim_y=1,
    node_size_min=40,
    node_size_max=60,
    textfont_size_min=8,
    textfont_size_max=20,
    xaxes_range=None,
    yaxes_range=None,
):
    """MDS 2D map."""

    frame = factor_clusters.centers_.iloc[:, [dim_x, dim_y]]
    node_occ = pd.Series(factor_clusters.labels_).value_counts().to_dict()
    node_occ = [node_occ[key] for key in sorted(node_occ.keys())]

    frame.index = [
        f"CL_{i:>02d} {occ}:0"
        for i, occ in zip(range(len(frame.index)), node_occ)
    ]

    fig = manifold_2d_map(
        node_x=frame[frame.columns[dim_x]],
        node_y=frame[frame.columns[dim_y]],
        node_text=frame.index.to_list(),
        node_occ=node_occ,
        node_color=px.colors.qualitative.Dark24,
        node_size_min=node_size_min,
        node_size_max=node_size_max,
        textfont_size_min=textfont_size_min,
        textfont_size_max=textfont_size_max,
        xaxes_range=xaxes_range,
        yaxes_range=yaxes_range,
    )

    return fig
