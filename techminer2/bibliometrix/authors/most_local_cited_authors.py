"""
Most Local Cited Authors
===============================================================================




>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_local_cited_authors.html"


>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.most_local_cited_authors(
...     topics_length=20,
...     directory=directory,
... )
>>> r.plot_.write_html(file_name)

.. raw:: html

    <iframe src="../../../_static/bibliometrix__most_local_cited_authors.html" height="600px" width="100%" frameBorder="0"></iframe>


>>> r.table_.head()    
authors
Butler T/1           19
Anagnostopoulos I    17
OBrien L             14
Arner DW              8
Buckley RP            8
Name: local_citations, dtype: int64

>>> print(r.prompt_)
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
| authors           |   local_citations |
|:------------------|------------------:|
| Butler T/1        |                19 |
| Anagnostopoulos I |                17 |
| OBrien L          |                14 |
| Arner DW          |                 8 |
| Buckley RP        |                 8 |
| Stieber H         |                 8 |
| Saxton K          |                 8 |
| Breymann W        |                 8 |
| Kavassalis P      |                 8 |
| Gross FJ          |                 8 |
| Zetzsche DA       |                 5 |
| Weber RH          |                 5 |
| Hamdan A          |                 5 |
| Turki M           |                 5 |
| Brooks R          |                 5 |
| Lin W             |                 4 |
| Singh C           |                 4 |
| Sarea A           |                 4 |
| Cummings RT       |                 4 |
| Anasweh M         |                 4 |
<BLANKLINE>
<BLANKLINE>


"""
from ..bibliometric_indicators_by_topic import bibliometric_indicators_by_topic


def most_local_cited_authors(
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
    """Most local cited authors."""

    return bibliometric_indicators_by_topic(
        criterion="authors",
        metric="local_citations",
        plot=plot,
        x_label=x_label,
        y_label=y_label,
        title="Most Local Cited Authors",
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
