"""
Most Global Cited Countries (*)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_global_cited_countries.png"
>>> most_global_cited_countries(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_global_cited_countries.png
    :width: 700px
    :align: center

"""

import plotly.express as px

from .column_indicators import column_indicators


def most_global_cited_countries(directory="./", top_n=20):

    indicators = column_indicators(column="countries", directory=directory)
    indicators = indicators.sort_values(
        by=["global_citations", "num_documents", "local_citations"], ascending=False
    )
    indicators = indicators.head(top_n)

    fig = px.scatter(
        x=indicators.global_citations,
        y=indicators.index,
        title="Most global cited countries",
        text=indicators.global_citations,
        labels={"x": "Global citations", "y": "Country"},
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
