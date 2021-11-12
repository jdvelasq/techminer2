"""
Tree map
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/tests/data/"
>>> tree_map(series=annual_indicators(directory)['num_documents'], darkness=annual_indicators(directory)['global_citations'])

.. image:: images/tree_map.png
    :width: 500px
    :align: center

"""

import textwrap

import matplotlib
import matplotlib.pyplot as plt
import squarify

TEXTLEN = 40


def tree_map(
    series,
    darkness=None,
    cmap="Greys",
    figsize=(6, 6),
    fontsize=11,
    alpha=0.9,
):
    """Creates a classification plot.."""
    darkness = series if darkness is None else darkness

    matplotlib.rc("font", size=fontsize)
    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    cmap = plt.cm.get_cmap(cmap)

    labels = series.index.astype(str)
    labels = [textwrap.shorten(text=text, width=TEXTLEN) for text in labels]
    labels = [textwrap.wrap(text=text, width=15) for text in labels]
    labels = ["\n".join(text) for text in labels]

    colors = [
        cmap(0.4 + 0.6 * (d - darkness.min()) / (darkness.max() - darkness.min()))
        for d in darkness
    ]

    squarify.plot(
        sizes=series,
        label=labels,
        color=colors,
        alpha=alpha,
        ax=ax,
        pad=True,
        bar_kwargs={"edgecolor": "k", "linewidth": 0.5},
        text_kwargs={"color": "w", "fontsize": fontsize},
    )
    ax.axis("off")

    fig.set_tight_layout(True)

    return fig
