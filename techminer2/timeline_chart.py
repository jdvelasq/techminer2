"""
Timeline Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/timeline_chart.png"
>>> timeline_chart(
...     column='author_keywords', 
...     top_n=20,
...     directory=directory,
... ).savefig(file_name)

.. image:: images/timeline_chart.png
    :width: 700px
    :align: center


"""

import matplotlib.pyplot as plt

from .annual_occurrence_matrix import annual_occurrence_matrix
from .topic_view import topic_view


def timeline_chart(
    column,
    metric="num_documents",
    top_n=None,
    min_occ=1,
    max_occ=None,
    sort_values=None,
    sort_index=None,
    directory="./",
    #
    figsize=(9, 6),
):
    indicators = topic_view(
        column=column,
        metric=metric,
        top_n=top_n,
        min_occ=min_occ,
        max_occ=max_occ,
        sort_values=sort_values,
        sort_index=sort_index,
        directory=directory,
    )

    topics = indicators.index

    production = annual_occurrence_matrix(
        column,
        min_occ=1,
        directory=directory,
    )

    production = production.loc[topics]

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
