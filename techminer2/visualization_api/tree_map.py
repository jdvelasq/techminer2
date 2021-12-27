"""
Tree Map
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/tree_map.png"
>>> series = annual_indicators(directory).num_documents
>>> darkness = annual_indicators(directory).global_citations
>>> tree_map(series=series, darkness=darkness).savefig(file_name)

.. image:: images/tree_map.png
    :width: 700px
    :align: center

"""

import textwrap

import matplotlib.pyplot as plt
import squarify

TEXTLEN = 40


def tree_map(
    series,
    darkness=None,
    cmap="Greys",
    figsize=(6, 6),
):
    """Creates a classification plot.."""

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
        alpha=0.9,
        ax=ax,
        pad=True,
        bar_kwargs={"edgecolor": "k", "linewidth": 0.5},
        text_kwargs={"color": "w", "fontsize": 9},
    )
    ax.axis("off")

    fig.set_tight_layout(True)

    return fig
