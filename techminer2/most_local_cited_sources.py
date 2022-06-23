"""
Most Local Cited Sources (in References) (ok!)
===============================================================================

Plot the most local cited sources in the references.

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data. In this case, use:

.. code:: python

    column_indicators(
        column="iso_source_name",
        directory=directory,
        file_name="references.csv",
    )


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
from .cleveland_plot import cleveland_plot
from .column_indicators import column_indicators


def most_local_cited_sources(
    top_n=10,
    directory="./",
):

    indicator = column_indicators(
        column="iso_source_name",
        directory=directory,
        file_name="references.csv",
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
