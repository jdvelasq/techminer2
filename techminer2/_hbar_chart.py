"""
HBar Chart
===============================================================================

>>> directory = "data/"
>>> file_name = "sphinx/images/_hbar_chart.png"
>>> from techminer2.column_indicators import column_indicators
>>> series = column_indicators(column="countries", directory=directory).num_documents.head(20)
>>> darkness = column_indicators("countries",directory=directory).global_citations.head(20)
>>> _hbar_chart(series, darkness).savefig(file_name)

.. image:: images/_horizontal_bar_chart.png
    :width: 700px
    :align: center


"""


import textwrap

import matplotlib.pyplot as plt
import numpy as np

# from techminer.plots.shorten_ticklabels import shorten_ticklabels

TEXTLEN = 29


def _hbar_chart(
    series,
    darkness=None,
    cmap="Greys",
    figsize=(9, 6),
    edgecolor="k",
    linewidth=0.5,
    title=None,
    xlabel=None,
    ylabel=None,
    zorder=10,
):
    """Make a horizontal bar plot."""
    darkness = series if darkness is None else darkness
    cmap = plt.cm.get_cmap(cmap)
    if max(darkness) == min(darkness):
        color = [cmap(0.1) for _ in darkness]
    else:
        color = [
            cmap(0.1 + 0.90 * (d - min(darkness)) / (max(darkness) - min(darkness)))
            for d in darkness
        ]

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.barh(
        y=range(len(series)),
        width=series,
        edgecolor=edgecolor,
        linewidth=linewidth,
        zorder=zorder,
        color=color,
    )

    if xlabel is None:
        xlabel = series.name
        xlabel = xlabel.replace("_", " ")
        xlabel = xlabel.title()

    if ylabel is None:
        ylabel = series.index.name
        ylabel = ylabel.replace("_", " ")
        ylabel = ylabel.title()

    ax.set_xlabel(xlabel, fontsize=7)
    ax.set_ylabel(ylabel, fontsize=7)

    yticklabels = series.index
    if yticklabels.dtype != "int64":
        yticklabels = [
            textwrap.shorten(
                text=yticklabels[i],
                width=TEXTLEN,
                placeholder="...",
                break_long_words=False,
            )
            for i in range(len(yticklabels))
        ]

    ax.invert_yaxis()
    ax.set_yticks(np.arange(len(series)))
    ax.set_yticklabels(yticklabels)

    for x in ["top", "right", "bottom"]:
        ax.spines[x].set_visible(False)

    ax.spines["left"].set_color("gray")

    ax.grid(axis="x", color="gray", linestyle=":")
    ax.tick_params(axis="x", labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    if title is not None:
        ax.set_title(
            title,
            fontsize=10,
            color="dimgray",
            loc="left",
        )

    fig.set_tight_layout(True)

    return fig
