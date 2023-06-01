"""
Most Global Cited Countries
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_countries.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.most_global_cited_countries(
...     directory=directory,
...     topics_length=20,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
countries
United Kingdom    199
Australia         199
Hong Kong         185
United States      59
Ireland            55
Name: global_citations, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| countries            |   global_citations |
|:---------------------|-------------------:|
| United Kingdom       |                199 |
| Australia            |                199 |
| Hong Kong            |                185 |
| United States        |                 59 |
| Ireland              |                 55 |
| Germany              |                 51 |
| Switzerland          |                 45 |
| Luxembourg           |                 34 |
| China                |                 27 |
| Greece               |                 21 |
| Bahrain              |                 19 |
| United Arab Emirates |                 13 |
| Japan                |                 13 |
| Jordan               |                 11 |
| South Africa         |                 11 |
| Italy                |                  5 |
| Spain                |                  4 |
| Ukraine              |                  4 |
| Malaysia             |                  3 |
| Palestine            |                  1 |
<BLANKLINE>
<BLANKLINE>


"""
from ...vantagepoint.analyze import list_view
from ..utils import bbx_generic_indicators_by_item


def most_global_cited_countries(
    plot="cleveland_chart",
    x_label=None,
    y_label=None,
    directory="./",
    topics_length=20,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most global cited countries."""

    return bbx_generic_indicators_by_item(
        fnc_view=list_view,
        field="countries",
        metric="global_citations",
        plot=plot,
        x_label=x_label,
        y_label=y_label,
        title="Most Global Cited Countries",
        root_dir=directory,
        top_n=topics_length,
        occ_range=topic_min_occ,
        topic_max_occ=topic_max_occ,
        gc_range=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_items=custom_topics,
        database=database,
        year_filter=start_year,
        cited_by_filter=end_year,
        **filters,
    )
