"""
Column chart
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> column_chart(series=annual_indicators(directory)['num_documents'], darkness=annual_indicators(directory)['global_citations'])

.. image:: images/column_chart.png
    :width: 500px
    :align: center


"""

import textwrap

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

TEXTLEN = 40


def column_chart(
    series,
    darkness=None,
    cmap="Greys",
    figsize=(6, 6),
    fontsize=9,
    edgecolor="k",
    linewidth=0.5,
    zorder=10,
    ylabel=None,
    xlabel=None,
):
    """Make a vertical bar chart.

    See https://matplotlib.org/3.2.2/api/_as_gen/matplotlib.axes.Axes.bar.html.



    """
    darkness = series if darkness is None else darkness

    cmap = plt.cm.get_cmap(cmap)
    color = [
        cmap(0.1 + 0.90 * (d - min(darkness)) / (max(darkness) - min(darkness)))
        for d in darkness
    ]

    matplotlib.rc("font", size=fontsize)
    fig = plt.Figure(figsize=figsize)
    ax_ = fig.subplots()

    ax_.bar(
        x=range(len(series)),
        height=series,
        edgecolor=edgecolor,
        linewidth=linewidth,
        zorder=zorder,
        color=color,
    )

    if ylabel is None:
        ylabel = series.name
        ylabel = ylabel.replace("_", " ")
        ylabel = ylabel.title()

    if xlabel is None:
        xlabel = series.index.name
        xlabel = xlabel.replace("_", " ")
        xlabel = xlabel.title()

    ax_.set_xlabel(xlabel)
    ax_.set_ylabel(ylabel)

    xticklabels = series.index
    if xticklabels.dtype != "int64":
        xticklabels = [
            textwrap.shorten(text=text, width=TEXTLEN) for text in xticklabels
        ]

    ax_.set_xticks(np.arange(len(series)))
    ax_.set_xticklabels(xticklabels)
    ax_.tick_params(axis="x", labelrotation=90)

    for x in ["top", "right", "left"]:
        ax_.spines[x].set_visible(False)

    ax_.grid(axis="y", color="gray", linestyle=":")

    fig.set_tight_layout(True)

    return fig
