"""
Most local cited authors plot
===============================================================================


>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_local_cited_authors.png"
>>> most_local_cited_authors_plot(directory=directory).savefig(file_name)

.. image:: images/most_local_cited_authors.png
    :width: 650px
    :align: center


"""
from os.path import join

import matplotlib.pyplot as plt
import pandas as pd

from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def most_local_cited_authors_plot(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
):

    indicators = pd.read_csv(
        join(directory, "references.csv"), sep=",", encoding="utf-8"
    )
    indicators = indicators[["authors", "local_citations"]]
    indicators = indicators.dropna()
    indicators = indicators.assign(authors=indicators.authors.str.split(";"))
    indicators = indicators.explode("authors")
    indicators = indicators.assign(authors=indicators.authors.str.strip())
    indicators = indicators.groupby("authors").sum()
    indicators = indicators.sort_values(by="local_citations", ascending=False)
    indicators = indicators.local_citations.head(top_n)

    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most Local Cited Authors",
        xlabel="Local Citations",
        ylabel="Source",
    )
