"""
Source impact plot
===============================================================================



>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/source_impact_plot.png"
>>> source_impact_plot(20, directory=directory).savefig(file_name)

.. image:: images/source_impact_plot.png
    :width: 700px
    :align: center




"""


from .cleveland_dot_chart import cleveland_dot_chart
from .impact_indicators import impact_indicators


def source_impact_plot(
    top_n=20,
    metric="h_index",
    color="k",
    figsize=(6, 6),
    directory="./",
):
    indicators = impact_indicators(directory=directory, column="iso_source_name")[
        metric
    ]
    indicators = indicators.sort_values(ascending=False).head(top_n)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Source local impact",
        xlabel=metric.replace("_", " ").title(),
        ylabel="Source",
    )
