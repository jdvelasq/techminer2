"""
Most Relevant Institutions (*)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/most_relevant_institutions.png"
>>> most_relevant_institutions(
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/most_relevant_institutions.png
    :width: 700px
    :align: center




"""
import plotly.express as px

from .column_indicators import column_indicators


def most_relevant_institutions(directory="./", top_n=20):

    indicators = column_indicators(column="institutions", directory=directory)
    indicators = indicators.sort_values(
        by=["num_documents", "global_citations", "local_citations"], ascending=False
    )
    indicators = indicators.head(top_n)

    fig = px.scatter(
        x=indicators.num_documents,
        y=indicators.index,
        title="Most relevant institutions",
        text=indicators.num_documents,
        labels={"x": "Num Documents", "y": "Institution Name"},
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

    return fig
