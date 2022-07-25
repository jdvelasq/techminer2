"""
World Map
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__world_map.html"

>>> from techminer2 import vantagepoint__world_map
>>> vantagepoint__world_map(
...     column="countries", 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint__world_map.html" height="450px" width="100%" frameBorder="0"></iframe>


"""
from ._indicators.indicators_by_topic import indicators_by_topic
from ._plots.world_map_plot import world_map_plot

TEXTLEN = 40


def vantagepoint__world_map(
    column,
    metric="OCC",
    colormap="Greys",
    directory="./",
    title=None,
    database="documents",
):
    """Worldmap"""

    dataframe = indicators_by_topic(
        criterion=column, directory=directory, database=database
    )[metric]
    return world_map_plot(
        dataframe=dataframe,
        metric=metric,
        colormap=colormap,
        title=title,
    )
