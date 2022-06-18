"""
Co-occurrence Network / Graph
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/co_occurrence_network_graph.png"
>>> co_occurrence_network_graph(
...     'author_keywords', 
...      min_occ=5,
...      directory=directory,
... ).savefig(file_name)

.. image:: images/co_occurrence_network_graph.png
    :width: 700px
    :align: center



"""

from .co_occurrence_matrix import co_occurrence_matrix
from .network import network
from .network_plot import network_plot


def co_occurrence_network_graph(
    column,
    min_occ=1,
    max_occ=None,
    normalization=None,
    scheme=None,
    clustering_method="louvain",
    manifold_method=None,
    directory="./",
    figsize=(7, 7),
    k=0.20,
    iterations=50,
    max_labels=50,
):

    coc_matrix = co_occurrence_matrix(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        normalization=normalization,
        scheme=scheme,
        directory=directory,
    )

    network_ = network(
        coc_matrix,
        clustering_method=clustering_method,
        manifold_method=manifold_method,
    )

    return network_plot(
        network_,
        figsize=figsize,
        k=k,
        iterations=iterations,
        max_labels=max_labels,
    )
