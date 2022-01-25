"""
Co-occurrence Network / Strategic Diagram
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> co_occurrence_network_strategic_diagram(
...     'author_keywords',
...     min_occ=2,
...     directory=directory,
... ).head()


"""

from matplotlib.pyplot import figimage

from .co_occurrence_matrix import co_occurrence_matrix
from .network import network
from .network_strategic_diagram import network_strategic_diagram


def co_occurrence_network_strategic_diagram(
    column,
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
    figsize=(8, 8),
):

    coc_matrix = co_occurrence_matrix(
        column=column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        directory=directory,
    )

    network_ = network(
        matrix=coc_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )

    return network_strategic_diagram(
        network_,
        figsize=figsize,
    )
