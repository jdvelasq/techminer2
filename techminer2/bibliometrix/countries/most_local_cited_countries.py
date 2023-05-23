"""
Most Local Cited Countries (GPT)
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_countries.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.most_local_cited_countries(
...     topics_length=20,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_countries.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
countries
United Kingdom    34
Ireland           22
Germany           17
Australia         15
Switzerland       13
Name: local_citations, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| countries            |   local_citations |
|:---------------------|------------------:|
| United Kingdom       |                34 |
| Ireland              |                22 |
| Germany              |                17 |
| Australia            |                15 |
| Switzerland          |                13 |
| United States        |                11 |
| Hong Kong            |                 8 |
| Luxembourg           |                 8 |
| Greece               |                 8 |
| United Arab Emirates |                 7 |
| China                |                 5 |
| Bahrain              |                 5 |
| Jordan               |                 4 |
| South Africa         |                 4 |
| Italy                |                 2 |
| Japan                |                 1 |
| Palestine            |                 1 |
| India                |                 1 |
| Spain                |                 0 |
| Ukraine              |                 0 |
<BLANKLINE>
<BLANKLINE>



"""
from ... import vantagepoint


def most_local_cited_countries(
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
    """Most local cited countries."""

    obj = vantagepoint.analyze.extract_topics(
        criterion="countries",
        directory=directory,
        database=database,
        metric="local_citations",
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
        title="Most Local Cited Countries",
        x_label="Local Citations",
        y_label="COUNTRIES",
    )

    return chart
