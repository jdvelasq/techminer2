"""
Stacked bar chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/stacked_bar_chart.png"
>>> data = collaboration_indicators("countries", directory=directory)
>>> data = data.sort_values(by="num_documents", ascending=False)
>>> data = data[["single_publication", "multiple_publication"]].head(20)
>>> title = "Country collaboration indicators"
>>> stacked_bar_chart(data, title=title).savefig(file_name)

.. image:: images/stacked_bar_chart.png
    :width: 700px
    :align: center


"""


import matplotlib.pyplot as plt


def stacked_bar_chart(
    data,
    height=0.7,
    colors=[
        "tab:blue",
        "tab:orange",
        "tab:green",
        "tab:red",
        "tab:purple",
        "tab:brow",
        "tab:pink",
        "tab:gray",
        "tab:olive",
        "tab:cyan",
    ],
    figsize=(6, 6),
    edgecolor="k",
    linewidth=0.5,
    title=None,
    xlabel=None,
    ylabel=None,
):
    """Make a horizontal stacked bar plot."""

    data = data.copy()
    data.index = data.index.str.title()

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    left = data[data.columns[0]].map(lambda w: 0.0)
    for i_col, col in enumerate(data.columns):

        ax.barh(
            y=data.index,
            width=data[col],
            height=height,
            left=left,
            label=col.replace("_", " ").title(),
            color=colors[i_col],
            alpha=0.8,
            edgecolor=edgecolor,
            linewidth=linewidth,
        )
        left = left + data[col]

    if xlabel is not None:
        ax.set_xlabel(xlabel, fontsize=9)

    if ylabel is not None:
        ax.set_ylabel(ylabel, fontsize=9)

    if title is not None:
        ax.set_title(
            title,
            fontsize=10,
            color="dimgray",
            loc="left",
        )

    ax.invert_yaxis()

    for x in ["top", "right", "bottom"]:
        ax.spines[x].set_visible(False)

    ax.grid(axis="x", color="gray", linestyle=":")

    ax.spines["left"].set_color("dimgray")
    ax.tick_params(axis="x", labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    ax.legend(fontsize=7)

    fig.set_tight_layout(True)

    return fig
