"""
Most Global Cited Countries (GPT)
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_countries.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.most_global_cited_countries(
...     directory,
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
from ... import vantagepoint


def most_global_cited_countries(
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

    obj = vantagepoint.analyze.extract_topics(
        criterion="countries",
        directory=directory,
        database=database,
        metric="global_citations",
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

    chart = vantagepoint.report.cleveland_chart(
        obj,
        title="Most Global Cited Countries",
        x_label="Global Citations",
        y_label="COUNTRIES",
    )

    return chart
