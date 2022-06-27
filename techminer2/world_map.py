"""
World map
===============================================================================


>>> from techminer2 import *
>>> directory = "data/"
>>> file_name = "sphinx/_static/world_map.html"

>>> world_map(
...     directory=directory,
...     metric="num_documents",
... ).write_html(file_name)

.. raw:: html

    <iframe src="_static/world_map.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .column_indicators_by_metric import column_indicators_by_metric
from .world_map_plot import world_map_plot


def world_map(
    directory="./",
    metric="num_documents",
    title=None,
    file_name="documents.csv",
):
    """Makes a world map from a dataframe."""

    indicators = column_indicators_by_metric(
        "countries",
        min_occ=None,
        max_occ=None,
        top_n=None,
        directory=directory,
        metric=metric,
        file_name=file_name,
    )

    return world_map_plot(
        dataframe=indicators,
        metric=metric,
        title=title,
        colormap="Blues",
    )
