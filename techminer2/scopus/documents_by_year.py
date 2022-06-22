"""
Documents by year (change plot)
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
from ..annual_indicators import annual_indicators
from ..plots import bar_plot


def documents_by_year(directory):

    indicators = annual_indicators(directory).num_documents
    fig = bar_plot(
        indicators,
        x_label=None,
        y_label=None,
        title="Documents by year",
    )

    return fig
