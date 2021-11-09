"""
Factor Analysis ---  members map
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"


.. image:: images/factor_members_map.png
    :width: 500px
    :align: center

"""

from ._bubble_map import bubble_map

# pyltin: disable=c0103
# pylint: disable=too-many-arguments
# pylint: disable=invalid-name


def factor_members_map(
    factor_matrix,
    members_matrix,
    x_dim=0,
    y_dim=1,
    color_scheme="clusters",
    figsize=(6, 6),
    fontsize=9,
    **kwargs,
):
    # computos
    matrix = factor_matrix.copy()
    node_sizes = matrix.index.get_level_values(1)

    return bubble_map(
        node_x=factor_matrix.iloc[:, x_dim].tolist(),
        node_y=factor_matrix.iloc[:, y_dim].tolist(),
        node_clusters=range(factor_matrix.shape[0]),
        node_texts=matrix.index.get_level_values(0).tolist(),
        node_sizes=node_sizes,
        x_axis_at=0,
        y_axis_at=0,
        color_scheme=color_scheme,
        xlabel=f"Dim-{x_dim}",
        ylabel=f"Dim-{y_dim}",
        figsize=figsize,
        fontsize=fontsize,
    )
