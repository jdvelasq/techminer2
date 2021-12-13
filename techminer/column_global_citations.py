"""
Column Global Citations
===============================================================================

Plots global citations by item in the selected column

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/column_global_citations.png"
>>> column_global_citations('countries', directory=directory).savefig(file_name)

.. image:: images/column_global_citations.png
    :width: 700px
    :align: center

>>> column_global_citations('countries', directory=directory, plot=False).head()
countries
germany           528
united states     503
united kingdom    500
china             333
australia         318
Name: global_citations, dtype: int64

"""

from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def column_global_citations(
    column,
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    indicators = column_indicators(directory=directory, column=column)[
        "global_citations"
    ]
    indicators = indicators.sort_values(ascending=False)

    if plot is False:
        return indicators

    indicators = indicators.head(top_n)

    return cleveland_dot_chart(
        indicators,
        color=color,
        figsize=figsize,
        xlabel="Total Citations",
        ylabel=column,
    )
