"""
Bar plot (!)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/plots/images/bar_plot.png"
>>> series = column_indicators(
...     column="countries", 
...     directory=directory,
... ).num_documents.head(20)

>>> bar_plot(
...     series,
...     x_label=None,
...     y_label=None,
...     title=None,
... ).write_image(file_name)

.. image:: images/bar_plot.png
    :width: 700px
    :align: center

"""
import textwrap

import plotly.express as px

TEXTLEN = 40


def bar_plot(
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

    fig = px.bar(
        x=series.values,
        y=series.index,
        text=series.astype(str),
        title=title,
        labels={"x": x_label, "y": y_label},
        orientation="h",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_traces(marker_color="lightgray", marker_line={"color": "gray"})
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
        # gridcolor="lightgray",
        # griddash="dot",
    )
    # fig.update_xaxes(tickangle=270)
    fig.update_xaxes(showticklabels=False)

    return fig
