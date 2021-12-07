"""
Institutions frequency
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/institutions_frequency.png"
>>> institutions_frequency(directory=directory).savefig(file_name)

.. image:: images/institutions_frequency.png
    :width: 550px
    :align: center


>>> institutions_frequency(directory=directory, plot=False).head()
                                                num_documents  ...  local_citations
institutions                                                   ...                 
Bina Nusantara University IDN                               6  ...                7
University of Sydney AUS                                    5  ...               25
Singapore Management University SGP                         5  ...               35
Universitas Indonesia IDN                                   4  ...                5
Poznan University of Economic and Business POL              4  ...                4
<BLANKLINE>
[5 rows x 3 columns]


"""
import matplotlib.pyplot as plt

from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def institutions_frequency(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
    plot=True,
):
    indicators = column_indicators("institutions", directory=directory)
    if plot is False:
        return indicators
    indicators = indicators.num_documents
    indicators = indicators.sort_values(ascending=False).head(top_n)
    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most relevant institutions",
        xlabel="Num Documents",
        ylabel="Institutions",
    )
