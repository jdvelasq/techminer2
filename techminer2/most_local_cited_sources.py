"""
Most Local Cited Sources in References (*)
===============================================================================

Plot the most local cited sources in the references.

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_local_cited_sources.png"
>>> most_local_cited_sources(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_local_cited_sources.png
    :width: 700px
    :align: center

"""
import os.path

import pandas as pd
import plotly.express as px

from .column_indicators import column_indicators


def most_local_cited_sources(
    top_n=10,
    directory="./",
):

    indicators = pd.read_csv(
        os.path.join(directory, "processed", "references.csv"),
        sep=",",
        encoding="utf-8",
    )
    indicators = indicators[["iso_source_name", "local_citations"]]
    indicators = indicators.groupby("iso_source_name").sum()
    indicators = indicators.sort_values(by="local_citations", ascending=False)
    if top_n is not None:
        indicators = indicators.head(top_n)
    indicators = indicators.local_citations

    fig = px.scatter(
        x=indicators.values,
        y=indicators.index,
        title="Most local cited sources in references",
        text=indicators.astype(str),
        labels={"x": "Local Citations", "y": "Source Title"},
    )
    fig.update_traces(marker=dict(size=10, color="black"))
    fig.update_traces(textposition="middle right")
    fig.update_traces(line=dict(color="black"))
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        autorange="reversed",
        griddash="dot",
    )
    fig.update_xaxes(showticklabels=False)
    return fig


# ###


# from os.path import join

# import pandas as pd

# from ._cleveland_chart import _cleveland_chart


# def most_local_cited_sources(
#     top_n=20,
#     color="k",
#     figsize=(9, 6),
#     directory="./",
#     plot=True,
# ):

#     indicators = pd.read_csv(
#         join(directory, "processed", "references.csv"), sep=",", encoding="utf-8"
#     )
#     indicators = indicators[["iso_source_name", "local_citations"]]
#     indicators = indicators.groupby("iso_source_name").sum()
#     indicators = indicators.sort_values(by="local_citations", ascending=False)

#     if plot is False:
#         return indicators.local_citations

#     indicators = indicators.local_citations.head(top_n)
#     return _cleveland_chart(
#         indicators,
#         figsize=figsize,
#         color=color,
#         title="Most local cited sources in references",
#         xlabel="Local citations",
#         ylabel="Source",
#     )
