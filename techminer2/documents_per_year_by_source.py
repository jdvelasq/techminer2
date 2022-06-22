"""
Documents per year by source (pendient)
===============================================================================

>>> from techminer2.scopus import *
>>> directory = "data/"
>>> file_name = "sphinx/images/documents_per_year_by_source.png"

>>> documents_per_year_by_source(
...     directory
... ).write_image(file_name)

.. image:: images/documents_per_year_by_source.png
    :width: 700px
    :align: center

"""
from .source_dynamics import source_dynamics


def documents_per_year_by_source(directory="./"):
    return source_dynamics(top_n=10, directory=directory)
