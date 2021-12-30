"""
Topic View / Cleveland Chart
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/topic_view_cleveland_chart.jpg"
>>> topic_view_cleveland_chart(
...    column="author_keywords", 
...    top_n=20,
...    directory=directory,
... ).savefig(file_name)

.. image:: images/topic_view_cleveland_chart.jpg
    :width: 700px
    :align: center

"""


from .cleveland_dot_chart import cleveland_dot_chart
from .topic_view import topic_view


def topic_view_cleveland_chart(
    column,
    metric="num_documents",
    top_n=None,
    min_occ=1,
    max_occ=None,
    sort_values=None,
    sort_index=None,
    directory="./",
    #
    color="k",
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

    indicators = indicators[metric]

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        xlabel=metric.replace("_", " ").title(),
        ylabel=column.replace("_", " ").title(),
    )
