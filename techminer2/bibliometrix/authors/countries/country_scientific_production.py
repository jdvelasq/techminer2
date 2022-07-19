"""
Country Scientific Production
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/country_scientific_production.html"


>>> from techminer2 import country_scientific_production
>>> country_scientific_production(
...     directory=directory
... ).write_html(file_name)
 
.. raw:: html

    <iframe src="../../../_static/country_scientific_production.html" height="410px" width="100%" frameBorder="0"></iframe>

"""
from ....world_map import world_map


def country_scientific_production(
    directory="./",
    metric="OCC",
    database="documents",
    colormap="Blues",
):
    """Worldmap plot with the number of documents per country."""

    return world_map(
        column="countries",
        directory=directory,
        metric=metric,
        title="Country Scientific Production",
        database=database,
        colormap=colormap,
    )
