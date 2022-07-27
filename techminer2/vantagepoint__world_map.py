"""
World Map (ok!)
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__world_map.html"

>>> from techminer2 import vantagepoint__world_map
>>> vantagepoint__world_map(
...     criterion="countries", 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../../../_static/vantagepoint__world_map.html" height="450px" width="100%" frameBorder="0"></iframe>


"""
from ._indicators.indicators_by_topic import indicators_by_topic
from ._plots.world_map_plot import world_map_plot

TEXTLEN = 40


def vantagepoint__world_map(
    criterion,
    directory="./",
    database="documents",
    metric="OCC",
    start_year=None,
    end_year=None,
    colormap="Greys",
    title=None,
    **filters,
):
    """Worldmap"""

    indicators = indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = indicators[metric]

    return world_map_plot(
        dataframe=indicators,
        metric=metric,
        colormap=colormap,
        title=title,
    )
