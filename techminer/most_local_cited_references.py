"""
Most Local Cited References
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_local_cited_references.png"
>>> most_local_cited_references(directory=directory).savefig(file_name)

.. image:: images/most_local_cited_references.png
    :width: 700px
    :align: center

>>> most_local_cited_references(directory=directory, plot=False).head()
                                   document_id  local_citations
2060              Lee I et al, 2018, BUS HORIZ               38
2055   Gomber P et al, 2018, J MANAGE INF SYST               31
3835      Haddad C et al, 2019, SMALL BUS ECON               22
2110          Gomber P et al, 2017, J BUS ECON               21
2247  Gai K et al, 2018, J NETWORK COMPUT APPL               19

"""
from os.path import join

import pandas as pd

from .cleveland_dot_chart import cleveland_dot_chart


def most_local_cited_references(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
    plot=True,
):

    indicators = pd.read_csv(
        join(directory, "references.csv"), sep=",", encoding="utf-8"
    )
    indicators = indicators[["document_id", "local_citations"]]
    indicators = indicators.dropna()
    indicators = indicators.sort_values(by="local_citations", ascending=False)

    if plot is False:
        return indicators

    indicators.index = indicators.document_id
    indicators = indicators.local_citations.head(top_n)
    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most Local Cited References",
        xlabel="Local Citations",
        ylabel="Document",
    )
