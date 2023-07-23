# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _performance.item_metrics:

Item Metrics
===============================================================================

>>> from techminer2.performance_analysis import item_metrics
>>> items = item_metrics(
...     #
...     # ITEMS PARAMS:
...     field='author_keywords',
...     metric="OCC",
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
>>> items.df_.head()
                       rank_occ  OCC
author_keywords                     
REGTECH                       1   28
FINTECH                       2   12
REGULATORY_TECHNOLOGY         3    7
COMPLIANCE                    4    7
REGULATION                    5    5

>>> print(items.prompt_)
Your task is to generate an analysis about the bibliometric indicators of \\
the 'author_keywords' field in a scientific bibliography database. \\
Summarize the table below, sorted by the 'OCC' metric, and delimited by \\
triple backticks, identify any notable patterns, trends, or outliers in the \\
data, and discuss their implications for the research field. Be sure to \\
provide a concise summary of your findings in no more than 150 words.
<BLANKLINE>
Table:
```
| author_keywords         |   rank_occ |   OCC |
|:------------------------|-----------:|------:|
| REGTECH                 |          1 |    28 |
| FINTECH                 |          2 |    12 |
| REGULATORY_TECHNOLOGY   |          3 |     7 |
| COMPLIANCE              |          4 |     7 |
| REGULATION              |          5 |     5 |
| ANTI_MONEY_LAUNDERING   |          6 |     5 |
| FINANCIAL_SERVICES      |          7 |     4 |
| FINANCIAL_REGULATION    |          8 |     4 |
| ARTIFICIAL_INTELLIGENCE |          9 |     4 |
| RISK_MANAGEMENT         |         10 |     3 |
| INNOVATION              |         11 |     3 |
| BLOCKCHAIN              |         12 |     3 |
| SUPTECH                 |         13 |     3 |
| SEMANTIC_TECHNOLOGIES   |         14 |     2 |
| DATA_PROTECTION         |         15 |     2 |
| SMART_CONTRACTS         |         16 |     2 |
| CHARITYTECH             |         17 |     2 |
| ENGLISH_LAW             |         18 |     2 |
| ACCOUNTABILITY          |         19 |     2 |
| DATA_PROTECTION_OFFICER |         20 |     2 |
```
<BLANKLINE>

>>> items.fig_.write_html("sphinx/_static/performance_analysis/item_metrics.html")

.. raw:: html

    <iframe src="../../../../_static/performance_analysis/item_metrics.html"
    height="600px" width="100%" frameBorder="0"></iframe>


"""
from dataclasses import dataclass

import plotly.express as px

from .._filtering_lib import generate_custom_items
from .._sorting_lib import sort_indicators_by_metric
from ..format_prompt_for_dataframes import format_prompt_for_dataframes
from ..techminer.metrics.global_indicators_by_field import global_indicators_by_field

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def item_metrics(
    #
    # ITEMS PARAMS:
    field,
    metric="OCC",
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
    data_frame = __table(
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
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = __select_columns(data_frame=data_frame, metric=metric)

    if metric == "OCCGC":
        metric = "OCC"

    prompt = __prompt(
        field=field,
        metric=metric,
        data_frame=data_frame,
    )

    fig = __fig(
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


def __table(
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
    # DATABASE PARAMS:
    root_dir,
    database,
    year_filter,
    cited_by_filter,
    **filters,
):
    """Returns a dataframe with the extracted items of database field."""

    #
    # MAIN CODE:
    #

    data_frame = global_indicators_by_field(
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    data_frame = sort_indicators_by_metric(data_frame, metric)

    if custom_items is None:
        if metric == "OCCGC":
            custom_items_occ = generate_custom_items(
                indicators=sort_indicators_by_metric(data_frame, "OCC"),
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items_gc = generate_custom_items(
                indicators=sort_indicators_by_metric(data_frame, "global_citations"),
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items = custom_items_occ[:]
            custom_items += [item for item in custom_items_gc if item not in custom_items_occ]

        else:
            custom_items = generate_custom_items(
                indicators=data_frame,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

    data_frame = data_frame[data_frame.index.isin(custom_items)]

    return data_frame


def __select_columns(data_frame, metric):
    #
    #
    if metric == "OCCGC":
        return data_frame[["rank_occ", "rank_gc", "OCC", "global_citations"]]

    if metric == "OCC":
        return data_frame[["rank_occ", "OCC"]]

    if metric in ["global_citations", "local_citations"]:
        return data_frame[
            [
                "rank_gc",
                "global_citations",
                "local_citations",
                "global_citations_per_document",
                "local_citations_per_document",
                "global_citations_per_year",
            ]
        ]

    if metric in [
        [
            "average_growth_rate",
            "average_docs_per_year",
            "percentage_docs_last_year",
        ]
    ]:
        return data_frame[
            [
                "average_growth_rate",
                "average_docs_per_year",
                "percentage_docs_last_year",
            ]
        ]

    if metric in ["h_index", "g_index", "m_index"]:
        return data_frame[["h_index", "g_index", "m_index"]]

    return data_frame


def __prompt(field, metric, data_frame):
    main_text = (
        "Your task is to generate an analysis about the bibliometric indicators of the "
        f"'{field}' field in a scientific bibliography database. Summarize the table below, "
        f"sorted by the '{metric}' metric, and delimited by triple backticks, identify "
        "any notable patterns, trends, or outliers in the data, and discuss their "
        "implications for the research field. Be sure to provide a concise summary "
        "of your findings in no more than 150 words."
    )
    return format_prompt_for_dataframes(main_text, data_frame.to_markdown())


def __fig(
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
