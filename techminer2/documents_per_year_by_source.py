"""
Documents per year by source (pendient)
===============================================================================

>>> from techminer2.scopus import *
>>> directory = "data/"
>>> file_name = "sphinx/images/documents_per_year_by_source.png"

>>> documents_by_author(
...     directory
... ).write_image(file_name)

.. image:: images/documents_per_year_by_source.png
    :width: 700px
    :align: center

"""
from .annual_scientific_production import annual_scientific_production

documents_per_year_by_source = None
