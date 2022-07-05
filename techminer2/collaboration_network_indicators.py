"""
Collaboration Network / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> collaboration_network_indicators('authors', min_occ=2, directory=directory).head()


"""
from .co_occurrence_network_indicators import co_occurrence_network_indicators


def collaboration_network_indicators(
    column,
    min_occ=2,
    normalization="association",
    clustering_method="louvain",
    directory="./",
):

    if column not in ["authors", "institutions", "countries"]:
        raise ValueError("The column must be 'authors', 'institutions' or 'countries'")

    return co_occurrence_network_indicators(
        column=column,
        min_occ=min_occ,
        normalization=normalization,
        clustering_method=clustering_method,
        directory=directory,
    )
