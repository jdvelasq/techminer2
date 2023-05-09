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
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 20
countries with more global_citations in a given bibliographic dataset. 
<BLANKLINE>
- 'OCC' is the number of documents published.  
<BLANKLINE>
- 'local_citations' are the local citations in the dataset.
<BLANKLINE>
- 'global_citations' are the citations received 
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
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
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

    return chart(
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
