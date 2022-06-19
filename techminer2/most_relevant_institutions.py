"""
Most Relevant Institutions (*)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_relevant_institutions.png"
>>> most_relevant_institutions(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_relevant_institutions.png
    :width: 700px
    :align: center

"""
from ._bibliometrix_scatter_plot import bibliometrix_scatter_plot
from .column_indicators import column_indicators


def most_relevant_institutions(directory="./", top_n=20):

    indicators = column_indicators(column="institutions", directory=directory)
    indicators = indicators.sort_values(
        by=["num_documents", "global_citations", "local_citations"], ascending=False
    )
    indicators = indicators.head(top_n)

    return bibliometrix_scatter_plot(
        x=indicators.num_documents,
        y=indicators.index,
        title="Most relevant institutions",
        text=indicators.num_documents,
        xlabel="Num Documents",
        ylabel="Institution Name",
    )
