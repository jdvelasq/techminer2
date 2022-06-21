"""
Most Global Cited Documents 
===============================================================================

See https://jdvelasq.github.io/techminer2/document_indicators.html

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_global_cited_documents.png"
>>> most_global_cited_documents(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_global_cited_documents.png
    :width: 700px
    :align: center

"""
from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .document_indicators import document_indicators


def most_global_cited_documents(
    top_n=20,
    directory="./",
):

    indicators = document_indicators(directory=directory)
    indicators = indicators.sort_values(by="global_citations", ascending=False)
    indicators = indicators.head(top_n)

    return bibliometrix_scatter_plot(
        x=indicators.global_citations,
        y=indicators.index,
        title="Most global cited documents",
        text=indicators.global_citations,
        xlabel="Global citations",
        ylabel="Document",
    )
