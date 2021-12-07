"""
Thematic map --- network
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/thematic_map_network.png"
>>> thematic_map_network('author_keywords', directory=directory).savefig(file_name)

.. image:: images/thematic_map_network.png
    :width: 650px
    :align: center

"""

from .co_occurrence_network import co_occurrence_network


def thematic_map_network(
    column,
    min_occ=2,
    figsize=(8, 8),
    k=0.2,
    iterations=50,
    max_labels=20,
    directory="./",
):

    return co_occurrence_network(
        column=column,
        min_occ=min_occ,
        max_occ=None,
        normalization="association",
        scheme=None,
        clustering_method="louvain",
        manifold_method=None,
        directory=directory,
        figsize=figsize,
        k=k,
        iterations=iterations,
        max_labels=max_labels,
    )
