"""
Co-occurrence Network / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> co_occurrence_network_indicators(
...     'author_keywords',
...     min_occ=2,
...     directory=directory,
... ).head()



"""

from .co_occurrence_matrix import co_occurrence_matrix
from .network import network
from .network_indicators import network_indicators


def co_occurrence_network_indicators(
    column,
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
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

    return network_indicators(network_)
