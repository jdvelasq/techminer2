"""
Lotka Law's plot
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/lotka.png"
>>> lotka_plot(directory).savefig(file_name)

.. image:: images/lotka.png
    :width: 600px
    :align: center

"""

import matplotlib
import matplotlib.pyplot as plt

from .core_authors import core_authors


def lotka_plot(
    directory=None,
    cmap="Greys",
    figsize=(6, 6),
):
    """
    Returns a dataframe with the core analysis.

    Parameters
    ----------
    dirpath_or_records: str or list
        path to the directory or the records object.

    Returns
    -------
    pandas.DataFrame
        Dataframe with the core sources of the records
    """

    fig, ax_ = plt.subplots(figsize=figsize)
    cmap = plt.cm.get_cmap(cmap)
    color = cmap(0.6)

    data = core_authors(directory)
    percentage_authors = data["%"].map(lambda w: float(w[:-2])).tolist()
    percentage_authors.reverse()
    documents_written = data["Documents written per Author"].tolist()
    documents_written.reverse()
    total_authors = data["Num Authors"].max()
    theoretical = [total_authors / float(x * x) for x in documents_written]
    total_theoretical = sum(theoretical)
    perc_theoretical_authors = [w / total_theoretical * 100 for w in theoretical]

    ax_.plot(
        documents_written,
        percentage_authors,
        linestyle="-",
        linewidth=2,
        color="k",
    )
    ax_.fill_between(
        documents_written,
        percentage_authors,
        color=color,
        alpha=0.6,
    )

    ax_.plot(
        documents_written,
        perc_theoretical_authors,
        linestyle=":",
        linewidth=4,
        color="k",
    )

    for side in ["top", "right", "left", "bottom"]:
        ax_.spines[side].set_visible(False)

    ax_.grid(axis="y", color="gray", linestyle=":")
    ax_.grid(axis="x", color="gray", linestyle=":")
    ax_.tick_params(axis="x", labelsize=7)
    ax_.tick_params(axis="y", labelsize=7)
    ax_.set_ylabel("% of Authors", fontsize=9)
    ax_.set_xlabel("Documets written per Author", fontsize=9)

    ax_.set_title(
        "Frequency distribution of scientific productivity",
        fontsize=10,
        color="dimgray",
        loc="left",
    )

    fig.set_tight_layout(True)

    return fig
