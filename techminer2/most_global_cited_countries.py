"""
Most Global Cited Countries
===============================================================================

See https://jdvelasq.github.io/techminer2/column_indicators.html

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_global_cited_countries.png"
>>> most_global_cited_countries(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_global_cited_countries.png
    :width: 700px
    :align: center

"""
from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .column_indicators import column_indicators


def most_global_cited_countries(directory="./", top_n=20):

    indicators = column_indicators(column="countries", directory=directory)
    indicators = indicators.sort_values(
        by=["global_citations", "num_documents", "local_citations"], ascending=False
    )
    indicators = indicators.head(top_n)

    return bibliometrix_scatter_plot(
        x=indicators.global_citations,
        y=indicators.index,
        title="Most global cited countries",
        text=indicators.global_citations,
        xlabel="Global citations",
        ylabel="Country",
    )
