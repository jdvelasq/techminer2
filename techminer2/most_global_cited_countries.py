"""
Most Global Cited Countries
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/most_global_cited_countries.png"
>>> most_global_cited_countries(directory=directory).savefig(file_name)

.. image:: images/most_global_cited_countries.png
    :width: 700px
    :align: center




"""
from .topic_view_cleveland_chart import topic_view_cleveland_chart


def most_global_cited_countries(
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
):
    return topic_view_cleveland_chart(
        column="countries",
        metric="global_citations",
        top_n=top_n,
        min_occ=1,
        max_occ=None,
        sort_values=None,
        sort_index=None,
        directory=directory,
        #
        color=color,
        figsize=figsize,
    )
