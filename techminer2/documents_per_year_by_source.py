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
# from .source_dynamics_table import source_dynamics_table


def documents_per_year_by_source(directory="./"):
    pass


#     return source_dynamics_table(top_n=10, directory=directory)
