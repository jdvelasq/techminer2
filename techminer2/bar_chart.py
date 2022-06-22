"""
Bar Chart
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

from ._column_indicators_by_metric import column_indicators_by_metric


def bar_chart(
    column,
    min_occ=None,
    max_occ=None,
    top_n=None,
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
        x=indicators.index,
        y=indicators.values,
        text=indicators.astype(str),
        labels={
            "y": metric.replace("_", " ").title(),
            "x": column.replace("_", " ").title(),
        },
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
    fig.update_yaxes(showticklabels=False)

    return fig
