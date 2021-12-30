"""
Topic View / Vertical Bar Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/topic_view_vbar_chart.png"
>>> topic_view_vbar_chart(
...     column='author_keywords',
...     top_n=15,
...     directory=directory,
... ).savefig(file_name)

.. image:: images/topic_view_vbar_chart.png
    :width: 700px
    :align: center


"""

from .topic_view import topic_view
from .vertical_bar_chart import vertical_bar_chart


def topic_view_vbar_chart(
    column,
    metric="num_documents",
    top_n=None,
    min_occ=1,
    max_occ=None,
    sort_values=None,
    sort_index=None,
    directory="./",
    #
    figsize=(8, 6),
    cmap="Greys",
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

    return vertical_bar_chart(
        indicators,
        darkness=indicators,
        cmap=cmap,
        figsize=figsize,
        edgecolor="k",
        linewidth=0.5,
        title=None,
        xlabel=None,
        ylabel=None,
        zorder=10,
    )
