"""
Most Local Cited Authors in References
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_local_cited_authors.png"
>>> most_local_cited_authors(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_local_cited_authors.png
    :width: 700px
    :align: center


"""
import plotly.express as px

from .column_indicators import column_indicators


def most_local_cited_authors(
    top_n=20,
    directory="./",
):

    indicators = column_indicators(
        column="authors", directory=directory, file_name="references.csv"
    )
    indicators = indicators.sort_values(by="local_citations", ascending=False)
    indicators = indicators.head(top_n)

    fig = px.scatter(
        x=indicators.local_citations,
        y=indicators.index,
        title="Most local cited authors in references",
        text=indicators.local_citations,
        labels={"x": "Local citations", "y": "Author Name"},
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
