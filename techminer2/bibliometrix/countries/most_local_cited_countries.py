"""
Most Local Cited Countries
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
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 20
countries with more local_citations in a given bibliographic dataset. 
<BLANKLINE>
- 'OCC' is the number of documents published.  
<BLANKLINE>
- 'local_citations' are the local citations in the dataset.
<BLANKLINE>
- 'global_citations' are the citations received 
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
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
<BLANKLINE>
<BLANKLINE>


"""
from ...vantagepoint.report.chart import chart


def most_local_cited_countries(
    directory="./",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    plot="cleveland",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Most Local Cited Countries (from Reference Lists)."""

    return chart(
        criterion="countries",
        directory=directory,
        database=database,
        metric="local_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Local Cited Countries (from Reference Lists)",
        plot=plot,
        **filters,
    )
