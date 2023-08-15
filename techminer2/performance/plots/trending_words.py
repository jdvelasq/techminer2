# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
# pylint: disable=import-outside-toplevel
"""
.. _performance.plots.trending_words:

Trending Words
===============================================================================


>>> from techminer2.performance.plots import trending_words
>>> chart = trending_words(
...     #
...     # PARAMS:
...     field="descriptors",
...     #
...     # TREND ANALYSIS:
...     time_window=2,
...     top_n_trend=200,
...     is_trend_analysis=False,
...     #
...     # CHART PARAMS:
...     title=None,
...     x_label=None,
...     y_label=None,
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
...     year_filter=None,
...     cited_by_filter=(None, None),
... )
>>> print(chart.df_.to_markdown())
| descriptors                 |   rank_occ |   OCC |   Before 2022 |   Between 2022-2023 |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |
|:----------------------------|-----------:|------:|--------------:|--------------------:|----------------------:|------------------------:|----------------------------:|
| REGTECH                     |          1 |    29 |            20 |                   9 |                  -0.5 |                     4.5 |                   0.155172  |
| REGULATORY_TECHNOLOGY       |          2 |    20 |            14 |                   6 |                  -1.5 |                     3   |                   0.15      |
| FINANCIAL_INSTITUTIONS      |          3 |    16 |            12 |                   4 |                  -1.5 |                     2   |                   0.125     |
| REGULATORY_COMPLIANCE       |          4 |    15 |            12 |                   3 |                  -0.5 |                     1.5 |                   0.1       |
| FINANCIAL_REGULATION        |          5 |    12 |             8 |                   4 |                  -1   |                     2   |                   0.166667  |
| FINTECH                     |          6 |    12 |            10 |                   2 |                  -0.5 |                     1   |                   0.0833333 |
| ARTIFICIAL_INTELLIGENCE     |          7 |     8 |             5 |                   3 |                  -0.5 |                     1.5 |                   0.1875    |
| FINANCIAL_SECTOR            |          8 |     7 |             5 |                   2 |                  -1.5 |                     1   |                   0.142857  |
| FINANCIAL_CRISIS            |          9 |     7 |             6 |                   1 |                  -0.5 |                     0.5 |                   0.0714286 |
| COMPLIANCE                  |         10 |     7 |             5 |                   2 |                   0   |                     1   |                   0.142857  |
| FINANCE                     |         11 |     7 |             4 |                   3 |                  -0.5 |                     1.5 |                   0.214286  |
| FINANCIAL_SERVICES          |         12 |     6 |             5 |                   1 |                  -0.5 |                     0.5 |                   0.0833333 |
| INFORMATION_TECHNOLOGY      |         13 |     6 |             4 |                   2 |                   0   |                     1   |                   0.166667  |
| GLOBAL_FINANCIAL_CRISIS     |         14 |     6 |             3 |                   3 |                   0.5 |                     1.5 |                   0.25      |
| FINANCIAL_TECHNOLOGY        |         15 |     6 |             5 |                   1 |                  -0.5 |                     0.5 |                   0.0833333 |
| ANTI_MONEY_LAUNDERING       |         16 |     6 |             6 |                   0 |                  -1.5 |                     0   |                   0         |
| FINANCIAL_SERVICES_INDUSTRY |         17 |     5 |             3 |                   2 |                   0   |                     1   |                   0.2       |
| FINANCIAL_SYSTEM            |         18 |     5 |             4 |                   1 |                   0   |                     0.5 |                   0.1       |
| REGULATION                  |         19 |     5 |             4 |                   1 |                  -0.5 |                     0.5 |                   0.1       |
| RISK_MANAGEMENT             |         20 |     5 |             4 |                   1 |                   0   |                     0.5 |                   0.1       |



>>> chart = trending_words(
...     #
...     # PARAMS:
...     field="descriptors",
...     #
...     # TREND ANALYSIS:
...     time_window=2,
...     top_n_trend=200,
...     is_trend_analysis=True,
...     #
...     # CHART PARAMS:
...     title=None,
...     x_label=None,
...     y_label=None,
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
...     year_filter=None,
...     cited_by_filter=(None, None),
... )
| descriptors                  |   rank_occ |   OCC |   Before 2022 |   Between 2022-2023 |   average_growth_rate |   average_docs_per_year |   percentage_docs_last_year |
|:-----------------------------|-----------:|------:|--------------:|--------------------:|----------------------:|------------------------:|----------------------------:|
| GLOBAL_FINANCIAL_CRISIS      |         14 |     6 |             3 |                   3 |                   0.5 |                     1.5 |                    0.25     |
| NEW_REGULATORY_TECHNOLOGIES  |         70 |     2 |             1 |                   1 |                   0.5 |                     0.5 |                    0.25     |
| COMPLIANCE                   |         10 |     7 |             5 |                   2 |                   0   |                     1   |                    0.142857 |
| INFORMATION_TECHNOLOGY       |         13 |     6 |             4 |                   2 |                   0   |                     1   |                    0.166667 |
| FINANCIAL_SERVICES_INDUSTRY  |         17 |     5 |             3 |                   2 |                   0   |                     1   |                    0.2      |
| FINANCIAL_SYSTEM             |         18 |     5 |             4 |                   1 |                   0   |                     0.5 |                    0.1      |
| RISK_MANAGEMENT              |         20 |     5 |             4 |                   1 |                   0   |                     0.5 |                    0.1      |
| REGTECH_SOLUTIONS            |         21 |     5 |             4 |                   1 |                   0   |                     0.5 |                    0.1      |
| DIGITAL_IDENTITY             |         28 |     3 |             3 |                   0 |                   0   |                     0   |                    0        |
| SUPTECH                      |         33 |     3 |             1 |                   2 |                   0   |                     1   |                    0.333333 |
| SYSTEMATIC_LITERATURE_REVIEW |         34 |     3 |             1 |                   2 |                   0   |                     1   |                    0.333333 |
| REGULATORY_FRAMEWORK         |         35 |     3 |             1 |                   2 |                   0   |                     1   |                    0.333333 |
| NEW_APPROACH                 |         37 |     2 |             2 |                   0 |                   0   |                     0   |                    0        |
| DISRUPTIVE_INNOVATION        |         38 |     2 |             2 |                   0 |                   0   |                     0   |                    0        |
| REGULATORY_SYSTEM            |         39 |     2 |             2 |                   0 |                   0   |                     0   |                    0        |
| FINANCIAL_STABILITY          |         40 |     2 |             2 |                   0 |                   0   |                     0   |                    0        |
| SEMANTIC_TECHNOLOGIES        |         41 |     2 |             2 |                   0 |                   0   |                     0   |                    0        |
| DATA_PROTECTION              |         42 |     2 |             1 |                   1 |                   0   |                     0.5 |                    0.25     |
| OPERATIONAL_RISK             |         43 |     2 |             2 |                   0 |                   0   |                     0   |                    0        |
| BLOCKCHAIN_TECHNOLOGY        |         44 |     2 |             2 |                   0 |                   0   |                     0   |                    0        |


>>> print(chart.df_.to_markdown())

>>> chart.fig_.write_html("sphinx/_static/performance/plots/trending_words.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/plots/trending_words.html" 
    height="600px" width="100%" frameBorder="0"></iframe>



>>> print(chart.df_.head(100).to_markdown())


>>> print(chart.prompt_)


"""
from dataclasses import dataclass

