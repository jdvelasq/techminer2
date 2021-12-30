"""
Topic View / Pie Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/topic_view_pie_chart.png"
>>> topic_view_pie_chart(
...     'author_keywords', 
...     top_n=15, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/topic_view_pie_chart.png
    :width: 700px
    :align: center



"""


from .pie_chart import pie_chart
from .topic_view import topic_view


def topic_view_pie_chart(
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
    cmap="Blues",
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

    return pie_chart(
        indicators,
        darkness=indicators,
        cmap=cmap,
        figsize=figsize,
        fontsize=9,
        wedgeprops={
            "width": 0.6,
            "edgecolor": "k",
            "linewidth": 0.5,
            "linestyle": "-",
            "antialiased": True,
        },
    )
