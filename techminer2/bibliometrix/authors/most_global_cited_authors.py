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
Imagine that you are a researcher analyzing a bibliographic dataset. The table below provides data on top 20 cited authors with highest number of total citations in the dataset ('global_citations' column). Use the information in the table to draw conclusions about the impact and relevance of the reseach published by the authors in the dataset. In your analysis, be sure to describe in a clear and concise way, any findings or any patterns you observe, and identify any outliers or anomalies in the data. Limit your description to one paragraph with no more than 250 words.
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

    obj = chart(
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

    obj.prompt_ = _create_prompt(obj.table_)

    return obj


def _create_prompt(table):
    return f"""
Imagine that you are a researcher analyzing a bibliographic dataset. The table \
below provides data on top {table.shape[0]} cited authors with highest \
number of total citations in the dataset ('global_citations' column). Use the \
information in the table to draw conclusions about the impact and relevance of \
the reseach published by the authors in the dataset. In your analysis, be sure \
to describe in a clear and concise way, any findings or any patterns you \
observe, and identify any outliers or anomalies in the data. \
Limit your description to one paragraph with no more than 250 words.

{table.to_markdown()}


"""
