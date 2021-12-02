"""
Author local impact plot
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/author_local_impact.png"
>>> author_local_impact(n_authors=20, directory=directory).savefig(file_name)


.. image:: images/author_local_impact_plot.png
    :width: 650px
    :align: center

"""


from .cleveland_dot_chart import cleveland_dot_chart
from .impact_indicators import impact_indicators


def author_local_impact(
    metric="h_index",
    n_authors=20,
    figsize=(6, 6),
    directory="./",
):
    indicators = impact_indicators("authors", directory=directory)[metric]
    indicators = indicators.sort_values(ascending=False).head(n_authors)
    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        title="Author Local Impact",
        xlabel=metric.replace("_", " ").title(),
        ylabel="Authors",
    )
