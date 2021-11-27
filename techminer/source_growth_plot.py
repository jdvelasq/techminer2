"""
Source growth plot
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/source_growth_plot.png"
>>> source_growth_plot(10, directory=directory).savefig(file_name)

.. image:: images/source_growth_plot.png
    :width: 700px
    :align: center


"""

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from .source_growth_table import source_growth_table


def source_growth_plot(n_sources=10, figsize=(8, 6), directory="./"):

    source_growth = source_growth_table(n_sources=n_sources, directory=directory)

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    for column in source_growth.columns:
        ax.plot(source_growth.index, source_growth[column], label=column)

    ax.tick_params(axis="x", labelsize=7)
    ax.tick_params(axis="y", labelsize=7)

    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(which="mayor", color="k", length=5)
    ax.tick_params(which="minor", color="k", length=2)

    for side in ["top", "bottom", "right"]:
        ax.spines[side].set_visible(False)

    ax.set_xlabel("Year", fontsize=9)
    ax.set_ylabel("Cum num documents", fontsize=9)
    ax.tick_params(axis="x", labelrotation=90)
    ax.grid(axis="y", color="gray", linestyle=":")
    ax.grid(axis="x", color="gray", linestyle=":")
    ax.legend(fontsize=8)

    fig.set_tight_layout(True)

    return fig
