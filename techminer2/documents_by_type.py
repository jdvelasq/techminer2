"""
Documents by type
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/documents_by_type.html"


>>> documents_by_type(
...     directory
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/documents_by_type.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .bar_chart import bar_chart


def documents_by_type(directory):

    return bar_chart(
        column="document_type",
        min_occ=None,
        max_occ=None,
        top_n=10,
        directory=directory,
        metric="num_documents",
    )
