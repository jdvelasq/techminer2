"""
Tree Map
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/tree_map.html"

>>> indicators = terms_list(
...    column='author_keywords',
...    min_occ=3,
...    directory=directory,
... )

>>> tree_map(indicators).write_html(file_name)

.. raw:: html

    <iframe src="_static/tree_map.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly


def tree_map(
    dataframe,
    metric="OCC",
    title=None,
    colormap="Greys",
):
    """Makes a treemap."""

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    fig = px.treemap(
        dataframe,
        path=[column],
        values=metric,
        color=metric,
        color_continuous_scale=colormap,
        title=title,
    )
    fig.update_traces(root_color="lightgrey")
    fig.update_layout(margin=dict(t=1, l=1, r=1, b=1))
    return fig
