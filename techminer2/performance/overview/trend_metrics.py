# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.performance.overview.trend_metrics:

Trend Metrics
===============================================================================


>>> from techminer2.performance.overview import trend_metrics
>>> metrics = trend_metrics(
...     #
...     # TABLE PARAMS:
...     selected_columns=[
...         "OCC",
...         "global_citations",
...         "mean_global_citations",
...         "mean_global_citations_per_year",
...     ],
...     #
...     # CHART PARAMS:
...     metric_to_plot="OCC",
...     auxiliary_metric_to_plot=None,
...     title="Annual Scientific Production",
...     year_label=None,
...     metric_label=None,
...     textfont_size=10,
...     marker_size=7,
...     line_width=1.5,
...     yshift=4,
...     #
...     # DATABASE PARAMS:
...     root_dir="data/regtech/",
...     database="main",
...     year_filter=(None, None),
...     cited_by_filter=(None, None),
... )
>>> metrics.fig_.write_html("sphinx/_static/performance/overview/trend_metrics.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/overview/trend_metrics.html"  
    height="600px" width="100%" frameBorder="0"></iframe>



>>> print(metrics.df_.to_markdown())
|   year |   OCC |   global_citations |   mean_global_citations |   mean_global_citations_per_year |
|-------:|------:|-------------------:|------------------------:|---------------------------------:|
|   2016 |     1 |                 30 |                30       |                             3.75 |
|   2017 |     4 |                162 |                40.5     |                             5.79 |
|   2018 |     3 |                182 |                60.6667  |                            10.11 |
|   2019 |     6 |                 47 |                 7.83333 |                             1.57 |
|   2020 |    14 |                 93 |                 6.64286 |                             1.66 |
|   2021 |    10 |                 27 |                 2.7     |                             0.9  |
|   2022 |    12 |                 22 |                 1.83333 |                             0.92 |
|   2023 |     2 |                  0 |                 0       |                             0    |



>>> print(metrics.df_.T.to_markdown())
|                                |   2016 |   2017 |     2018 |     2019 |     2020 |   2021 |     2022 |   2023 |
|:-------------------------------|-------:|-------:|---------:|---------:|---------:|-------:|---------:|-------:|
| OCC                            |   1    |   4    |   3      |  6       | 14       |   10   | 12       |      2 |
| global_citations               |  30    | 162    | 182      | 47       | 93       |   27   | 22       |      0 |
| mean_global_citations          |  30    |  40.5  |  60.6667 |  7.83333 |  6.64286 |    2.7 |  1.83333 |      0 |
| mean_global_citations_per_year |   3.75 |   5.79 |  10.11   |  1.57    |  1.66    |    0.9 |  0.92    |      0 |



>>> print(metrics.prompt_)
Your task is to generate a short summary for a research paper about the \\
annual performance metrics of a bibliographic dataset. The table below \\
provides data on: the number of publications per yeear (OCC); the number of \\
citations per year (global_citations); the average number of citations per \\
document for each year (mean_global_citations); the average number of \\
citations per document divided by the age of the documents \\
(mean_global_citations_per_year);  Use the the information in the table to \\
draw conclusions about the impact per year. In your analysis, be sure to \\
describe in a clear and concise way, any trends or patterns you observe, \\
and identify any outliers or anomalies  in the data. Limit your description \\
to one paragraph with no more than 250 words.
<BLANKLINE>
Table:
```
|   year |   OCC |   global_citations |   mean_global_citations |   mean_global_citations_per_year |
|-------:|------:|-------------------:|------------------------:|---------------------------------:|
|   2016 |     1 |                 30 |                30       |                             3.75 |
|   2017 |     4 |                162 |                40.5     |                             5.79 |
|   2018 |     3 |                182 |                60.6667  |                            10.11 |
|   2019 |     6 |                 47 |                 7.83333 |                             1.57 |
|   2020 |    14 |                 93 |                 6.64286 |                             1.66 |
|   2021 |    10 |                 27 |                 2.7     |                             0.9  |
|   2022 |    12 |                 22 |                 1.83333 |                             0.92 |
|   2023 |     2 |                  0 |                 0       |                             0    |
```
<BLANKLINE>


"""
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go

from ...format_prompt_for_dataframes import format_prompt_for_dataframes
from ._compute_trend_metrics import compute_trend_metrics
from ._plot_trend_metrics import plot_trend_metrics

MARKER_COLOR = "#7793a5"
MARKER_LINE_COLOR = "#465c6b"


def trend_metrics(
    #
    # TABLE PARAMS:
    selected_columns=None,
    #
    # CHART PARAMS:
    metric_to_plot: str = "OCC",
    auxiliary_metric_to_plot: str = None,
    title: str = None,
    year_label: str = None,
    metric_label: str = None,
    textfont_size=10,
    marker_size=7,
    line_width=1.5,
    yshift=4,
    #
    # DATABASE PARAMS:
    root_dir: str = "./",
    database: str = "main",
    year_filter: tuple = (None, None),
    cited_by_filter: tuple = (None, None),
    **filters,
):
    """Global citations per year.

    :meta private:
    """

    #
    # Compute metrics per year
    data_frame = compute_trend_metrics(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )

    #
    # Select only columns existent in the data frame
    if selected_columns is None:
        selected_columns = data_frame.columns.copy()
    else:
        selected_columns = [col for col in selected_columns if col in data_frame.columns]
    data_frame = data_frame[selected_columns]

    #
    # Plot
    fig = plot_trend_metrics(
        #
        # METRICS:
        data_frame=data_frame,
        metric_to_plot=metric_to_plot,
        auxiliary_metric_to_plot=auxiliary_metric_to_plot,
        #
        # CHART PARAMS:
        title=title,
        year_label=year_label,
        metric_label=metric_label,
        textfont_size=textfont_size,
        marker_size=marker_size,
        line_width=line_width,
        yshift=yshift,
    )

    @dataclass
    class Result:
        df_: pd.DataFrame = data_frame
        fig_: go.Figure = fig
        prompt_: str = generate_prompt(data_frame)

    return Result()


def generate_prompt(data_frame: pd.DataFrame) -> str:
    """
    :meta private:
    """
    main_text = (
        "Your task is to generate a short summary for a research paper about "
        "the annual performance metrics of a bibliographic dataset. The table "
        "below provides data on: "
    )

    for col in data_frame.columns:
        if col == "OCC":
            main_text += "the number of publications per yeear (OCC); "
        if col == "cum_OCC":
            main_text += "the cummulative number of publications per yeear (OCC); "
        if col == "local_citations":
            main_text += "the number of local citations per year (local_citations); "
        if col == "global_citations":
            main_text += "the number of citations per year (global_citations); "
        if col == "citable_years":
            main_text += "the number of citable years (citable_years); "
        if col == "mean_global_citations":
            main_text += "the average number of citations per document for each year (mean_global_citations); "
        if col == "cum_global_citations":
            main_text += "the cummulative number of citations per document for each year (cum_global_citations); "
        if col == "mean_global_citations_per_year":
            main_text += "the average number of citations per document divided by the age of the documents (mean_global_citations_per_year); "
        if col == "mean_local_citations":
            main_text += "the average number of local citations per document for each year (mean_local_citations); "
        if col == "cum_local_citations":
            main_text += "the cummulative number of local citations per document for each year (cum_local_citations); "
        if col == "mean_local_citations_per_year":
            main_text += "the average number of local citations per document divided by the age of the documents (mean_local_citations_per_year); "

    main_text += (
        " Use the the information in the table "
        "to draw conclusions about the impact per year. In your analysis, be "
        "sure to describe in a clear and concise way, any trends or patterns "
        "you observe, and identify any outliers or anomalies  in the data. "
        "Limit your description to one paragraph with no more than 250 words. "
    )

    table_text = data_frame.to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)
