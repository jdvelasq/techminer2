"""
Most local cited references plot
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_local_cited_references.png"
>>> most_local_cited_references_plot(directory=directory).savefig(file_name)

.. image:: images/most_local_cited_references.png
    :width: 650px
    :align: center


"""
from os.path import join

import pandas as pd

from .cleveland_dot_chart import cleveland_dot_chart


def most_local_cited_references_plot(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
):

    indicators = pd.read_csv(
        join(directory, "references.csv"), sep=",", encoding="utf-8"
    )
    indicators = indicators[["document_id", "local_citations"]]
    indicators = indicators.dropna()
    indicators = indicators.sort_values(by="local_citations", ascending=False)
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
