"""
Documents by affiliation (!)
===============================================================================

>>> from techminer2.scopus import *
>>> directory = "data/"
>>> file_name = "sphinx/images/documents_by_affiliation.png"

>>> documents_by_affiliation(
...     directory
... ).write_image(file_name)

.. image:: images/documents_by_affiliation.png
    :width: 700px
    :align: center

"""
from .bar_chart import bar_chart


def documents_by_affiliation(directory):

    return bar_chart(
        column="institutions",
        min_occ=None,
        max_occ=None,
        top_n=10,
        directory=directory,
        metric="num_documents",
    )
