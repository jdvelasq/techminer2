"""
Heat Map
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> coc_matrix = co_occurrence_matrix(directory=directory, column='authors', min_occ=3)
>>> file_name = "/workspaces/techminer2/sphinx/images/co_occurrence_heat_map.png"
>>> heat_map(coc_matrix, cmap='Blues').savefig(file_name)

.. image:: images/co_occurrence_heat_map.png
    :width: 700px
    :align: center

"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

TEXTLEN = 40


def heat_map(
    matrix,
    cmap="Greys",
    figsize=(6, 6),
):
    """Plots a heatmap from a matrix."""
    matrix = matrix.copy()

    if isinstance(matrix.columns, pd.MultiIndex):
        matrix.columns = matrix.columns.get_level_values(0)
    if isinstance(matrix.index, pd.MultiIndex):
        matrix.index = matrix.index.get_level_values(0)

    fig = plt.figure(figsize=figsize)
    ax = fig.subplots()

    ax = sns.heatmap(
        matrix,
        ax=ax,
        cmap=cmap,
        vmax=0.3,
        square=True,
        linewidths=0.2,
        cbar=False,
        linecolor="gainsboro",
    )
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    ax.tick_params(axis="x", labelrotation=90)

    ax.set_xlabel("")
    ax.set_ylabel("")

    fig.set_tight_layout(True)

    return fig
