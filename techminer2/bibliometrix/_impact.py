"""Make impact indicators plot."""

import textwrap
from dataclasses import dataclass

from .._px.bar_px import bar_px
from .._px.cleveland_px import cleveland_px
from .._px.column_px import column_px
from .._px.line_px import line_px
from .._px.pie_px import pie_px
from ..techminer.indicators.impact_indicators_by_topic import impact_indicators_by_topic


@dataclass(init=False)
class _Results:
    table_ = None
    plot_ = None


TEXTLEN = 40


def _impact(
    criterion,
    impact_measure="h_index",
    topics_length=20,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    title=None,
    plot="cleveland",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """computes local impact by <column>"""

    if impact_measure not in [
        "h_index",
        "g_index",
        "m_index",
        "global_citations",
    ]:
        raise ValueError(
            "Impact measure must be one of: h_index, g_index, m_index, global_citations"
        )

    indicators = impact_indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if topic_min_occ is not None:
        indicators = indicators[indicators["OCC"] >= topic_min_occ]
    if topic_min_citations is not None:
        indicators = indicators[indicators["global_citations"] >= topic_min_citations]

    indicators = indicators.sort_values(
        by=[impact_measure, "global_citations"], ascending=[False, False]
    )
    indicators = indicators.head(topics_length)
    indicators = indicators.reset_index()
    indicators[criterion] = indicators[criterion].apply(_shorten)

    column_names = {
        column: column.replace("_", " ").title() for column in indicators.columns
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

    plot_function = {
        "bar": bar_px,
        "column": column_px,
        "line": line_px,
        "pie": pie_px,
        "cleveland": cleveland_px,
    }[plot]

    results = _Results()
    results.table_ = indicators
    results.plot_ = plot_function(
        dataframe=indicators,
        x_label=impact_measure.replace("_", "-").title(),
        y_label=criterion.replace("_", " ").title(),
        title=title,
    )

    return results


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )
