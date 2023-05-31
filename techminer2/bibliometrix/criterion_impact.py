"""Make impact indicators plot."""

import textwrap
from dataclasses import dataclass

from .. import vantagepoint
from .._px.bar_px import bar_px
from .._px.cleveland_px import cleveland_px
from .._px.column_px import column_px
from .._px.line_px import line_px
from .._px.pie_px import pie_px
from ..item_utils import generate_custom_items
from ..techminer.indicators.impact_indicators_by_topic import (
    impact_indicators_by_topic,
)


@dataclass(init=False)
class _ImpactIndicators:
    table_: None
    metric_: None


TEXTLEN = 40


def criterion_impact(
    criterion,
    directory="./",
    database="documents",
    metric="h_index",
    topics_length=20,
    topic_min_occ=None,
    topic_max_occ=None,
    topic_min_citations=None,
    topic_max_citations=None,
    custom_topics=None,
    title=None,
    x_label=None,
    y_label=None,
    start_year=None,
    end_year=None,
    **filters,
):
    """computes local impact by <column>"""

    def check_metric(metric):
        if metric not in [
            "h_index",
            "g_index",
            "m_index",
            "global_citations",
        ]:
            raise ValueError(
                "Impact measure must be one of: h_index, g_index, m_index, global_citations"
            )

    def sort_indicators(indicators, metric):
        return indicators.sort_values(
            by=[metric, "global_citations"], ascending=[False, False]
        )

    check_metric(metric)

    indicators = impact_indicators_by_topic(
        criterion=criterion,
        root_dir=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators = sort_indicators(indicators, metric)

    if custom_topics is None:
        custom_topics = generate_custom_items(
            topics_length,
            topic_min_occ,
            topic_max_occ,
            topic_min_citations,
            topic_max_citations,
            indicators,
        )
    else:
        custom_topics = filter_custom_topics(indicators, custom_topics)

    indicators = indicators.loc[custom_topics, :]

    # if custom_topics is None:
    #     custom_topics = generate_custom_topics(
    #         topics_length,
    #         topic_min_occ,
    #         topic_max_occ,
    #         topic_min_citations,
    #         topic_max_citations,
    #         indicators,
    #     )
    # else:
    #     custom_topics = filter_custom_topics(indicators, custom_topics)

    # indicators = indicators.loc[custom_topics, :]

    # indicators[criterion] = indicators[criterion].apply(_shorten)

    column_names = {
        column: column.replace("_", " ").title()
        for column in indicators.columns
    }

    indicators = indicators.rename(columns=column_names)
    indicators = indicators.rename(
        columns={
            "H Index": "H-Index",
            "G Index": "G-Index",
            "M Index": "M-Index",
            "Occ": "OCC",
        }
    )

    obj = _ImpactIndicators()
    obj.table_ = indicators
    obj.criterion_ = criterion
    obj.metric_ = (
        metric.replace("h_index", "H-Index")
        .replace("g_index", "G-Index")
        .replace("m_ndex", "M-Index")
        .replace("Occ", "OCC")
    )

    chart = vantagepoint.report.cleveland_chart(
        obj,
        title=title,
        x_label=x_label,
        y_label=y_label,
    )

    chart.table_ = indicators

    return chart


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )
