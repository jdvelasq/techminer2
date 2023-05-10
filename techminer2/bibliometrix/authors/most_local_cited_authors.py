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
<BLANKLINE>
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 most local cited authors in the references of the documents in the dataset ('local_citations' column). Use the information in the table to draw conclusions about the impact and relevance of the reseach published by the cited authors. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
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
<BLANKLINE>


"""
from ...vantagepoint.report.chart import chart


def most_local_cited_authors(
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
    """Most Local Cited Authors (from Reference Lists)."""

    obj = chart(
        criterion="authors",
        directory=directory,
        database=database,
        metric="local_citations",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Local Cited Authors (from Reference Lists)",
        plot=plot,
        **filters,
    )

    obj.prompt_ = _create_prompt(obj.table_)

    return obj


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} most local cited authors in the \
references of the documents in the dataset ('local_citations' column). Use the \
information in the table to draw conclusions about the impact and relevance of \
the reseach published by the cited authors. In your analysis, be sure \
to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
