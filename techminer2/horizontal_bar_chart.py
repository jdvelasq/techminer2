"""
Horizontal Bar Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/horizontal_bar_chart.png"
>>> horizontal_bar_chart(
...     'author_keywords', 
...     top_n=20, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/horizontal_bar_chart.png
    :width: 700px
    :align: center



"""
from ._horizontal_bar_chart import _horizontal_bar_chart
from .topic_view import topic_view


def horizontal_bar_chart(
    column,
    metric="num_documents",
    top_n=None,
    min_occ=1,
    max_occ=None,
    sort_values=None,
    sort_index=None,
    directory="./",
    #
    cmap="Greys",
    figsize=(8, 6),
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

    indicators = indicators[metric]

    return _horizontal_bar_chart(
        indicators,
        darkness=indicators,
        cmap=cmap,
        figsize=figsize,
        edgecolor="k",
        linewidth=0.5,
        title=None,
        xlabel=metric.replace("_", " ").title(),
        ylabel=column.replace("_", " ").title(),
        zorder=10,
    )
