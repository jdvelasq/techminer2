"""
Line chart
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/line_chart.png"
>>> series = annual_indicators().global_citations
>>> line_chart(series, title="Citations per year").savefig(file_name)


.. image:: images/line_chart.png
    :width: 600px
    :align: center
"""

import matplotlib.pyplot as plt
import numpy as np

# from techminer.plots.shorten_ticklabels import shorten_ticklabels

TEXTLEN = 29
import matplotlib.ticker as tick


def _yaxis_format(y_value, y_position):
    y_formated = "{:1.0f}".format(y_value)
    return y_formated


def line_chart(
    series,
    color="k",
    figsize=(6, 6),
    linewidth=1,
    marker="o",
    markersize=8,
    title=None,
    xlabel=None,
    ylabel=None,
    alpha=1.0,
):

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.plot(
        series.index.astype(str),
        series.values,
        linewidth=linewidth,
        marker=marker,
        markersize=markersize,
        color=color,
        alpha=alpha,
    )

    if title is not None:
        ax.set_title(title, fontsize=10, color="dimgray", loc="left")

    if xlabel is None:
        xlabel = series.index.name
        xlabel = xlabel.replace("_", " ")
        xlabel = xlabel.title()
        ax.set_xlabel(xlabel, color="dimgray")

    if ylabel is None:
        ylabel = series.name
        ylabel = ylabel.replace("_", " ")
        ylabel = ylabel.title()
        ax.set_ylabel(ylabel, color="dimgray")

    ax.set_xticklabels(
        series.index.astype(str),
        rotation=90,
        horizontalalignment="center",
        fontsize=7,
        color="dimgray",
    )

    ax.set_yticklabels(
        ax.get_yticks(),
        fontsize=7,
        color="dimgray",
    )

    if series.dtype == np.int64:
        ax.yaxis.set_major_formatter(tick.FuncFormatter(_yaxis_format))

    for x in ["top", "right"]:
        ax.spines[x].set_visible(False)

    ax.spines["left"].set_color("dimgray")
    ax.spines["bottom"].set_color("dimgray")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.5)

    fig.set_tight_layout(True)

    return fig
