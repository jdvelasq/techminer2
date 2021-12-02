"""
Most global cited documents
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_global_cited_documents.png"
>>> most_global_cited_documents(directory=directory).savefig(file_name)

.. image:: images/most_global_cited_documents.png
    :width: 650px
    :align: center

"""

from .cleveland_dot_chart import cleveland_dot_chart
from .document_indicators import document_indicators


def most_global_cited_documents(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
):

    indicators = document_indicators(
        global_citations=True,
        normalized_citations=False,
        n_top=top_n,
        directory=directory,
    )
    indicators.index = indicators.document_id
    indicators = indicators.global_citations

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most Global Cited Documents",
        xlabel="Total Citations",
        ylabel="Document",
    )
