"""
Tree Map (*)
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/tree_map.png"
>>> tree_map(
...     'author_keywords',
...     top_n=15, 
...     directory=directory,
... ).write_image(file_name)

.. image:: images/tree_map.png
    :width: 700px
    :align: center

"""
import plotly.express as px

from ._column_indicators_by_metric import column_indicators_by_metric


def tree_map(
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

    fig = px.treemap(
        names=indicators.index,
        parents=[""] * len(indicators),
        values=indicators,
        color_continuous_scale="Greys",
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=1, l=1, r=1, b=1))
    return fig
