"""
Most Relevant Sources
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/bibliometrix__most_relevant_sources.html"

>>> from techminer2 import bibliometrix__most_relevant_sources
>>> bibliometrix__most_relevant_sources(
...     directory=directory,
...     topics_length=20,
...     plot="cleveland",
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/bibliometrix__most_relevant_sources.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .vantagepoint.report.chart import chart


def bibliometrix__most_relevant_sources(
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
    """Most Relevant Sources."""

    return chart(
        criterion="source_abbr",
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=None,
        title="Most Relevant Sources",
        plot=plot,
        **filters,
    )
