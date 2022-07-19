"""Production over time."""

import textwrap

import plotly.express as px

from ..co_occ_matrix_list import _add_counters_to_items
from ..column_indicators import column_indicators
from .column_indicators_by_year import column_indicators_by_year

TEXTLEN = 40


def production_over_time(
    column,
    top_n=10,
    directory="./",
    title=None,
    metric="OCC",
):
    """Production over time."""

    indicators_by_year = _compute_production_over_time(
        column=column,
        top_n=top_n,
        directory=directory,
    )

    indicators_by_year = _add_counters_to_items(
        column,
        column.replace("_", " ").title(),
        directory,
        "documents",
        indicators_by_year,
    )

    indicators_by_year["global_occ"] = (
        indicators_by_year[column.replace("_", " ").title()]
        .str.split()
        .map(lambda x: x[-1])
        .str.split(":")
        .map(lambda x: x[0])
    )
    indicators_by_year = indicators_by_year.sort_values(
        by=["global_occ", "Global Citations", column.replace("_", " ").title(), "Year"],
        ascending=[False, False, True, True],
    )

    if indicators_by_year[column.replace("_", " ").title()].dtype != "int64":
        indicators_by_year[column.replace("_", " ").title()] = indicators_by_year[
            column.replace("_", " ").title()
        ].apply(_shorten)

    indicators_by_year.pop("global_occ")

    fig = px.scatter(
        indicators_by_year,
        x="Year",
        y=column.replace("_", " ").title(),
        size=metric,
        hover_data=indicators_by_year.columns.to_list(),
        title=title,
        color=column.replace("_", " ").title(),
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

    indicators_by_year = indicators_by_year.rename(
        columns={
            col: col.replace("_", " ").title()
            for col in indicators_by_year.columns
            if col not in ["OCC", "cum_OCC"]
        }
    )

    # indicators_by_year = indicators_by_year.rename(
    #     columns={
    #         "cum_OCC": "Cum OCC",
    #     }
    # )

    return indicators_by_year


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )
