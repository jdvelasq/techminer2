"""
Most relevant sources
===============================================================================

Plots the most relevant sources in the main collection.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_relevant_sources.png"
>>> most_relevant_sources(directory=directory).savefig(file_name)

.. image:: images/most_relevant_sources.png
    :width: 500px
    :align: center


"""


from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def most_relevant_sources(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
):
    indicators = column_indicators(
        directory=directory, column="iso_source_name"
    ).num_documents
    indicators = indicators.sort_values(ascending=False).head(top_n)
    indicators = indicators.astype(int)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most relevant sources",
        xlabel="Num Documents",
        ylabel="Source",
    )
