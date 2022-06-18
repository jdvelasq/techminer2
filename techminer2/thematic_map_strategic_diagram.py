"""
Thematic Map / Centrality Density Map
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/thematic_map_strategic_diagram.png"
>>> thematic_map_strategic_diagram('author_keywords', directory=directory).savefig(file_name)

.. image:: images/thematic_map_strategic_diagram.png
    :width: 700px
    :align: center

"""

from .co_occurrence_network_strategic_diagram import (
    co_occurrence_network_strategic_diagram,
)


def thematic_map_strategic_diagram(
    column,
    min_occ=2,
    figsize=(8, 8),
    directory="./",
):

    return co_occurrence_network_strategic_diagram(
        column=column,
        min_occ=min_occ,
        max_occ=None,
        normalization="association",
        clustering_method="louvain",
        manifold_method=None,
        directory=directory,
        figsize=figsize,
    )
