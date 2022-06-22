"""
Bubble Chart (!)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/bubble_chart.png"
>>> matrix = co_occurrence_matrix(
...     column='authors', 
...     min_occ=2, 
...     directory=directory,
... )
>>> bubble_chart(matrix).savefig(file_name)

.. image:: images/bubble_chart.png
    :width: 700px
    :align: center

"""

import textwrap

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

TEXTLEN = 35


def collapse_text(w, width=TEXTLEN):
    if not isinstance(w, str):
        return w
    text_begining = " ".join(w.split(" ")[:-1])
    text_ending = w.split(" ")[-1]
    return textwrap.shorten(text=text_begining, width=TEXTLEN) + " " + text_ending


def bubble_chart(
    matrix,
    darkness=None,
    figsize=(11, 11),
    cmap="Greys",
    grid_lw=1.0,
    grid_c="gray",
    grid_ls=":",
    **kwargs,
):
    matrix = matrix.copy()

    # -----------------------------------------------------------------------------------
    if isinstance(matrix.columns, pd.MultiIndex):
        column_labels = collapse_text(matrix.columns.get_level_values(0))
    else:
        column_labels = collapse_text(matrix.columns)

    if isinstance(matrix.index, pd.MultiIndex):
        index_labels = collapse_text(matrix.index.get_level_values(0))
    else:
        index_labels = collapse_text(matrix.index)

    # -----------------------------------------------------------------------------------
    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    cmap = plt.cm.get_cmap(cmap)

    size_max = matrix.max().max()
    size_min = matrix.min().min()

    if darkness is None:
        darkness = matrix
    darkness = darkness.loc[:, matrix.columns]

    color_max = darkness.max().max()
    color_min = darkness.min().min()

    for idx in range(len(matrix.index.tolist())):

        sizes = [
            150 + 1000 * (w - size_min) / (size_max - size_min) if w != 0 else 0
            for w in matrix.iloc[idx, :]
        ]

        colors = [
            cmap(0.2 + 0.8 * (w - color_min) / (color_max - color_min))
            for w in darkness.iloc[idx, :]
        ]

        ax.scatter(
            list(range(len(matrix.columns))),
            [idx] * len(matrix.columns),
            marker="o",
            s=sizes,
            alpha=0.75,
            c=colors,
            edgecolors="k",
            zorder=11,
        )

    for idx in range(matrix.shape[0]):
        ax.axhline(
            idx,
            linewidth=grid_lw,
            color=grid_c,
            linestyle=grid_ls,
        )

    for idx in range(matrix.shape[1]):
        ax.axvline(
            idx,
            linewidth=grid_lw,
            color=grid_c,
            linestyle=grid_ls,
        )

    mean_color = 0.5 * (color_min + color_max)
    for idx_column_label, column_label in enumerate(column_labels):
        for idx_index_label, row in enumerate(index_labels):

            if matrix.iloc[idx_index_label][idx_column_label] != 0:

                if darkness.iloc[idx_index_label][idx_column_label] >= 0.8 * mean_color:
                    text_color = "w"
                else:
                    text_color = "k"

                ax.text(
                    idx_column_label,
                    idx_index_label,
                    "{}".format(matrix.iloc[idx_index_label][idx_column_label])
                    if matrix.iloc[idx_index_label][idx_column_label].dtype == "int64"
                    else "{:.2f}".format(
                        matrix.iloc[idx_index_label][idx_column_label]
                    ),
                    va="center",
                    ha="center",
                    zorder=12,
                    color=text_color,
                )

    ax.set_aspect("equal")

    ax.set_xlim(-1, len(matrix.columns))
    ax.set_ylim(-1, len(matrix.index) + 1)

    ax.set_xticks(np.arange(len(column_labels)))
    ax.set_xticklabels(column_labels)
    ax.tick_params(axis="x", labelrotation=90)
    ax.xaxis.tick_top()

    ax.invert_yaxis()
    ax.set_yticks(np.arange(len(index_labels)))
    ax.set_yticklabels(index_labels)

    for side in [
        "top",
        "right",
        "left",
        "bottom",
    ]:
        ax.spines[side].set_visible(False)

    fig.set_tight_layout(True)

    return fig
