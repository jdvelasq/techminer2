"""
Most Relevant Sources
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_relevant_sources.png"
>>> most_relevant_sources(directory=directory).savefig(file_name)

.. image:: images/most_relevant_sources.png
    :width: 650px
    :align: center


>>> most_relevant_sources(directory=directory, plot=False).head()
                               num_documents  global_citations  local_citations
iso_source_name                                                                
SUSTAINABILITY                            15                97               22
FINANCIAL INNOV                           11               132               17
J OPEN INNOV: TECHNOL MARK CO              8                35               15
E3S WEB CONF                               7                 3                0
FRONTIER ARTIF INTELL                      5                23                4



"""
from .column_frequency import column_frequency


def most_relevant_sources(
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    return column_frequency(
        column="iso_source_name",
        top_n=top_n,
        color=color,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
