"""
Topic View / Word Cloud
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/topic_view_word_cloud.png"
>>> topic_view_word_cloud(
...     column='author_keywords', 
...     top_n=50, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/topic_view_word_cloud.png
    :width: 700px
    :align: center


"""

from ._word_cloud import _word_cloud
from .topic_view import topic_view


def topic_view_word_cloud(
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

    return _word_cloud(
        series=indicators,
        darkness=indicators,
        cmap=cmap,
        figsize=figsize,
    )
