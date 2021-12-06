"""
Author's production over time
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/authors_production_time.png"
>>> authors_production_over_time(min_occ=2, directory=directory).savefig(file_name)


.. image:: images/authors_production_time.png
    :width: 500px
    :align: center

"""


from .annual_occurrence_matrix import annual_occurrence_matrix
from .dotted_timeline_chart import dotted_timeline_chart


def authors_production_over_time(
    min_occ=10,
    figsize=(6, 6),
    directory="./",
):
    production = annual_occurrence_matrix(
        "authors", min_occ=min_occ, directory=directory
    )
    return dotted_timeline_chart(production, figsize=figsize)
