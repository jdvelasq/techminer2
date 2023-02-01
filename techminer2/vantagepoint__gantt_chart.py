"""
Gantt Chart
===============================================================================


>>> directory = "data/regtech/"
>>> file_name = "sphinx/_static/vantagepoint__gantt_chart.html"

>>> from techminer2 import vantagepoint__gantt_chart
>>> vantagepoint__gantt_chart(
...     criterion='author_keywords',
...     topics_length=20, 
...     directory=directory,
... ).write_html(file_name)

.. raw:: html

    <iframe src="../../_static/vantagepoint__gantt_chart.html" height="800px" width="100%" frameBorder="0"></iframe>

"""
import plotly.express as px

from ._read_records import read_records
from .tm2__indicators_by_topic import tm2__indicators_by_topic


def vantagepoint__gantt_chart(
    criterion="author_keywords",
    directory="./",
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    custom_topics=None,
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Makes a gantt (timeline) chart."""

    records = read_records(
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    records = records[["year", criterion]]
    records = records.dropna(subset=[criterion])
    records[criterion] = records[criterion].str.split(";")
    records = records.explode(criterion)
    records[criterion] = records[criterion].str.strip()
    records = records.groupby(criterion).agg({"year": [min, max]})
    records.columns = records.columns.droplevel()
    records = records.rename(columns={"min": "start", "max": "finish"})
    records["data"] = records.index

    records["start"] = records["start"].astype(str) + "-01-01"
    records["finish"] = records["finish"].astype(str) + "-12-31"

    indicators = tm2__indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )
    indicators = indicators.sort_values(
        ["OCC", "global_citations", "local_citations"],
        ascending=[False, False, False],
    )
    if custom_topics is None:
        custom_topics = indicators.copy()
        if topic_min_occ is not None:
            custom_topics = custom_topics[custom_topics["OCC"] >= topic_min_occ]
        if topic_min_citations is not None:
            custom_topics = custom_topics[
                custom_topics["global_citations"] >= topic_min_citations
            ]
        custom_topics = custom_topics.index.copy()
        custom_topics = custom_topics[:topics_length]
    else:
        custom_topics = [
            topic for topic in custom_topics if topic in indicators.index.tolist()
        ]

    records = records.loc[custom_topics, :]

    fig = px.timeline(
        records,
        x_start="start",
        x_end="finish",
        y="data",
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=1, r=1, t=1, b=1),
        yaxis_title=None,
    )
    fig.update_traces(
        marker_color="lightgray",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        autorange="reversed",
    )

    return fig
