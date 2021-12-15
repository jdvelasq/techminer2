"""
Collaboration Network / Degree Plot
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/collaboration_network_degree_plot.png"
>>> collaboration_network_degree_plot('authors', min_occ=2, directory=directory).savefig(file_name)

.. image:: images/collaboration_network_degree_plot.png
    :width: 700px
    :align: center

"""

from .co_occurrence_degree_plot import co_occurrence_degree_plot


def collaboration_network_degree_plot(
    column,
    min_occ=2,
    normalization="association",
    clustering_method="louvain",
    figsize=(8, 8),
    directory="./",
):
    if column not in ["authors", "institutions", "countries"]:
        raise ValueError("The column must be 'authors', 'institutions' or 'countries'")

    return co_occurrence_degree_plot(
        column=column,
        min_occ=min_occ,
        normalization=normalization,
        clustering_method=clustering_method,
        figsize=figsize,
        directory=directory,
    )
