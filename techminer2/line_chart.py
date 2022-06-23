"""
Line Chart
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

from .column_indicators_by_metric import column_indicators_by_metric


def line_chart(
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

    fig = px.line(
        x=indicators.index,
        y=indicators.values,
        markers=True,
        text=indicators.astype(str),
        labels={
            "y": metric.replace("_", " ").title(),
            "x": column.replace("_", " ").title(),
        },
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
