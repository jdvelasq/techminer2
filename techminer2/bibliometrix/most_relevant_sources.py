"""
Most Relevant Sources
===============================================================================

See https://jdvelasq.github.io/techminer2/column_indicators.html

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/bibliometrix/images/most_relevant_sources.png"

>>> most_relevant_sources(
...     directory=directory,
...     top_n=10,
... ).write_image(file_name)

.. image:: images/most_relevant_sources.png
    :width: 700px
    :align: center

"""
from ..column_indicators import column_indicators
from ..plots import cleveland_plot


def most_relevant_sources(directory="./", top_n=20):

    indicator = column_indicators(column="iso_source_name", directory=directory)
    indicator = indicator.sort_values(
        by=["num_documents", "global_citations", "local_citations"],
        ascending=False,
    )
    indicator = indicator.head(top_n)
    indicator = indicator.num_documents

    fig = cleveland_plot(
        series=indicator,
        x_label=None,
        y_label=None,
        title="Most relevant sources",
    )

    return fig
