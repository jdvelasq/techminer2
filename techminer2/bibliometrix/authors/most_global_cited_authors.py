"""Most Global Cited Authors
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_global_cited_authors.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.most_global_cited_authors(
...     directory,
...     topics_length=20,
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
Analyze the table below, which provides bibliographic indicators for a collection of research articles. Identify any notable patterns, trends, or outliers in the data, and discuss their implications for the research field. Be sure to provide a concise summary of your findings in no more than 150 words.
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
<BLANKLINE>


"""
from ... import vantagepoint


def most_global_cited_authors(
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
    """Most global cited authors."""

    obj = vantagepoint.analyze.extract_topics(
        criterion="authors",
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
        title="Most Global Cited Authors",
        x_label="Global Citations",
        y_label="AUTHORS",
    )

    return chart
