"""
Cleveland Dot Chart
===============================================================================



>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/cleveland_dot_chart.png" 
>>> cleveland_dot_chart(
...     series=annual_indicators(directory).num_documents, 
... ).savefig(file_name)


.. image:: images/cleveland_dot_chart.png
    :width: 700px
    :align: center



"""
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
from matplotlib.ticker import MaxNLocator


def cleveland_dot_chart(
    series,
    color="k",
    figsize=(8, 5),
    markersize=60,
    title=None,
    xlabel=None,
    ylabel=None,
    alpha=1.0,
):

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    x_data = series.values
    y_data = series.index

    ax.scatter(
        x_data,
        y_data,
        color=color,
        s=markersize,
        alpha=alpha,
        zorder=10,
    )

    # ax.set_xlim(0 - 0.1, max(x_data) + 0.1)

    loc = plticker.MultipleLocator(1)
    ax.yaxis.set_major_locator(loc)
    ax.set_ylim(-0.5, len(series) - 0.5)
    ax.set_yticklabels([""] + series.index.tolist(), fontsize=9)

    if title is not None:
        ax.set_title(
            title,
            fontsize=12,
            # color="dimgray",
            loc="left",
        )

    if xlabel is not None:
        ax.set_xlabel(
            xlabel,
            fontsize=9,
            # color="dimgray",
        )

    if ylabel is not None:
        ax.set_ylabel(
            ylabel,
            fontsize=9,
            # color="dimgray",
        )

    for x in ["top", "right", "bottom"]:
        ax.spines[x].set_visible(False)

    ax.grid(axis="y", color="gray", linestyle=":", linewidth=0.5)
    ax.spines["left"].set_color("dimgray")
    # ax.tick_params(axis="x", colors="dimgray")
    # ax.tick_params(axis="y", colors="dimgray")
    ax.invert_yaxis()

    if series.dtype == "int64":
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))

    fig.set_tight_layout(True)

    return fig
