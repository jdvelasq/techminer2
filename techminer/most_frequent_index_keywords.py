"""
Most frequent index keywords
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_frequent_index_keywords.png"
>>> most_frequent_index_keywords(directory=directory).savefig(file_name)

.. image:: images/most_frequent_index_keywords.png
    :width: 550px
    :align: center


>>> most_frequent_index_keywords(directory=directory, plot=False).head()
                         num_documents  global_citations  local_citations
index_keywords                                                           
fintech                             48               269               52
financial service                   19               347               52
finance                             18               489               77
sustainable development             12                93               21
investment                          10               187               20

"""
import matplotlib.pyplot as plt

from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def most_frequent_index_keywords(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
    plot=True,
):
    indicators = column_indicators("index_keywords", directory=directory)
    if plot is False:
        return indicators
    indicators = indicators.num_documents
    indicators = indicators.sort_values(ascending=False).head(top_n)
    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most Frequent Index Keywords",
        xlabel="Num Documents",
        ylabel="Author Keywords",
    )
