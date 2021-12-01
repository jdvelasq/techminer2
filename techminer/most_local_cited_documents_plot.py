"""
Most local cited documents plot
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_local_cited_documents.png"
>>> most_local_cited_documents_plot(directory=directory).savefig(file_name)

.. image:: images/most_local_cited_documents.png
    :width: 650px
    :align: center


"""

from .cleveland_dot_chart import cleveland_dot_chart
from .document_indicators import document_indicators


def most_local_cited_documents_plot(
    n_top=20,
    color="k",
    figsize=(8, 6),
    directory="./",
):
    indicators = document_indicators(
        global_citations=False,
        normalized_citations=False,
        n_top=n_top,
        directory=directory,
    )
    indicators.index = indicators.document_id
    indicators = indicators.local_citations

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most Local Cited Documents",
        xlabel="Local Citations",
        ylabel="Document",
    )
