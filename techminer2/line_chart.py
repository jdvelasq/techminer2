"""
Line Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/line_chart.png"
>>> line_chart(
...     'author_keywords', 
...     top_n=15, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/line_chart.png
    :width: 700px
    :align: center



"""

from ._line_chart import _line_chart
from .topic_view import topic_view


def line_chart(
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
    color="black",
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

    return _line_chart(
        indicators,
        color=color,
        figsize=figsize,
        linewidth=1,
        marker="o",
        markersize=8,
        title=None,
        xlabel=None,
        ylabel=None,
        alpha=1.0,
    )
