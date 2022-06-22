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
...     metric="num_documents",
... ).write_image(file_name)

.. image:: images/bar_chart.png
    :width: 700px
    :align: center

"""
from ._column_indicators_by_metric import column_indicators_by_metric
from .bar_plot import bar_plot


def bar_chart(
    column,
    min_occ=None,
    max_occ=None,
    top_n=None,
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

    fig = bar_plot(
        indicator,
        x_label=None,
        y_label=None,
        title=None,
    )

    return fig
