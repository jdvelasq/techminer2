"""
Most Local Cited Sources (in References)
===============================================================================

Plot the most local cited sources in the references.

See https://jdvelasq.github.io/techminer2/column_indicators.html

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/bibliometrix/images/most_local_cited_sources.png"
>>> most_local_cited_sources(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_local_cited_sources.png
    :width: 700px
    :align: center

"""
from ..column_indicators import column_indicators
from ..plots import cleveland_plot


def most_local_cited_sources(
    top_n=10,
    directory="./",
):

    indicator = column_indicators(
        column="iso_source_name", directory=directory, file_name="references.csv"
    )
    indicator = indicator.sort_values(by="local_citations", ascending=False)
    indicator = indicator.head(top_n)
    indicator = indicator.local_citations

    fig = cleveland_plot(
        series=indicator,
        x_label=None,
        y_label="Source Title",
        title="Most local cited sources in references",
    )

    return fig
