"""
Country Scientific Production
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_scientific_production.html"


>>> from techminer2 import bibliometrix__country_scientific_production
>>> bibliometrix__country_scientific_production(
...     directory=directory
... ).write_html(file_name)
 
.. raw:: html

    <iframe src="../../../_static/bibliometrix__country_scientific_production.html" height="410px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint__world_map import vantagepoint__world_map


def bibliometrix__country_scientific_production(
    directory="./",
    metric="OCC",
    database="documents",
    colormap="Blues",
):
    """Worldmap plot with the number of documents per country."""

    return vantagepoint__world_map(
        column="countries",
        directory=directory,
        metric=metric,
        title="Country Scientific Production",
        database=database,
        colormap=colormap,
    )
