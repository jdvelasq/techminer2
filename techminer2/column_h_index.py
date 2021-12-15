"""
Column H-index
===============================================================================



>>> from techminer2 import *
>>> directory = "/workspaces/techminer2/data/"
>>> file_name = "/workspaces/techminer2/sphinx/images/column_h_index.png"
>>> column_h_index(column='iso_source_name', top_n=20, directory=directory).savefig(file_name)

.. image:: images/column_h_index.png
    :width: 700px
    :align: center


>>> column_h_index(column='iso_source_name', top_n=20, directory=directory, plot=False).head(5)
                         num_documents  ...  avg_global_citations
FINANCIAL INNOV                     11  ...                 12.00
SUSTAINABILITY                      15  ...                  6.47
ENVIRON PLANN A                      4  ...                  7.50
FRONTIER ARTIF INTELL                5  ...                  4.60
J ASIAN FINANC ECON BUS              3  ...                  5.33
<BLANKLINE>
[5 rows x 9 columns]

"""


from .cleveland_dot_chart import cleveland_dot_chart
from .impact_indicators import impact_indicators


def column_h_index(
    column,
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
    plot=True,
):
    indicators = impact_indicators(directory=directory, column=column)
    indicators = indicators.sort_values(by="h_index", ascending=False)

    if plot is False:
        return indicators

    indicators = indicators["h_index"].head(top_n)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Source local impact",
        xlabel="H-index",
        ylabel=column,
    )
