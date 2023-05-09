"""
Most Frequent Countries
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_countries.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.countries.most_frequent_countries(
...     directory,
...     topics_length=20,
...     plot="cleveland",
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
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 20
countries with more OCC in a given bibliographic dataset. 
<BLANKLINE>
- 'OCC' is the number of documents published.  
<BLANKLINE>
- 'local_citations' are the local citations in the dataset.
<BLANKLINE>
- 'global_citations' are the citations received 
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
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
<BLANKLINE>
<BLANKLINE>



"""
from ...vantagepoint.report.chart import chart


def most_frequent_countries(
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
    """Plots the number of documents by country using the specified plot."""

    return chart(
        criterion="countries",
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Frequent Countries",
        plot=plot,
        **filters,
    )
