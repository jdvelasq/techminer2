"""
Most Relevant Institutions
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/most_relevant_institutions.png"
>>> most_relevant_institutions(directory=directory).savefig(file_name)

.. image:: images/most_relevant_institutions.png
    :width: 700px
    :align: center


>>> most_relevant_institutions(directory=directory, plot=False).head()
institutions
Bina Nusantara University IDN          6
Singapore Management University SGP    5
University of Sydney AUS               5
University of Latvia LVA               4
University of Pavia ITA                4
Name: num_documents, dtype: int64


"""
from .cleveland_chart import cleveland_chart


def most_relevant_institutions(
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):

    return cleveland_chart(
        column="institutions",
        top_n=top_n,
        color=color,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
