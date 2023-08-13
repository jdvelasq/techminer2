# flake8: noqa
# pylint: disable=invalid-name
# pylint: disable=line-too-long
# pylint: disable=missing-docstring
# pylint: disable=too-many-arguments
# pylint: disable=too-many-locals
"""
.. _tm2.performance.overview.average_citations_per_year:

Average Citations per Year
===============================================================================


>>> from techminer2.performance.overview import average_citations_per_year
>>> chart = average_citations_per_year(
...     #
...     # CHART PARAMS:
...     title="Average Citations per Year",
...     year_label=None,
...     metric_label="Average Citations per Year",
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
>>> chart.fig_.write_html("sphinx/_static/performance/overview/average_citations_per_year.html")

.. raw:: html

    <iframe src="../../../../../_static/performance/overview//average_citations_per_year.html"  
    height="600px" width="100%" frameBorder="0"></iframe>


>>> print(chart.df_.head().to_markdown())
|   year |   mean_global_citations |   mean_global_citations_per_year |
|-------:|------------------------:|---------------------------------:|
|   2016 |                30       |                             3.75 |
|   2017 |                40.5     |                             5.79 |
|   2018 |                60.6667  |                            10.11 |
|   2019 |                 7.83333 |                             1.57 |
|   2020 |                 6.64286 |                             1.66 |


>>> print(chart.df_.T.to_markdown())
|                                |   2016 |   2017 |    2018 |    2019 |    2020 |   2021 |    2022 |   2023 |
|:-------------------------------|-------:|-------:|--------:|--------:|--------:|-------:|--------:|-------:|
| mean_global_citations          |  30    |  40.5  | 60.6667 | 7.83333 | 6.64286 |    2.7 | 1.83333 |      0 |
| mean_global_citations_per_year |   3.75 |   5.79 | 10.11   | 1.57    | 1.66    |    0.9 | 0.92    |      0 |


>>> print(chart.prompt_)
The table below provides data on the average citations per year and the \\
average citations per year divided by the age of the documents in the \\
dataset. Use the the information in in the table to draw conclusions about \\
the impact per year. In your analysis, be sure to describe in a clear and \\
concise way, any trends or patterns you observe, and identify any outliers \\
or anomalies in the data. Limit your description to one paragraph with no \\
more than 250 words.
<BLANKLINE>
Table:
```
|   year |   mean_global_citations |   mean_global_citations_per_year |
|-------:|------------------------:|---------------------------------:|
|   2016 |                30       |                             3.75 |
|   2017 |                40.5     |                             5.79 |
|   2018 |                60.6667  |                            10.11 |
|   2019 |                 7.83333 |                             1.57 |
|   2020 |                 6.64286 |                             1.66 |
|   2021 |                 2.7     |                             0.9  |
|   2022 |                 1.83333 |                             0.92 |
|   2023 |                 0       |                             0    |
```
<BLANKLINE>



"""
from dataclasses import dataclass

import pandas as pd
import plotly.graph_objects as go

from ...format_prompt_for_dataframes import format_prompt_for_dataframes
from ._compute_metrics_per_year import compute_metrics_per_year
from ._plot_metrics_by_year import plot_metrics_by_year


def average_citations_per_year(
    #
    # CHART PARAMS:
    title: str = "Average Citations per Year",
    year_label=None,
    metric_label=None,
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
    """Average citations per year.

    :meta private:
    """

    data_frame = compute_metrics_per_year(
        #
        # DATABASE PARAMS
        root_dir=root_dir,
        database=database,
        year_filter=year_filter,
        cited_by_filter=cited_by_filter,
        **filters,
    )
    data_frame = data_frame[["mean_global_citations", "mean_global_citations_per_year"]]

    prompt = __generate_prompt(data_frame)

    fig = plot_metrics_by_year(
        indicator_to_plot="mean_global_citations_per_year",
        auxiliary_indicator="mean_global_citations",
        #
        # CHART PARAMS:
        title=title,
        year_label=year_label,
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
    class Result:
        df_: pd.DataFrame = data_frame
        fig_: go.Figure = fig
        prompt_: str = prompt

    return Result(
        df_=data_frame,
        fig_=fig,
        prompt_=prompt,
    )


def __generate_prompt(data_frame: pd.DataFrame) -> str:
    main_text = (
        "The table below provides data on the average citations per "
        "year and the average citations per year divided by the age "
        "of the documents in the dataset. Use the the information in "
        "in the table to draw conclusions about the impact per year. "
        "In your analysis, be "
        "sure to describe in a clear and concise way, any trends or "
        "patterns you observe, and identify any outliers or anomalies "
        "in the data. Limit your description to one paragraph with no "
        "more than 250 words."
    )

    table_text = data_frame.to_markdown()

    return format_prompt_for_dataframes(main_text, table_text)
