"""
Documents by type (!)
===============================================================================

>>> from techminer2.scopus import *
>>> directory = "data/"
>>> file_name = "sphinx/scopus/images/documents_by_type.png"

>>> documents_by_type(
...     directory
... ).write_image(file_name)

.. image:: images/documents_by_type.png
    :width: 700px
    :align: center

"""
from ..vantagepoint import *


def documents_by_type(directory):
    return bar_chart(
        column="document_type",
        min_occ=None,
        max_occ=None,
        top_n=10,
        directory=directory,
        metric="num_documents",
    )
