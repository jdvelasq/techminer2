"""
Column Timeline Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/column_timeline_chart.png"
>>> column_timeline_chart('author_keywords', min_occ=8, directory=directory).savefig(file_name)

.. image:: images/column_timeline_chart.png
    :width: 700px
    :align: center

>>> column_timeline_chart('author_keywords', min_occ=8, directory=directory, plot=False).head()
pub_year          2016  2017  2018  2019  2020  2021
author_keywords                                     
bank                 1     1     1     3     2     5
blockchain           0     2     3     4     2     6
covid-19             0     0     0     0     2     6
crowdfunding         0     0     2     1     2     3
cryptocurrencies     0     0     1     3     1     3

"""

import matplotlib.pyplot as plt

from .annual_occurrence_matrix import annual_occurrence_matrix


def column_timeline_chart(
    column,
    min_occ=2,
    figsize=(9, 6),
    directory="./",
    plot=True,
):
    production = annual_occurrence_matrix(
        column,
        min_occ=min_occ,
        directory=directory,
    )

    if plot is False:
        return production

    fig = plt.Figure(figsize=figsize)
    ax = fig.subplots()

    for i_row, row in production.iterrows():
        ax.plot(production.columns, row, "o-", label=i_row)

    ax.set_xticklabels(
        production.columns.astype(str),
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

    ax.spines["left"].set_color("dimgray")
    ax.spines["bottom"].set_color("dimgray")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(alpha=0.5, linestyle=":")

    ax.legend(fontsize="x-small")

    return fig
