"""
Country Scientific Production
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__country_scientific_production.html"


>>> from techminer2 import bibliometrix
>>> chart = bibliometrix.countries.country_scientific_production(
...     directory=directory
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
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| countries            |   OCC |
|:---------------------|------:|
| United Kingdom       |     7 |
| Australia            |     7 |
| United States        |     6 |
| Ireland              |     5 |
| China                |     5 |
| Italy                |     5 |
| Germany              |     4 |
| Switzerland          |     4 |
| Bahrain              |     4 |
| Hong Kong            |     3 |
| Luxembourg           |     2 |
| United Arab Emirates |     2 |
| Spain                |     2 |
| Indonesia            |     2 |
| Greece               |     1 |
| Japan                |     1 |
| Jordan               |     1 |
| South Africa         |     1 |
| Ukraine              |     1 |
| Malaysia             |     1 |
<BLANKLINE>
<BLANKLINE>



"""
from ... import vantagepoint


def country_scientific_production(
    directory="./",
    database="documents",
    metric="OCC",
    start_year=None,
    end_year=None,
    topics_length=20,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    colormap="Blues",
    title="Country Scientific Production",
    **filters,
):
    """Worldmap plot with the number of documents per country."""

    obj = vantagepoint.analyze.list_view(
        criterion="countries",
        root_dir=directory,
        database=database,
        metric=metric,
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        **filters,
    )

    return vantagepoint.report.world_map(
        obj,
        title=title,
        colormap=colormap,
    )
