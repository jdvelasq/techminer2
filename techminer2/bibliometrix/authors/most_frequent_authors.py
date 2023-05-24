"""
Most Frequent Authors
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_authors.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.most_frequent_authors(
...     directory=directory,
...     topics_length=20,
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
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
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
<BLANKLINE>


"""
from ..bibliometric_indicators_by_topic import bibliometric_indicators_by_topic


def most_frequent_authors(
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
    """Plots the number of documents by author using the specified plot."""

    return bibliometric_indicators_by_topic(
        criterion="authors",
        metric="OCC",
        plot=plot,
        x_label=x_label,
        y_label=y_label,
        title="Most Frequent Authors",
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
