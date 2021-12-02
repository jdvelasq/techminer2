"""
Corresponding author's country
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/corresponding_authors_country.png"
>>> corresponding_authors_country(directory=directory).savefig(file_name)

.. image:: images/corresponding_authors_country.png
    :width: 500px
    :align: center


"""

from .collaboration_indicators import collaboration_indicators
from .stacked_bar_chart import stacked_bar_chart


def corresponding_authors_country(top_n=20, directory="./"):

    indicators = collaboration_indicators("countries", directory=directory)
    indicators = indicators.sort_values(by="num_documents", ascending=False)
    indicators = indicators[["single_publication", "multiple_publication"]].head(top_n)
    indicators = indicators
    return stacked_bar_chart(
        indicators,
        title="Corresponding Author's Country",
        xlabel="Num Documents",
        ylabel="Country",
    )
