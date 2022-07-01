"""Primitive to plot production over time."""
import textwrap

import plotly.express as px

from .column_indicators import column_indicators
from .column_indicators_by_year import column_indicators_by_year

TEXTLEN = 40


def production_over_time(
    column,
    top_n=10,
    directory="./",
    title=None,
):
    """Primitive to plot production over time."""

    indicators_by_year = _compute_production_over_time(
        column=column,
        top_n=top_n,
        directory=directory,
    )

    fig = px.scatter(
        indicators_by_year,
        x="Year",
        y=column.replace("_", " ").title(),
        size="Num Documents",
        hover_data=indicators_by_year.columns.to_list(),
        title=title,
        color=column.replace("_", " ").title(),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        xaxis_type="category",
        showlegend=False,
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
    )
    fig.update_yaxes(
        linecolor="white",
        linewidth=1,
        gridcolor="gray",
        griddash="dot",
    )

    return fig


def _compute_production_over_time(
    column,
    top_n=10,
    directory="./",
):

    indicators_by_year = column_indicators_by_year(
        column=column, directory=directory, database="documents", use_filter=True
    )
    indicators_by_year = indicators_by_year.reset_index()
    selected_terms = column_indicators(column=column, directory=directory).head(top_n)
    terms = selected_terms.index.to_list()

    indicators_by_year = indicators_by_year[
        indicators_by_year[column].map(lambda x: x in terms)
    ]

    if indicators_by_year[column].dtype != "int64":
        indicators_by_year[column] = indicators_by_year[column].apply(_shorten)

    indicators_by_year = indicators_by_year.rename(
        columns={
            col: col.replace("_", " ").title() for col in indicators_by_year.columns
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
