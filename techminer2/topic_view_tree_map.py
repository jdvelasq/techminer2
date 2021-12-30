"""
Topic View / Tree Map
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/topic_view_tree_map.png"
>>> topic_view_tree_map(
...     'author_keywords',
...     top_n=15, 
...     directory=directory,
... ).savefig(file_name)

.. image:: images/topic_view_tree_map.png
    :width: 700px
    :align: center


"""


from .topic_view import topic_view
from .tree_map import tree_map


def topic_view_tree_map(
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

    return tree_map(
        series=indicators,
        darkness=indicators,
        cmap=cmap,
        figsize=figsize,
    )
