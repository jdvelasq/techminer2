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
...     #
...     # FILTER PARAMS:
...     metric='OCCGC',
...     top_n=20,
...     occ_range=(None, None),
...     gc_range=(None, None),
...     custom_terms=None,
...     #
...     # DATABASE PARAMS:
...     root_dir="example/", 
...     database="main",
...     year_filter=None,
...     cited_by_filter=None,
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

from .._core.metrics.calculate_global_performance_metrics import calculate_global_performance_metrics
from .._core.metrics.filter_records_by_metric import filter_records_by_metric
from .._core.metrics.select_record_columns_by_metric import select_record_columns_by_metric
from ..helpers.helper_format_prompt_for_dataframes import helper_format_prompt_for_dataframes

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def performance_metrics(
    #
    # ITEMS PARAMS:
    field,
    #
    # FILTER PARAMS:
    metric="OCCGC",
    top_n=20,
    occ_range=(None, None),
    gc_range=(None, None),
    custom_terms=None,
    #
    # DATABASE PARAMS:
    root_dir="./",
    database="main",
    year_filter=(None, None),
    cited_by_filter=(None, None),
    **filters,
):
    """:meta private:"""

    records = calculate_global_performance_metrics(
        #
        # ITEMS PARAMS:
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    filtered_records = filter_records_by_metric(
        records=records,
        metric=metric,
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
    )

    selected_records = select_record_columns_by_metric(
        filtered_records,
        metric,
    )

    if metric == "OCCGC":
        metric = "OCC"

    prompt = generate_prompt(
        field=field,
        metric=metric,
        indicators=selected_records.head(200),
    )

    #
    # Save results to disk as csv tab-delimited file for papers
    file_path = os.path.join(root_dir, "reports", field + ".csv")
    selected_records.to_csv(file_path, sep="\t", header=True, index=True)

    @dataclass
    class Results:
        df_ = selected_records
        prompt_ = prompt

    return Results()


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
    return helper_format_prompt_for_dataframes(main_text, indicators.to_markdown())
