"""
Column plot (!)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/column_plot.png"
>>> series = column_indicators(
...     column="countries", 
...     directory=directory,
... ).num_documents.head(20)

>>> column_plot(
...     series,
...     x_label=None,
...     y_label=None,
...     title=None,
... ).write_image(file_name)

.. image:: images/column_plot.png
    :width: 700px
    :align: center

"""
import textwrap

import plotly.express as px

TEXTLEN = 40


def column_plot(
    series,
    x_label=None,
    y_label=None,
    title=None,
):
    if x_label is None:
        x_label = series.index.name.replace("_", " ").title()

    if y_label is None:
        y_label = series.name.replace("_", " ").title()

    if series.index.dtype != "int64":
        series.index = [
            textwrap.shorten(
                text=text,
                width=TEXTLEN,
                placeholder="...",
                break_long_words=False,
            )
            for text in series.index.to_list()
        ]

    fig = px.bar(
        x=series.index,
        y=series.values,
        text=series.astype(str),
        title=title,
        labels={"x": x_label, "y": y_label},
        orientation="v",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_traces(marker_color="lightgray", marker_line={"color": "gray"})
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
    )
    fig.update_xaxes(tickangle=270)
    fig.update_yaxes(showticklabels=False)

    return fig
