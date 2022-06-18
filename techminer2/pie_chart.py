"""
Pie Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/pie_chart.png"
>>> pie_chart(
...     'author_keywords', 
...     top_n=15, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/pie_chart.png
    :width: 700px
    :align: center



"""


from ._pie_chart import _pie_chart
from .topic_view import topic_view


def pie_chart(
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

    return _pie_chart(
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
