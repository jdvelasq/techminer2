"""
Lotka Law's Plot
===============================================================================

"""

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

from .core_authors_report import core_authors
from .utils import *


def _lotka_plot_from_records(
    records,
    cmap,
    figsize,
    fontsize,
):

    matplotlib.rc("font", size=fontsize)
    fig, ax_ = plt.subplots(figsize=figsize)
    cmap = plt.cm.get_cmap(cmap)
    color = cmap(0.6)

    data = core_authors(records)
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
    ax_.set_ylabel("% of Authors")
    ax_.set_xlabel("Documets written per Author")

    fig.set_tight_layout(True)

    return fig


def _lotka_plot_from_directory(
    directory,
    cmap,
    figsize,
    fontsize,
):
    return _lotka_plot_from_records(
        records=load_filtered_documents(directory),
        cmap=cmap,
        figsize=figsize,
        fontsize=fontsize,
    )


def lotka_plot(
    dirpath_or_records,
    cmap="Greys",
    figsize=(8, 6),
    fontsize=11,
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
    if isinstance(dirpath_or_records, str):
        return _lotka_plot_from_directory(
            directory=dirpath_or_records,
            cmap=cmap,
            figsize=figsize,
            fontsize=fontsize,
        )
    elif isinstance(dirpath_or_records, pd.DataFrame):
        return _lotka_plot_from_records(
            records=dirpath_or_records,
            cmap=cmap,
            figsize=figsize,
            fontsize=fontsize,
        )
    else:
        raise TypeError("dirpath_or_records must be a string or a pandas.DataFrame")
