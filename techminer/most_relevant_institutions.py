"""
Most relevant institutions
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_relevant_institutions.png"
>>> most_relevant_institutions(directory=directory).savefig(file_name)

.. image:: images/most_relevant_institutions.png
    :width: 500px
    :align: center


"""
import matplotlib.pyplot as plt

from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def most_relevant_institutions(
    top_n=20,
    color="k",
    figsize=(10, 6),
    directory="./",
):
    indicators = column_indicators("institutions", directory=directory).num_documents
    indicators = indicators.sort_values(ascending=False).head(top_n)
    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most relevant institutions",
        xlabel="Num Documents",
        ylabel="Institutions",
    )
