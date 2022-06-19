"""
Line Chart (*)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/line_chart.png"
>>> line_chart(
...     'author_keywords', 
...     top_n=15, 
...     directory=directory,
... ).write_image(file_name)

.. image:: images/line_chart.png
    :width: 700px
    :align: center



"""

import plotly.express as px

from .column_indicators import column_indicators


def line_chart(
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

    fig = px.line(
        x=indicators.index,
        y=indicators.values,
        markers=True,
        text=indicators.astype(str),
        labels={"y": "Num Documents", "x": column.replace("_", " ").title()},
    )
    fig.update_traces(marker=dict(size=12))
    fig.update_traces(textposition="top right")
    fig.update_traces(line=dict(color="black"))
    fig.update_xaxes(tickangle=270)
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_xaxes(linecolor="gray", gridcolor="lightgray")
    fig.update_yaxes(linecolor="gray", gridcolor="white")
    fig.update_yaxes(visible=True)
    fig.update_yaxes(showticklabels=False)
    return fig
