"""
Documents by author (!)
===============================================================================

>>> from techminer2.scopus import *
>>> directory = "data/"
>>> file_name = "sphinx/images/documents_by_author.png"

>>> documents_by_author(
...     directory
... ).write_image(file_name)

.. image:: images/documents_by_author.png
    :width: 700px
    :align: center

"""
from .bar_chart import bar_chart


def documents_by_author(directory):
    return bar_chart(
        column="authors",
        min_occ=None,
        max_occ=None,
        top_n=10,
        directory=directory,
        metric="num_documents",
    )
