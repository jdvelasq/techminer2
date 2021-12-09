"""
Most Global Cited Countries
===============================================================================

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_global_cited_countries.png"
>>> most_global_cited_countries(directory=directory).savefig(file_name)

.. image:: images/most_global_cited_countries.png
    :width: 700px
    :align: center


>>> most_global_cited_countries(directory=directory, plot=False).head()
countries
germany           528
united states     503
united kingdom    500
china             333
australia         318
Name: global_citations, dtype: int64



"""
from .column_global_citations import column_global_citations


def most_global_cited_countries(
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):
    return column_global_citations(
        column="countries",
        top_n=top_n,
        color=color,
        figsize=figsize,
        directory=directory,
        plot=plot,
    )
