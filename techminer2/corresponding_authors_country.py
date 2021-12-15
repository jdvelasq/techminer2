"""
Corresponding Author's Country
===============================================================================


>>> from techminer2 import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/corresponding_authors_country.png"
>>> corresponding_authors_country(directory=directory).savefig(file_name)

.. image:: images/corresponding_authors_country.png
    :width: 700px
    :align: center


>>> corresponding_authors_country(directory=directory, plot=False).head()
                single_publication  multiple_publication  mcp_ratio
countries                                                          
china                           20                    23   1.150000
united kingdom                  19                    22   1.157895
indonesia                       21                     1   0.047619
united states                    7                    15   2.142857
australia                        4                    14   3.500000


"""

from .collaboration_indicators import collaboration_indicators
from .stacked_bar_chart import stacked_bar_chart


def corresponding_authors_country(top_n=20, directory="./", plot=True):

    indicators = collaboration_indicators("countries", directory=directory)
    indicators = indicators.sort_values(by="num_documents", ascending=False)
    indicators = indicators[["single_publication", "multiple_publication"]]

    if plot is False:
        indicators = indicators.assign(
            mcp_ratio=indicators["multiple_publication"]
            / indicators["single_publication"]
        )
        return indicators

    indicators = indicators.head(top_n)
    return stacked_bar_chart(
        indicators,
        title="Corresponding Author's Country",
        xlabel="Num Documents",
        ylabel="Country",
    )
