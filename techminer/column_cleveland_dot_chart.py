"""
Column Cleveland Dot Chart
===============================================================================

Plots the number of documents per item in the selected column


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/column_cleveland_dot_chart.png"
>>> column_cleveland_dot_chart(column="authors", directory=directory).savefig(file_name)

.. image:: images/column_cleveland_dot_chart.png
    :width: 700px
    :align: center


>>> column_cleveland_dot_chart(column='authors', directory=directory, plot=False).head()
                num_documents  global_citations  local_citations
authors                                                         
Wojcik D                    5                19                4
Hornuf L                    3               110               24
Rabbani MR                  3                39                3
Gomber P                    2               228               34
Worthington AC              2                 7                1


"""


from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def column_cleveland_dot_chart(
    column,
    top_n=20,
    color="k",
    figsize=(6, 6),
    directory="./",
    plot=True,
):

    indicators = column_indicators(column, directory=directory)
    if plot is False:
        return indicators
    indicators = indicators.num_documents
    indicators = indicators.sort_values(ascending=False).head(top_n)
    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        xlabel="Num Documents",
        ylabel=column.replace("_", " ").title(),
    )
