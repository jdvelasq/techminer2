"""
Thematic Map / Graph
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/thematic_map_network.png"
>>> thematic_map_network('author_keywords', directory=directory).savefig(file_name)

.. image:: images/thematic_map_network.png
    :width: 700px
    :align: center

"""

from .co_occurrence_network_graph import co_occurrence_network_graph


def thematic_map_network(
    column,
    min_occ=2,
    figsize=(8, 8),
    k=0.2,
    iterations=50,
    max_labels=20,
    directory="./",
):

    return co_occurrence_network_graph(
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
