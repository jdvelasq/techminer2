"""
Most Local Cited Sources (in References)
===============================================================================

Plot the most local cited sources in the references.

See https://jdvelasq.github.io/techminer2/column_indicators.html

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_local_cited_sources.png"
>>> most_local_cited_sources(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_local_cited_sources.png
    :width: 700px
    :align: center

"""
from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .column_indicators import column_indicators


def most_local_cited_sources(
    top_n=10,
    directory="./",
):

    indicators = column_indicators(
        column="iso_source_name", directory=directory, file_name="references.csv"
    )
    indicators = indicators.sort_values(by="local_citations", ascending=False)
    indicators = indicators.head(top_n)

    return bibliometrix_scatter_plot(
        x=indicators.local_citations,
        y=indicators.index,
        title="Most local cited sources in references",
        text=indicators.local_citations,
        xlabel="Num Documents",
        ylabel="Source Title",
    )
