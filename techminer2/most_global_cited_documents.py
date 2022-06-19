"""
Most Global Cited Documents (*)
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_global_cited_documents.png"
>>> most_global_cited_documents(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_global_cited_documents.png
    :width: 700px
    :align: center


"""
import plotly.express as px

from .document_indicators import document_indicators


def most_global_cited_documents(
    top_n=20,
    directory="./",
):

    indicators = document_indicators(directory=directory)
    indicators = indicators.sort_values(by="global_citations", ascending=False)
    indicators = indicators.head(top_n)

    fig = px.scatter(
        x=indicators.global_citations,
        y=indicators.index,
        title="Most global cited documents",
        text=indicators.global_citations,
        labels={"x": "Global citations", "y": "Document"},
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
