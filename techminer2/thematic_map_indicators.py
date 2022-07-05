"""
Thematic Map / Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> thematic_map_indicators(
...     'author_keywords', min_occ=4, directory=directory
... ).head()


"""


from .co_occurrence_network_indicators import co_occurrence_network_indicators


def thematic_map_indicators(
    column,
    min_occ=2,
    directory="./",
):

    return co_occurrence_network_indicators(
        column,
        min_occ=min_occ,
        normalization="association",
        clustering_method="louvain",
        directory=directory,
    )