import plotly.express as px

from ..performance_metrics import performance_metrics

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def trending_words(
    #
    # PARAMS:
    field,
    #
    # TREND ANALYSIS:
    time_window=2,
    top_n_trend=200,
    is_trend_analysis=False,
    #
    # CHART PARAMS:
    title=None,
    x_label=None,
    y_label=None,
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
    """Top Trending Topics Graph.  :meta private:"""

    #
    # Extracs only the performance metrics data frame
    data_frame = performance_metrics(
        #
        # ITEMS PARAMS:
        field=field,
        metric="trending_words",
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
    ).df_

    #
    # Creates a bar plot of trending terms

    # Index(['OCC', 'Before 2022', 'Between 2022-2023', 'average_growth_rate',
    #    'average_docs_per_year', 'percentage_docs_last_year'],
    #   dtype='object')

    # x_label = "Average Growth Rate" if x_label is None else x_label
    # y_label = "Percentage of Documents in Last Years" if y_label is None else y_label

    # fig = px.scatter(
    #     data_frame,
    #     x="average_growth_rate",
    #     y="percentage_docs_last_year",
    # )

    # fig.update_layout(
    #     paper_bgcolor="white",
    #     plot_bgcolor="white",
    #     title_text=title if title is not None else "",
    # )
    # fig.update_traces(
    #     marker_color=MARKER_COLOR,
    #     marker_line={"color": MARKER_LINE_COLOR},
    # )
    # fig.update_xaxes(
    #     linecolor="gray",
    #     linewidth=2,
    #     gridcolor="lightgray",
    #     griddash="dot",
    #     title_text=x_label,
    # )
    # fig.update_yaxes(
    #     linecolor="gray",
    #     linewidth=2,
    #     autorange="reversed",
    #     gridcolor="lightgray",
    #     griddash="dot",
    #     title_text=y_label,
    # )

    @dataclass
    class Results:
        df_ = data_frame
        # prompt_ = prompt
        # fig_ = fig

    return Results()
