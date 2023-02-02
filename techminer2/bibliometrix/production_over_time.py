"""Production over time."""

import textwrap

import plotly.express as px

from ..techminer.indicators.indicators_by_topic import indicators_by_topic
from ..techminer.indicators.indicators_by_topic_per_year import (
    indicators_by_topic_per_year,
)
from ..vantagepoint.analyze.matrix.co_occ_matrix_list import _add_counters_to_items

TEXTLEN = 40


def bibliometrix__production_over_time(
    criterion,
    topics_length=10,
    topic_min_occ=None,
    topic_min_citations=None,
    directory="./",
    title=None,
    metric="OCC",
    database="documents",
    start_year=None,
    end_year=None,
    **filters,
):
    """Production over time."""

    indicators_by_year = _compute_production_over_time(
        criterion=criterion,
        topics_length=topics_length,
        topic_min_occ=topic_min_occ,
        topic_min_citations=topic_min_citations,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators_by_year = _add_counters_to_items(
        matrix_list=indicators_by_year,
        column_name=criterion.replace("_", " ").title(),
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators_by_year["global_occ"] = (
        indicators_by_year[criterion.replace("_", " ").title()]
        .str.split()
        .map(lambda x: x[-1])
        .str.split(":")
        .map(lambda x: x[0])
    )

    indicators_by_year = indicators_by_year.sort_values(
        by=[
            "global_occ",
            "Global Citations",
            criterion.replace("_", " ").title(),
            "Year",
        ],
        ascending=[False, False, True, True],
    )

    if indicators_by_year[criterion.replace("_", " ").title()].dtype != "int64":
        indicators_by_year[criterion.replace("_", " ").title()] = indicators_by_year[
            criterion.replace("_", " ").title()
        ].apply(_shorten)

    indicators_by_year.pop("global_occ")

    fig = px.scatter(
        indicators_by_year,
        x="Year",
        y=criterion.replace("_", " ").title(),
        size=metric,
        hover_data=indicators_by_year.columns.to_list(),
        title=title,
        color=criterion.replace("_", " ").title(),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=False,
        xaxis_title=None,
    )
    fig.update_traces(
        marker=dict(
            line=dict(
                color="black",
                width=2,
            ),
        ),
        marker_color="darkslategray",
        mode="lines+markers",
    )
    fig.update_xaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
        tickangle=270,
        dtick=1.0,
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
    )

    return fig


def _compute_production_over_time(
    criterion,
    topics_length,
    topic_min_occ,
    topic_min_citations,
    directory,
    database,
    start_year,
    end_year,
    **filters,
):

    indicators_by_year = indicators_by_topic_per_year(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    indicators_by_year = indicators_by_year.reset_index()

    selected_terms = indicators_by_topic(
        criterion=criterion,
        directory=directory,
        database=database,
        start_year=start_year,
        end_year=end_year,
        **filters,
    )

    if topic_min_occ is not None:
        selected_terms = selected_terms[selected_terms["OCC"] >= topic_min_occ]
    if topic_min_citations is not None:
        selected_terms = selected_terms[
            selected_terms["global_citations"] >= topic_min_citations
        ]

    selected_terms = selected_terms.head(topics_length)

    terms = selected_terms.index.to_list()

    indicators_by_year = indicators_by_year[
        indicators_by_year[criterion].map(lambda x: x in terms)
    ]

    indicators_by_year = indicators_by_year.rename(
        columns={
            col: col.replace("_", " ").title()
            for col in indicators_by_year.columns
            if col not in ["OCC", "cum_OCC"]
        }
    )

    return indicators_by_year


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )
