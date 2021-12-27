"""
Most Relevant Authors
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/most_relevant_authors.png"
>>> most_relevant_authors(directory=directory).savefig(file_name)

.. image:: images/most_relevant_authors.png
    :width: 700px
    :align: center


>>> most_relevant_authors(directory=directory, plot=False).head()
             num_documents  global_citations  local_citations
authors                                                      
Wojcik D                 5                19                4
Hornuf L                 3               110               24
Rabbani MR               3                39                3
Gomber P                 2               228               34
Kauffman RJ              2               228               34



"""
from .column_cleveland_dot_chart import column_cleveland_dot_chart


def most_relevant_authors(
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    return column_cleveland_dot_chart(
        column="authors",
        top_n=top_n,
        color=color,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
