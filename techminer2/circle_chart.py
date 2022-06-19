"""
Circle Chart (*)
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

from .column_indicators import column_indicators


def circle_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    hole=0.0,
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

    fig = px.pie(
        values=indicators.values,
        names=indicators.index,
        hole=hole,
    )
    fig.update_traces(textinfo="value")
    fig.update_layout(legend=dict(y=0.5))
    return fig
