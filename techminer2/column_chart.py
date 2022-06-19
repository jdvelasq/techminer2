"""
Column Chart (*)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/column_chart.png"
>>> column_chart(
...     'author_keywords',
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/column_chart.png
    :width: 700px
    :align: center



"""
import plotly.express as px

from ._column_indicators_by_metric import column_indicators_by_metric


def column_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
):

    indicators = column_indicators_by_metric(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
    )

    fig = px.bar(
        x=indicators.values,
        y=indicators.index,
        text=indicators.astype(str),
        labels={"x": "Num Documents", "y": column.replace("_", " ").title()},
        orientation="h",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_traces(marker_color="lightgray")
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        autorange="reversed",
        griddash="dot",
    )
    fig.update_xaxes(showticklabels=False)

    return fig
