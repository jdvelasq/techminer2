"""
Gantt points chart
===============================================================================


>>> gantt_points_chart(annual_occurrence_matrix(directory, 'authors',  min_occ=3).head(10))

.. image:: images/gantt_points_chart.png
    :width: 400px
    :align: center


"""

import textwrap

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TEXTLEN = 40


def gantt_points_chart(
    annual_occurrence_matrix,
    figsize=(8, 8),
    fontsize=12,
    grid_lw=1.0,
    grid_c="gray",
    grid_ls=":",
    *args,
    **kwargs,
):

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    x = annual_occurrence_matrix.copy().transpose()
    if "linewidth" not in kwargs.keys() and "lw" not in kwargs.keys():
        kwargs["linewidth"] = 4
    if "marker" not in kwargs.keys():
        kwargs["marker"] = "o"
    if "markersize" not in kwargs.keys() and "ms" not in kwargs.keys():
        kwargs["markersize"] = 8
    if "color" not in kwargs.keys() and "c" not in kwargs.keys():
        kwargs["color"] = "k"
    for idx, col in enumerate(x.columns):
        w = x[col]
        w = w[w > 0]
        ax.plot(w.index, [idx] * len(w.index), **kwargs)

    ax.grid(axis="both", color=grid_c, linestyle=grid_ls, linewidth=grid_lw)

    ax.set_yticks(np.arange(len(x.columns)))
    ax.set_yticklabels(x.columns)
    ax.invert_yaxis()

    years = list(range(min(x.index), max(x.index) + 1))

    ax.set_xticks(years)
    ax.set_xticklabels(years)
    ax.tick_params(axis="x", labelrotation=90)

    for x in ["top", "right", "left"]:
        ax.spines[x].set_visible(False)

    ax.set_aspect("equal")

    return fig
