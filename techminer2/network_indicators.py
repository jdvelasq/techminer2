"""
Network Indicators
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/co_occurrence_network_map.png"
>>> coc_matrix = co_occurrence_matrix(
...     column='author_keywords', 
...     min_occ=7, 
...     directory=directory,
... )
>>> from techminer2.network_api.network import network
>>> network_ = network(coc_matrix)
>>> from techminer2.network_api.network_indicators import network_indicators
>>> network_indicators(network_).head()


"""


def network_indicators(network):
    indicators = network["indicators"].copy()
    indicators = indicators.set_index("node")
    return indicators
