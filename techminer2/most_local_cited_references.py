"""
Most Local Cited References (!)
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_local_cited_references.png"
>>> most_local_cited_references(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_local_cited_references.png
    :width: 700px
    :align: center


"""
from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .document_indicators import document_indicators


def most_local_cited_references(
    top_n=20,
    directory="./",
):

    indicators = document_indicators(directory=directory, file_name="references.csv")
    indicators = indicators.sort_values(by="local_citations", ascending=False)
    indicators = indicators.head(top_n)

    return bibliometrix_scatter_plot(
        x=indicators.local_citations,
        y=indicators.index,
        title="Most local cited references",
        text=indicators.local_citations,
        xlabel="Local citations",
        ylabel="Reference",
    )
