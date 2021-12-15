"""
Co-occurrence Network / Degree Plot
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/co_occurrence_degree_plot.png"
>>> co_occurrence_degree_plot('author_keywords', directory=directory).savefig(file_name)

.. image:: images/co_occurrence_degree_plot.png
    :width: 700px
    :align: center

"""

from .co_occurrence_matrix import co_occurrence_matrix
from .network import network
from .network_degree_plot import network_degree_plot


def co_occurrence_degree_plot(
    column,
    min_occ=2,
    max_occ=None,
    normalization=None,
    clustering_method="louvain",
    manifold_method=None,
    figsize=(8, 8),
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

    return network_degree_plot(
        network_,
        figsize=figsize,
    )
