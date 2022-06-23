"""
Column Chart
===============================================================================

>>> from techminer2.vantagepoint import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/column_chart.html"

>>> column_chart(
...     'author_keywords',
...     top_n=20,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/column_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

from .column_indicators_by_metric import column_indicators_by_metric


def column_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
    title=None,
):

    indicators = column_indicators_by_metric(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
    )
    indicators = indicators.reset_index()
    column_names = {
        column: column.replace("_", " ").title() for column in indicators.columns
    }
    indicators = indicators.rename(columns=column_names)

    fig = px.bar(
        indicators,
        x=column.replace("_", " ").title(),
        y=metric.replace("_", " ").title(),
        hover_data=["Num Documents", "Global Citations", "Local Citations"],
        title=title,
        orientation="v",
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(paper_bgcolor="white", plot_bgcolor="white")
    fig.update_traces(marker_color="lightgray", marker_line={"color": "gray"})
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )

    return fig
