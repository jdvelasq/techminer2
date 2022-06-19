"""
Cleveland Chart (*)
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/cleveland_chart.jpg"
>>> cleveland_chart(
...    column="author_keywords", 
...    top_n=20,
...    directory=directory,
... ).write_image(file_name)

.. image:: images/cleveland_chart.jpg
    :width: 700px
    :align: center

"""
import plotly.express as px

from .column_indicators import column_indicators


def cleveland_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
):

    indicators = column_indicators(
        column=column,
        directory=directory,
    ).num_documents

    indicators = indicators.sort_values(ascending=False)

    if top_n is not None:
        indicators = indicators.head(top_n)

    if min_occ is not None:
        indicators = indicators[indicators >= min_occ]

    if max_occ is not None:
        indicators = indicators[indicators <= max_occ]

    fig = px.scatter(
        x=indicators.values,
        y=indicators.index,
        text=indicators.astype(str),
        labels={"x": "Num Documents", "y": column.replace("_", " ").title()},
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
