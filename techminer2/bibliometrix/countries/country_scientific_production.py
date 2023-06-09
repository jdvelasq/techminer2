# flake8: noqa
"""
Country Scientific Production
===============================================================================


>>> root_dir = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_scientific_production.html"


>>> from techminer2 import bibliometrix
>>> chart = bibliometrix.countries.country_scientific_production(
...     root_dir=root_dir
... )
>>> chart.plot_.write_html(file_name)
 
.. raw:: html

    <iframe src="../../../_static/bibliometrix__country_scientific_production.html" height="410px" width="100%" frameBorder="0"></iframe>

    
>>> chart.table_.head()
countries
United Kingdom    7
Australia         7
United States     6
Ireland           5
China             5
Name: OCC, dtype: int64


>>> print(chart.prompt_)
Analyze the table below, which provides bibliometric indicators for the field 'countries' in a scientific bibliography database. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| countries      |   OCC |   global_citations |   local_citations |   global_citations_per_document |   local_citations_per_document |
|:---------------|------:|-------------------:|------------------:|--------------------------------:|-------------------------------:|
| United Kingdom |     7 |                199 |                34 |                           28.43 |                           4.86 |
| Australia      |     7 |                199 |                15 |                           28.43 |                           2.14 |
| United States  |     6 |                 59 |                11 |                            9.83 |                           1.83 |
| Ireland        |     5 |                 55 |                22 |                           11    |                           4.4  |
| China          |     5 |                 27 |                 5 |                            5.4  |                           1    |
| Italy          |     5 |                  5 |                 2 |                            1    |                           0.4  |
| Germany        |     4 |                 51 |                17 |                           12.75 |                           4.25 |
| Switzerland    |     4 |                 45 |                13 |                           11.25 |                           3.25 |
| Bahrain        |     4 |                 19 |                 5 |                            4.75 |                           1.25 |
| Hong Kong      |     3 |                185 |                 8 |                           61.67 |                           2.67 |
<BLANKLINE>
<BLANKLINE>



# pylint: disable=line-too-long
"""
from ...vantagepoint.analyze import list_view
from ...vantagepoint.report import world_map


# pylint: disable=too-many-arguments
def country_scientific_production(
    root_dir="./",
    database="main",
    metric="OCC",
    # Chart options:
    colormap="Blues",
    title=None,
    # Item filters:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    # Database filters:
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Worldmap plot

    Args:


    Returns:
        BasicChart: A basic chart object.
    """

    obj = list_view(
        field="countries",
        root_dir=root_dir,
        database=database,
        metric=metric,
        # Item filters:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        # Database filters:
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if title is None:
        title = "Country scientific production"

    return world_map(
        obj,
        title=title,
        colormap=colormap,
    )
