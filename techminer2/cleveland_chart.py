"""
Cleveland Chart (New)
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/cleveland_chart.jpg"
>>> cleveland_chart(
...    column="author_keywords", 
...    top_n=20,
...    directory=directory,
... ).write_image(file_name)

.. image:: images/cleveland_chart.jpg
    :width: 700px
    :align: center

"""
import plotly.express as px

from ._column_indicators_by_metric import column_indicators_by_metric


def cleveland_chart(
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

    fig = px.scatter(
        x=indicators.values,
        y=indicators.index,
        text=indicators.astype(str),
        labels={
            "x": metric.replace("_", " ").title(),
            "y": column.replace("_", " ").title(),
        },
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
