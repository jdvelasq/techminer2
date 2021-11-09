"""
Factor Analysis ---  cluster map
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"


.. image:: images/factor_cluster_map.png
    :width: 500px
    :align: center

"""

from typing import AsyncGenerator

from ._bubble_map import bubble_map

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def factor_cluster_map(
    centers_matrix,
    members_matrix,
    x_dim=0,
    y_dim=1,
    color_scheme="4q",
    figsize=(6, 6),
    fontsize=9,
    **kwargs,
):
    # computos
    matrix = centers_matrix.copy()
    # matrix.columns = matrix.columns.get_level_values(0)
    node_sizes = members_matrix.value_counts()
    node_sizes = node_sizes.sort_index(ascending=True)

    return bubble_map(
        node_x=centers_matrix.iloc[:, x_dim].tolist(),
        node_y=centers_matrix.iloc[:, y_dim].tolist(),
        node_clusters=range(centers_matrix.shape[0]),
        node_texts=matrix.index.tolist(),
        node_sizes=node_sizes,
        x_axis_at=0,
        y_axis_at=0,
        color_scheme=color_scheme,
        xlabel=f"Dim-{x_dim}",
        ylabel=f"Dim-{y_dim}",
        figsize=figsize,
        fontsize=fontsize,
    )
