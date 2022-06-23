"""
Most relevant authors (ok!)
===============================================================================

See :doc:`column indicators <column_indicators>` to obtain a `pandas.Dataframe` 
with the data.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_relevant_authors.png"

>>> most_relevant_authors(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_relevant_authors.png
    :width: 700px
    :align: center


"""
from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .column_indicators import column_indicators


def most_relevant_authors(directory="./", top_n=20):

    indicators = column_indicators(
        column="authors", directory=directory, file_name="documents.csv"
    )
    indicators = indicators.sort_values(
        by=["num_documents", "global_citations", "local_citations"], ascending=False
    )
    indicators = indicators.head(top_n)

    return bibliometrix_scatter_plot(
        x=indicators.num_documents,
        y=indicators.index,
        title="Most relevant authors",
        text=indicators.num_documents,
        xlabel="Num Documents",
        ylabel="Author Name",
    )
