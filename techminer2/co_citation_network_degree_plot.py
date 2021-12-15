"""
Co-citation Network / Degree Plot
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/co_citation_network_degree_plot.png"
>>> co_citation_network_degree_plot(directory=directory).savefig(file_name)

.. image:: images/co_citation_network_degree_plot.png
    :width: 700px
    :align: center



"""

from .co_citation_matrix import co_citation_matrix
from .network import network
from .network_degree_plot import network_degree_plot


def co_citation_network_degree_plot(
    top_n=50,
    clustering_method="louvain",
    figsize=(8, 8),
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

    return network_degree_plot(
        network_,
        figsize=figsize,
    )
