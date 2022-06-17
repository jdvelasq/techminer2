"""
RPYS (Reference Publication Year Spectroscopy)
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/rpys.png"
>>> rpys(directory=directory).savefig(file_name)

.. image:: images/rpys.png
    :width: 700px
    :align: center


"""
from os.path import join

import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import pandas as pd
from matplotlib.ticker import MaxNLocator

from techminer2._read_records import read_all_records


def _yaxis_format(y_value, y_position):
    y_formated = "{:1.0f}".format(y_value)
    return y_formated


def rpys(
    starting_year=None,
    ending_year=None,
    figsize=(8, 6),
    directory="./",
    plot=True,
):

    references = pd.read_csv(
        join(directory, "processed", "references.csv"), sep=",", encoding="utf-8"
    )
    references = references["pub_year"]
    references = references.dropna()
    references = references.value_counts()
    max_year = references.index.max()
    min_year = references.index.min()

    documents = read_all_records(directory)
    documents = documents["pub_year"]
    documents = documents.dropna()
    max_year = max(max_year, documents.max())
    min_year = min(min_year, documents.min())

    years = list(range(min_year, max_year + 1))
    num_references = pd.Series(0, index=years)
    for year in years:
        if year in references.index:
            num_references[year] = references[year]

    median = pd.Series(0, index=years)
    for year in years[4:]:
        median[year] = num_references.loc[year - 4 : year].median()

    indicator = num_references - median

    if starting_year is not None:
        indicator = indicator.loc[starting_year:]
        num_references = num_references.loc[starting_year:]

    if ending_year is not None:
        indicator = indicator.loc[:ending_year]
        num_references = num_references.loc[:ending_year]

    if plot is False:
        return indicator

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    ax.plot(
        num_references.index.astype(str),
        num_references.values,
        ".-",
        color="grey",
        alpha=0.5,
    )

    ax.plot(
        indicator.index.astype(str),
        indicator.values,
        ".-",
        color="k",
        alpha=1.0,
    )

    ax.set_title(
        "Reference Publication Year Spectroscopy",
        fontsize=12,
        color="dimgray",
        loc="left",
    )
    ax.set_ylabel("Cited References", color="dimgray")
    ax.set_xlabel("Year", color="dimgray")
    ax.set_xticklabels(
        num_references.index.astype(str),
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

    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    ax.yaxis.set_major_formatter(
        tick.FuncFormatter(_yaxis_format),
    )

    ax.spines["left"].set_color("dimgray")
    ax.spines["bottom"].set_color("dimgray")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.5)
    return fig
