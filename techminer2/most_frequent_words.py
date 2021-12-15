"""
Most Frequent Words
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_frequent_words.png"
>>> most_frequent_words('author_keywords', directory=directory).savefig(file_name)

.. image:: images/most_frequent_words.png
    :width: 700px
    :align: center


>>> most_frequent_words('author_keywords', directory=directory, plot=False).head()
                        num_documents  global_citations  local_citations
author_keywords                                                         
fintech                           139              1285              218
financial technologies             28               225               41
financial inclusion                17               339               61
blockchain                         17               149               22
innovation                         13               249               46



"""
from .column_cleveland_dot_chart import column_cleveland_dot_chart


def most_frequent_words(
    column,
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    return column_cleveland_dot_chart(
        column=column,
        top_n=top_n,
        color=color,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
