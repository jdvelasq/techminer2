"""
Most local cited sources
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_local_cited_sources.png"
>>> most_local_cited_sources(directory=directory).savefig(file_name)

.. image:: images/most_local_cited_sources.png
    :width: 500px
    :align: center


"""
from os.path import join

import matplotlib.pyplot as plt
import pandas as pd

from .column_indicators import column_indicators


def most_local_cited_sources(
    num_sources=20,
    cmap="Greys",
    figsize=(6, 6),
    directory="./",
):

    references = pd.read_csv(
        join(directory, "references.csv"), sep=",", encoding="utf-8"
    )
    references = references[["iso_source_name", "local_citations"]]
    references = references.groupby("iso_source_name").sum()
    references = references.sort_values(by="local_citations", ascending=False)
    sources = references.local_citations.head(num_sources)

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
    ax.set_title("Most local cited sources", fontsize=10, loc="left", color="k")
    ax.set_ylabel("Source", color="k")
    ax.set_xlabel("Local Citations", color="k")
    ax.set_yticklabels(
        sources.index,
        fontsize=7,
    )

    for item in ax.get_xticklabels():
        item.set_fontsize(7)
    ax.invert_yaxis()

    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_color("gray")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.set_tight_layout(True)
    return fig
