"""
Most Frequent Countries
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_countries.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.most_frequent_countries(
...     directory=directory,
...     topics_length=20,
...     database="documents",
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_frequent_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

>>> r.table_.head()
countries
United Kingdom    7
Australia         7
United States     6
Ireland           5
China             5
Name: OCC, dtype: int64

>>> print(r.prompt_)
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
from ..bibliometric_indicators_by_topic import bibliometric_indicators_by_topic


def most_frequent_countries(
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
    """Plots the number of documents by country using the specified plot."""

    return bibliometric_indicators_by_topic(
        criterion="countries",
        metric="OCC",
        plot=plot,
        x_label=x_label,
        y_label=y_label,
        title="Most Frequent Countries",
        directory=directory,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_max_occ=topic_max_occ,
        topic_min_citations=topic_min_citations,
        topic_max_citations=topic_max_citations,
        custom_topics=custom_topics,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
