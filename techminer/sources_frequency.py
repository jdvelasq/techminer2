"""
Sources frequency
===============================================================================

Plots the most relevant sources in the main collection.


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/sources_frequency.png"
>>> sources_frequency(directory=directory).savefig(file_name)

.. image:: images/sources_frequency.png
    :width: 650px
    :align: center

>>> sources_frequency(directory=directory, plot=False).head()
iso_source_name
SUSTAINABILITY                   15
FINANCIAL INNOV                  11
J OPEN INNOV: TECHNOL MARK CO     8
E3S WEB CONF                      7
FRONTIER ARTIF INTELL             5
Name: num_documents, dtype: int64

"""


from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def sources_frequency(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
    plot=True,
):
    indicators = column_indicators(
        directory=directory, column="iso_source_name"
    ).num_documents
    indicators = indicators.astype(int)

    if plot is False:
        return indicators

    indicators = indicators.sort_values(ascending=False).head(top_n)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most relevant sources",
        xlabel="Num Documents",
        ylabel="Source",
    )
