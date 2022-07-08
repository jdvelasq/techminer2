"""
Network strategic map
===============================================================================

>>> from techminer2 import *
>>> directory = "data/regtech/"
>>> file_name = "sphinx/images/network_strategic_diagram.png"
>>> coc_matrix = co_occurrence_matrix(
...     column='author_keywords', 
...     normalization="equivalence",
...     min_occ=7, 
...     directory=directory,
... )
>>> from techminer2.network_api.network import network
>>> network_ = network(coc_matrix)
>>> from techminer2.network_api.network_map import network_strategic_diagram
>>> network_strategic_map(network_).savefig(file_name)

.. image:: images/network_strategic_diagram.png
    :width: 700px
    :align: center

"""
from .bubble_map import bubble_map


def network_strategic_diagram(
    network,
    figsize=(8, 8),
):

    strategic_diagram = network["strategic_diagram"]

    return bubble_map(
        node_x=strategic_diagram["callon_centrality"],
        node_y=strategic_diagram["callon_density"],
        node_clusters=strategic_diagram.index,
        node_texts=strategic_diagram["cluster_name"],
        node_sizes=strategic_diagram["n_items"],
        x_axis_at=strategic_diagram["callon_density"].mean(),
        y_axis_at=strategic_diagram["callon_centrality"].mean(),
        color_scheme="4q",
        xlabel="Centrality",
        ylabel="Density",
        figsize=figsize,
        fontsize=7,
    )
