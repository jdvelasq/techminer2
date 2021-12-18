"""
Most Frequent Words
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/words_most_frequent.png"
>>> words_most_frequent('author_keywords', directory=directory).savefig(file_name)

.. image:: images/words_most_frequent.png
    :width: 700px
    :align: center


>>> words_most_frequent('author_keywords', directory=directory, plot=False).head()
                        num_documents  global_citations  local_citations
author_keywords                                                         
fintech                           139              1285              218
financial technologies             28               225               41
financial inclusion                17               339               61
block-chain                        17               149               22
bank                               13               193               23



"""
from .column_cleveland_dot_chart import column_cleveland_dot_chart


def words_most_frequent(
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
