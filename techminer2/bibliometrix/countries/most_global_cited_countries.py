"""
Most Global Cited Countries
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_countries.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.most_global_cited_countries(
...     directory,
...     topics_length=20,
...     plot="cleveland",
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
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 cited countries with highest number of total citations in the dataset ('global_citations' column). Use the information in the table to draw conclusions about the impact and relevance of the reseach published by the country in the dataset. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
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
<BLANKLINE>

"""
from ...vantagepoint.report.chart import chart


def most_global_cited_countries(
    directory="./",
    topics_length=20,
    plot="cleveland",
    database="documents",
    topic_min_occ=None,
    topic_min_citations=None,
    start_year=None,
    end_year=None,
    **filters,
):
    """Most global cited countries."""

    obj = chart(
        criterion="countries",
        directory=directory,
        database=database,
        metric="global_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Global Cited Countries",
        plot=plot,
        **filters,
    )

    obj.prompt_ = _create_prompt(obj.table_)

    return obj


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} cited countries with highest \
number of total citations in the dataset ('global_citations' column). Use the \
information in the table to draw conclusions about the impact and relevance of \
the reseach published by the country in the dataset. In your analysis, be sure \
to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
