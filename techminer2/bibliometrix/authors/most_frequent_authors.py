"""
Most Frequent Authors
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_authors.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.most_frequent_authors(
...     directory,
...     topics_length=20,
...     plot="cleveland",
...     database="documents",
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_frequent_authors.html" height="600px" width="100%" frameBorder="0"></iframe>

    
>>> r.table_.head()
authors
Arner DW       3
Buckley RP     3
Barberis JN    2
Butler T/1     2
Hamdan A       2
Name: OCC, dtype: int64

>>> print(r.prompt_)
<BLANKLINE>
Act as a researcher realizing a bibliometric analysis. Analyze the following 
table, which provides data corresponding to the top 20
authors with more OCC in a given bibliographic dataset. 
<BLANKLINE>
- 'OCC' is the number of documents published.  
<BLANKLINE>
- 'local_citations' are the local citations in the dataset.
<BLANKLINE>
- 'global_citations' are the citations received 
<BLANKLINE>
| authors           |   OCC |
|:------------------|------:|
| Arner DW          |     3 |
| Buckley RP        |     3 |
| Barberis JN       |     2 |
| Butler T/1        |     2 |
| Hamdan A          |     2 |
| Turki M           |     2 |
| Lin W             |     2 |
| Singh C           |     2 |
| Brennan R         |     2 |
| Crane M           |     2 |
| Ryan P            |     2 |
| Sarea A           |     2 |
| Grassi L          |     2 |
| Lanfranchi D      |     2 |
| Arman AA          |     2 |
| Anagnostopoulos I |     1 |
| OBrien L          |     1 |
| Baxter LG         |     1 |
| Zetzsche DA       |     1 |
| Weber RH          |     1 |
<BLANKLINE>
Write a clear and concise paragraph describing the main findings and any 
important trends or patterns you notice. 
<BLANKLINE>
Limit your description to a paragraph with no more than 250 words.        
<BLANKLINE>
<BLANKLINE>


"""
from ...vantagepoint.report.chart import chart


def most_frequent_authors(
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
    """Plots the number of documents by author using the specified plot."""

    return chart(
        criterion="authors",
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Frequent Authors",
        plot=plot,
        **filters,
    )
