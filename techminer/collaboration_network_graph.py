"""
Collaboration Network / Graph
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/collaboration_network_graph.png"
>>> collaboration_network_graph('authors', min_occ=2, directory=directory).savefig(file_name)

.. image:: images/collaboration_network_graph.png
    :width: 700px
    :align: center

"""

from .co_occurrence_network import co_occurrence_network


def collaboration_network_graph(
    column,
    min_occ=1,
    normalization="association",
    clustering_method="louvain",
    directory="./",
    figsize=(7, 7),
    k=0.20,
    iterations=50,
    max_labels=50,
):
    if column not in ["authors", "institutions", "countries"]:
        raise ValueError("The column must be 'authors', 'institutions' or 'countries'")

    return co_occurrence_network(
        column=column,
        min_occ=min_occ,
        normalization=normalization,
        clustering_method=clustering_method,
        directory=directory,
        figsize=figsize,
        k=k,
        iterations=iterations,
        max_labels=max_labels,
    )
