"""
Most cited countries plot
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_cited_countries.png"
>>> most_cited_countries_plot(directory=directory).savefig(file_name)

.. image:: images/most_cited_countries.png
    :width: 500px
    :align: center


"""

from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def most_cited_countries_plot(
    n_countries=20,
    color="k",
    figsize=(6, 6),
    directory="./",
):
    indicators = column_indicators(directory=directory, column="countries")[
        "num_documents"
    ]
    indicators = indicators.sort_values(ascending=False).head(n_countries)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        title="Most cited countries",
        xlabel="Total Citations",
        ylabel="Country",
    )
