"""
Line Chart
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__line_chart.html"

>>> from techminer2 import vantagepoint
>>> vantagepoint.report.line_chart(
...     criterion='author_keywords',
...     topics_length=15,
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__line_chart.html" height="600px" width="100%" frameBorder="0"></iframe>

"""
from .chart import chart


def line_chart(
    criterion,
    directory="./",
    database="documents",
    start_year=None,
    end_year=None,
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    title=None,
    **filters
):
    """Plots a bar chart from a column of a dataframe."""

    return chart(
        criterion=criterion,
        directory=directory,
        database=database,
        metric="OCC",
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        custom_topics=custom_topics,
        title=title,
        plot="line",
        **filters,
    )
