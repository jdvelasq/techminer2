# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Country Scientific Production
===============================================================================


>>> from techminer2 import bibliometrix
>>> root_dir = "data/regtech/"
>>> production = bibliometrix.countries.countries_scientific_production(
...     root_dir=root_dir
... )
>>> production.fig_.write_html("sphinx/_static/countries_scientific_production.html")
 
.. raw:: html

    <iframe src="../../../../../_static/countries_scientific_production.html" height="410px" width="100%" frameBorder="0"></iframe>

    
>>> production.df_.head()
                rank_occ  OCC
countries                    
United Kingdom         1    7
Australia              2    7
United States          3    6
Ireland                4    5
China                  5    5

>>> print(production.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'countries' field in a scientific bibliography database. Summarize the \\
table below, sorted by the 'OCC' metric, and delimited by triple backticks, \\
identify any notable patterns, trends, or outliers in the data, and discuss \\
their implications for the research field. Be sure to provide a concise \\
summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| countries            |   rank_occ |   OCC |
|:---------------------|-----------:|------:|
| United Kingdom       |          1 |     7 |
| Australia            |          2 |     7 |
| United States        |          3 |     6 |
| Ireland              |          4 |     5 |
| China                |          5 |     5 |
| Italy                |          6 |     5 |
| Germany              |          7 |     4 |
| Switzerland          |          8 |     4 |
| Bahrain              |          9 |     4 |
| Hong Kong            |         10 |     3 |
| Luxembourg           |         11 |     2 |
| United Arab Emirates |         12 |     2 |
| Spain                |         13 |     2 |
| Indonesia            |         14 |     2 |
| Greece               |         15 |     1 |
| Japan                |         16 |     1 |
| Jordan               |         17 |     1 |
| South Africa         |         18 |     1 |
| Ukraine              |         19 |     1 |
| Malaysia             |         20 |     1 |
| India                |         21 |     1 |
| Palestine            |         22 |     1 |
| Taiwan               |         23 |     1 |
| Belgium              |         24 |     1 |
| France               |         25 |     1 |
| Netherlands          |         26 |     1 |
| Poland               |         27 |     1 |
| Romania              |         28 |     1 |
| Singapore            |         29 |     1 |
```
<BLANKLINE>



"""

from ...vantagepoint.report.world_map import world_map


def countries_scientific_production(
    metric="OCC",
    #
    # Chart options:
    colormap="Blues",
    title=None,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=None,
    gc_range=None,
    custom_items=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=None,
    cited_by_filter=None,
    **filters,
):
    """Worldmap plot

    Args:


    Returns:
        BasicChart: A basic chart object.
    """

    if title is None:
        title = "Country scientific production"

    return world_map(
        #
        # ITEMS PARAMS:
        metric=metric,
        #
        # CHART PARAMS:
        title=title,
        colormap=colormap,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
