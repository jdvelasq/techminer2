"""
Cleveland plot
===============================================================================


>>> from techminer2 import *
>>> from techminer2.plots import *
>>> directory = "data/"
>>> file_name = "sphinx/plots/images/cleveland_plot.png"
>>> series = column_indicators(
...     column="countries", 
...     directory=directory,
... ).num_documents.head(20)

>>> cleveland_plot(
...     series,
...     x_label=None,
...     y_label=None,
...     title=None,
... ).write_image(file_name)

.. image:: images/cleveland_plot.png
    :width: 700px
    :align: center

"""
import textwrap

import plotly.express as px

TEXTLEN = 40


def cleveland_plot(
    series,
    x_label=None,
    y_label=None,
    title=None,
):

    if x_label is None:
        x_label = series.name.replace("_", " ").title()

    if y_label is None:
        y_label = series.index.name.replace("_", " ").title()

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

    fig = px.scatter(
        x=series.values,
        y=series.index,
        title=title,
        text=series.astype(str),
        labels={"x": x_label, "y": y_label},
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
