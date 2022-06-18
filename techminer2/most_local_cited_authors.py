"""
Most Local Cited Authors
===============================================================================

Most local cited authors in references.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_local_cited_authors.png"
>>> most_local_cited_authors(directory=directory).savefig(file_name)

.. image:: images/most_local_cited_authors.png
    :width: 700px
    :align: center


>>> most_local_cited_authors(directory=directory, plot=False).head(5)
             local_citations
authors                     
Kauffman RJ               62
Gomber P                  57
Lee I                     43
Hornuf L                  41
Weber B                   40



"""
from os.path import join

import pandas as pd

from ._cleveland_chart import _cleveland_chart


def most_local_cited_authors(
    top_n=20,
    color="k",
    figsize=(8, 6),
    directory="./",
    plot=True,
):

    indicators = pd.read_csv(
        join(directory, "processed", "references.csv"), sep=",", encoding="utf-8"
    )
    indicators = indicators[["authors", "local_citations"]]
    indicators = indicators.dropna()
    indicators = indicators.assign(authors=indicators.authors.str.split(";"))
    indicators = indicators.explode("authors")
    indicators = indicators.assign(authors=indicators.authors.str.strip())
    indicators = indicators.groupby("authors").sum()
    indicators = indicators.sort_values(by="local_citations", ascending=False)
    if plot is False:
        return indicators
    indicators = indicators.local_citations.head(top_n)

    return _cleveland_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most Local Cited Authors",
        xlabel="Local Citations",
        ylabel="Source",
    )
