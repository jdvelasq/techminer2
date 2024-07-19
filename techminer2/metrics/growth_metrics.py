# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
Growth Metrics
===============================================================================

>>> from techminer2.metrics import growth_metrics
>>> metrics = growth_metrics(
...     field='author_keywords',
...     time_window=2,
...     #
...     # FILTER PARAMS:
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
| author_keywords      |   rank_occ |   OCC |   between_2018_2019 |   before_2018 |   growth_percentage |   average_growth_rate |   average_docs_per_year |
|:---------------------|-----------:|------:|--------------------:|--------------:|--------------------:|----------------------:|------------------------:|
| FINTECH              |          1 |    31 |                  18 |            13 |               58.06 |                  -1   |                     9   |
| INNOVATION           |          2 |     7 |                   1 |             6 |               14.29 |                  -1.5 |                     0.5 |
| FINANCIAL_SERVICES   |          3 |     4 |                   3 |             1 |               75    |                   0   |                     1.5 |
| FINANCIAL_INCLUSION  |          4 |     3 |                   0 |             3 |                0    |                  -1   |                     0   |
| FINANCIAL_TECHNOLOGY |          5 |     3 |                   2 |             1 |               66.67 |                   0   |                     1   |




>>> print(metrics.prompt_) # doctest: +ELLIPSIS
Your task is ...




"""
import os

#
# TechMiner2+ computes three growth indicators for each item in a field (usually
# keywords or noun phrases):
#
# * Average growth rate (AGR):
#
# .. code-block::
#
#            sum_{i=Y_start}^Y_end  Num_Documents[i] - Num_Documents[i-1]
#     AGR = --------------------------------------------------------------
#                             Y_end - Y_start + 1
#
#
# * Average documents per year (ADY):
#
# .. code-block::
#
#            sum_{i=Y_start}^Y_end  Num_Documents[i]
#     ADY = -----------------------------------------
#                     Y_end - Y_start + 1
#
#
# * Percentage of documents in last year (PDLY):
#
# .. code-block::
#
#            sum_{i=Y_start}^Y_end  Num_Documents[i]      1
#     PDLY = ---------------------------------------- * _____
#                   Y_end - Y_start + 1                  TND
#
# With:
#
# .. code-block::
#
#     Y_start = Y_end - time_window + 1
#
# If ``Y_end = 2018`` and ``time_window = 2``, then ``Y_start = 2017``.
#
from dataclasses import dataclass

from .._core.metrics.calculate_global_performance_metrics import calculate_global_performance_metrics
from .._core.metrics.filter_records_by_metric import filter_records_by_metric
from .._core.metrics.items_occurrences_by_year import items_occurrences_by_year
from .._core.metrics.select_record_columns_by_metric import select_record_columns_by_metric
from ..helpers.helper_format_prompt_for_dataframes import helper_format_prompt_for_dataframes


def growth_metrics(
    field,
    time_window=2,
    #
    # FILTER PARAMS:
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

    #
    # Compute global performance metrics
    global_indicators = calculate_global_performance_metrics(
        field=field,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    #
    # Computes item occurrences by year
    items_by_year = items_occurrences_by_year(
        #
        # FUNCTION PARAMS:
        field=field,
        cumulative=False,
        #
        # DATABASE PARAMS:
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Computes the range of years in the time window
    year_end = items_by_year.columns.max()
    year_start = year_end - time_window + 1
    year_columns = list(range(year_start, year_end + 1))

    #
    # Check the time window
    if items_by_year.columns.max() - items_by_year.columns.min() <= time_window:
        raise ValueError("Time window must be less than the number of years in the database")

    #
    # Computes the number of documents per period by item
    between = f"between_{year_start}_{year_end}"
    before = f"before_{year_start}"
    between_occ = items_by_year.loc[:, year_columns].sum(axis=1)
    before_occ = items_by_year.sum(axis=1) - between_occ
    global_indicators.loc[between_occ.index, between] = between_occ
    global_indicators.loc[before_occ.index, before] = before_occ

    global_indicators = global_indicators.assign(
        growth_percentage=(100 * global_indicators[between].copy() / global_indicators["OCC"].copy()).round(2)
    )

    #
    # sort the columns
    columns = ["OCC", before, between, "growth_percentage"] + [
        col for col in global_indicators.columns if col not in ["OCC", before, between, "growth_percentage"]
    ]
    global_indicators = global_indicators[columns]

    #
    # selects the columns of interest
    items_by_year = items_by_year.loc[:, [year_columns[0] - 1] + year_columns]

    # agr: average growth rate
    agr = items_by_year.diff(axis=1)
    agr = agr.loc[:, year_columns]
    agr = agr.sum(axis=1) / time_window
    global_indicators.loc[agr.index, "average_growth_rate"] = agr

    # ady: average documents per year
    ady = items_by_year.loc[:, year_columns].sum(axis=1) / time_window
    global_indicators.loc[ady.index, "average_docs_per_year"] = ady

    # pdly: percentage of documents in last year
    global_indicators = global_indicators.assign(
        percentage_docs_last_year=(global_indicators.average_docs_per_year.copy() / global_indicators.OCC.copy())
    )

    filtered_indicators = filter_records_by_metric(
        records=global_indicators,
        metric="OCC",
        top_n=top_n,
        occ_range=occ_range,
        gc_range=gc_range,
        custom_items=custom_items,
    )
    selected_indicators = select_record_columns_by_metric(filtered_indicators, "OCC")

    prompt = generate_prompt(
        field=field,
        metric="OCC",
        indicators=selected_indicators.head(200),
    )

    #
    # Save results to disk as csv tab-delimited file for papers
    file_path = os.path.join(root_dir, "reports", field + ".csv")
    selected_indicators.to_csv(file_path, sep="\t", header=True, index=True)

    @dataclass
    class Results:
        """:meta private:"""

        df_ = selected_indicators
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
