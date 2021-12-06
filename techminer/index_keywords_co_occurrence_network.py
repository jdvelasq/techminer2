"""
Index keywords co-occurrence network
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/index_keywords_co_occurrence_network.png"
>>> index_keywords_co_occurrence_network(directory=directory).savefig(file_name)

.. image:: images/index_keywords_co_occurrence_network.png
    :width: 550px
    :align: center

"""

from .co_occurrence_matrix import co_occurrence_matrix
from .co_occurrence_network import co_occurrence_network
from .network_plot import network_plot


def index_keywords_co_occurrence_network(
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    figsize=(8, 8),
    k=0.2,
    iterations=50,
    max_labels=10,
    directory="./",
):

    coc_matrix = co_occurrence_matrix(
        column="index_keywords",
        min_occ=min_occ,
        max_occ=max_occ,
        association=normalization,
        directory=directory,
    )

    network = co_occurrence_network(
        co_occurrence_matrix=coc_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )

    return network_plot(
        network,
        figsize=figsize,
        k=k,
        iterations=iterations,
        max_labels=max_labels,
    )
