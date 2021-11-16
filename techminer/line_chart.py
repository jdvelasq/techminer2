"""
Bar chart
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> line_chart(series=annual_indicators(directory)['num_documents'], darkness=annual_indicators(directory)['global_citations'])

.. image:: images/bar_chart.png
    :width: 400px
    :align: center


"""


import textwrap

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# from techminer.plots.shorten_ticklabels import shorten_ticklabels

TEXTLEN = 29


def line_chart(
    series,
    color="Greys",
    figsize=(6, 6),
    fontsize=9,
    linewidth=0.5,
    xlabel=None,
    ylabel=None,
    zorder=10,
):
    """Make a line plot.

    Returns:
        container: Container with all the bars and optionally errorbars.


    """

    matplotlib.rc("font", size=fontsize)
    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.plot(
        series.index,
        series,
        linewidth=linewidth,
        marker="o",
        zorder=zorder,
        color=color,
    )

    if xlabel is None:
        xlabel = series.index.name
        xlabel = xlabel.replace("_", " ")
        xlabel = xlabel.title()

    if ylabel is None:
        ylabel = series.name
        ylabel = ylabel.replace("_", " ")
        ylabel = ylabel.title()

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # yticklabels = series.index
    # if yticklabels.dtype != "int64":
    #     yticklabels = [
    #         textwrap.shorten(
    #             text=yticklabels[i],
    #             width=TEXTLEN,
    #             placeholder="...",
    #             break_long_words=False,
    #         )
    #         for i in range(len(yticklabels))
    #     ]

    # ax.invert_yaxis()
    # ax.set_yticks(np.arange(len(series)))
    # ax.set_yticklabels(yticklabels)

    for x in ["top", "right"]:
        ax.spines[x].set_visible(False)

    ax.grid(axis="x", color="gray", linestyle="-")
    ax.grid(axis="y", color="gray", linestyle="-")

    fig.set_tight_layout(True)

    return fig
