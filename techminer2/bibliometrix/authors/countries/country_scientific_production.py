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
from ....vantagepoint.report.world_map import world_map


def bibliometrix__country_scientific_production(
    directory="./",
    metric="OCC",
    database="documents",
    colormap="Blues",
    start_year=None,
    end_year=None,
    title="Country Scientific Production",
    **filters,
):
    """Worldmap plot with the number of documents per country."""

    return world_map(
        criterion="countries",
        directory=directory,
        database=database,
        metric=metric,
        start_year=start_year,
        end_year=end_year,
        colormap=colormap,
        title=title,
        **filters,
    )
