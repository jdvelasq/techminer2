# flake8: noqa
# pylint: disable=line-too-long
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
"""Indicators by year module"""

from dataclasses import dataclass

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from .._chatbot import format_chatbot_prompt_for_df


def indicators_by_year(filtered_records):
    filtered_records = filtered_records.copy()

    filtered_records = filtered_records.assign(OCC=1)

    columns = ["OCC", "year"]

    if "local_citations" in filtered_records.columns:
        columns.append("local_citations")
    if "global_citations" in filtered_records.columns:
        columns.append("global_citations")
    filtered_records = filtered_records[columns]

    filtered_records["year"] = filtered_records["year"].astype(int)
    filtered_records = filtered_records.groupby("year", as_index=True).sum()
    filtered_records = filtered_records.sort_index(ascending=True, axis=0)
    filtered_records = filtered_records.assign(
        cum_OCC=filtered_records.OCC.cumsum()
    )
    filtered_records.insert(1, "cum_OCC", filtered_records.pop("cum_OCC"))

    current_year = filtered_records.index.max()
    filtered_records = filtered_records.assign(
        citable_years=current_year - filtered_records.index + 1
    )

    if "global_citations" in filtered_records.columns:
        filtered_records = filtered_records.assign(
            mean_global_citations=filtered_records.global_citations
            / filtered_records.OCC
        )
        filtered_records = filtered_records.assign(
            cum_global_citations=filtered_records.global_citations.cumsum()
        )
        filtered_records = filtered_records.assign(
            mean_global_citations_per_year=filtered_records.mean_global_citations
            / filtered_records.citable_years
        )
        filtered_records.mean_global_citations_per_year = (
            filtered_records.mean_global_citations_per_year.round(2)
        )

    if "local_citations" in filtered_records.columns:
        filtered_records = filtered_records.assign(
            mean_local_citations=filtered_records.local_citations
            / filtered_records.OCC
        )
        filtered_records = filtered_records.assign(
            cum_local_citations=filtered_records.local_citations.cumsum()
        )
        filtered_records = filtered_records.assign(
            mean_local_citations_per_year=filtered_records.mean_local_citations
            / filtered_records.citable_years
        )
        filtered_records.mean_local_citations_per_year = (
            filtered_records.mean_local_citations_per_year.round(2)
        )

    return filtered_records


def time_plot(
    indicators,
    metric,
    title,
):
    """Makes a line plot for annual indicators."""

    column_names = {
        column: column.replace("_", " ").title()
        for column in indicators.columns
        if column not in ["OCC", "cum_OCC"]
    }
    column_names["OCC"] = "OCC"
    column_names["cum_OCC"] = "cum_OCC"
    indicators = indicators.rename(columns=column_names)

    fig = px.line(
        indicators,
        x=indicators.index,
        y=column_names[metric],
        title=title,
        markers=True,
        hover_data=["OCC", "Global Citations", "Local Citations"],
    )
    fig.update_traces(
        marker={"size": 10, "line": {"color": "darkslategray", "width": 2}},
        marker_color="rgb(171,171,171)",
        line={"color": "darkslategray"},
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
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
    )
    return fig


@dataclass
class IndicatorsPerYearChart:
    df_: pd.DataFrame
    fig_: go.Figure
    prompt_: str


def records_per_year_chart(
    records: pd.DataFrame,
    title: str,
):
    def generate_chatgpt_prompt(table):
        main_text = (
            "The table below, delimited by triple backticks, provides data on the annual scientific "
            "production in a bibliographic database. Use the table to draw conclusions about annual "
            "research productivity and the cumulative productivity. The "
            "column 'OCC' is the number of documents published in a given "
            "year. The column 'cum_OCC' is the cumulative number of "
            "documents published up to a given year. The information in the "
            "table is used to create a line plot of number of publications "
            "per year. In your analysis, be sure to describe in a clear and "
            "concise way, any trends or patterns you observe, and identify "
            "any outliers or anomalies in the data. Limit your description "
            "to one paragraph with no more than 250 words."
        )

        table_text = table.to_markdown()
        return format_chatbot_prompt_for_df(main_text, table_text)

    #
    # Main code
    #

    indicators = indicators_by_year(records)
    fig = time_plot(
        indicators,
        metric="OCC",
        title=title,
    )
    prompt = generate_chatgpt_prompt(indicators[["OCC", "cum_OCC"]])

    return IndicatorsPerYearChart(
        df_=indicators,
        fig_=fig,
        prompt_=prompt,
    )
