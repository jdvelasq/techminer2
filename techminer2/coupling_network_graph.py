"""
Coupling Network / Graph
===============================================================================

Builds a coupling network from a coupling matrix.

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/coupling__network_graph.png"
>>> coupling_network_graph(
...     column='author_keywords',
...     min_occ=4, 
...     top_n=20,
...     directory=directory,
...     k=1.0,
... ).savefig(file_name)

.. image:: images/coupling__network_graph.png
    :width: 700px
    :align: center

"""


from .coupling_matrix import coupling_matrix
from .network import network
from .network_plot import network_plot


def coupling_network_graph(
    column,
    top_n=100,
    min_occ=1,
    metric="global_citations",
    directory="./",
    clustering_method="louvain",
    manifold_method=None,
    figsize=(7, 7),
    k=0.20,
    iterations=50,
    max_labels=50,
):
    # -------------------------------------------------------------------------
    # Documents
    matrix = coupling_matrix(
        column=column,
        top_n=top_n,
        min_occ=min_occ,
        metric=metric,
        directory=directory,
    )

    network_ = network(
        matrix,
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
