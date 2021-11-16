"""
Average citations per year
===============================================================================


>>> from techminer import *
>>> average_citations_per_year()

.. image:: images/average_citations_per_year.png
    :width: 600px
    :align: center


"""
import matplotlib.pyplot as plt
import matplotlib.ticker as tick

from .annual_indicators import annual_indicators


def _yaxis_format(y_value, y_position):
    y_formated = "{:1.0f}".format(y_value)
    return y_formated


def average_citations_per_year(
    directory=None,
    figsize=(6, 6),
    color="k",
):

    if directory is None:
        directory = "/workspaces/techminer-api/tests/data/"

    production = annual_indicators(directory)["mean_global_citations"]

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.plot(
        production.index.astype(str),
        production.values,
        "o-",
        markersize=8,
        color=color,
        alpha=1.0,
    )

    ax.set_title("Average citations per year", fontsize=10, color="dimgray", loc="left")
    ax.set_ylabel("Citations", color="dimgray")
    ax.set_xlabel("Year", color="dimgray")
    ax.set_xticklabels(
        production.index.astype(str),
        rotation=90,
        horizontalalignment="center",
        fontsize=7,
        color="dimgray",
    )
    ax.set_yticklabels(
        ax.get_yticks(),
        fontsize=7,
        color="dimgray",
    )

    ax.yaxis.set_major_formatter(
        tick.FuncFormatter(_yaxis_format),
    )

    ax.spines["left"].set_color("dimgray")
    ax.spines["bottom"].set_color("dimgray")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.5)
    return fig
