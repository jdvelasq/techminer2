"""
Most relevant sources
===============================================================================


>>> from techminer import *
>>> most_relevant_sources()

.. image:: images/most_relevant_sources.png
    :width: 500px
    :align: center


"""
import matplotlib.pyplot as plt

from .column_indicators import column_indicators


def most_relevant_sources(
    directory=None,
    num_sources=20,
    cmap="Greys",
    figsize=(6, 6),
):
    sources = column_indicators(directory=directory, column="iso_source_name")[
        "num_documents"
    ]
    sources = sources.sort_values(ascending=False).head(num_sources)

    cmap = plt.cm.get_cmap(cmap)
    color = [
        cmap(0.3 + 0.70 * (d - min(sources)) / (max(sources) - min(sources)))
        for d in sources
    ]

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.barh(
        sources.index,
        sources.values,
        color=color,
        alpha=0.7,
    )
    ax.set_title("Most relevant sources", fontsize=10, loc="left", color="k")
    ax.set_ylabel("Source", color="k")
    ax.set_xlabel("Num Documents", color="k")
    ax.set_yticklabels(
        sources.index,
        fontsize=7,
    )

    # ax.set_xticklabels(
    #     sources.sort_values(ascending=True).values,
    #     fontsize=7,
    # )
    for item in ax.get_xticklabels():
        item.set_fontsize(7)
    ax.invert_yaxis()

    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("gray")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # ax.grid(alpha=0.5)
    fig.set_tight_layout(True)
    return fig
