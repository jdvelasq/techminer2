# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Performance Metrics
===============================================================================

>>> from techminer2.metrics import performance_metrics
>>> metrics = performance_metrics(
...     field='author_keywords',
...     filter_params = {
...         "metric": 'OCCGC',
...         "top_n": 20,
...         "occ_range": (None, None),
...         "gc_range": (None, None),
...         "custom_items": None,
...     },
...     database_params = {
...         "root_dir": "example/",
...         "database": "main",
...         "year_filter": (None, None),
...         "cited_by_filter": (None, None),
...     }
... )
>>> print(metrics.df_.head().to_markdown())
| author_keywords      |   rank_occ |   rank_gcs |   rank_lcs |   OCC |   global_citations |   local_citations |   h_index |   g_index |   m_index |
|:---------------------|-----------:|-----------:|-----------:|------:|-------------------:|------------------:|----------:|----------:|----------:|
| FINTECH              |          1 |          1 |          1 |    31 |               5168 |                26 |        31 |        12 |      7.75 |
| INNOVATION           |          2 |          2 |          2 |     7 |                911 |                 5 |         7 |         7 |      1.75 |
| FINANCIAL_SERVICES   |          3 |          4 |         40 |     4 |                667 |                 1 |         4 |         4 |      1    |
| FINANCIAL_INCLUSION  |          4 |          5 |          3 |     3 |                590 |                 5 |         3 |         3 |      0.75 |
| FINANCIAL_TECHNOLOGY |          5 |         15 |         41 |     3 |                461 |                 1 |         3 |         3 |      1    |



>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
import os
from dataclasses import dataclass

from .._common._filtering_lib import generate_custom_items
from .._common._sorting_lib import sort_indicators_by_metric
from .._common.format_prompt_for_dataframes import format_prompt_for_dataframes
from .global_indicators_by_field import global_indicators_by_field

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def performance_metrics(
    field,
    filter_params,
    database_params,
):
    """:meta private:"""

    global_indicators = global_indicators_by_field(
        field=field,
        database_params=database_params,
    )
    filtered_indicators = filter_indicators_by_metric(
        indicators=global_indicators,
        **filter_params,
    )
    selected_indicators = select_indicators_by_metric(
        filtered_indicators, filter_params["metric"]
    )

    if filter_params["metric"] == "OCCGC":
        filter_params["metric"] = "OCC"

    prompt = generate_prompt(
        field=field,
        metric=filter_params["metric"],
        indicators=selected_indicators.head(200),
    )

    #
    # Save results to disk as csv tab-delimited file for papers
    file_path = os.path.join(database_params["root_dir"], "reports", field + ".csv")
    selected_indicators.to_csv(file_path, sep="\t", header=True, index=True)

    @dataclass
    class Results:
        df_ = selected_indicators
        prompt_ = prompt

    return Results()


def filter_indicators_by_metric(
    indicators,
    metric,
    top_n,
    occ_range,
    gc_range,
    custom_items,
):
    """:meta private:"""

    indicators = indicators.copy()

    if custom_items is None:
        #
        if metric == "OCCGC":
            #
            # In this case not is possibe to use trend_analysis
            #
            # Selects the top_n items by OCC
            custom_items_occ = generate_custom_items(
                indicators=indicators,
                metric="OCC",
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            #
            # Selects the top_n items by GCS
            custom_items_gc = generate_custom_items(
                indicators=indicators,
                metric="global_citations",
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

            custom_items = custom_items_occ[:]
            custom_items += [
                item for item in custom_items_gc if item not in custom_items_occ
            ]

        else:
            #
            # Default custom items selection
            custom_items = generate_custom_items(
                indicators=indicators,
                metric=metric,
                top_n=top_n,
                occ_range=occ_range,
                gc_range=gc_range,
            )

    indicators = indicators[indicators.index.isin(custom_items)]
    indicators = sort_indicators_by_metric(indicators, metric)

    return indicators


def select_indicators_by_metric(indicators, metric):
    """:meta private:"""

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
            indicators.columns[4],
            indicators.columns[5],
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

    return indicators[columns]


def generate_prompt(field, metric, indicators):
    """:meta private:"""

    main_text = (
        "Your task is to generate an analysis about the bibliometric indicators of the "
        f"'{field}' field in a scientific bibliography database. Summarize the table below, "
        f"sorted by the '{metric}' metric, and delimited by triple backticks, identify "
        "any notable patterns, trends, or outliers in the data, and discuss their "
        "implications for the research field. Be sure to provide a concise summary "
        "of your findings in no more than 150 words. "
    )
    return format_prompt_for_dataframes(main_text, indicators.to_markdown())
