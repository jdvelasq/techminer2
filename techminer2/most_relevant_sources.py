"""
Most relevant sources (ok!)
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_relevant_sources.png"

>>> most_relevant_sources(
...     directory=directory,
...     top_n=10,
... ).write_image(file_name)

.. image:: images/most_relevant_sources.png
    :width: 700px
    :align: center

"""
from .cleveland_plot import cleveland_plot
from .column_indicators import column_indicators


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
