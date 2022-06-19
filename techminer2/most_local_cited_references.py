"""
Most Local Cited References (*)
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_local_cited_references.png"
>>> most_local_cited_references(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_local_cited_references.png
    :width: 700px
    :align: center


"""
import os.path

import pandas as pd
import plotly.express as px


def most_local_cited_references(
    top_n=20,
    directory="./",
):

    indicators = pd.read_csv(
        os.path.join(directory, "processed", "references.csv"),
        sep=",",
        encoding="utf-8",
    )
    indicators = indicators[["document_id", "local_citations"]]
    indicators = indicators.dropna()
    indicators = indicators.sort_values(by="local_citations", ascending=False)
    indicators = indicators.head(top_n)

    fig = px.scatter(
        x=indicators.local_citations,
        y=indicators.document_id,
        title="Most local cited references",
        text=indicators.local_citations,
        labels={"x": "Local citations", "y": "Document"},
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
