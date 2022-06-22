"""
Circle Chart
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/circle_chart.png"
>>> circle_chart(
...     'author_keywords', 
...     top_n=15, 
...     directory=directory,
...     hole=0.5,
... ).write_image(file_name)

.. image:: images/circle_chart.png
    :width: 700px
    :align: center

"""

import plotly.express as px

from ._column_indicators_by_metric import column_indicators_by_metric


def circle_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    hole=0.0,
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

    fig = px.pie(
        values=indicators.values,
        names=indicators.index,
        hole=hole,
    )
    fig.update_traces(textinfo="value")
    fig.update_layout(legend=dict(y=0.5))
    return fig
