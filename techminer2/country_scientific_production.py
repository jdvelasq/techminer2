"""
Country Scientific Production
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/country_scientific_production.png"
>>> country_scientific_production(directory=directory).savefig(file_name)
 
.. image:: images/country_scientific_production.png
    :width: 700px
    :align: center

"""
import json
from os.path import dirname, join

import matplotlib.pyplot as plt
import numpy as np

from .column_indicators import column_indicators

TEXTLEN = 40


def country_scientific_production(
    cmap="Blues",
    figsize=(9, 5),
    directory="./",
):

    """Worldmap plot with the number of documents per country."""

    series = column_indicators("countries", directory=directory).num_documents

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()
    cmap = plt.cm.get_cmap(cmap)

    df = series.to_frame()

    df["color"] = series.map(
        lambda w: 0.1 + 0.9 * (w - series.min()) / (series.max() - series.min())
    )

    module_path = dirname(__file__)
    with open(join(module_path, "files/worldmap.data"), "r", encoding="utf-8") as file:
        countries = json.load(file)

    for country in countries.keys():
        data = countries[country]
        for item in data:
            ax.plot(item[0], item[1], "-k", linewidth=0.5)
            if country.lower() in df.index.tolist():
                ax.fill(item[0], item[1], color=cmap(df.color[country.lower()]))
    #
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    xleft = xmax - 0.02 * (xmax - xmin)
    xright = xmax
    xbar = np.linspace(xleft, xright, 10)
    ybar = np.linspace(ymin, ymin + (ymax - ymin), 100)
    xv, yv = np.meshgrid(xbar, ybar)
    z = yv / (ymax - ymin) - ymin
    ax.pcolormesh(xv, yv, z, cmap=cmap)
    #
    pos = np.linspace(ymin, ymin + (ymax - ymin), 11)
    value = [
        round(series.min() + (series.max() - series.min()) * i / 10, 0)
        for i in range(11)
    ]
    for i in range(11):
        ax.text(
            xright + 0.4 * (xright - xleft),
            pos[i],
            str(int(value[i])),
            ha="left",
            va="center",
        )

    ax.plot(
        [xleft - 0.1 * (xright - xleft), xleft - 0.1 * (xright - xleft)],
        [ymin, ymax],
        color="gray",
        linewidth=1,
    )
    for i in range(11):
        ax.plot(
            [xleft - 0.0 * (xright - xleft), xright],
            [pos[i], pos[i]],
            linewidth=2.0,
            color=cmap((11 - i) / 11),
        )

    ax.set_aspect("equal")
    ax.axis("on")
    ax.set_xticks([])
    ax.set_yticks([])

    ax.spines["bottom"].set_color("gray")
    ax.spines["top"].set_color("gray")
    ax.spines["right"].set_color("gray")
    ax.spines["left"].set_color("gray")

    ax.set_title(
        "country Scientific Production",
        fontsize=10,
        color="dimgray",
        loc="left",
    )

    fig.set_tight_layout(True)

    return fig
