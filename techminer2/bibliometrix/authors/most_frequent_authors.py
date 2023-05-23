"""
Most Frequent Authors (GPT)
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_frequent_authors.html"

>>> from techminer2 import bibliometrix
>>> r = bibliometrix.authors.most_frequent_authors(
...     directory,
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


"""
from ... import vantagepoint


def most_frequent_authors(
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

    obj = vantagepoint.analyze.extract_topics(
        criterion="authors",
        directory=directory,
        database=database,
        metric="OCC",
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
        title="Most Frequent Authors",
        x_label="OCC",
        y_label="AUTHORS",
    )

    return chart
