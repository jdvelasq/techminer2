"""
Column Chart (Updated to use Plotly)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/hbar_chart.png"
>>> column_chart(
...     'author_keywords',
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/hbar_chart.png
    :width: 700px
    :align: center



"""
import plotly.express as px

from .column_indicators import column_indicators


def column_chart(
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

    fig = px.bar(
        x=indicators.values,
        y=indicators.index,
        text=indicators.astype(str),
        labels={"x": "Num Documents", "y": column.replace("_", " ").title()},
        orientation="h",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_traces(marker_color="gray")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        autorange="reversed",
        griddash="dot",
    )

    return fig
