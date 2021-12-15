"""
Thematic Map / Degree Plot
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/thematic_map_degree_plot.png"
>>> thematic_map_degree_plot('author_keywords', min_occ=4, directory=directory).savefig(file_name)

.. image:: images/thematic_map_degree_plot.png
    :width: 700px
    :align: center

"""


from .co_occurrence_degree_plot import co_occurrence_degree_plot


def thematic_map_degree_plot(
    column,
    min_occ=2,
    figsize=(8, 8),
    directory="./",
):

    return co_occurrence_degree_plot(
        column,
        min_occ=min_occ,
        normalization="association",
        clustering_method="louvain",
        figsize=figsize,
        directory=directory,
    )
