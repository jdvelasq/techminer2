"""Most Global Cited Authors
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_authors.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.most_global_cited_authors(
...     directory,
...     topics_length=20,
...     plot="cleveland",
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_global_cited_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
authors
Arner DW             185
Buckley RP           185
Barberis JN          161
Anagnostopoulos I    153
Butler T/1            41
Name: global_citations, dtype: int64

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 20
authors with more global_citations in a given bibliographic dataset. 
<BLANKLINE>
- 'OCC' is the number of documents published.  
<BLANKLINE>
- 'local_citations' are the local citations in the dataset.
<BLANKLINE>
- 'global_citations' are the citations received 
<BLANKLINE>
| authors           |   global_citations |
|:------------------|-------------------:|
| Arner DW          |                185 |
| Buckley RP        |                185 |
| Barberis JN       |                161 |
| Anagnostopoulos I |                153 |
| Butler T/1        |                 41 |
| OBrien L          |                 33 |
| Baxter LG         |                 30 |
| Zetzsche DA       |                 24 |
| Weber RH          |                 24 |
| Stieber H         |                 21 |
| Saxton K          |                 21 |
| Breymann W        |                 21 |
| Kavassalis P      |                 21 |
| Gross FJ          |                 21 |
| Hamdan A          |                 18 |
| Turki M           |                 18 |
| Lin W             |                 17 |
| Singh C           |                 17 |
| Brennan R         |                 14 |
| Crane M           |                 14 |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
<BLANKLINE>
<BLANKLINE>

"""
from ...vantagepoint.report.chart import chart


def most_global_cited_authors(
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
    """Most global cited authors."""

    return chart(
        criterion="authors",
        directory=directory,
        database=database,
        metric="global_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Global Cited Authors",
        plot=plot,
        **filters,
    )
