# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""Most cited documents."""

import os
from dataclasses import dataclass

import plotly.express as px

from ..._read_records import read_records
from ...format_prompt_for_records import format_prompt_for_records
from ...format_report_for_records import format_report_for_records
from ...performance_metrics.global_indicators_by_document import global_indicators_by_document

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def most_cited_documents(
    #
    # FUNCTION PARAMS:
    metric,
    top_n,
    #
    # CHART PARAMS:
    title,
    field_label,
    metric_label,
    textfont_size,
    marker_size,
    line_width,
    yshift,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Most cited documents."""

    __report(
        #
        # FUNCTION PARAMS:
        metric=metric,
        top_n=top_n,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators, fig = __indicators_and_fig(
        #
        # FUNCTION PARAMS:
        metric=metric,
        top_n=top_n,
        #
        # CHART PARAMS:
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    @dataclass
    class Results:
        df_ = indicators
        fig_ = fig

    return Results()


def __indicators_and_fig(
    #
    # FUNCTION PARAMS:
    metric,
    top_n,
    #
    # CHART PARAMS:
    title,
    field_label,
    metric_label,
    textfont_size,
    marker_size,
    line_width,
    yshift,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    indicators = global_indicators_by_document(
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    indicators = indicators.sort_values([metric], ascending=False)
    indicators = indicators.head(top_n)
    indicators = indicators.reset_index()
    indicators = indicators.set_index("article")

    metric_label = metric.replace("_", " ").upper() if metric_label is None else metric_label

    field_label = (
        metric.replace("_", " ").upper() + " RANKING" if field_label is None else field_label
    )

    table = indicators.copy()
    table["Rank"] = list(range(1, len(table) + 1))

    fig = px.line(
        table,
        x="Rank",
        y=metric,
        hover_data=indicators.columns.to_list(),
        markers=True,
    )

    fig.update_traces(
        marker={
            "size": marker_size,
            "line": {"color": MARKER_LINE_COLOR, "width": 1},
        },
        marker_color=MARKER_COLOR,
        line={"color": MARKER_LINE_COLOR, "width": line_width},
    )
    fig.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        title_text=title if title is not None else "",
    )
    fig.update_yaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=metric_label,
    )
    fig.update_xaxes(
        linecolor="gray",
        linewidth=1,
        gridcolor="lightgray",
        griddash="dot",
        title=field_label,
    )

    for name, row in table.iterrows():
        fig.add_annotation(
            x=row["Rank"],
            y=row[metric],
            text=name,
            showarrow=False,
            textangle=-90,
            yanchor="bottom",
            font={"size": textfont_size},
            yshift=yshift,
        )

    return indicators, fig


def __report(
    #
    # FUNCTION PARAMS:
    metric,
    top_n,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    records = read_records(
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    if metric == "local_citations":
        columns = ["local_citations", "global_citations", "year", "article"]
        ascending = [False, False, False, True]
        if database == "main":
            report_filename = "most_local_cited_documents__abstracts.txt"
            prompt_filename = "most_local_cited_documents__prompt.txt"
        if database == "references":
            report_filename = "most_local_cited_references__abstracts.txt"
            prompt_filename = "most_local_cited_references__prompt.txt"
    else:
        columns = ["global_citations", "local_citations", "year", "article"]
        ascending = [False, False, False, True]
        if database == "main":
            report_filename = "most_global_cited_documents__abstracts.txt"
            prompt_filename = "most_global_cited_documents__prompt.txt"
        if database == "references":
            report_filename = "most_global_cited_references__abstracts.txt"
            prompt_filename = "most_global_cited_references__prompt.txt"

    records = records.sort_values(columns, ascending=ascending)
    records = records.head(top_n)

    format_report_for_records(
        root_dir=root_dir,
        target_dir="",
        records=records,
        report_filename=report_filename,
    )

    main_text = (
        "Your task is to generate a short summary for each of the following "
        "paragraphs. Summarize each one the paragraphs below, delimited by "
        "triple backticks, in at most 30 words, focusing on the main "
        "contribution described in the paragraph. "
    )

    text = format_prompt_for_records(
        main_text,
        records,
        weight=None,
    )

    file_name = os.path.join(root_dir, "reports", prompt_filename)
    with open(file_name, "w", encoding="utf-8") as file:
        print(text, file=file)

    print(f"--INFO-- The file '{file_name}' was created.")
