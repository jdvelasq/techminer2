"""
Word cloud
===============================================================================

>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/images/word_cloud.png"

>>> indicators = terms_list(
...    column='author_keywords',
...    top_n=250,
...    directory=directory,
... )

>>> word_cloud(indicators).savefig(file_name)

.. image:: images/word_cloud.png
    :width: 900px
    :align: center

"""

from .format_dataset_to_plot_with_plotly import format_dataset_to_plot_with_plotly
from .word_cloud_py import word_cloud_py

TEXTLEN = 40


def word_cloud(
    dataframe,
    metric="OCC",
    title=None,
    figsize=(8, 8),
):
    """Makes a cleveland plot from a dataframe."""

    metric, column, dataframe = format_dataset_to_plot_with_plotly(dataframe, metric)

    return word_cloud_py(
        dataframe=dataframe,
        metric=metric,
        column=column,
        title=title,
        figsize=figsize,
    )
