# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Performance Metrics
===============================================================================

>>> from techminer2.analyze import performance_metrics
>>> metrics = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     metric='OCCGC',
...     #
...     # CHART PARAMS:
...     title=None,
...     field_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # TREND ANALYSIS:
...     time_window=2,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.head().to_markdown())
| author_keywords       |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:----------------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| REGTECH               |          1 |          1 |          1 |    28 |                329 |                74 |         9 |         4 |      1.29 |
| FINTECH               |          2 |          2 |          2 |    12 |                249 |                49 |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY |          3 |          8 |          9 |     7 |                 37 |                10 |         4 |         2 |      1    |
| COMPLIANCE            |          4 |         12 |         10 |     7 |                 30 |                 9 |         3 |         2 |      0.6  |
| REGULATION            |          5 |          4 |          3 |     5 |                164 |                22 |         2 |         2 |      0.33 |



>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...



>>> metrics.fig_.write_html("sphinx/_static/analyze/performance_metrics.html")

.. raw:: html

    <iframe src="../../../../_static/analyze/performance_metrics.html"
    height="600px" width="100%" frameBorder="0"></iframe>

    
>>> from techminer2.performance import performance_metrics
>>> metrics = performance_metrics(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     metric='OCC',
...     #
...     # CHART PARAMS:
...     title=None,
...     field_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # ITEM FILTERS:
...     top_n=20,
...     occ_range=(2, 4),
...     gc_range=(None, None),
...     custom_items=None,
...     #
...     # TREND ANALYSIS:
...     time_window=2,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.head().to_markdown())
| author_keywords         |   rank_occ |   OCC |   before_2022 |   between_2022_2023 |   growth_percentage |
|:------------------------|-----------:|------:|--------------:|--------------------:|--------------------:|
| FINANCIAL_SERVICES      |          7 |     4 |             3 |                   1 |               25    |
| FINANCIAL_REGULATION    |          8 |     4 |             2 |                   2 |               50    |
| ARTIFICIAL_INTELLIGENCE |          9 |     4 |             3 |                   1 |               25    |
| RISK_MANAGEMENT         |         10 |     3 |             2 |                   1 |               33.33 |
| INNOVATION              |         11 |     3 |             2 |                   1 |               33.33 |



"""
import os
from dataclasses import dataclass

import plotly.express as px

from .._filtering_lib import generate_custom_items
from .._sorting_lib import sort_indicators_by_metric
from ..format_prompt_for_dataframes import format_prompt_for_dataframes
from ..indicators.global_indicators_by_field import global_indicators_by_field

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def performance_metrics(
    #
    # PERFORMANCE PARAMS:
    field,
    metric=None,
    #
    # CHART PARAMS:
    title=None,
    field_label=None,
    metric_label=None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # ITEM FILTERS:
    top_n=None,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_items=None,
    #
    # TREND ANALYSIS:
    time_window=2,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """
    :meta private:
    """
    #
    # MAIN CODE:
    #
    data_frame = ___table(
        #
        # ITEMS PARAMS:
        field=field,
        metric=metric,
        #
        # ITEM FILTERS:
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
        #
        # TREND ANALYSIS:
        time_window=time_window,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = _select_columns(data_frame=data_frame, metric=metric)

    if metric == "OCCGC":
        metric = "OCC"

    prompt = _prompt(
        field=field,
        metric=metric,
        data_frame=data_frame.head(200),
    )

    fig = _fig(
        #
        # DATA PARAMS:
        field=field,
        metric=metric,
        data_frame=data_frame.head(200),
        #
        # CHART PARAMS:
        title=title,
        field_label=field_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
    )

    #
    # Save results to disk as csv tab-delimited file for papers
    file_path = os.path.join(root_dir, "reports", field + ".csv")
    data_frame.to_csv(file_path, sep="\t", header=True, index=True)
    # print("--INFO-- File saved to ", file_path)

    @dataclass
    class Results:
        df_ = data_frame
        prompt_ = prompt
        fig_ = fig

    return Results()


def ___table(
    #
    # ITEMS PARAMS:
    field,
    metric,
    #
    # ITEM FILTERS:
    top_n,
    occ_range,
    gc_range,
    custom_items,
    #
    # TREND ANALYSIS:
    time_window,
    #
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    #
    # MAIN CODE:
    #

    #
    # Compute performance metrics for all items in the field
    data_frame = global_indicators_by_field(
        field=field,
        #
        # TREND ANALYSIS:
        time_window=time_window,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Sorts the performance metrics table with all indicators by the metric
    # data_frame = sort_indicators_by_metric(data_frame, metric, is_trend_analysis=False)

    if custom_items is None:
        #
        if metric == "OCCGC":
            #
            # In this case not is possibe to use trend_analysis
            #
            # Selects the top_n items by OCC
            custom_items_occ = generate_custom_items(
                indicators=data_frame,
                metric="OCC",
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            #
            # Selects the top_n items by GCS
            custom_items_gc = generate_custom_items(
                indicators=data_frame,
                metric="global_citations",
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items = custom_items_occ[:]
            custom_items += [item for item in custom_items_gc if item not in custom_items_occ]

        else:
            #
            # Default custom items selection
            custom_items = generate_custom_items(
                indicators=data_frame,
                metric=metric,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

    data_frame = data_frame[data_frame.index.isin(custom_items)]
    data_frame = sort_indicators_by_metric(data_frame, metric)

    return data_frame


def _select_columns(data_frame, metric):
    #
    #

    if metric == "OCCGC":
        columns = [
            "rank_occ",
            "rank_gcs",
            "rank_lcs",
            "OCC",
            "global_citations",
            "local_citations",
            "h_index",
            "g_index",
            "m_index",
        ]

    if metric == "OCC":
        columns = [
            "rank_occ",
            "OCC",
            data_frame.columns[4],
            data_frame.columns[5],
            "growth_percentage",
        ]

    if metric in [
        "global_citations",
        "local_citations",
    ]:
        columns = [
            "rank_gcs",
            "rank_lcs",
            "global_citations",
            "local_citations",
            "global_citations_per_document",
            "local_citations_per_document",
            "global_citations_per_year",
        ]

    if metric in [
        "h_index",
        "g_index",
        "m_index",
    ]:
        columns = [
            "h_index",
            "g_index",
            "m_index",
        ]

    return data_frame[columns]


def _prompt(field, metric, data_frame):
    main_text = (
        "Your task is to generate an analysis about the bibliometric indicators of the "
        f"'{field}' field in a scientific bibliography database. Summarize the table below, "
        f"sorted by the '{metric}' metric, and delimited by triple backticks, identify "
        "any notable patterns, trends, or outliers in the data, and discuss their "
        "implications for the research field. Be sure to provide a concise summary "
        "of your findings in no more than 150 words. "
    )
    return format_prompt_for_dataframes(main_text, data_frame.to_markdown())


def _fig(
    #
    # DATA PARAMS:
    field,
    metric,
    data_frame,
    #
    # CHART PARAMS:
    title,
    field_label,
    metric_label,
    textfont_size,
    marker_size,
    line_width,
    yshift,
):
    """Creates a rank chart."""

    if metric == "word_trends":
        metric = "OCC"

    metric_label = metric.replace("_", " ").upper() if metric_label is None else metric_label

    field_label = (
        field.replace("_", " ").upper() + " RANKING" if field_label is None else field_label
    )

    table = data_frame.copy()
    table["Rank"] = list(range(1, len(table) + 1))

    fig = px.line(
        table,
        x="Rank",
        y=metric,
        hover_data=data_frame.columns.to_list(),
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

    return fig
