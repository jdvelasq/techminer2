"""
Column Chart (!)
===============================================================================

>>> from techminer2.vantagepoint import *
>>> directory = "data/"
>>> file_name = "sphinx/vantagepoint/images/column_chart.png"
>>> column_chart(
...     'author_keywords',
...     top_n=20,
...     directory=directory,
... ).write_image(file_name)

.. image:: images/column_chart.png
    :width: 700px
    :align: center

"""
from .._column_indicators_by_metric import column_indicators_by_metric
from ..plots import column_plot


def column_chart(
    column,
    top_n=None,
    min_occ=None,
    max_occ=None,
    directory="./",
    metric="num_documents",
):

    indicator = column_indicators_by_metric(
        column,
        min_occ=min_occ,
        max_occ=max_occ,
        top_n=top_n,
        directory=directory,
        metric=metric,
    )

    fig = column_plot(
        indicator,
        x_label=None,
        y_label=None,
        title=None,
    )

    return fig
