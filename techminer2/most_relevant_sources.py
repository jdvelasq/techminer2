"""
Most Relevant Sources
===============================================================================

>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/most_relevant_sources.png"
>>> most_relevant_sources(directory=directory).savefig(file_name)

.. image:: images/most_relevant_sources.png
    :width: 700px
    :align: center


>>> most_relevant_sources(directory=directory, plot=False).head()
iso_source_name
SUSTAINABILITY                   15
FINANCIAL INNOV                  11
J OPEN INNOV: TECHNOL MARK CO     8
E3S WEB CONF                      7
FRONTIER ARTIF INTELL             5
Name: num_documents, dtype: int64



"""
from .cleveland_chart import cleveland_chart


def most_relevant_sources(
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    return cleveland_chart(
        column="iso_source_name",
        top_n=top_n,
        color=color,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
