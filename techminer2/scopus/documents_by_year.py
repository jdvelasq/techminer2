"""
Documents by year (!)
===============================================================================

>>> from techminer2.scopus import *
>>> directory = "data/"
>>> file_name = "sphinx/scopus/images/documents_by_year.png"

>>> documents_by_year(
...     directory
... ).write_image(file_name)

.. image:: images/documents_by_year.png
    :width: 700px
    :align: center

"""
from ..bibliometrix import annual_scientific_production

documents_by_year = annual_scientific_production
