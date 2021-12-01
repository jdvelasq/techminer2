"""
Most relevant authors plot
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_relevant_authors.png"
>>> most_relevant_authors_plot(directory=directory).savefig(file_name)

.. image:: images/most_relevant_authors.png
    :width: 500px
    :align: center


"""
from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def most_relevant_authors_plot(
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
):
    indicators = column_indicators(directory=directory, column="authors").num_documents
    indicators = indicators.sort_values(ascending=False).head(top_n)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most relevant authors",
        xlabel="Num Documents",
        ylabel="Author",
    )
