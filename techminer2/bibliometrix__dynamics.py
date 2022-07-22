"""Bibliometrix generic dynamics plot."""

import textwrap

import numpy as np
import pandas as pd
import plotly.express as px

from ._indicators.column_indicators_by_year import column_indicators_by_year

TEXTLEN = 40


def bibliometrix__dynamics(
    column,
    top_n=10,
    directory="./",
    plot=True,
    title=None,
):
    """Bibliometrix generic dynamics plot."""

    indicators = column_indicators_by_year(directory=directory, column=column)
    indicators = indicators[["OCC"]]
    indicators = indicators.reset_index()
    indicators = indicators.sort_values([column, "year"], ascending=True)
    indicators = indicators.pivot(index="year", columns=column, values="OCC")
    indicators = indicators.fillna(0)

    # complete missing years
    year_range = list(range(indicators.index.min(), indicators.index.max() + 1))
    missing_years = [year for year in year_range if year not in indicators.index]
    pdf = pd.DataFrame(
        np.zeros((len(missing_years), len(indicators.columns))),
        index=missing_years,
        columns=indicators.columns,
    )
    indicators = indicators.append(pdf)
    indicators = indicators.sort_index()

    # top items
    occ = indicators.sum(axis=0)
    occ = occ.sort_values(ascending=False)

    indicators = indicators[occ.index[:top_n]]

    # cumsum
    indicators = indicators.cumsum()
    indicators = indicators.astype(int)
    if not plot:
        return indicators

    # plot
    indicators.columns = [col for col in indicators.columns]
    indicators = indicators.reset_index()
    indicators = indicators.rename(columns={"index": "year"})
    indicators = indicators.melt(
        id_vars="year",
        value_vars=indicators.columns,
        var_name=column,
        value_name="cum_OCC",
    )
    indicators[column] = indicators[column].apply(_shorten)

    #
    fig = px.line(
        indicators,
        x="year",
        y="cum_OCC",
        title=title,
        markers=True,
        hover_data=[column, "year", "cum_OCC"],
        color=column,
    )
    fig.update_traces(
        marker=dict(size=10, line=dict(color="darkslategray", width=2)),
        # marker_color="rgb(171,171,171)",
        # line=dict(color="darkslategray"),
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        # showlegend=False,
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=2,
        gridcolor="lightgray",
        griddash="dot",
        tickangle=270,
        dtick=1,
    )
    return fig


def _shorten(text):
    return textwrap.shorten(
        text=text,
        width=TEXTLEN,
        placeholder="...",
        break_long_words=False,
    )
