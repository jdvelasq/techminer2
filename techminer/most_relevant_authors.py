"""
Most Relevant Authors
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_relevant_authors.png"
>>> most_relevant_authors(directory=directory).savefig(file_name)

.. image:: images/most_relevant_authors.png
    :width: 650px
    :align: center


>>> most_relevant_authors(directory=directory, plot=False).head()
                num_documents  global_citations  local_citations
authors                                                         
Wojcik D                    5                19                4
Hornuf L                    3               110               24
Rabbani MR                  3                39                3
Gomber P                    2               228               34
Worthington AC              2                 7                1



"""
from .column_frequency import column_frequency


def most_relevant_authors(
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    return column_frequency(
        column="authors",
        top_n=top_n,
        color=color,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
