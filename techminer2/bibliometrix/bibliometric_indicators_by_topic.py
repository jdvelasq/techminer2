"""Biblometric indicators by topic



"""

from .. import vantagepoint


def bibliometric_indicators_by_topic(
    criterion,
    metric,
    plot,
    x_label=None,
    y_label=None,
    title=None,
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

    obj = vantagepoint.analyze.list_view(
        criterion=criterion,
        root_dir=directory,
        database=database,
        metric=metric,
        start_year=start_year,
        end_year=end_year,
        topics_length=topics_length,
        topic_occ_min=topic_min_occ,
        topic_occ_max=topic_max_occ,
        topic_citations_min=topic_min_citations,
        topic_citations_max=topic_max_citations,
        custom_topics=custom_topics,
        **filters,
    )

    vantagepoint_chart = {
        "bar_chart": vantagepoint.report.bar_chart,
        "cleveland_chart": vantagepoint.report.cleveland_chart,
        "column_chart": vantagepoint.report.column_chart,
        "line_chart": vantagepoint.report.line_chart,
    }[plot]

    chart = vantagepoint_chart(
        obj,
        title=title,
        x_label=x_label,
        y_label=y_label,
    )

    return chart
