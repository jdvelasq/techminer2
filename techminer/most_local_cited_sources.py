"""
Most Local Cited Sources
===============================================================================

Plot the most local cited sources in the references.

>>> from techminer import *
>>> directory = "/workspaces/techminer-api/data/"
>>> file_name = "/workspaces/techminer-api/sphinx/images/most_local_cited_sources.png"
>>> most_local_cited_sources(directory=directory).savefig(file_name)

.. image:: images/most_local_cited_sources.png
    :width: 700px
    :align: center



>>> most_local_cited_sources(directory=directory, plot=False).head(10)
iso_source_name
ELECT COMMER RES APPL          90
MIS QUART MANAGE INF SYST      76
REV FINANC STUD                75
J MANAGE INF SYST              73
J FINANC ECON                  72
SUSTAINABILITY                 64
J FINANC                       62
TECHNOL FORECAST SOC CHANGE    57
MANAGE SCI                     53
RES POLICY                     52
Name: local_citations, dtype: int64


"""
from os.path import join

import matplotlib.pyplot as plt
import pandas as pd

from .cleveland_dot_chart import cleveland_dot_chart
from .column_indicators import column_indicators


def most_local_cited_sources(
    top_n=20,
    color="k",
    figsize=(9, 6),
    directory="./",
    plot=True,
):

    indicators = pd.read_csv(
        join(directory, "references.csv"), sep=",", encoding="utf-8"
    )
    indicators = indicators[["iso_source_name", "local_citations"]]
    indicators = indicators.groupby("iso_source_name").sum()
    indicators = indicators.sort_values(by="local_citations", ascending=False)

    if plot is False:
        return indicators.local_citations

    indicators = indicators.local_citations.head(top_n)
    return cleveland_dot_chart(
        indicators,
        figsize=figsize,
        color=color,
        title="Most local cited sources in references",
        xlabel="Local citations",
        ylabel="Source",
    )
