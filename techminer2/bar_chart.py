"""
Bar Chart (*)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/bar_chart.png"
>>> bar_chart(
...     column='author_keywords',
...     top_n=15,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/bar_chart.png
    :width: 700px
    :align: center


"""

import plotly.express as px

from .column_indicators import column_indicators


def bar_chart(
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
        x=indicators.index,
        y=indicators.values,
        text=indicators.astype(str),
        labels={"y": "Num Documents", "x": column.replace("_", " ").title()},
        orientation="v",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_traces(marker_color="lightgray")
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(tickangle=270)
    fig.update_yaxes(visible=False)

    return fig
