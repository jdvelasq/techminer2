# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.performance.performance_metrics:

Performance Metrics
===============================================================================

>>> from techminer2.performance import performance_metrics
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
...     # DATABASE PARAMS:
...     root_dir="data/karla/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
...     #
...     authors=['Lau HC', 'Handoko SD'],
... )
>>> print(metrics.df_.head().to_markdown())


>>> from techminer2.performance import performance_metrics
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
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> print(metrics.df_.head().to_markdown())
| author_keywords       |   rank_occ |   rank_gc |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:----------------------|-----------:|----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| REGTECH               |          1 |         1 |    28 |                329 |                73 |         9 |         4 |      1.29 |
| FINTECH               |          2 |         2 |    12 |                249 |                48 |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY |          3 |         8 |     7 |                 37 |                10 |         4 |         2 |      1    |
| COMPLIANCE            |          4 |        12 |     7 |                 30 |                 9 |         3 |         2 |      0.6  |
| REGULATION            |          5 |         4 |     5 |                164 |                22 |         2 |         2 |      0.33 |


>>> print(metrics.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'author_keywords' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords                           |   rank_occ |   rank_gc |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:------------------------------------------|-----------:|----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| REGTECH                                   |          1 |         1 |    28 |                329 |                73 |         9 |         4 |      1.29 |
| FINTECH                                   |          2 |         2 |    12 |                249 |                48 |         5 |         3 |      0.83 |
| REGULATORY_TECHNOLOGY                     |          3 |         8 |     7 |                 37 |                10 |         4 |         2 |      1    |
| COMPLIANCE                                |          4 |        12 |     7 |                 30 |                 9 |         3 |         2 |      0.6  |
| REGULATION                                |          5 |         4 |     5 |                164 |                22 |         2 |         2 |      0.33 |
| ANTI_MONEY_LAUNDERING                     |          6 |        10 |     5 |                 34 |                 6 |         3 |         2 |      0.75 |
| FINANCIAL_SERVICES                        |          7 |         3 |     4 |                168 |                20 |         3 |         2 |      0.43 |
| FINANCIAL_REGULATION                      |          8 |         9 |     4 |                 35 |                 7 |         2 |         2 |      0.29 |
| ARTIFICIAL_INTELLIGENCE                   |          9 |        19 |     4 |                 23 |                 4 |         3 |         2 |      0.6  |
| RISK_MANAGEMENT                           |         10 |        25 |     3 |                 14 |                 6 |         2 |         2 |      0.33 |
| INNOVATION                                |         11 |        32 |     3 |                 12 |                 4 |         1 |         1 |      0.25 |
| BLOCKCHAIN                                |         12 |        59 |     3 |                  5 |                 0 |         1 |         1 |      0.14 |
| SUPTECH                                   |         13 |        60 |     3 |                  4 |                 2 |         1 |         1 |      0.2  |
| SEMANTIC_TECHNOLOGIES                     |         14 |         7 |     2 |                 41 |                19 |         2 |         2 |      0.33 |
| DATA_PROTECTION                           |         15 |        13 |     2 |                 27 |                 4 |         2 |         1 |      0.5  |
| SMART_CONTRACTS                           |         16 |        20 |     2 |                 22 |                 8 |         1 |         1 |      0.14 |
| CHARITYTECH                               |         17 |        23 |     2 |                 17 |                 4 |         2 |         1 |      0.5  |
| ENGLISH_LAW                               |         18 |        24 |     2 |                 17 |                 4 |         2 |         1 |      0.5  |
| ACCOUNTABILITY                            |         19 |        26 |     2 |                 14 |                 3 |         2 |         1 |      0.5  |
| DATA_PROTECTION_OFFICER                   |         20 |        27 |     2 |                 14 |                 3 |         2 |         1 |      0.5  |
| BUSINESS_MODELS                           |         26 |         5 |     1 |                153 |                17 |         1 |         1 |      0.17 |
| FUTURE_RESEARCH_DIRECTION                 |         27 |         6 |     1 |                153 |                17 |         1 |         1 |      0.17 |
| STANDARDS                                 |         28 |        11 |     1 |                 33 |                14 |         1 |         1 |      0.2  |
| DIGITAL_IDENTITY                          |         29 |        14 |     1 |                 24 |                 4 |         1 |         1 |      0.25 |
| EUROPEAN_UNION                            |         30 |        15 |     1 |                 24 |                 4 |         1 |         1 |      0.25 |
| GENERAL_DATA_PROTECTION_REGULATION (GDPR) |         31 |        16 |     1 |                 24 |                 4 |         1 |         1 |      0.25 |
| OPEN_BANKING                              |         32 |        17 |     1 |                 24 |                 4 |         1 |         1 |      0.25 |
| PAYMENT_SERVICES_DIRECTIVE_2 (PSD_2)      |         33 |        18 |     1 |                 24 |                 4 |         1 |         1 |      0.25 |
```
<BLANKLINE>



>>> metrics.fig_.write_html("sphinx/_static/performance/performance_metrics.html")

.. raw:: html

    <iframe src="../../../../_static/performance/performance_metrics.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
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
    top_n_trend=200,
    is_trend_analysis=False,
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
    data_frame = _table(
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
        top_n_trend=top_n_trend,
        is_trend_analysis=is_trend_analysis,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = _select_columns(
        data_frame=data_frame, metric=metric, is_trend_analysis=is_trend_analysis
    )

    if metric == "OCCGC":
        metric = "OCC"

    prompt = _prompt(
        field=field,
        metric=metric,
        data_frame=data_frame,
    )

    if metric == "word_trends":
        metric = "OCC"

    if metric == "trending_words":
        metric = "OCC"

    fig = _fig(
        #
        # DATA PARAMS:
        field=field,
        metric=metric,
        data_frame=data_frame,
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

    @dataclass
    class Results:
        df_ = data_frame
        prompt_ = prompt
        fig_ = fig

    return Results()


def _table(
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
    top_n_trend,
    is_trend_analysis,
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
    data_frame = sort_indicators_by_metric(data_frame, metric, is_trend_analysis=False)

    if is_trend_analysis is False:
        top_n_trend = top_n

    if custom_items is None:
        if metric == "OCCGC":
            custom_items_occ = generate_custom_items(
                indicators=sort_indicators_by_metric(
                    data_frame,
                    "OCC",
                    is_trend_analysis=False,
                ),
                top_n=top_n_trend,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items_gc = generate_custom_items(
                indicators=sort_indicators_by_metric(
                    data_frame,
                    "global_citations",
                    is_trend_analysis=False,
                ),
                top_n=top_n_trend,
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
                top_n=top_n_trend,
                occ_range=occ_range,
                gc_range=gc_range,
            )

    data_frame = data_frame[data_frame.index.isin(custom_items)]

    if is_trend_analysis is True:
        data_frame = sort_indicators_by_metric(data_frame, metric, is_trend_analysis=True)
        data_frame = data_frame.head(top_n)

    return data_frame


def _select_columns(data_frame, metric, is_trend_analysis):
    #
    #
    # if metric == "trending_words":
    #     columns = [
    #         "OCC",
    #         data_frame.columns[3],
    #         data_frame.columns[4],
    #         "average_growth_rate",
    #         "average_docs_per_year",
    #         "percentage_docs_last_year",
    #     ]
    if metric == "trending_words":
        columns = [
            "rank_occ",
            "OCC",
            data_frame.columns[3],
            data_frame.columns[4],
            "average_growth_rate",
            "average_docs_per_year",
            "percentage_docs_last_year",
        ]

    if metric == "word_trends":
        columns = [
            "OCC",
            data_frame.columns[3],
            data_frame.columns[4],
        ]

    if metric == "OCCGC":
        columns = [
            "rank_occ",
            "rank_gc",
            "OCC",
            "global_citations",
            "local_citations",
            "h_index",
            "g_index",
            "m_index",
        ]

    if metric == "OCC":
        columns = ["rank_occ", "OCC"]

    if metric in ["global_citations", "local_citations"]:
        columns = [
            "rank_gc",
            "global_citations",
            "local_citations",
            "global_citations_per_document",
            "local_citations_per_document",
            "global_citations_per_year",
        ]

    if metric in [
        "average_growth_rate",
        "average_docs_per_year",
        "percentage_docs_last_year",
    ]:
        columns = [
            data_frame.columns[3],
            data_frame.columns[4],
            "average_growth_rate",
            "average_docs_per_year",
            "percentage_docs_last_year",
        ]

    if metric in ["h_index", "g_index", "m_index"]:
        columns = ["h_index", "g_index", "m_index"]

    # if is_trend_analysis and metric not in [
    #     "average_growth_rate",
    #     "average_docs_per_year",
    #     "percentage_docs_last_year",
    # ]:
    #     columns += [
    #         "average_growth_rate",
    #         "average_docs_per_year",
    #         "percentage_docs_last_year",
    #     ]

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
