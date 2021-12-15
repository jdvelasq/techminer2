"""
Co-citation Network / Graph
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/co_citation_network_graph.png"
>>> co_citation_network_graph(directory=directory).savefig(file_name)

.. image:: images/co_citation_network_graph.png
    :width: 700px
    :align: center



"""

from .co_citation_matrix import co_citation_matrix
from .network import network
from .network_plot import network_plot


def co_citation_network_graph(
    top_n=50,
    clustering_method="louvain",
    figsize=(8, 8),
    k=0.2,
    iterations=50,
    max_labels=10,
    directory="./",
):
    matrix = co_citation_matrix(
        top_n=top_n,
        directory=directory,
    )

    network_ = network(
        matrix=matrix,
        clustering_method=clustering_method,
    )

    return network_plot(
        network_,
        figsize=figsize,
        k=k,
        iterations=iterations,
        max_labels=max_labels,
    )
