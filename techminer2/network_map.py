"""
Network Map
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/co_occurrence_network_map.png"
>>> coc_matrix = co_occurrence_matrix(
...     column='author_keywords', 
...     min_occ=7, 
...     directory=directory,
... )
>>> from techminer2.network_api.network import network
>>> network_ = network(coc_matrix)
>>> from techminer2.network_api.network_map import network_map
>>> network_map(network_).savefig(file_name)

.. image:: images/co_occurrence_network_map.png
    :width: 700px
    :align: center

"""
from .tlab.co_occ_analysis.word_association.bubble_map import bubble_map


def network_map(
    network,
    color_scheme="clusters",
    figsize=(7, 7),
):

    manifold = network["manifold_data"]

    return bubble_map(
        node_x=manifold["Dim-0"],
        node_y=manifold["Dim-1"],
        node_clusters=manifold["cluster"],
        node_texts=manifold["node"],
        node_sizes=manifold["degree"],
        x_axis_at=0,
        y_axis_at=0,
        color_scheme=color_scheme,
        xlabel="X-Axis",
        ylabel="Y-Axis",
        figsize=figsize,
        fontsize=7,
    )
